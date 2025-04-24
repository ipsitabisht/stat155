
## Introduction

### Questions:

What audio features best predict a track's popularity within specific genres, and how do these success factors differ across genres? Could track lists that deviate from the typical features of their genre still be successful?

### Motivation

In the digital world, streaming music on platforms like Spotify has made it easier than ever for people to listen to all kinds of music. With a vast amount of songs available to stream, there is also a lot of information available to understand the different features of songs that can be helpful in understanding trends among the different genres. This amount of information can help us learn more about what contributes to the success of a song based on those musical features and elements which in turn can assist in predicting if a song will be a hit within its genre.

Some studies have shown that there were common features that top chart songs had based on musical elements like tempo, energy, etc. However these studies didn't look into what made certain songs popular within a specific genre. Each genre has its own distinct characteristics and audience which can make certain musical elements more likely to contribute to the success of the song.

That is why I will be studying how these different musical features can contribute to the success of certain songs within a genre and also look into what other attributes come about while exploring the data set. This can be helpful in understanding trends and evolution of musical preferences and also can be applicable to music producers/artists who want to enhance their musical performance and production within the genre they cater to.

#### reference

Interiano, M., Kazemi, K., Wang, L., Yang, J., Yu, Z., & Komarova, N. L. (2018). Musical trends and predictability of success in contemporary songs in and out of the top charts. Royal Society Open Science

### Hypothesis

...

### Spotify TrackList Dataset

This data set provides a comprehensive overview of over 100,000 tracks in Spotify and contains songs from over 125 different genres. Each observation in the data set contains the track metadata (name, album, artist, duration), popularity scale, and numerous musical features. The popularity scale is given by Spotify as a range from 0-100 based mostly on recent listening activity. The musical features and metrics for example are danceability, tempo, liveness, valence, etc which are derived from Spotify's own algorithms and techniques.

These features and metrics come from the Spotfiy's Web API that is able to get audio feature information based on the trackid.
