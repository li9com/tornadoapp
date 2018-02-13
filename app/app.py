import tornado.ioloop
import tornado.web
import datetime
import platform

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        now = datetime.datetime.now()
        self.write("This is an example Python applicaiton\n")
        self.write("It is running on " +platform.node() +"\n" )
        self.write("Current time is " + str(now)+"\n")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    #app = tornado.httpserver.HTTPServer(make_app)
    app.listen(8888, '0.0.0.0')
    tornado.ioloop.IOLoop.current().start()

