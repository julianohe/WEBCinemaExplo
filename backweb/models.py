from django.db import models
"""  """

class Filme(models.Model):
    nome = models.CharField(max_length= 30, null = False, blank = False)
    genero = models.CharField(max_length=25)
    duracao = models.CharField(max_length=30)
    descricao = models.TextField(max_length= 250)

    def __str__(self):
        return self.nome ## Tabela Principal...
    

class Agendamento(models.Model):
        
 def __str__(self):## FKKKK da tabela FILME para mostrar o nome junto com o horario ao agendar.
        return self.nome

"""class Bonus(models.Model):        pass ## Bonus se atrelará ao cliente para ter dados ou seja (FK)
"""
class Cliente:
        pass ## para obter bonus tem que ter os dados do clientes 
        
        
        """
        Alguns dos comandos SQL mais importantes

         SELECT - extrai dados de um banco de dados
         UPDATE - atualiza dados em um banco de dados
         DELETE - exclui dados de um banco de dados
         INSERT INTO - insere novos dados em um banco de dados
         CREATE DATABASE - cria um novo banco de dados
         ALTER DATABASE - modifica um banco de dados
         CREATE TABLE - cria uma nova tabela
         ALTER TABLE - modifica uma tabela
         DROP TABLE - exclui uma tabela
         CREATE INDEX - cria um índice (chave de pesquisa)
         DROP INDEX - exclui um índice"""

""" Criar #TABELAS
    CREATE TABLE myapp_person (
    "id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY,
    "first_name" varchar(30) NOT NULL,
    "last_name" varchar(30) NOT NULL
);
          """