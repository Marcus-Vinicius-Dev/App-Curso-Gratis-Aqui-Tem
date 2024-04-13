from ninja import Router
from datetime import datetime
from ninja import ModelSchema, Schema
from .models import Curso, Instituicao, Estudante, Categoria
from django.http import JsonResponse
from typing import List
from django.shortcuts import get_object_or_404

cursos_router = Router()

class CursoSchema(ModelSchema):
    class Meta:
        model = Curso
        fields = '__all__'
        
class EstudanteSchema(ModelSchema):
    class Meta:
        model = Estudante
        fields = '__all__'
        
class InstituicaoSchema(ModelSchema):
    class Meta:
        model = Instituicao
        fields = '__all__'
        
class CategoriaSchema(ModelSchema):
    class Meta:
        model = Categoria
        fields = '__all__'
        
@cursos_router.post('/cursos/')
def post_curso(request, cursos: CursoSchema):
    cursos = Curso(
        nome = cursos.nome,
        descricao = cursos.descricao,
        data = cursos.inscricao,
        categoria = get_categoria,
        instituicao = get_instituicao
    )
    cursos.save()
    return

@cursos_router.get('/cursos/', response=List[CursoSchema])
def get_curso(request, nome: str = None):
    curso_list = Curso.objetos.all()
    
    if nome:
        curso_list = curso_list.filter(nome_icontains=nome)
    return curso_list

@cursos_router.put('/cursos/{id_curso}', response=CursoSchema)
def put_curso(request, id_curso: int):
    curso = get_object_or_404(Curso, id=id_curso)
    return curso

@cursos_router.delete('/cursos/{id_curso}', response=CursoSchema)
def delete_curso(request, id_curso: int):
    curso = get_object_or_404(Curso, id=id_curso)
    curso.delete()
    return curso

@cursos_router.post('/instituicao/', response=InstituicaoSchema)
def post_instituicao(request, instituicao: InstituicaoSchema):
    instituicao = Instituicao(
        nome = instituicao.nome,
        cep = instituicao.cep,
        endereco = instituicao.endereco,
        cidade = instituicao.cidade,
        uf = instituicao.uf,
        telefone = instituicao.telefone,
        email = instituicao.email,
        site = instituicao.site
    )
    instituicao.save()
    return

@cursos_router.get('/instituicao/', response=List[InstituicaoSchema])
def get_instituicao(request):
    instituicao = Instituicao.objetos.all()
    return instituicao

@cursos_router.put('/instituicao/{id_instituicao}', response=InstituicaoSchema)
def put_instituicao(request, id_instituicao: int):
    instituicao = get_object_or_404(Instituicao, id=id_instituicao)
    return instituicao

@cursos_router.delete('/instituicao/{id_instituicao}', response=InstituicaoSchema)
def delete_instituicao(request, id_instituicao: int):
    instituicao = get_object_or_404(Instituicao, id=id_instituicao)
    instituicao.delete()
    return instituicao

@cursos_router.post('/categoria/', response=CategoriaSchema)
def post_categoria(request, categoria: CategoriaSchema):
    categoria = Categoria(
        nome = categoria.nome,
    )
    categoria.save()
    return

@cursos_router.get('/categoria/', response=List[CategoriaSchema])
def get_categoria(request):
    categoria = Categoria.objects.all()
    return categoria

@cursos_router.put('/categoria/{id_categoria}', response=CategoriaSchema)
def put_categoria(request, id_categoria: int):
    categoria = get_object_or_404(Categoria, id=id_categoria)
    return categoria

@cursos_router.delete('/categoria/{id_categoria}', response=CategoriaSchema)
def delete_categoria(request, id_categoria: int):
    categoria = get_object_or_404(Categoria, id=id_categoria)
    categoria.delete()
    return categoria

@cursos_router.post('/estudante/', response=EstudanteSchema)
def post_estudante(request, estudante: EstudanteSchema):
    estudante = Estudante(
        nome = estudante.nome,
        sobrenome = estudante.sobrenome,
        #data_nascimento = estudante.data_nascimento,
        telefone = estudante.telefone,
        email = estudante.email,
        sexo = estudante.sexo,
    )
    estudante.save()
    return

@cursos_router.get('/estudante/', response=List[EstudanteSchema])
def get_estudante(request):
    estudante = Estudante.objects.all()
    return estudante

@cursos_router.put('/estudante/{id_estudante}', response=EstudanteSchema)
def put_estudante(request, id_estudante: int):
    estudante = get_object_or_404(Estudante, id=id_estudante)
    return estudante

@cursos_router.delete('/estudante/{id_estudante}', response=EstudanteSchema)
def delete_estudante(request, id_estudante: int):
    estudante = get_object_or_404(Estudante, id=id_estudante)
    estudante.delete()
    return estudante


