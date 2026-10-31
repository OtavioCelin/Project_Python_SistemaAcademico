class Aluno:
    
    def __init__(self, matricula, nome, curso):
        self._matricula = matricula  # Atributo protegido por convenção
        self._nome = nome            # Atributo protegido por convenção
        self._curso = curso          # Atributo protegido por convenção
        self._notas = []             # Atributo protegido por convenção

    def adicionar_nota(self, nota):
        if nota >= 0 and nota <= 10:
            self._notas.append(nota)
            return True
        return False

    def calcular_media(self):
        if len(self._notas) == 0:
            return 0.0
        return sum(self._notas) / len(self._notas)

    def obter_situacao(self):
        if len(self._notas) == 0:
            return "Sem avaliações"
        
        media = self.calcular_media()
        if media >= 7.0:
            return "Aprovado"
        elif media >= 5.0 and media < 7.0:
            return "Recuperação"
        else:
            return "Reprovado"