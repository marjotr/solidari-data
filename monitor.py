import json
import os

# Nome do arquivo onde as doações serão salvas para não sumirem ao fechar o programa
ARQUIVO_DADOS = "doacoes.json"

def carregar_doacoes():
    """Carrega as doações já salvas no arquivo JSON"""
    if os.path.exists(ARQUIVO_DADOS):
        with open(ARQUIVO_DADOS, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    return []

def salvar_doacoes(doacoes):
    """Salva a lista atualizada de doações no arquivo JSON"""
    with open(ARQUIVO_DADOS, "w", encoding="utf-8") as arquivo:
        json.dump(doacoes, arquivo, indent=4, ensure_ascii=False)

def registrar_doacao(doacoes):
    """Registra uma nova ação de solidariedade"""
    print("\n--- 🌸 Registrar Nova Doação 🌸 ---")
    tipo = input("Tipo de doação (ex: Alimentos, Roupas, Bíblias, Itens de Higiene): ").strip()
    quantidade = input("Quantidade (apenas números, ex: 10): ").strip()
    
    # Validação simples para garantir que digitaram um número
    if not quantidade.isdigit():
        print("❌ Erro: Por favor, digite uma quantidade válida em números!")
        return
        
    quantidade = int(quantidade)
    impacto_estimado = input("Quem ou quantas famílias essa doação ajuda? (ex: 2 famílias): ").strip()

    # Criando o dicionário da doação (Ciência de Dados na prática!)
    nova_doacao = {
        "tipo": tipo,
        "quantidade": quantidade,
        "impacto": impacto_estimado
    }

    doacoes.append(nova_doacao)
    salvar_doacoes(doacoes)
    print(f"✨ Sucesso! {quantidade}x {tipo} registrados com muito carinho!")

def exibir_relatorio(doacoes):
    """Mostra o impacto social gerado até o momento"""
    print("\n--- 📊 Relatório de Impacto Social e Solidariedade 📊 ---")
    if not doacoes:
        print("Nenhuma doação registrada ainda. Que tal começar a fazer o bem hoje? ✨")
        return

    total_itens = 0
    print("\n📋 Detalhes dos registros:")
    for i, item in enumerate(doacoes, 1):
        print(f"  {i}. {item['quantidade']}x {item['tipo']} -> Impacto: {item['impacto']}")
        total_itens += item['quantidade']

    print("\n--- 🌱 Resumo Consolidado ---")
    print(f"💖 Total de itens arrecadados: {total_itens}")
    print(f"🌍 Obrigado por usar a tecnologia para servir ao próximo!")

def menu_principal():
    """Menu interativo do sistema"""
    doacoes = carregar_doacoes()

    while True:
        print("\n======================================")
        print("      🌟 MONITOR SOLIDÁRIO v1.0 🌟      ")
        print("======================================")
        print("1. 🌸 Registrar Nova Doação")
        print("2. 📊 Ver Relatório de Impacto Social")
        print("3. ❌ Sair do Sistema")
        
        opcao = input("\nEscolha uma opção (1-3): ").strip()

        if opcao == "1":
            registrar_doacao(doacoes)
        elif opcao == "2":
            exibir_relatorio(doacoes)
        elif opcao == "3":
            print("\n✨ Que o Senhor abençoe seus planos! Até logo! 👋🌸")
            break
        else:
            print("❌ Opção inválida. Tente novamente!")

# Linha que inicia o programa automaticamente ao rodar o arquivo
if __name__ == "__main__":
    menu_principal()