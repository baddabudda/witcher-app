# Task 1. Basics of containerization

## Task Description

Set up a network of 2 Docker containers:

- One Hosts the database (SQLite or else)

- Other is your entry point

You must demonstrate the ability to query the container1 DB from container2. Data in the SQLite database must not disappear when you restart the containers!

## Application Info
This application consists of 3 main components:
- Vite+React frontend
- FastAPI backend
- MySQL database with SQL-script for initialization

Each component is represented by a corresponding folder.

List of endpoints as follows:
- GET / get current amount of coins that were given to the Witcher
- POST / edit current amount of coins (you can either toss (+1) or steal (-1) coins from the Witcher)

## Start
1. Clone the repository
```
git clone https://github.com/baddabudda/witcher-app.git
```
2. Build the application (Note: don't use `--detach` if you don't want containers to run in the background)
```
docker-compose up --build --detach
```
3. Visit `http://localhost:3000` in order to communicate with the application (entrypoint)

## Stop
In order to stop the application, use:
```
docker-compose down
```
If you want to remove images and cleanup volumes, use:
```
docker-compose down --rmi local --volumes
```
