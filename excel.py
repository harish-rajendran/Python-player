from flask import Flask
import MySQLdb.cursors
import MySQLdb
from databases import databases
from flask.ext import excel
from flask_cors import CORS, cross_origin

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


app = Flask(__name__)
datab=databases()
db=datab.connect

@cross_origin()
@app.route('/vendor/download/')
def main(self,values):

    vid = values['vendorid'] 
    sname = values['storename']
    sid = values['storeid']
    city = values['city']
    branch = values['branch']
    cursor = db.cursor()
    cursor.execute("SELECT * FROM vendor WHERE vendorid =%s AND storeid = %s" ,(vid,sid))
    data=cursor.fetchall(MySQLdb.cursors.DictCursor)
    output = excel.make_response_from_array(data, 'csv')
    output.headers["Content-Disposition"] = "attachment; filename=export.csv"
    output.headers["Content-type"] = "text/csv"
    return output

if __name__ == "__main__":
    app.debug=True
    app.run(port = 5010)