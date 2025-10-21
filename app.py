from flask import Flask, render_template
from db_config import get_connection
import traceback

app = Flask(__name__)

@app.route('/')
def index():
    try:
        connection = get_connection()
        if connection is None:
            raise Exception("No se pudo conectar a la base de datos")
        with connection.cursor() as cursor:
            cursor.execute("SELECT ID, Name, CountryCode, District, Population FROM city LIMIT 20;")
            cities = cursor.fetchall()
        connection.close()
        return render_template('index.html', cities=cities)
    except Exception as e:
        error_info = {"error": str(e), "traceback": traceback.format_exc()}
        return render_template('index.html', cities=[], error=error_info), 500

if __name__ == '__main__':
    app.run(debug=True)
