import flet as ft


async def login_view_factory(page: ft.Page) -> ft.View:
    return ft.View(
        route='/login',
        controls=[
            ft.Text('Login'),
            ft.ElevatedButton(
                'Signup', on_click=lambda _: page.go_async('/signup')
            ),
        ],
    )
