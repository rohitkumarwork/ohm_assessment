from flask import jsonify, render_template, request, Response
from flask.ext.login import current_user, login_user
from sqlalchemy import create_engine
from functions.connect_to import getConnection
from functions import generate_mysql_uri
from functions import app
from models import User


@app.route('/community', methods=['GET'])
def community():
    args = {
        'users': []
    }
    # MYSQL CONNECTION
    access = getConnection('access')
    generate_url = generate_mysql_uri(access)
    engine = create_engine(generate_url)
    mysql_connect = engine.connect()
    query = mysql_connect.execute('''SELECT user_id, display_name, tier, point_balance, signup_date from user ORDER BY signup_date DESC LIMIT 5''')
    result = list(query)
    for row in result:
        args['users'].append({
                'display_name':row[1],
                'tier': row[2],
                'point_balance': row[3]
        })
    return render_template("community_template.html", **args )

