from django.db import models


# Create your models here.
class Base(models.Model):
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Curso(Base):
    titulo = models.CharField(max_length=50)
    url = models.URLField(unique=True)

    verbose_name = 'Curso'

    def __str__(self):
        return self.titulo


class Avaliacao(Base):
    curso = models.ForeignKey(Curso, related_name='avaliacao', on_delete=models.CASCADE)
    nome = models.CharField(max_length=50)
    email = models.EmailField()
    comentarios = models.TextField(default='', max_length=200)
    nota = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = 'Avaliações'
        unique_together = ['curso', 'email']

    def __str__(self):
        return f'{self.nome} avaliou o curso {self.curso}'
