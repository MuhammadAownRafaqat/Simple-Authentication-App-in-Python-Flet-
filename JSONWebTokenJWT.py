import flet as ft
import datetime
import jwt

SECRET_KEY = "ABC123"
password = "abc"
username = "abc"

def create_jwt_token(user_id):
    payload = {
        'sub': user_id,
        'iat': datetime.datetime.now(datetime.timezone.utc),
        'exp': datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=1) 
    }
    return jwt.encode(payload, SECRET_KEY, algorithm = 'HS256')

def validate_jwt_token(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms = ['HS256'])
        return payload
    except jwt.ExpiredSignatureError:
        return "The token got expired"
    except jwt.InvalidTokenError:
        return "Somethine changed in the token"






def function(page: ft.Page):
    page.window.height = 500
    page.window.width = 500

    def login():
        if password == "abc" and username == "abc":
            token = create_jwt_token("user_parker")
            page.add(ft.Text(f"Token has been created: {token}"))
            token = validate_jwt_token(token)
            page.add(ft.Text(f"Validation was successful: {token}"))
        else:
            page.add(ft.Text(value = "Either the password or the username is incorrect"))

    buttonn = ft.TextButton(text = "Login", on_click= lambda _: login())
    page.add(buttonn)
ft.app(function)
