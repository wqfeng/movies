import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://www.google.com/imgres?imgurl=http%3A%2F%2Fwww.impawards.com%2F1995%2Fposters%2Ftoy_story_ver2.jpg&imgrefurl=http%3A%2F%2Fwww.impawards.com%2F1995%2Ftoy_story_ver2.html&docid=giqTyWo_qCPS_M&tbnid=MHq3Le_UaWMA4M%3A&vet=1&w=509&h=755&client=opera&bih=1244&biw=1262&q=toy%20story%20poster&ved=0ahUKEwjY2Oniw_LRAhXCZiYKHVnHD2gQMwhFKAQwBA&iact=mrc&uact=8",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://www.google.com/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&cad=rja&uact=8&ved=0ahUKEwiKhtnRw_LRAhWBWCYKHYNEBJIQjRwIBw&url=https%3A%2F%2Fwww.movieposter.com%2Fq%2Favatar_posters.html&psig=AFQjCNFRys69Aot7psQvpF9p4NbTtJAw1g&ust=1486163240139587",
                     "https://www.youtube.com/watch?v=cRdxXPV9GNQ")

debbie_does_dallas = media.Movie("Debbie Does Dallas",
                                 "A cheerleader exposes some gaping holes to the Dallas Cowboys",
                                 "https://www.google.com/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&cad=rja&uact=8&ved=0ahUKEwij9PmyxvLRAhUK5iYKHe6lBmsQjRwIBw&url=http%3A%2F%2Fwww.allposters.com%2F-sp%2FDebbie-Does-Dallas-Retro-Adult-Movie-Poster-Posters_i9485495_.htm&psig=AFQjCNHZXikDEv8lf2AUuKighNbaoEr6og&ust=1486163978127250",
                                 "https://www.youtube.com/watch?v=Svfq2BqiHns")

faceoff = media.Movie("Faceoff",
                      "Faces used to be on, but now they're off",
                      "https://www.google.com/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&cad=rja&uact=8&ved=0ahUKEwjy4531x_LRAhVGwiYKHWXfAcIQjRwIBQ&url=http%3A%2F%2Fbollywoodcopy.com%2Fek-vilain-poster-is-copied-from-face-off%2F&psig=AFQjCNEWN0MlHCl0J81x95oOQaQ16CY6EQ&ust=1486164389255456",
                      "https://www.youtube.com/watch?v=YiwA3C2qeRo")

shrek = media.Movie("Shrek",
                    "An ogre learns to love a beautiful woman and despise a jackass, there is also a prince",
                    "https://www.google.com/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&cad=rja&uact=8&ved=0ahUKEwj7ktefyPLRAhWCRCYKHXs_AcUQjRwIBQ&url=https%3A%2F%2Fwww.pinterest.com%2Fpin%2F41587996529548970%2F&psig=AFQjCNE5b_6uCSuzjHEKrBIlcFpCoFskEw&ust=1486164478269436",
                    "https://www.youtube.com/watch?v=W37DlG1i61s")


clerks = media.Movie("Clerks",
                     "Two schmucks schmuck around for a while, lessons are learned",
                     "https://www.google.com/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&cad=rja&uact=8&ved=0ahUKEwjChszIyPLRAhWH2yYKHf38BGkQjRwIBw&url=http%3A%2F%2Fwww.impawards.com%2F1994%2Fclerks_ver4.html&psig=AFQjCNHBduwSRRDNfbBd24Ak0G6FvQjgBA&ust=1486164558885467",
                     "https://www.youtube.com/watch?v=Mlfn5n-E2WE")

movies = {toy_story, avatar, debbie_does_dallas, faceoff, shrek, clerks}
fresh_tomatoes.open_movies_page(movies)