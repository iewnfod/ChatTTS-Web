import {Box} from "@mui/joy";
import NavBar from "./components/NavBar.tsx";
import MainPage from "./components/MainPage.tsx";
import {useState} from "react";
import {Audio} from "./scripts/audio.ts";

function App() {
    const [audioList, setAudioList] = useState<Array<Audio>>([]);
    const [timbreOptions, setTimbreOptions] = useState<Array<string>>([]);

    return (
        <Box sx={{display: "flex", flexDirection: "column"}}>
            <NavBar/>
            <MainPage audioList={audioList} timbreOptions={timbreOptions}/>
        </Box>
    );
}

export default App
