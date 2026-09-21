import flet as ft
from PIL import Image
import xbrz
import io
import base64

def main(page: ft.page):
    page.tittle = "image upscaler"
    page.theme_mode = ft.ThemeMode.DARK
    page.vertical_alignment = ft.MainAxisAlignemt.START
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = 20
