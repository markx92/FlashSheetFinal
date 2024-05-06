
from app.db import BaseModel

class Sandwich(BaseModel):

    SHEET_NAME = "sandwiches"

    COLUMNS = ["name", "price", "filling", "photo"]

    SEEDS = [
        {"name": "Philly Cheesesteak", "price": "12.99", "filling": "thin sliced steak with melted provolone cheese, white American cheese, or Cheez Whiz, as well as fried onions", "photo": "https://shorturl.at/aCMUY"},
        {"name": "Meatball Sub", "price": "13.99", "filling": "fresh made beef and pork meatballs, marinara sayce, melty provolone cheese", "photo": "https://shorturl.at/buU26"},
        {"name": "Caprese Sandwich", "price": "9.99", "filling": "mozzarella, tomato, basil, and the fixins", "photo": "https://shorturl.at/BKQW8"},
        {"name": "The Original Italian", "price": "11.99", "filling": "morty-d, salami, provolone, onions, pickles, vinegar, lettuce and tomato, can't get any better", "photo": "https://shorturl.at/empZ9"},
    ]


if __name__ == "__main__":

    sandwiches = Sandwich.all()
    print("FOUND", len(sandwiches), "SANDWICHES")
    if any(sandwiches):
        for sandwich in sandwiches:
            print(sandwich.name, sandwich.price, sandwich.filling, sandwich.photo)
    else:
        Sandwich.seed()

