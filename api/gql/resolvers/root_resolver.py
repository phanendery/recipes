from ariadne import QueryType

query = QueryType()

# import resolvers
from api.gql.resolvers.hello_resolver import resolve_hello
import api.gql.resolvers.users_resolver