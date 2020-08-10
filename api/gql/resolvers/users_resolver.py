from api.gql.resolvers.root_resolver import query
from api.server import db

@query.field("user")
def resolve_user(_, info):
    return {

        
        # "id": 1,
        # "first_name": "Ivana",
        # "last_name": "Tinkle",
        # "email": "iTinkle69@email.com"
    }