import web

render= web .template.render('application/views/',base='master')


class Index:
    def __init__(self):
        pass

    def GET(self):
        datos=['Omar','omargsb@hotmail.com']
        return render.index(datos)
