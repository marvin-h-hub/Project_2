from flask import Flask, render_template, jsonify
from flask_cors import CORS, cross_origin
import pandas as pd
from sqlalchemy import create_engine

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

connection_string = "postgres:PostgreSQL1!@localhost:5432/Project_2"
engine = create_engine(f'postgresql://{connection_string}')
conn = engine.connect()

@app.route("/")
def home(): 
    return "<a href=/AIG-US>AIG</a>"


@app.route("/stock-names")
@cross_origin()
def stock_names():
    data = pd.read_sql("SELECT DISTINCT ticker FROM in_search_of_alpha", conn)
    return data.to_json()

@app.route("/<stock_name>")
@cross_origin()
def stock(stock_name):
    #REad records from DB
    data = pd.read_sql(f"SELECT * FROM in_search_of_alpha WHERE ticker = '{stock_name}'", conn)
    
    return data.to_json()

if __name__ == "__main__":
    app.run(debug=True)
