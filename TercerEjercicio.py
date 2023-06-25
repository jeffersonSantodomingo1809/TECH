# Importamos el módulo 're' para trabajar con expresiones regulares
import re

def unique_domains(html_fragment):
    # Utilizamos expresiones regulares para encontrar todas las URLs en el fragmento de HTML
    urls = re.findall(r'https?://(?:www\.)?([\w.-]+)', html_fragment)

    # Creamos un conjunto para almacenar los dominios únicos
    unique_domains = set()

    # Iteramos sobre cada URL encontrada
    for url in urls:
        # Dividimos el dominio en partes utilizando el carácter '.'
        domain_parts = url.split('.')

        # Verificamos si el dominio tiene al menos dos partes (por ejemplo, 'dominio.com')
        if len(domain_parts) >= 2:
            # Unimos las últimas dos partes del dominio y lo agregamos al conjunto de dominios únicos
            unique_domains.add('.'.join(domain_parts[-2:]))

    # Ordenamos los dominios únicos alfabéticamente
    sorted_domains = sorted(unique_domains)

    # Devolvemos los dominios únicos como una cadena separada por ';'
    return ' ; '.join(sorted_domains)

# Solicitamos al usuario que ingrese un fragmento de HTML
num = input("Ingresa un fragmento de HTML: ")

# Creamos una lista vacía para almacenar las líneas del fragmento de HTML
html_lines = []

# Iteramos sobre cada carácter en la entrada del usuario y lo agregamos a la lista de líneas
for i in num:
    html_lines.append(i)

# Concatenamos todas las líneas del fragmento de HTML en una sola cadena
html_fragment = ''.join(html_lines)

# Llamamos a la función unique_domains pasando el fragmento de HTML y almacenamos el resultado en domain_list
domain_list = unique_domains(html_fragment)

# Imprimimos la lista de dominios únicos
print(domain_list)
