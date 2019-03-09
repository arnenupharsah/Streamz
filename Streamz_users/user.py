import web
import model
import json
urls = ('/login', 'Login',
        '/logout', 'Logout',
        '/register', 'Register')



class Register:
    def GET(self):
	id=model.new_user('firstname','lastname','dfghbvd','erthfert','sdfgnbv','dghgfert')
	return id
    def POST(self):
        """ REST API TO ADD NEW ENTRY  """
        data = web.data()
	fn=json.loads(data)['firstname']
	ln=json.loads(data)['lastname']
	ph=json.loads(data)['phone']
	eml=json.loads(data)['email']
	un=json.loads(data)['username']
	pwd=json.loads(data)['password']
        model.new_user(fn,ln,ph,eml,un,pwd)
        

class Login:
    def GET(self):
        return "hi"
    def POST(self):
        """resr api to authentication"""
        data=web.data()
        un=json.loads(data)['username']
	pwd=json.loads(data)['password']
        model.check_user(un,pwd)


app = web.application(urls, globals())

if __name__ == '__main__':
    app.run()
