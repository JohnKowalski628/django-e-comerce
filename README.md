# django-e-comerce
E-commerce website for selling tennis equipment

## General info
A web application that enables the sale of tennis equipment in a user-friendly and convenient way,
while providing an effective tool for users. The application allows you to easily add products,
manage inventory and handle service. It provides access to a range of services, quick and 
trouble-free implementation and customer service control.

## Technologies
Project is created with:
* Python version: 3.11.2
* Django version: 4.2.6
* Vue.js version: v3.3.4.
* Bootstrap version: 4.0.0
* Stripe version: 8.0.1

## Features
* User Registration and Authentication
* Product Browsing and Search
* Shopping Cart Management
* Secure Online Payment Processing (Stripe Integration)
* User Ratings and Reviews
* Administrative Panel for Content Management

## Setup
### 1. Clone repository
```
git clone https://github.com/JohnKowalski628/django-e-comerce.git
```
### 2. Setup Virtualenv
```
virtualenv env
source env/bin/activate
```
### 3. Install stripe
```
pip install stripe
```
### 4. Migrate and Start Server
```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
