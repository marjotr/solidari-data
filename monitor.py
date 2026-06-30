import json
import os

# Arquivo que guardará os registros da campanha Quilo do Amor
ARQUIVO_DADOS = "quilo_do_amor_dados.json"

def carregar_dados():
    """Carrega os registros de alimentos salvos"""
    if os.path.exists(ARQUIVO_DADOS):
        with open(ARQUIVO_DADOS, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    return []

def salvar_dados(dados):
    """Salva os registros atuais no arquivo JSON"""
    with open(ARQUIVO_DADOS, "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)

def registrar_alimento(dados):
    """Registra a arrecadação de alimentos da Santa Ceia"""
    print("\n--- 🧺 Registrar Arrecadação (Quilo do Amor) 🧺 ---")
    alimento = input("Tipo do alimento (ex: Arroz, Feijão, Macarrão, Óleo): ").strip().capitalize()
    peso_input = input("Quantidade arrecadada em Quilos (ex: 5 para 5kg): ").strip()
    
    # Validação para garantir que digitaram um número válido
    if not peso_input.isdigit():
        print("❌ Erro: Por favor, digite o peso apenas em números inteiros!")
        return
        
    peso_kg = int(peso_input)

    # Cria o registro estruturado da doação
    novo_registro = {
        "alimento": alimento,
        "peso_kg": peso_kg
    }

    dados.append(novo_registro)
    salvar_dados(dados)
    print(f"✨ Glória a Deus! {peso_kg}kg de {alimento} registrados com sucesso para a campanha!")

def exibir_relatorio_impacto(dados):
    """Mostra o relatório consolidado e o impacto social/espiritual"""
    print("\n=======================================================")
    print(" 📊 RELATÓRIO DE IMPACTO - INSTITUTO ASSISTENCIAL ATITUDE ")
    print("=======================================================")
    
    if not dados:
        print("Nenhum alimento registrado nesta campanha ainda.")
        print("Tragam os mantimentos ao templo na próxima Santa Ceia! 📖🕊️")
        return

    total_geral_kg = 0
    resumo_alimentos = {}

    print("\n📋 Detalhe das Entradas por Culto:")
    for i, registro in enumerate(dados, 1):
        print(f"  {i}. {registro['peso_kg']}kg de {registro['alimento']}")
        total_geral_kg += registro['peso_kg']
        
        # Agrupa os alimentos para o resumo consolidado
        nome_alimento = registro['alimento']
        resumo_alimentos[nome_alimento] = resumo_alimentos.get(nome_alimento, 0) + registro['peso_kg']

    print("\n📦 Resumo Consolidado por Item:")
    for alimento, peso in resumo_alimentos.items():
        print(f"  • {alimento}: {peso} kg")

    print("\n🌱 Métricas de Impacto Social & Boa Mordomia:")
    print(f"  🔹 Total arrecadado: {total_geral_kg} kg de alimentos.")
    
    # Regra de negócio: Consideramos uma cesta básica média com 15kg de alimentos
    cestas_estimadas = total_geral_kg // 15
    if cestas_estimadas > 0:
        print(f"  💖 Impacto Estimado: Cerca de {cestas_estimadas} famílias em vulnerabilidade abençoadas com cestas básicas!")
    else:
        print(f"  💖 Impacto Estimado: Arrecadando mantimentos para montar a primeira cesta básica (meta: 15kg).")
        
    print("\n<i>'Quem se compadece do pobre empresta ao Senhor, que lhe retribuirá o benefício.' — Provérbios 19:17</i> ✨")

def menu_principal():
    """Menu adaptado para a realidade da Igreja Batista Atitude"""
    dados = carregar_dados()

    while True:
        print("\n======================================")
        print("     🕊️ CAMPANHA QUILO DO AMOR v1.0    ")
        print("======================================")
        print("1. 🧺 Registrar Alimentos (Culto de Santa Ceia)")
        print("2. 📊 Ver Relatório de Impacto Social")
        print("3. ❌ Sair do Sistema")
        
        opcao = input("\nEscolha uma opção (1-3): ").strip()

        if opcao == "1":
            registrar_alimento(dados)
        elif opcao == "2":
            exibir_relatorio_impacto(dados)
        elif opcao == "3":
            print("\n✨ Que o Senhor abençoe o Instituto Assistencial Atitude! Até logo! 👋🌸")
            break
        else:
            print("❌ Opção inválida. Tente novamente!")

if __name__ == "__main__":
    menu_principal()