import {Box, List, ListItem, Typography} from "@mui/joy";

export default function NavBar() {
    return (
        <Box sx={{ position: 'sticky', top: 0, left: 0, width: '100%' }}>
            <List sx={{ flexGrow: 1 }} orientation="horizontal">
                <ListItem>
                    <Typography level="h4">
                        ChatTTS Web
                    </Typography>
                </ListItem>
            </List>
        </Box>
    );
}
