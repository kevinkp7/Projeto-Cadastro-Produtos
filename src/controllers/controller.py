from flask.views import MethodView
from flask import request,render_template,redirect
from src.db import mysql

class IndexController(MethodView):
    def get(self):
        with mysql.cursor() as cur:
            cur.execute("SELECT * FROM produtos")
            data = cur.fetchall()
            
            cur.execute("SELECT * FROM categorias")
            categorias = cur.fetchall()
        return render_template('public/index.html', data=data, categorias=categorias)
    
    def post(self):
        codigo = request.form['codigo']    
        nome = request.form['nome']
        estoque = request.form['estoque']    
        valor = request.form['valor']    
        categorias = request.form['categorias']  
        
        with mysql.cursor()as cur:
            cur.execute("INSERT INTO produtos VALUES (%s, %s, %s, %s, %s)", (codigo, nome, estoque, valor, categorias))
            cur.connection.commit()
            return redirect('/')
      
        
class DeleteProdutoController(MethodView):
    def post(self, codigo):
        with mysql.cursor()as cur:
            cur.execute("DELETE FROM produtos WHERE codigo=%s",(codigo))
            cur.connection.commit()
            return redirect('/')

class UpdateProdutoController(MethodView):
    def get(self, codigo):
        with mysql.cursor()as cur:
            cur.execute("SELECT * FROM produtos WHERE codigo=%s",(codigo))
            produtos = cur.fetchone()
        return render_template('public/update.html',produtos=produtos)
        
    def post(self, codigo):
    
        codigoProduto = request.form['codigo']    
        nome = request.form['nome']
        estoque = request.form['estoque']    
        valor = request.form['valor']
        
        with mysql.cursor()as cur:
            cur.execute("UPDATE produtos SET codigo=%s, nome=%s, estoque=%s, valor=%s WHERE codigo=%s",(codigoProduto, nome, estoque, valor, codigo))
            cur.connection.commit()
        return redirect('/')
    
    
class CategoriesController(MethodView):
    def get(self):
        return render_template('public/categorias.html')
    
    def post(self):
        id = request.form['id']    
        nome = request.form['nome']
        descricao = request.form['descricao']    
        
        with mysql.cursor()as cur:
            cur.execute("INSERT INTO categorias VALUES(%s,%s,%s)",(id, nome, descricao))
            cur.connection.commit()
        return redirect('/')
       