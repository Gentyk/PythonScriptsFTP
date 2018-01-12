from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

authorizer = DummyAuthorizer()
authorizer.add_user("user", 12345, "./home", perm="elradfmw")
authorizer.add_anonymous("./homeAnon", perm="elradfmw")

handler = FTPHandler
handler.authorizer = authorizer

server = FTPServer(("127.0.0.1", 1026), handler)#создание сокета
server.serve_forever() #запускает ассинхроный цикл ввода-вывода



