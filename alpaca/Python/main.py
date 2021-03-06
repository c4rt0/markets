# main.py
import graphene
import uvicorn

from fastapi import FastAPI
from starlette.graphql import GraphQLApp


class Query(graphene.ObjectType):
    hello = graphene.String(name=graphene.String(default_value=", World!"))

    def resolve_hello(self, info, name):
        return "Hello " + name


app = FastAPI()

# Managed to teg it up and running, using : https://www.youtube.com/watch?v=2_puWfTK8bQ&t=604s
app.add_route("/graphql", GraphQLApp(schema=graphene.Schema(query=Query)))


@app.get("/", tags=["test"])
def greet():
    return {"Hello": "World"}
