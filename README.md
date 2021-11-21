# ECOMMERCE_API
Ecommerce API created with python django framework
---
# End Points
| Request Type | End Point | Description |
| ----------- | ----------- | ----------- |
| `GET` | /api/v1/users/ | get info about the logged in user |
| `GET` | /api/v1/latest-products/ | get newly released products. (by default latest 5 products will be returned in response | 
| `GET` | /api/v1/products/{category slug}/ | get all the products from a specific category | 
| `GET` | /api/v1/products/{category slug}/{product slug}/ | get details about a specific product | 
| `GET` | /api/v1/orders/ | get orders for the logged in user |
| `POST` | /api/v1/token/login/ | send 'username' and 'password' and in response you will get auth token |
| `POST` | /api/v1/users/ | register a new user. |
| `POST` | /api/v1/{djoser endpoints}/ | You can use djoser endpoints. [djoser docs](https://djoser.readthedocs.io/en/latest/getting_started.html#available-endpoints)  |
| `POST` | /api/v1/checkout/ | send details to process stripe charge and create orders | 

# Docker 

```bash
docker-compose up
```

# Manual Installations & Setup 
1. Clone the repo to local system 
``` 
git clone https://github.com/akhtersoyeb/ECOMMERCE_API.git
```
3. Install the packages from requirements.txt file.
```
pipenv install -r requirements.txt 
```
4. Create a account in stripe website and generate you API keys . 
5. Go to config/settings.py file and edit the line 
``` 
# config/settings.py 
STRIPE_SECRET_KEY = 'put your stripe secret key here'
```
6. Make the migrations and run the migrate command from terminal 
``` 
python manage.py makemigrations 
python manage.py migrate 
``` 
---
> Working on more details and features to add to the API. If anything is wrong with the code please create a issue. 
