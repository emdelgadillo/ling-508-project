# Exercise Search
This project provides a REST API that allows users to search for exercises by available equipment, muscle group, and workout type.

## Disclaimer:
This project has been tested on Linux. It should also run on Windows and macOS as long as Docker is installed, but behavior may vary slightly depending on the system setup.

## Steps to use this repo with Pycharm:
* Please ensure that you have [Docker](https://docs.docker.com/engine/) installed on your system.
* Clone this repository to your machine by opening your terminal, navigating to the folder in which you would like this repository to live, then entering this command: **git clone https://github.com/emdelgadillo/ling-508-project.git**
* Open Pycharm and select file > open and navigate to the main project folder 'ling-508-project' and hit OK
* You will then open a terminal in pycharm in the root directory (aka the ling-508-project folder) and type **docker-compose up**
* To ensure that all the docker containers opened properly you can type **docker ps** in either a pycharm terminal or your local terminal
* If properly started, you will see 2 docker containers, one for the app and one for the db
* To find more docker commands, visit https://docs.docker.com/get-started/docker_cheatsheet.pdf
