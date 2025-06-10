import flet as ft

def main(page: ft.Page):
    page.title = "Wacko Gani - Flet"
    page.theme_mode = "light"
    page.padding = 0
    page.bgcolor = ft.Colors.BLACK

    def on_nav_click(e):
        print(f"{e.control.data} clicked!")

    def handle_hover(e):
        e.control.bgcolor = ft.Colors.with_opacity(0.1, ft.Colors.WHITE) if e.data == "true" else None
        e.control.update()

    def nav_button(text, icon):
        return ft.Container(
            content=ft.Column([
                ft.Icon(icon, size=24, color=ft.Colors.WHITE),
                ft.Text(text, size=12, color=ft.Colors.WHITE)
            ], alignment="center", horizontal_alignment="center"),
            width=100, height=60, alignment=ft.alignment.center,
            ink=True, on_click=on_nav_click, on_hover=handle_hover,
            data="true", border_radius=8
        )

    page.add(
        ft.Container(
            ft.Row([
                ft.Image(src="duda-ko-ani-ba.jpg", width=40, height=40),
                ft.Text("Wacko Gani", size=20, weight="bold", color=ft.Colors.YELLOW_300),
            ], alignment="start", vertical_alignment="center", spacing=10),
            padding=10, bgcolor=ft.Colors.BLACK
        ),
        ft.Container(expand=True),
        ft.Container(
            ft.Row([
                nav_button("Home", ft.Icons.HOME),
                nav_button("Class", ft.Icons.SCHOOL),
                nav_button("Options", ft.Icons.SETTINGS),
            ], alignment="spaceEvenly"),
            bgcolor=ft.Colors.BLACK, padding=10, height=80
        )
    )

ft.app(target=main, assets_dir="assets")
