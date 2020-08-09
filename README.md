# API for appliance shop    

# Requirements
Python *3.X*  
Pipenv  (`pip install pipenv`)
SQLite3    

# Installation
Clone folder
```
git clone https://github.com/Rissap/djangorest-shop
```    
In *djangorest-shop* create **.env** file. Use **.env.example** to fill the **.env** file with required variables.

Install virtualenv and packages(in */djangorest-shop*):
```
pipenv install
pipenv shell
```    
In *django* folder:
1. Make migrations
```
python manage.py migrate
```
  2. Create superuser (use **admin** for user&password)  
```
python manage.py createsuperuser
```  
2. Run server
```
python manage.py runserver
```

Use *sql* folder to insert test data to database (or you can use **admin** panel in django). By default, API uses **sqlite3**.

# API requests  
Use Postman to make queries. In *postman/* open collection of all requests.