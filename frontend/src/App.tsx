import {Box} from "@mui/joy";
import NavBar from "./components/NavBar.tsx";
import MainPage from "./components/MainPage.tsx";
import {useEffect, useState} from "react";

function App() {
    const [audioList, setAudioList] = useState<Array<string>>([]);

    useEffect(() => {
        fetch('/api/get_audio_list').then((res) => res.json())
            .then((response) => {
                console.log(response);
                setAudioList(response.audioList);
            });
    }, []);

    return (
        <Box sx={{display: "flex", flexDirection: "column"}}>
            <NavBar/>
            <MainPage audioList={audioList} setAudioList={setAudioList}/>
        </Box>
    );
}

export default App;
