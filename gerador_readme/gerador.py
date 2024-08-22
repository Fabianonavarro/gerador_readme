# gerador_readme/gerador.py

import os

def main():
    print("Gerador de README.md")
    
    # Solicitar entradas ao usuário
    project_name = input("Nome do Projeto: ")
    description = input("Descrição do Projeto: ")
    author = input("Autor do Projeto: ")
    email = input("Email do Autor (opcional): ")
    linkedin = input("LinkedIn do Autor (opcional): ")
    github = input("GitHub do Autor (opcional): ")
    license_type = input("Tipo de Licença: ")
    
    # Montar o conteúdo do README
    readme_content = f"""# {project_name}

{description}

## Licença

Licença {license_type}.

## Contatos

{author}
{f"Email: {email}" if email else ""}
{f"LinkedIn: {linkedin}" if linkedin else ""}
{f"GitHub: {github}" if github else ""}
"""

    # Definir o caminho do arquivo README.md
    readme_path = os.path.join(os.getcwd(), 'README.md')
    
    # Gravar o conteúdo no arquivo README.md
    with open(readme_path, 'w') as f:
        f.write(readme_content)

    print(f"README.md gerado com sucesso em {readme_path}")

if __name__ == "__main__":
    main()
