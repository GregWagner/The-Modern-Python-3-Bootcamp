from bs4 import BeautifulSoup

html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <title>First HTML Page</title>
    </head>
    <body>
      <div id="first">
        <h3 data-example="yes">hi</h3>
        <p>more text.</p>
      </div>
      <ol>
        <li class="special">This list item is special.</li>
        <li class="special">This list item is also special.</li>
        <li>This list item is not special.</li>
      </ol>
      <div data-example="yes">bye</div>
    </body>
    </html>
    """

soup = BeautifulSoup(html, "html.parser")

data = soup.body.contents
print(data)
print('-' * 20)

data = soup.body.contents[1]
print(data)
print('-' * 20)

data = soup.body.contents[1].contents
print(data)
print('-' * 20)

# need to do twice to go over newline
data = soup.body.contents[1].next_sibling.next_sibling
print(data)
print('-' * 20)

data = soup.find(class_="special").parent
print(data)
print('-' * 20)

# does not display the newline like next_sibling
data = soup.find(id="first").find_next_sibling().find_next_sibling()
print(data)
print('-' * 20)

data = soup.select("[data-example]")[1].find_previous_sibling()
print(data)
print('-' * 20)

data = soup.find("h3").find_parent()
print(data)
print('-' * 20)
