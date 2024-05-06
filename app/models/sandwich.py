
from app.db import BaseModel

class sandwich(BaseModel):

    SHEET_NAME = "sandwiches"

    COLUMNS = ["sandwich", "price", "filling", "photo"]

    SEEDS = [
        {"sandwich": "Philly Cheesesteak", "price": "12.99", "filling": "thin sliced steak with melted provolone cheese, white American cheese, or Cheez Whiz, as well as fried onions", "photo": "https://shorturl.at/aCMUY"},
        {"sandwich": "Meatball Sub", "price": "13.99", "filling": "fresh made beef and pork meatballs, marinara sayce, melty provolone cheese", "photo": "https://shorturl.at/buU26"},
        {"sandwich": "Caprese Sandwich", "price": "9.99", "filling": "mozzarella, tomato, basil, and the fixins", "photo": "https://shorturl.at/BKQW8"},
        {"sandwich": "The Original Italian", "price": "11.99", "filling": "morty-d, salami, provolone, onions, pickles, vinegar, lettuce and tomato, can't get any better", "photo": "https://shorturl.at/empZ9"},
    ]


if __name__ == "__main__":

    sandwiches = sandwich.all()
    print("FOUND", len(sandwiches), "SANDWICHES")
    if any(sandwiches):
        for sandwich in sandwiches:
            print(sandwich.sandwich, sandwich.price, sandwich.filling, sandwich.photo)
    else:
        Sandwich.seed()

