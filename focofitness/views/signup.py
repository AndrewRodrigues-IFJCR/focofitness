import flet as ft


async def signup_view_factory(page: ft.Page) -> ft.View:
    return ft.View(
        route='/signup',
        controls=[
            ft.Text('signup'),
            ft.ElevatedButton(
                'Login', on_click=lambda _: page.go_async('/login')
            ),
        ],
    )
