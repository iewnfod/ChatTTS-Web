import {Autocomplete, Box, Button, FormControl, FormLabel, List, ListItem, Textarea, Typography} from "@mui/joy";
import {useState} from "react";

export default function MainPage({
    audioList,
    setAudioList
} : {
    audioList: Array<string>,
    setAudioList: (a: Array<string>) => void,
}) {
    const [t, setT] = useState<string>("");

    const timbreOptions: Array<string> = ["female", "male"];

    function newAudio() {
        fetch('/api/new_chat', {
            method: "POST",
            body: JSON.stringify({
                text: t
            })
        }).then((res) => res.json())
            .then((response) => {
                if (response.uid) {
                    setAudioList([response.uid, ...audioList]);
                }
            });
    }

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
                <Box sx={{width: "50%", height: "100%"}}>
                    <List orientation="vertical" variant="outlined" sx={{borderRadius: 10, height: '100%'}}>
                        {audioList.length === 0 ? (
                            <ListItem sx={{display: "flex", flexDirection: "column", justifyContent: "center", alignItems: "flex-start"}}>
                                <Typography>
                                    尝试新生成一个音频
                                </Typography>
                                <Typography>
                                    Try to Generate a New Audio
                                </Typography>
                            </ListItem>
                        ) : audioList.map((a) => (
                            <ListItem>
                                <audio src={`audio/${a}`} controls/>
                            </ListItem>
                        ))}
                    </List>
                </Box>
            </Box>
            <Box>
                <Button sx={{width: "100%"}} onClick={newAudio}>
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
                    />
                </FormControl>
            </Box>
        </Box>
    );
}
