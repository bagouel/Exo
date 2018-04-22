#! /usr/bin/python
# -*- coding:utf-8 -*-

from flask import Flask, request
app = Flask(__name__)

@app.route('/housale.com/<page>')
def index(page=''):
	return """<table border="0" height="100%" width="100%">
			<tr height="10%" bgcolor="#6666CC">
			    <td width="10%" align="left">Housale.com</td>
			    <td width="75%" align="right">
				<a href="index">Accueil</a>
                 	     | <a href="article">Articles</a>
			     | <a href="panier">Paniers</a>
			     | <a href="forum">Forums</a>
			    </td>
			</tr>
			<tr>
			  <td bgcolor="#CCFFFF" width="30%">SIDEBAR</td>
			  <td>MENU</td>
			</tr>
			<tr height="10%" bgcolor="#CCFFFF">
			 <td colspan="2">Copyright @ 2018, Housale.com</td>
			</tr>
		</table>"""
                        

if __name__ == '__main__' :
   app.run()
