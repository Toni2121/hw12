oscar_winners = {"Leonardo DiCaprio", "Meryl Streep", "Denzel Washington", "Emma Stone", "Tom Hanks", "Natalie Portman", "Robert De Niro", "Al Pacino"}
titanic_actors = {"Leonardo DiCaprio", "Kate Winslet", "Billy Zane", "Kathy Bates"}
dark_knight_actors = {"Christian Bale", "Heath Ledger", "Michael Caine", "Gary Oldman", "Aaron Eckhart"}
avengers_actors = {"Robert Downey Jr.", "Chris Evans", "Scarlett Johansson", "Mark Ruffalo", "Chris Hemsworth", "Jeremy Renner"}
iron_man_actors = {"Robert Downey Jr.", "Gwyneth Paltrow", "Terrence Howard"}
legendary_actors = {"Al Pacino", "Robert De Niro", "Marlon Brando", "Jack Nicholson", "Dustin Hoffman"}
actor_list = {"Robert Downey Jr.", "Chris Evans", "Scarlett Johansson", "Leonardo DiCaprio", "Tom Hanks"}
movie_cast = {"Tom Hanks", "Tom Cruise", "Will Smith", "Matt Damon", "Brad Pitt"}

oscar_winners.add("Emma watson")
print(oscar_winners)
oscar_winners.discard("Meryl Streep")
print(oscar_winners)
oscar_winners.copy()
print(oscar_winners)
# oscar_winners.clear()
# print(oscar_winners)
titanic_and_darkknight = titanic_actors & dark_knight_actors
print("titanic_and_darkknight -", titanic_and_darkknight)
print("No actor played in both movies")
ironman_and_avengers = iron_man_actors.isdisjoint(avengers_actors)
print("ironman_and_avengers -", ironman_and_avengers)
oscar_winners_and_actors = oscar_winners <= actor_list
print("oscar_winners_and_actors -", oscar_winners_and_actors)
actors_and_avengers = actor_list <= avengers_actors
print("actors_and_avengers -", actors_and_avengers)
movie_cast.discard("Will Smith")
print(movie_cast)
titanic_and_oscar = titanic_actors - oscar_winners
print("titanic_and_oscar -", titanic_and_oscar)
titanic_or_darkknight = titanic_actors ^ dark_knight_actors
print("titanic_or_darkknight -", titanic_or_darkknight)
Blanchett_Cate_Lewis_Day_Daniel = {"Blanchett Cate", "Lewis-Day Daniel"}
oscar_winners.update(Blanchett_Cate_Lewis_Day_Daniel)
print(oscar_winners)
titanic_union_darkknight = titanic_actors | dark_knight_actors
print(titanic_union_darkknight)
dark_knight_rises_actors = {"Christian Bale", "Michael Caine", "Gary Oldman",
"Tom Hardy", "Joseph Gordon-Levitt"}
dark_knight_rises_and_darkknight = dark_knight_actors <= dark_knight_rises_actors
print(dark_knight_rises_and_darkknight)
legendary_and_oscar = legendary_actors >= oscar_winners
print(legendary_and_oscar)
avengers_who_were_not_in_ironman = avengers_actors - iron_man_actors
print(avengers_who_were_not_in_ironman)
only_darkknight_or_only_avengers = dark_knight_actors ^ avengers_actors
print(only_darkknight_or_only_avengers)
ironman_union_darkknight = iron_man_actors | dark_knight_actors
print(ironman_union_darkknight)
fs = frozenset(legendary_actors)
print(fs)