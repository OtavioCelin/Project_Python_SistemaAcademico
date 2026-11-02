import random
from Aluno import Aluno

class SistemaAcademico:
    def __init__(self):
        self._alunos = {}  

    def gerar_matricula(self):
        while True:
            matricula = str(random.randint(1000, 9999))
            if matricula not in self._alunos:
                return matricula

    def cadastrar_aluno(self, nome, curso):
        if nome == "" or curso == "":
            print("Erro: Nome e curso não podem estar vazios.")
            return None
        
        matricula = self.gerar_matricula()
        novo_aluno = Aluno(matricula, nome, curso)
        self._alunos[matricula] = novo_aluno
        return matricula

    def buscar_aluno(self, matricula):
        if matricula in self._alunos:
            return self._alunos[matricula]
        return None

    def registrar_nota(self, matricula, nota):
        aluno = self.buscar_aluno(matricula)
        if aluno == None:
            print("Erro: Aluno não encontrado.")
            return False
        
        if aluno.adicionar_nota(nota) == True:
            print("Nota registrada com sucesso!")
            return True
        else:
            print("Erro: A nota deve estar entre 0 e 10.")
            return False

    def gerar_relatorio_geral(self):
        total_alunos = len(self._alunos)
        if total_alunos == 0:
            return None

        alunos_com_notas = []
        for aluno in self._alunos.values():
            if len(aluno._notas) > 0:
                alunos_com_notas.append(aluno)
        
        contagem = {"Aprovado": 0, "Recuperação": 0, "Reprovado": 0, "Sem avaliações": 0}
        for aluno in self._alunos.values():
            situacao = aluno.obter_situacao()
            contagem[situacao] = contagem[situacao] + 1

        relatorio = {
            "total_alunos": total_alunos,
            "alunos_com_notas": len(alunos_com_notas),
            "contagem_situacao": contagem,
            "media_geral": 0.0,
            "maior_media": 0.0,
            "menor_media": 0.0
        }

        if len(alunos_com_notas) > 0:
            soma_medias = 0
            for aluno in alunos_com_notas:
                soma_medias = soma_medias + aluno.calcular_media()
            
            relatorio["media_geral"] = soma_medias / len(alunos_com_notas)

            maior = alunos_com_notas[0].calcular_media()
            menor = alunos_com_notas[0].calcular_media()
            
            for aluno in alunos_com_notas:
                med = aluno.calcular_media()
                if med > maior:
                    maior = med
                if med < menor:
                    menor = med
                    
            relatorio["maior_media"] = maior
            relatorio["menor_media"] = menor

        return relatorio