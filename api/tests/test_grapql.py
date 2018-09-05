# -*- coding: utf-8 -*-
# Facebook GraphQL API  而非 RESTful API
#pip install graphene
import graphene

class Query(graphene.ObjectType):
    hello =  graphene.String(name=graphene.String(default_value='World'))

    def resolve_hello(self,info,name):
        return 'Hello'+name
    
schema = graphene.Schema(query=Query)
result = schema.execute('{hello}')
print(type(result.data['hello']))