import flet 
from flet import Page, Text

def main(page: Page):
	page.add(Text(value="Hello World!"))

flet.app(target=main)
