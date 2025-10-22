from flask import Flask, render_template, jsonify
from db_config import get_connection
import traceback

app = Flask(__name__)

@app.route('/')
def index():
    # Página inicial con los botones
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    # Ruta original sin cambios
    try:
        connection = get_connection()
        if connection is None:
            raise Exception("No se pudo conectar a la base de datos")
        with connection.cursor() as cursor:
            cursor.execute("SELECT ID, Name, CountryCode, District, Population FROM city LIMIT 20;")
            cities = cursor.fetchall()
        connection.close()
        return render_template('dashboard.html', cities=cities)
    except Exception as e:
        error_info = {"error": str(e), "traceback": traceback.format_exc()}
        return render_template('dashboard.html', cities=[], error=error_info), 500

# Nueva ruta API para devolver resultados en JSON
@app.route('/api/<table>')
def api_table(table):
    queries = {
        'city': "SELECT ID, Name, CountryCode, District, Population FROM city;",
        'country': "SELECT Code, Name, Continent, Region, Population FROM country;",
        'countrylanguage': "SELECT CountryCode, Language, IsOfficial, Percentage FROM countrylanguage;"
    }

    if table not in queries:
        return jsonify({"error": f"Tabla desconocida: {table}"}), 400

    try:
        connection = get_connection()
        if not connection:
            raise Exception("No se pudo conectar a la base de datos")

        with connection.cursor() as cursor:
            cursor.execute(queries[table])
            rows = cursor.fetchall()

        connection.close()
        return jsonify(rows)

    except Exception as e:
        error_info = {"error": str(e), "traceback": traceback.format_exc()}
        return jsonify(error_info), 500

if __name__ == '__main__':
    app.run(debug=True)
