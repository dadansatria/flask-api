import uuid
from flask import Flask
from flask_cqlalchemy import CQLAlchemy
import json

app = Flask(__name__)
app.config['CASSANDRA_HOSTS'] = ['172.20.0.2']
app.config['CASSANDRA_KEYSPACE'] = "dadan"
app.config['CASSANDRA_USERNAME'] = "cassandra"
app.config['CASSANDRA_PASSWORD'] = "cassandra"
# Koneksi DB Cassandra ke docker masih error.
# db = CQLAlchemy(app)

@app.route('/')
def api():
	data = [
	    {'city': 'Bandung', 'date_joined': '2019-01-01','email': 'dadansatria7@gmail.com','fullname' : 'Dadan Satria Nugraha', 'password' : '', 'zip_code' : '2392389'},
	    {'city': 'Jakarta', 'date_joined': '2013-03-01','email': 'dheanata@gmail.com','fullname' : 'Dhenata Silvia', 'password' : '', 'zip_code' : '89789789'},
	]
	return json.dumps(data)

# class User(db.Model):
#     uid = db.columns.UUID(primary_key=True, default=uuid.uuid4)
#     username = db.columns.Text(required=False)