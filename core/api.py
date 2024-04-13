from ninja import NinjaAPI
from cursos.api import cursos_router

api = NinjaAPI()

api.add_router('/cursos/', cursos_router)