# NetFlex 

A Netflix-style web app for browsing a database of legendary bodybuilders. Search athletes, like your favourites, and see the most popular ones on the homepage.

Built as a team project with Flask, MongoDB and vanilla JavaScript.



> Demo video: see `Netflex.mp4` in this repo.

Features

- **Homepage** with the top 5 most liked athletes
- **Athletes page** with a case-insensitive search by name
- **Like button** that updates the counter instantly and saves it to the database
- Responsive dark UI built with Bootstrap 5
- Seed script that fills the database with 20 athletes

# Tech stack

| Layer | Tools |
|---|---|
| Backend | Python, Flask, Flask-PyMongo, Flask-CORS |
| Database | MongoDB |
| Frontend | HTML (Jinja2 templates), Bootstrap 5, vanilla JavaScript (fetch API) |

# API endpoints

| Method | Route | Description |
|---|---|---|
| GET | `/` | Homepage |
| GET | `/items` | Athletes page |
| GET | `/search?name=<text>` | Athletes matching the name, sorted by price (desc) |
| GET | `/popular` | Top 5 athletes by number of likes |
| POST | `/like` | Increments the likes of an athlete (`{"id": "<athlete id>"}`) |

# Run locally

Requirements: Python 3.9+ and a running MongoDB instance on `localhost:27017`.

```bash
git clone https://github.com/gianniskallionis/netflex.git
cd netflex

python -m venv venv
source venv/bin/activate       
pip install -r requirements.txt

python seed.py                  # fills the database with athletes
python app.py                   # starts the server
```

Then open http://127.0.0.1:5000

# Project structure

```
netflex/
├── app.py            # Flask app and API routes
├── seed.py           # Fills MongoDB with the athletes
├── templates/        # base.html, homepage.html, items.html
├── static/           # style.css, items.js, images
└── Netflix.mp4       # demo video
```

# Team

| Name | Role |
|---|---|
| Giannis Kallionakis | Fullstack / API |
| Nikos Psomadakis | Fullstack / Database |
| Antonis Gardikiotis | Frontend / Templates |
| Nikolai Zernov | Frontend / UI-UX |

# Note

Athlete photos are used for educational purposes only.
