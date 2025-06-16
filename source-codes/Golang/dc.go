package main

import (
	"github.com/gofiber/fiber/v2"
)

type Film struct {
	Image string `json:"image"`
}

func main() {
	app := fiber.New()

	films := []Film{
		{Image: "/film-images/you.jpg"},
		{Image: "/film-images/mrrobot.jpg"},
		{Image: "/film-images/lacasadepapel.jpg"},
		{Image: "/film-images/strangerthings.webp"},
		{Image: "/film-images/squidgame.jpg"},
		{Image: "/film-images/peakyblinders.webp"},
		{Image: "/film-images/blackmirror.jpg"},
		{Image: "/film-images/queensgambit.jpg"},
		{Image: "/film-images/vikings_0.webp"},
		{Image: "/film-images/wednesday.jpg"},
	}

	app.Static("/", "./static")

	app.Get("/", func(c *fiber.Ctx) error {
		return c.SendFile("./templates/index.html")
	})

	app.Get("/api/films/popular", func(c *fiber.Ctx) error {
		return c.JSON(films)
	})

	err := app.Listen(":8080")
	if err != nil {
		panic(err)
	}
}