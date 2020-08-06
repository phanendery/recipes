import os

import graphene
from flask import Flask
from flask_graphql import GraphQLView
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://robin:QZgXSbE1XfkjHsTi@cluster0-f2h3f.mongodb.net/test?retryWrites=true&w=majority"
app.config['MONGO_DBNAME'] = 'test'
app.config['SECRET_KEY'] = '4c982e94-c84d-456e-978b-667354cc58af'

mongo = PyMongo(app)
db = mongo.db

# db.

# class User(db.Model):
#     __tablename__ = 'users'
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(256))        # index => should not be duplicate
#     username = db.Column(db.String(256), index=True, unique=True)
#     password = db.Column(db.String(256))


# def __repr__(self):
#     return '<User %r>' % self.email


# class UserObject(SQLAlchemyObjectType):
#     class Meta:
#         model = User
#         interfaces = (graphene.relay.Node,)


# class Query(graphene.ObjectType):
#     node = graphene.relay.Node.Field()
#     all_users = SQLAlchemyConnectionField(UserObject)


# schema_query = graphene.Schema(query=Query)


@app.route('/')
def hello_world():
    return mongo.db.all_users


# app.add_url_rule('/graphql-query', view_func=GraphQLView.as_view(
#     'graphql-query',
#     schema=schema_query, graphiql=True
# ))


if __name__ == '__main__':
    app.run()
