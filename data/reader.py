import csv


with open("data/anime.csv", "r") as file:
    reader = csv.DictReader(file)

    genres = [
        "Psychological Thriller",
        "Psychological Action",
        "Psychological Sci-Fi",
        "Action Dark Fantasy",
        "Action Adventure",
        "Adventure Fantasy",
        "Action Supernatural",
        "Action Fantasy",
        "Historical Action",
        "Sci-Fi Thriller",
        "Dark Fantasy",
        "Action Horror",
        "Action Superhero",
        "Sports",
        "Drama Romance",
        "Drama Slice of Life",
        "Drama",
        "Romance Fantasy",
        "Romance Slice of Life",
        "Fantasy Adventure",
        "Comedy Action",
        "Romantic Comedy",
        "Isekai Fantasy"
    ]
    option = input('enter the number 1 for anime name and 2 for anime genre and 3 for exit ')
    if option == "1":
       user_name = input('enter the name of the anime' )
       for row in reader:
           if row['Name'].lower() == user_name.lower():
               print(f"\n'anime name is {row['Name']}, genre is {row['Genre']}")

    elif option == "2":
        
        print("\nAvailable Genres:\n")
        for genre in genres:
           print(f"- {genre}")
        user_genre = input('enter the genre you want from the available genres ')   
        print("\nRecommended Anime:(happy watching)\n")
        for row in reader:
               if row["Genre"].lower() == user_genre.lower():
                 print(row["Name"])
    elif option == "3":
        print('Thank you for using the anim rec, Happy watching.')
    else:
        print('invalid option, please enter 1 or 2 or 3')
        

       