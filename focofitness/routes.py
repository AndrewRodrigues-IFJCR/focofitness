import flet as ft
from controllers import login, signup
from .views import login_view_factory, signup_view_factory
from fastapi import FastAPI

def configure_routes(app: FastAPI):

    # Views:
    def main(page: ft.Page):

        pages = {
            'login': await login_view_factory(page),
            'signup': await signup_view_factory(page),
        }

        def on_change_route(event: ft.RouteChangeEvent):
            page.views.clear()
            page.views.append(pages[event.route])
            page.update()

        page.on_route_change = on_change_route

    app.mount('/views', ft.fastapi.app(main))

    # Controllers:
    login.subscribe_controller(app)
    signup.subscribe_controller(app)
