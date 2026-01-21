# Sistema de Identificação de Plantas do Ceará

Este projeto é um sistema em Python desenvolvido para auxiliar na identificação de plantas, com foco em espécies comuns no Ceará e no bioma da Caatinga. O sistema utiliza princípios de Orientação a Objetos (POO) para classificar as plantas em seus respectivos grupos botânicos (Briófitas, Pteridófitas, Gimnospermas e Angiospermas) e realizar diagnósticos baseados em características visuais.

## 📋 Funcionalidades

O sistema oferece as seguintes funcionalidades principais através de um menu interativo no console:

1.  **Diagnóstico Visual**: Um sistema de perguntas e respostas que guia o usuário para identificar uma planta desconhecida.
    *   Identifica primeiramente o grupo botânico (ex: Angiosperma, Pteridófita).
    *   Refina a busca com perguntas específicas sobre espinhos e formato das folhas.
    *   Exibe as possíveis plantas cadastradas que correspondem às características informadas.
2.  **Catálogo de Plantas**: Listagem de todas as plantas atualmente cadastradas no sistema, exibindo suas principais características.
3.  **Cadastro de Espécies**: O código já vem pré-carregado com diversas espécies nativas (Carnaúba, Mandacaru, Jurema-preta, etc.), mas é extensível para novos cadastros.

## 🛠️ Tecnologias e Conceitos de POO

O projeto foi construído utilizando **Python** e demonstra aplicação prática dos 4 pilares da Orientação a Objetos:

*   **Abstração**: Uso da classe abstrata `Planta` (`classes/planta.py`) que define o contrato para todas as plantas, mas não pode ser instanciada diretamente.
*   **Herança**: As classes `Briofita`, `Pteridofita`, `Gimnosperma` e `Angiosperma` (`classes/grupos.py`) herdam características e comportamentos da classe base `Planta`.
*   **Polimorfismo**: O método `descricao_reprodutiva()` é implementado de forma diferente em cada subclasse, retornando a descrição biológica correta para cada grupo.
*   **Encapsulamento**: Os atributos das plantas (como `_nome_comum`, `_tamanho`) são protegidos e acessados através de *properties* (getters), garantindo a integridade dos dados (ex: validação do formato da folha).

## 📂 Estrutura do Projeto

*   `main.py`: Arquivo principal. Inicializa o sistema, carrega as plantas no banco de dados e executa o menu interativo.
*   `classes/`
    *   `sistema.py`: Contém a lógica do sistema (`SistemaClassificacao`), gerenciamento do banco de dados e lógica do diagnóstico.
    *   `planta.py`: Define a classe base abstrata `Planta`.
    *   `grupos.py`: Define as subclasses concretas para cada grupo botânico.
    *   `folhas.py`: Define constantes auxilares (ex: tipos de folhas permitidos).

## 🚀 Como Executar

Certifique-se de ter o Python instalado em sua máquina.

1.  Navegue até o diretório do projeto via terminal.
2.  Execute o arquivo `main.py`:

```bash
python main.py
```

3.  Utilize o menu númerico para navegar entre as opções:
    *   Digite `1` para iniciar o diagnóstico de uma planta.
    *   Digite `2` para ver a lista de plantas cadastradas.
    *   Digite `0` para sair.

## 🌿 Exemplos de Plantas Cadastradas

*   **Carnaúba** (*Copernicia prunifera*)
*   **Mandacaru** (*Cereus jamacaru*)
*   **Jurema-preta** (*Mimosa tenuiflora*)
*   **Xique-xique** (*Pilosocereus gounellei*)
*   **Samambaia-de-bordo** (*Pteris sp.*)
