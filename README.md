# Benford's Law
This is a small flask application that will consume a file of census data, assert Benford's law & display a bar graph with Chart.js. 

## Trello
A small [trello board]() I made for this project (remaining items deal with docker)

## To run:
### Via Docker
Build image first
>sudo docker build -t benford.

Run container
>sudo docker run --publish 5000:5000 --name test
Should be good to go!

### Via Flask
#### Linux/Mac
>$ export FLASK_APP=flaskr
>
>$ export FLASK_ENV=development
>
>$ flask run

#### Windows cmd
> set FLASK_APP=flaskr
>
> set FLASK_ENV=development
>
> flask run

#### Window powershell
> $env:FLASK_APP = "flaskr"
>
> $env:FLASK_ENV = "development"
>
> flask run
Should be good to go!
