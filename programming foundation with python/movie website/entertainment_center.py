import fresh_tomatoes
import media

toy_story = media.movie("Toy Story", 
						"A story of a boy and toy that comes to life", 
						"http://ezenkiri.com/wp-content/uploads/2016/10/Toy-Story-4-.jpg",
						"https://www.youtube.com/watch?v=Bj4gS1JQzjk&t=3s")

avatar = media.movie("Avatar",
					"A marine on an Alien planet",
					"https://images-na.ssl-images-amazon.com/images/M/MV5BMTYwOTEwNjAzMl5BMl5BanBnXkFtZTcwODc5MTUwMw@@._V1_UX182_CR0,0,182,268_AL_.jpg",
					"https://www.youtube.com/watch?v=5PSNL1qE6VY")

hunger_games = media.movie("Hunger Games",
					"A reality game show",
					"https://images-na.ssl-images-amazon.com/images/I/91ikvZgoHZL._SL1500_.jpg",
					"https://www.youtube.com/watch?v=mfmrPu43DF8")

movies = [toy_story, avatar, hunger_games]
fresh_tomatoes.open_movies_page(movies)