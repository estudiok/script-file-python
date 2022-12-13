from jinja2 import Environment, FileSystemLoader

title = "A15 La cancion del lobo / Wolfsong"
image = "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiKRKgl0Vo1mHActU-OcaDmcA2qHvwxM54TCbAelVOSBGkiEH207Ao8WcldzpKWMq38xtoIvCvbfq2Su576BP5rVi0_tpEXNUoIHeRCBAkKt3rM3O1JKCJCU40pJzztDmuzO8txPzlp6K3mk4C6UDd5GnFrnIcXdS4nrk4bKn9V8w6ewTTtCTYOytiF/s320/cancionlobo.jpg"
autor =  "TJ Klune" 
link1 = "https://drive.google.com/uc?export=download&id=1lnK5xrUE8PpeOmliBbYawNYgY4REpKX8"
link2 = "https://www.dropbox.com/s/qmd5ugy0jtxttaf/La%20cancion%20del%20lobo%20Wolfsong%20%28TJ%20KLUNE%29%20%28wotrolib.blogspot.com%29.pdf?dl=1"
link3 = "https://onedrive.live.com/download?cid=9A0B75B7C7F57F18&resid=9A0B75B7C7F57F18%21106&authkey=AHT9V9SqndUIfvY&em=2" 

environment = Environment(loader=FileSystemLoader("templates/"))
template = environment.get_template("message.txt")

content = template.render(
    title = title,
    image = image,
    autor =  autor,
    link1 = link1,
    link2 = link2,
    link3 = link3 
)

with open("perro.txt", mode="w", encoding="utf-8") as message:
    message.write(content)
    print(f"... wrote perro.txt")
