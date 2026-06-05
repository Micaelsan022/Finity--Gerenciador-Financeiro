from services.calculos import gastos_por_categoria, total_gastos

def analisar_gastos():
    alertas = []
    categorias = gastos_por_categoria()
    total = total_gastos()

    if total == 0:
        return alertas

    for item in categorias:
        if item["porcentagem"] > 30:
            alertas.append(
                f" Você gastou {item['porcentagem']}% do seu orçamento com {item['categoria']} este mês."
            )

    return alertas