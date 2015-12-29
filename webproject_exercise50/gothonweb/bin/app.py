import web

urls = (
    '/', 'Index',
    '/hello', 'Hello'
)

app = web.application(urls, globals())

render = web.template.render('templates/')


class Hello(object):
    def GET(self):
        form = web.input(name="Nobody", greet="Hello")
        if form.greet:
            greeting = "%s, %s" % (form.greet, form.name)
            return render.index(greeting = greeting) # run it as http://localhost:8080/hello?name=Frank&greet=Hola
        else:
            return "ERROR: greet is required."


class Index(object):
    def GET(self):
        greeting = "Hello World"
        return render.index(greeting = greeting)

if __name__ == "__main__":
    app.run()