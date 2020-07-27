# Benford's Law
This is a small flask application that will consume a file of census data, assert Benford's law & display a bar graph with Chart.js. 
A small [trello board](https://trello.com/b/bzN5qSoy/project) I made for this project (remaining items deal with docker)

## To run:
My dockerfile is currently not working so you will have to run via flask (in the main directory):
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