from ariadne import QueryType

query = QueryType()

# import resolvers
from gql.resolvers.hello_resolver import resolve_hello
import gql.resolvers.users_resolver