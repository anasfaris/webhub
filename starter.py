from bottle import *
import bottle
import os
from pymongo import MongoClient
import pymongo

# db = MongoClient("mongodb://db_username:db_pwd@db_ip:db_port").db_name

application = default_app()

@error(500)
@error(505)
@error(404)
def errors(error):
	return error

@route("/")
def main():
	return template('views/index.html',
					title="Bottle Starter")

@route('/favicon.ico')
def get_favicon():
	return server_static('favicon.ico')


@route('/robots.txt')
def serve_robots():
    return static_file('robots.txt', root='./static/')

# specifying the path for the files
@route('/<filepath:path>')
@route('/scanner/<filepath:path>')
def server_static(filepath):
	return static_file(filepath, root='./static/')

if __name__ == '__main__':
	application.run(reloader=True, host="0.0.0.0", port=int(os.environ.get("PORT", 9000)))
