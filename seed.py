from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["netflex"]
collection = db["athletes"]

athletes = [
    {
        "name": "Arnold Schwarzenegger",
        "photo": "/static/assets/images/arnold.jpg",
        "description": "7x Mr. Olympia. The face of bodybuilding worldwide.",
        "likes": 0,
        "nationality": "Austrian",
        "era": "1970s",
        "price": 10000
    },
    {
        "name": "Ronnie Coleman",
        "photo": "/static/assets/images/ronnie.jpg",
        "description": "8x Mr. Olympia. Known for his iconic lifts and unmatched mass.",
        "likes": 0,
        "nationality": "American",
        "era": "2000s",
        "price": 9500
    },
    {
    "name": "Giannis Kallionakis",
    "photo": "/static/assets/images/GiannisKallionakis.jpg",
    "description": "Creator of the site, Best coder out of all 20 bodybuilders ",
    "likes": 0,
    "nationality": "Greek",
    "era": "2020s",
    "price": 9000
},
    {
        "name": "Dexter Jackson",
        "photo": "/static/assets/images/dexter_jackson.jpg",
        "description": "Mr. Olympia 2008. Longest competitive career in bodybuilding history.",
        "likes": 0,
        "nationality": "American",
        "era": "2000s",
        "price": 6500
    },
    {
        "name": "Dorian Yates",
        "photo": "/static/assets/images/dorian_yates.jpg",
        "description": "6x Mr. Olympia. Pioneer of the mass monster era.",
        "likes": 0,
        "nationality": "British",
        "era": "1990s",
        "price": 7500
    },
    {
        "name": "Flex Wheeler",
        "photo": "/static/assets/images/flex_wheeler.jpg",
        "description": "4x Arnold Classic champion. Called the most genetically gifted ever.",
        "likes": 0,
        "nationality": "American",
        "era": "1990s",
        "price": 6500
    },
    {
        "name": "Franco Columbu",
        "photo": "/static/assets/images/franco_columbu.jpg",
        "description": "2x Mr. Olympia and Arnold's closest training partner.",
        "likes": 0,
        "nationality": "Italian",
        "era": "1970s",
        "price": 5500
    },
    {
        "name": "Hidetada Yamagishi",
        "photo": "/static/assets/images/hidetada_yamagishi.jpg",
        "description": "Top IFBB Pro. First Japanese athlete to compete at Mr. Olympia.",
        "likes": 0,
        "nationality": "Japanese",
        "era": "2010s",
        "price": 4000
    },
    {
        "name": "Jay Cutler",
        "photo": "/static/assets/images/jay_cutler.webp",
        "description": "4x Mr. Olympia. Known for incredible size and work ethic.",
        "likes": 0,
        "nationality": "American",
        "era": "2000s",
        "price": 8000
    },
    {
        "name": "Kai Greene",
        "photo": "/static/assets/images/kai_greene.webp",
        "description": "3x Arnold Classic champion. Known for his artistic approach to bodybuilding.",
        "likes": 0,
        "nationality": "American",
        "era": "2010s",
        "price": 7000
    },
    {
        "name": "Kevin Levrone",
        "photo": "/static/assets/images/kevin_levrone.jpg",
        "description": "4x Mr. Olympia runner-up. Known as the Maryland Muscle Machine.",
        "likes": 0,
        "nationality": "American",
        "era": "1990s",
        "price": 6000
    },
    {
        "name": "Lee Haney",
        "photo": "/static/assets/images/lee_haney.jpg",
        "description": "8x Mr. Olympia. First to win 8 consecutive titles.",
        "likes": 0,
        "nationality": "American",
        "era": "1980s",
        "price": 7000
    },
    {
        "name": "Lou Ferrigno",
        "photo": "/static/assets/images/lou_ferrigno.jpg",
        "description": "2x IFBB Mr. Universe. Known for his role as The Incredible Hulk.",
        "likes": 0,
        "nationality": "American",
        "era": "1970s",
        "price": 6000
    },
    {
        "name": "Phil Heath",
        "photo": "/static/assets/images/phil_heath.jpg",
        "description": "7x Mr. Olympia. Exceptional symmetry and conditioning.",
        "likes": 0,
        "nationality": "American",
        "era": "2010s",
        "price": 8500
    },
    {
        "name": "Rich Gaspari",
        "photo": "/static/assets/images/rich_gaspari.webp",
        "description": "3x Mr. Olympia runner-up. Pioneer of conditioning in bodybuilding.",
        "likes": 0,
        "nationality": "American",
        "era": "1980s",
        "price": 5000
    },
    {
        "name": "Sergio Oliva",
        "photo": "/static/assets/images/sergio_oliva.jpg",
        "description": "3x Mr. Olympia. The only man to beat Arnold at the Olympia.",
        "likes": 0,
        "nationality": "Cuban",
        "era": "1960s",
        "price": 5000
    },
    {
        "name": "Shawn Ray",
        "photo": "/static/assets/images/shawn_ray.jpg",
        "description": "Top Olympia competitor throughout the 1990s. Known for perfect conditioning.",
        "likes": 0,
        "nationality": "American",
        "era": "1990s",
        "price": 5000
    },
    {
        "name": "Shawn Rhoden",
        "photo": "/static/assets/images/shawn_rhoden.webp",
        "description": "Mr. Olympia 2018. Known for his incredible aesthetics and conditioning.",
        "likes": 0,
        "nationality": "American",
        "era": "2010s",
        "price": 5500
    },
    {
        "name": "Tom Platz",
        "photo": "/static/assets/images/tom_platz.jpg",
        "description": "Known as The Golden Eagle. Legendary for his incredible leg development.",
        "likes": 0,
        "nationality": "American",
        "era": "1980s",
        "price": 5500
    },
    {
        "name": "Chris Bumstead",
        "photo": "/static/assets/images/bumstead.jpg",
        "description": "4x Classic Physique Olympia. Modern era icon.",
        "likes": 0,
        "nationality": "Canadian",
        "era": "2020s",
        "price": 9000
    }
]


collection.drop()
collection.insert_many(athletes)      
collection.create_index([("name", "text")])