# list of all packages that we are using 
library(tidyverse)
library(naniar)
library(superheat)
library(patchwork)


spotify_data <- read_csv("Project_1/data/spotify.csv")

View(spotify_data)

house <- spotify_data |> 
  filter(track_genre == "house")
ggplot(house, aes(danceability)) +
  geom_histogram(binwidth = 0.05, fill = "steelblue", colour = "white") +
  labs(title = "Danceability of HouseGenre Tracks",
       x = "Danceability (0=least, 1=most)",
       y = "Number of tracks") +
  theme_minimal(base_size = 12)
