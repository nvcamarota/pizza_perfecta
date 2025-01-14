"""
PIZZA PERFECTA
Contexto: Son chefs en una pizzería que permite a los clientes personalizar sus pizzas. Deben crear un sistema para calcular el precio de una pizza con ingredientes personalizados.
Actividad:
Escribe una función hacer_pizza(base, *ingredientes, **extras) que:
• Reciba el tipo de base ("fina", "gruesa").
• Reciba una lista de ingredientes principales como *args.
• Reciba extras opcionales como **kwargs ("queso_extra", "salsa_bbq").
• Calcule el precio final
• Cada ingrediente cuesta $500.
• Los extras tienen precios definidos en **kwargs.
"""

def hacer_pizza(base, *ingredientes, **extras):
    costo_ingredientes = len(ingredientes) * 500
    costo_extras = sum(extras.values())
    costo_total = costo_ingredientes + costo_extras

    print(f'Base: {base}')
    print('Ingredientes principales:')
    for ingrediente in ingredientes:
        print(f'- {ingrediente}')
    print('Extras:')
    for extra, precio in extras.items():
        print(f'- {extra}: ${precio}')
    print(f'Precio final: ${costo_total}')
    
print(hacer_pizza(
        'gruesa',
        'muzzarella', 'salsa de tomate', 'aceitunas',
        queso_azul = 200, anchoas = 400, anana = 500
    ))