from flask import Flask,render_template
from flask_mysqldb import MySQL

app = Flask(__name__)


app.config["MYSQL_HOST"]="138.41.20.102"
app.config["MYSQL_PORT"]=53306
app.config["MYSQL_USER"]="ospite"
app.config["MYSQL_PASSWORD"]="ospite"
app.config["MYSQL_DB"]="w3schools"
mysql=MySQL(app)


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/prodotti")
def prodotti():
    cursor=mysql.connection.cursor()
    q="SELECT * FROM products"
    cursor.execute(q)
    data=cursor.fetchall()
    return render_template("prodotti.html",prodotti=data)

@app.route("/dettagli<categoria>")
def dettagli(categoria):
    cursor=mysql.connection.cursor()
    q="SELECT * FROM categories WHERE categoryID="+categoria
    cursor.execute(q)
    data=cursor.fetchall()
    return render_template("dettagli_categoria.html",categorie=data)
    

app.run(debug=True)
