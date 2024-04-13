from django.contrib import admin
from .models import Curso, Estudante, Instituicao, Categoria

class EstudanteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'sobrenome', 'email')
    
class InstituicaoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'endereco', 'telefone', 'email')
    
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')
    
class CursoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'instituicao', 'categoria', 'descricao')

admin.site.register(Curso, CursoAdmin)
admin.site.register(Estudante,EstudanteAdmin)
admin.site.register(Instituicao, InstituicaoAdmin)
admin.site.register(Categoria, CategoriaAdmin)
