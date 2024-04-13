from django.db import models


class Instituicao(models.Model):
    
    nome = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    cep = models.CharField(
        max_length=9,
        null=False,
        blank=False
    )
    
    endereco = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    cidade = models.CharField(
        max_length=150,
        null=False,
        blank=False
    )
    
    uf = models.CharField(
        max_length=2,
        null=False,
        blank=False
    )

    telefone = models.CharField(
        max_length=15,
        null=False,
        blank=True
    )
    
    email = models.EmailField(
        max_length=50,
        null=True,
        blank=True
    )
    
    site = models.CharField(
        max_length=50,
        null=True,
        blank=True
    )
    
    objetos = models.Manager()

    def __str__(self):
        return f"{self.nome}"


class Categoria(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    
    def  __str__(self):
        return self.nome


class Curso(models.Model):
    instituicao = models.ForeignKey(Instituicao, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)

    nome = models.CharField(
        max_length=100,
        null=False,
        blank=False
    )

    descricao = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )
    
    inscricao = models.DateField(
        null=True,
        blank=True
    )
    
    objetos = models.Manager()

    def __str__(self):
        return f"{self.nome} {self.descricao}"


class Estudante(models.Model):
    nome=models.CharField(max_length=100)
    sobrenome=models.CharField(max_length=100)
    #data_nascimento=models.DateField(auto_created=input)
    telefone=models.CharField(max_length = 15)
    email=models.EmailField()
    sexo=models.CharField(max_length=1)

    def __str__(self):
        return f'{self.nome} {self.sobrenome}'

