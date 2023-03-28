# Viewsbook
It is an online social media platform where users can review each other. Also Users can post pictures with cool effects like cartoonify effect.


### Setup For Dev Environment

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/ADITYA97-CODER/cartoonify-website
$ cd cartoonify-website
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ virtualenv2 --no-site-packages venv
$ source venv/bin/activate
```
Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt    # Install all requirements
(env)$ python manage.py makemigrations    # Make Database Migrations
(env)$ python manage.py migrate           # Migrate Changes
```
Note the `(venv)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv2`.

Once `pip` has finished downloading the dependencies:
```sh
(venv)$ python manage.py runserver
```
## Demo
![screenshot](https://github.com/ADITYA97-CODER/cartoonify-website/blob/a2da1c4ac9fb0329f0e0015dc7f97c8b0fc055b9/login%20and%206%20more%20pages%20-%20Personal%20-%20Microsoft%E2%80%8B%20Edge%203_27_2023%2012_31_22%20PM.png)![screenshot](https://github.com/ADITYA97-CODER/cartoonify-website/blob/93d0cdc9383d00a588cf4c31e36fd23c23cac9f4/login%20and%206%20more%20pages%20-%20Personal%20-%20Microsoft%E2%80%8B%20Edge%203_27_2023%2012_32_47%20PM.png)![screenshot](https://github.com/ADITYA97-CODER/cartoonify-website/blob/93d0cdc9383d00a588cf4c31e36fd23c23cac9f4/login%20and%206%20more%20pages%20-%20Personal%20-%20Microsoft%E2%80%8B%20Edge%203_27_2023%2012_32_26%20PM.png)


## Demo

## Authors

* **Aditya Ojha** - *Initial work* - [ADITYA97-CODER](https://github.com/ADITYA97-CODER)


## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc


