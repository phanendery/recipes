from api.gql.resolvers.root_resolver import query

@query.field("hello")
def resolve_hello(_, info):
    return "Sa"