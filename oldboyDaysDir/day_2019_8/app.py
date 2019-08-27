
import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        print('GET:......')
        u = self.get_argument('user')
        p = self.get_argument('passwd')

        if u == 'alex':
            if p == '123456':
                self.write("ok")
            else:
                self.write('Error Passwd')
        else:
            self.write("Error User")

    def post(self,*args,**kwargs):
        print('POST:......')
        u = self.get_argument('user')
        p = self.get_argument('passwd')

        if u == 'alex':
            if p == '123456':
                self.write("ok")
            else:
                self.write('Error Passwd')
        else:
            self.write("Error User")
app = tornado.web.Application([(r"/index",MainHandler)])

if __name__ == "__main__":
    app.listen(8888)
    tornado.ioloop.IOLoop.instance().start()