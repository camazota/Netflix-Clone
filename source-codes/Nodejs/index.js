const express = require("express");
const path = require("path");

const app = express();
const port = 8080;




const films = [
    {
        image: "/film-images/you.jpg"
    },
    { image: "/film-images/mrrobot.jpg" },

    {
        image: "/film-images/lacasadepapel.jpg"
    },
    { image: "/film-images/strangerthings.webp" },
    {
        image: "/film-images/squidgame.jpg"
    },
    { image: "/film-images/peakyblinders.webp" },
    { image: "/film-images/blackmirror.jpg" },
    { image: "/film-images/queensgambit.jpg" },
    { image: "/film-images/vikings_0.webp" },
    { image: "/film-images/wednesday.jpg" }

];

app.use(express.static(path.join(__dirname, "../../","static")))

app.get("/", (req, res) => {
    res.sendFile(path.join(__dirname,"../../", "templates", "index.html"))
})


app.get("/api/films/popular", (req, res) => {
    res.json(films)
})




app.listen(port, () => {
    console.log(`Sunucu ${port} portunda dinleniyor!`);
})