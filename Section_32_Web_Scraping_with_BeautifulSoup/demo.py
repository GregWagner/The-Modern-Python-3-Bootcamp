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
print(soup)
print("-" * 40)
print(soup.body)
print("-" * 40)
print(soup.body.div)
print("-" * 40)
print(soup.find("div"))
print("-" * 40)
print(soup.find_all("div"))
print("-" * 40)
print(soup.find(id="first"))
print("-" * 40)
print(soup.find_all(class_="special"))
print("-" * 40)
print(soup.find_all(attrs={"data-example": "yes"}))
print(type(soup))

# by CSS Selectors
print("-" * 40)
print(soup.select("#first")[0])
print("-" * 40)
print(soup.select(".special"))
print("-" * 40)
print(soup.select("div"))
print("-" * 40)
print(soup.select("[data-example]"))
