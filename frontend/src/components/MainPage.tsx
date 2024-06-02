import {Autocomplete, Box, Button, Divider, FormControl, FormLabel, IconButton, Input, List, ListItem, Sheet, Textarea, Typography} from "@mui/joy";
import {useEffect, useState} from "react";
import toast from "react-hot-toast";
import DeleteIcon from '@mui/icons-material/Delete';
import FileDownloadIcon from '@mui/icons-material/FileDownload';

export default function MainPage({
    audioList,
    setAudioList
} : {
    audioList: Array<string>,
    setAudioList: (a: Array<string>) => void,
}) {
    const [t, setT] = useState<string>("");
    const [audioText, setAudioText] = useState<Map<number, string>>(new Map<number, string>());
    const [loading, setLoading] = useState<boolean>(false);

    const timbreOptions: Array<string> = ["random", "female", "male"];
    const [timbreType, setTimbreType] = useState<string>(timbreOptions[0]);
    const [chatPrompt, setChatPrompts] = useState<string>("");

    useEffect(() => {
        fetch('/api/get_config').then((res) => res.json())
            .then((response) => {
                setTimbreType(response.timbre_type || timbreType);
                setChatPrompts(response.prompt || chatPrompt);
            });
    }, []);

    function newAudio() {
        setLoading(true);
        if (t === "") {
            toast.error("生成文本不能为空");
            return;
        }
        toast.success('开始生成');
        fetch('/api/new_chat', {
            method: "POST",
            body: JSON.stringify({
                text: t.trim(),
                new_chat_config: {
                    timbre_type: timbreType,
                    prompt: chatPrompt,
                }
            })
        }).then((res) => res.json())
            .then((response) => {
                if (response.uid) {
                    setAudioList([response.uid, ...audioList]);
                }
                toast.success('生成成功');
                setLoading(false);
            });
    }

    function downloadAudio(uid: string) {
        const link = document.createElement("a");
        link.href = `/audio/${uid}`;
        link.download = `${uid}.wav`;
        link.target = "_blank";
        link.click();
        toast.success('开始下载');
    }

    function deleteAudio(uid: string) {
        fetch(`/api/remove_chat/${uid}`).then((res) => res.json()).then((response) => {
            if (response.uid) {
                setAudioList(audioList.filter((a) => a !== response.uid));
                toast.success('成功删除');
            }
        });
    }

    useEffect( () => {
        const texts = new Map<number, string>();
        const promises: Array<Promise<any>> = [];
        audioList.map((uid, index) => {
            const res = fetch(`/api/get_audio_text/${uid}`);
            promises.push(res);
            const responsePromise = res.then((r) => r.json());
            promises.push(responsePromise);
            responsePromise.then((response) => {
                if (response.text) {
                    texts.set(index, response.text);
                }
            });
        });
        Promise.all(promises).then(() => {
            setAudioText(texts);
        });
    }, [audioList]);

    return (
        <Box sx={{p: 2, display: "flex", flexDirection: "column", justifyContent: "center", alightItems: "center", gap: 3}}>
            <Box sx={{ display: "flex", flexDirection: "row", justifyContent: "space-between", alignItems: "center", gap: 3, height: "50vh" }}>
                <Textarea
                    minRows={2}
                    sx={{width: "50%", height: "100%", borderRadius: 10}}
                    placeholder="输入一些内容吧 Type something here..."
                    value={t}
                    onChange={e => setT(e.target.value)}
                />
                <Box sx={{width: '50%', height: '100%', display: 'flex', flexDirection: 'column'}}>
                    <Sheet sx={{flex: 1, overflow: 'auto', borderRadius: 10, p: 2}} variant="outlined">
                        <List orientation="vertical">
                            {audioList.length === 0 ? (
                                <ListItem sx={{display: "flex", flexDirection: "column", justifyContent: "center", alignItems: "flex-start"}}>
                                    <Typography>
                                        尝试新生成一个音频
                                    </Typography>
                                    <Typography>
                                        Try to Generate a New Audio
                                    </Typography>
                                </ListItem>
                            ) : audioList.map((a, index) => (
                                <ListItem sx={{display: "flex", flexDirection: "column", justifyContent: "center", alignItems: "flex-start"}}>
                                    {index !== 0 ? <Divider sx={{mt: 2, mb: 2}}/> : <></>}
                                    <Box sx={{
                                        display: "flex",
                                        flexDirection: "row",
                                        justifyContent: "space-between",
                                        alignItems: "center",
                                        width: "100%"
                                    }}>
                                        <Typography>
                                            {audioText.get(index)}
                                        </Typography>
                                        <Box>
                                            <IconButton onClick={() => downloadAudio(a)}>
                                                <FileDownloadIcon/>
                                            </IconButton>
                                            <IconButton onClick={() => deleteAudio(a)}>
                                                <DeleteIcon/>
                                            </IconButton>
                                        </Box>
                                    </Box>
                                    <audio src={`audio/${a}`} controls style={{width: '100%'}}/>
                                </ListItem>
                            ))}
                        </List>
                    </Sheet>
                </Box>
            </Box>
            <Box>
                <Button sx={{width: "100%"}} onClick={newAudio} loading={loading}>
                    生成音频 Generate Audio
                </Button>
            </Box>
            <Box sx={{display: "flex", flexGrow: 1, gap: 3}}>
                <FormControl>
                    <FormLabel>
                        音色 Timbre
                    </FormLabel>
                    <Autocomplete
                        options={timbreOptions}
                        value={timbreType}
                        onChange={(_e, value) => {
                            if (value) {
                                setTimbreType(value);
                            }
                        }}
                    />
                </FormControl>
                <FormControl sx={{flexGrow: 1}}>
                    <FormLabel>
                        聊天提示 Chat Prompt
                    </FormLabel>
                    <Input
                        value={chatPrompt}
                        onChange={(e) => setChatPrompts(e.target.value)}
                    />
                </FormControl>
            </Box>
        </Box>
    );
}
