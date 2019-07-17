import random

def generate_page(head, body):
    page = "<html>" + head + body + "</html>"
    return page

def generate_head(title):
    head = "<meta charset = 'utf-8'> " + "<title>" + title + "</title>"
    return "<head>" + head + "</head>"

def generate_body(header):
    body = "<h1>" + header + "</h1>"
    url = "index.html"

    time = ["Утром", "После обеда", "Вечером"]
    do = ["Остерегайтесь", "ожидайте"]

    for i in range(0, len(time)):
        body += "<p>" + random.choice(time) + "</p>"

    for i in range(0, len(do)):
        body += "<ul>" + "<li>" + random.choice(do) + "</li>" + "</ul>"

    link = '<a href="' + url + '">html</a>'
    body += link

    return body

def save_page(title, header, output="about.html"):
    fp = open(output, "w", encoding="utf-8")
    page = generate_page(
        head=generate_head(title),
        body=generate_body(header)
    )
    print(page, file=fp)
    fp.close()

save_page(title='About', header = 'О чем все это')





