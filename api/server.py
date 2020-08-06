from gql.resolvers.root_resolver import query

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from ariadne import graphql_sync, make_executable_schema, gql, load_schema_from_path
from ariadne.constants import PLAYGROUND_HTML

import os

# initialize flask server, connect to postgres db and enable flask-migrate tool
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URI")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# initialize gql server
type_defs = gql(load_schema_from_path("./gql/schema/"))
schema = make_executable_schema(type_defs, query)

@app.route("/graphql", methods=["GET"])
def graphql_playground():
    """Serve GraphiQL playground"""
    return PLAYGROUND_HTML, 200

@app.route("/graphql", methods=["POST"])
def graphql_server():
    data = request.get_json()
    success, result = graphql_sync(
        schema,
        data,
        context_value=request,
        debug=app.debug
    )
    status_code = 200 if success else 400
    return jsonify(result), status_code

if __name__ == '__main__':
    app.run(debug=True)