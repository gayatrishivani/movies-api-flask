# Flask API
The movie API contains ‘api’ and requirements.txt folder and file respectively.

## Run the API
To run the api, use the following command
``` cmd
pip install -r requirements.txt
set FLASK_APP=api 
flask run
```
## CURD operations of API
Urls for the operation

1. Add movie : localhost:5000/add_movie (POST method)
2. Show movie: localhost:5000/movies 
3. Delete movie: localhost:5000/delete/<id> (DELETE/GET method)
4. Update movie: localhost:5000/update (POST method)
