from classes.sistema import SistemaClassificacao
from classes.grupos import Angiosperma, Pteridofita

def main():
    sistema = SistemaClassificacao()

    print("\nCarregando dados do sistema...\n")
    
    try:
        sistema.cadastrar_planta(Angiosperma(
        nome_comum="Carnaúba",
        nome_cientifico="Copernicia prunifera",
        tamanho="Grande",
        tem_espinhos=False,
        tem_flor_visivel=False,
        formato_folha="Palmada (leque)"
        ))
    except ValueError as e:
        print(f"\nErro ao cadastrar planta: {e}\n")

    try:
        sistema.cadastrar_planta(Angiosperma(
            nome_comum="Mandacaru",
            nome_cientifico="Cereus jamacaru",
            tamanho="Grande",
            tem_espinhos=True,
            tem_flor_visivel=True,
            formato_folha="Ausente (cacto)"
        ))
    except ValueError as e:
        print(f"\nErro ao cadastrar planta: {e}\n")

    try:
        sistema.cadastrar_planta(Angiosperma(
            nome_comum="Cajueiro",
            nome_cientifico="Anacardium occidentale",
            tamanho="Grande",
            tem_espinhos=False,
            tem_flor_visivel=True,
            formato_folha="Elíptica"   
        ))
    except ValueError as e:
        print(f"\nErro ao cadastrar planta: {e}\n")

    try:
        sistema.cadastrar_planta(Angiosperma(
            nome_comum="Jurema-preta",
            nome_cientifico="Mimosa tenuiflora",
            tamanho="Médio",
            tem_espinhos=True,
            tem_flor_visivel=True,
            formato_folha="Composta bipinada"
        ))
    except ValueError as e:
        print(f"\nErro ao cadastrar planta: {e}\n")

    try:
        sistema.cadastrar_planta(Pteridofita(
            nome_comum="Samambaia-de-bordo",
            nome_cientifico="Pteris sp.",
            tamanho="Médio",
            tem_espinhos=False,
            tem_flor_visivel=False,
            formato_folha="Recortada (penada)"
        ))
    except ValueError as e:
        print(f"\nErro ao cadastrar planta: {e}\n")

    try:
        sistema.cadastrar_planta(Angiosperma(
            nome_comum="Xique-xique",
            nome_cientifico="Pilosocereus gounellei",
            tamanho="Médio",
            tem_espinhos=True,
            tem_flor_visivel=False,
            formato_folha="Ausente (cacto)"
        ))
    except ValueError as e:
        print(f"\nErro ao cadastrar planta: {e}\n")

    try:
        sistema.cadastrar_planta(Angiosperma(
            nome_comum="Juazeiro",
            nome_cientifico="Ziziphus joazeiro",
            tamanho="Grande",
            tem_espinhos=True,
            tem_flor_visivel=False,
            formato_folha="Oval"
        ))
    except ValueError as e:
        print(f"\nErro ao cadastrar planta: {e}\n")

    try:
        sistema.cadastrar_planta(Angiosperma(
            nome_comum="Coroa-de-frade",
            nome_cientifico="Melocactus zehntneri",
            tamanho="Pequeno",
            tem_espinhos=True,
            tem_flor_visivel=True,
            formato_folha="Ausente (cacto)"
        ))
    except ValueError as e:
        print(f"\nErro ao cadastrar planta: {e}\n")

    try:
        sistema.cadastrar_planta(Angiosperma(
            nome_comum="Macambira",
            nome_cientifico="Bromelia laciniosa",
            tamanho="Pequeno",
            tem_espinhos=True,
            tem_flor_visivel=True,
            formato_folha="Roseta"
        ))
    except ValueError as e:
        print(f"\nErro ao cadastrar planta: {e}\n")
    
    while True:
        print("\n---SISTEMA DE IDENTIFICAÇÃO DE PLANTAS DO CEARÁ---")
        print("\n1. Iniciar Diagnóstico")
        print("2. Ver catálogo de plantas")
        print("0. Sair\n")
        
        op = input("Opção: ")
        
        if op == '1':
            sistema.iniciar_diagnostico()
        elif op == '2':
            sistema.listar_todas()
        elif op == '0':
            print("\nFinalizando sistema...")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()