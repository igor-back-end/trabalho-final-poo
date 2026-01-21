from .planta import Planta
from .folhas import TIPOS_FOLHA

class SistemaClassificacao:
    def __init__(self):
        self.banco_plantas = []

    def cadastrar_planta(self, planta):
        self.banco_plantas.append(planta)
        print(f"[Sistema] Planta '{planta.nome_comum}' cadastrada com sucesso.")

    def listar_todas(self):
        print("\n--- Plantas no Banco de Dados ---")
        for p in self.banco_plantas:
            print(f"- {p.nome_comum} ({p.grupo}) | Folha: {p.formato_folha} | {'Possui espinhos' if p.tem_espinhos else 'Não possui espinhos'}")
    
    def iniciar_diagnostico(self):
        print("\n---INICIANDO DIAGNÓSTICO VISUAL---")
        print("Responda às perguntas observando a planta na sua frente, digite 's' para sim e 'n' para não.\n")

        grupo_detectado = self._identificar_grupo()

        if not grupo_detectado:
            print("\nResposta inválida, retornando ao menu inicial...")
            return

        print(f"\nAnálise Preliminar: A planta parece ser do grupo das {grupo_detectado.upper()}S.\n")
        print(f"O próximo passo é descobrir a qual espécie pertence essa planta...")

        self._identificar_especie(grupo_detectado)

    def _identificar_grupo(self):
    
        print("1. A planta é minúscula (alguns cm), parece um tapete aveludado e está em local úmido?")
        resp = input("   (s/n): ").lower()
        if resp == 's':
            return 'Briófita'
        elif resp == 'n':
            pass
        else:
            return None

        print("2. A planta possui flores coloridas ou algum tipo de fruto visível?")
        resp = input("   (s/n): ").lower()
        if resp == 's':
            return 'Angiosperma'
        elif resp == 'n':
            pass
        else:
            return None
        
        print("3. As folhas parecem agulhas finas ou escamas (como pinheiro) e/ou possuem pinhas(cones)?")
        resp = input("   (s/n): ").lower()
        if resp == 's':
            return 'Gimnosperma'
        elif resp == 'n':
            pass
        else:
            return None
        
        print("4. As folhas são grandes, recortadas (como penas) e brotam enroladas?")
        resp = input("   (s/n): ").lower()
        if resp == 's':
            return 'Pteridófita'
        elif resp == 'n':
            pass
        else:
            return None
        
        print("\nNão identifiquei características comuns a nenhum grupo.")
        print("Assumiremos então que ela é do grupo das Angiospermas, pois é a planta mais comum em nosso banco de dados.")
        return 'Angiosperma'

    def _identificar_especie(self, grupo_alvo):

        candidatas = [p for p in self.banco_plantas if p.grupo == grupo_alvo]

        if not candidatas:
            print(f"O sistema não possui plantas do grupo das {grupo_alvo.upper()}S cadastradas no sistema.")
            return

        tem_espinhos_lista = [p.tem_espinhos for p in candidatas]
        if True in tem_espinhos_lista and False in tem_espinhos_lista:
            resp = input("\n1. A planta possui espinhos visíveis? (s/n): ").lower()
            tem_espinho = (resp == 's')

            candidatas = [p for p in candidatas if p.tem_espinhos == tem_espinho]

        if len(candidatas) == 1:
            self._mostrar_resultado(candidatas[0])
            return

        print("\n2. Como é o formato da folha?")
        for i, tipo in enumerate(TIPOS_FOLHA, 1):
            print(f"    {i}. {tipo}")

        try:
            escolha_usuario = int(input("\nDigite o número da opção: "))
            if escolha_usuario < 1 or escolha_usuario > len(TIPOS_FOLHA):
                print("Opção inválida, retornando ao menu inicial...")
                return
        except ValueError:
                print("Opção inválida, retornando ao menu inicial...")
                return

        indice = escolha_usuario - 1
        tipo_selecionado = TIPOS_FOLHA[indice]

        if tipo_selecionado:
            print(f"\nfiltro utilizado na busca: '{tipo_selecionado}'")
            candidatas = [p for p in candidatas if p.formato_folha == tipo_selecionado]
        else:
            print("Opção inválida.")

        if len(candidatas) == 1:
            self._mostrar_resultado(candidatas[0])
        elif len(candidatas) > 1:
            print(f"\nEncontrei {len(candidatas)} plantas possíveis com essas características:")
            for p in candidatas:
                print(f"-> {p.nome_comum} ({p.nome_cientifico})")
        else:
            print("\nFalha na identificação, o sistema ainda não é capaz de identificar a planta observada.")

    def _mostrar_resultado(self, planta):
        print(f"\nPlanta identificado: {planta.nome_comum}")
        print(f"Nome Científico: {planta.nome_cientifico}")
        print(f"Grupo: {planta.grupo}")
        print(f"Reprodução: {planta.descricao_reprodutiva()}")
        print(f"Características: Folha {planta.formato_folha} e "
              f"{'possui espinhos' if planta.tem_espinhos else 'não possui espinhos'}.")