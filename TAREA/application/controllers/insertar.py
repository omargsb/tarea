import web

render= web .template.render('application/views/',base='master')


class Insertar:
    def __init__(self):
        pass

    def GET(self):
        datos=['7721121700','37']
        return render.insertar(datos)
        