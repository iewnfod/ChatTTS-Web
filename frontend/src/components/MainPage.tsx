import {Autocomplete, Box, Button, FormControl, FormLabel, List, ListItem, Textarea, Typography} from "@mui/joy";
import {Audio} from "../scripts/audio.ts";

export default function MainPage({
    audioList,
    timbreOptions
} : {
    audioList: Array<Audio>,
    timbreOptions: Array<string>
}) {
    return (
        <Box sx={{p: 2, display: "flex", flexDirection: "column", justifyContent: "center", alightItems: "center", gap: 3}}>
            <Box sx={{ display: "flex", flexDirection: "row", justifyContent: "space-between", alignItems: "center", gap: 3, height: "50vh" }}>
                <Textarea minRows={2} sx={{width: "50%", height: "100%", borderRadius: 10}}
                    placeholder="输入一些内容吧 Type something here..."
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
                                <audio src={`audio/${a.uid}`}/>
                            </ListItem>
                        ))}
                    </List>
                </Box>
            </Box>
            <Box>
                <Button sx={{width: "100%"}}>
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
