# a) Permitir a decolagem do primeiro avião na fila.
# b) Adicionar um avião na fila de decolagem.
# c) Mostrar o total de aviões aguardando na fila de colagem.
# d) Lista todos os aviões na fila de decolagem.
# e) Listar as características do próximo a decolar (o avião que está na frente da fila).
# f) Mostrar a posição de um avião conforme o número do voo.

class Aviao:
	def __init__(self, modelo, empresa, origem, destino, passageiros, numero):
		self.modelo = modelo
		self.empresa = empresa
		self.origem = origem
		self.destino = destino
		self.passageiros = passageiros
		self.numero = numero	
	
	def __str__(self):
		return f'{self.modelo} {self.empresa} {self.origem} {self.destino} {self.passageiros} {self.numero}'

class Controladora:		
		def __init__(self):
			self.fila = []
	
		def __str__(self):
			return [f'{self.fila}' for i in self.fila]

		
		def adicionar_na_fila(self, object):
			
			self.fila.append(object)
			print(f'Avião numero {object.numero} adicionado a fila com sucesso!')

		def remover_fila(self):
			valor_removido = self.fila.pop(0)
			

		def proximo_aviao(self):
			return str(self.fila[0])
		
		def total_de_avioes(self):
			return str(len(self.fila))

		def listar_avioes_na_pista(self):
			na_pista = []
			for aviao in self.fila:
				na_pista.append(str(aviao))
			return na_pista


aviao_atributos = {	'modelo' : "a254", 'empresa' : "Gol", 'origem' : "RS", 
					'destino' : "SP", 'passageiros' : 214, 'numero' : "50" }
a1 = Aviao(**aviao_atributos)


a2 = Aviao("B411", "LATAM", "RJ", "MG", 365, "245718")

controladora = Controladora()

controladora.adicionar_na_fila(a1)
controladora.adicionar_na_fila(a2)

print("Comandos: \n adicionar: Adicionar um avião na fila! \n decolar: Faz o primeiro avião da fila decolar! \n listar: Lista todos os aviões que estão na fila! \n proximo: Exibe as informações do próximo avião a decolar! \n total: Exibe o número total de aviões que estão na fila! \n posição: Exibe a posição do avião na fila pelo seu número! \n sair: Sai do programa!" )


while True:
	comandos = input("Digite o comando: ")
	if comandos == "sair":
		print("Saindo do programa!")
		break

	elif comandos == "adicionar":
		modelo = input("Digite o modelo do avião: ")
		empresa = input("Digite a empresa: ")
		origem = input("Digite a origem: ")
		destino = input("Digite o destino: ")
		passageiros = input("Digite o número de passageiros: ")
		numero = input("Digite o número do avião: ")
		controladora.adicionar_na_fila(Aviao(modelo, empresa, origem, destino, passageiros, numero))		

	elif comandos == "decolar":
		print(f'Avião {controladora.fila[0]} decolou com sucesso!')
		controladora.remover_fila()

	elif comandos == "listar":
		print(controladora.listar_avioes_na_pista())

	elif comandos == "proximo":
		print("O próximo avião na vila de decolagem é: " + controladora.proximo_aviao())
	elif comandos == "total":
		print("Total de aviões na fila de decolagem: " + controladora.total_de_avioes())
	elif comandos == "posicao":
		posicao = input("Digite o número do avião: ")		
		for index, av in enumerate(controladora.fila):
			if av.numero == posicao:
				print(f"O avião está na posição: {index}")
				break

			
	else:
		print("Comando inválido!")