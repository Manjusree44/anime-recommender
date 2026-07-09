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

    print("\nAvailable Genres:\n")

    for genre in genres:
        print(f"- {genre}")

    user_genre = input("\nThe genre you want is: ")

    print("\nRecommended Anime:\n")

    for row in reader:
        if row["Genre"].lower() == user_genre.lower():
            print(row["Name"])

       