import os
import json

def configurar_sistema()
    if not os.path.exists("uploads_projetos"):
        os.makedirs("uploads_projetos")

def listar_projetos():
    arquivos = [f for f in os.listdir("uploads_projetos") if f.endswith(".json")]
    print('\n'+ '~' * 40)
    print('projetos cadastrados:')
    print('~' * 40)

    if not arquivos:
        print("Nenhum projeto encontrado.")

        return []
    
    for i, arquivo in enumerate(arquivos, 1):
        nome_exibicao = arquivo.replace("projeto_", "").replace(".json", "").replace("_", " ")
        print(f"{i}. {nome_exibicao.title()}")
    
    return arquivos

def gerenciar_projeto():
    arquivos = listar_projetos()
    if not arquivos:
        return
    
    escolha = int(input("\nEscolha um numero do projeto para gerenciar (ou '0' para voltar): "))
    
    if escolha == 0:
        return
    
    nome_arquivo = arquivos[escolha - 1]
    caminho = f"uploads_projetos/{nome_arquivo}"

    with open(caminho, "r", encoding="utf-8") as f:
        dados = json.load(f)

    print(f"\n---Dados Atuais---")
    print(f"aluno: {dados['aluno']}")
    print(f"projeto: {dados['projeto']}")

    confirmar = input("\nDeseja alterar as informações do projeto? (s/n): ").lower()

    if confirmar == 's':
        dados['aluno'] = input(f"Novo nome [{dados['aluno']}]: ")
        dados['projeto'] = input("Novo resumo: ") or dados['projeto']

        with open(caminho, "w", encoding="utf-8") as f:
            json.dump(dados, f, ensure_ascii=False, indent=4)
        print("Projeto atualizado com sucesso!")
    except 