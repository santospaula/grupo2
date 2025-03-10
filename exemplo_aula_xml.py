import xml.etree.ElementTree as ET

def ler_xml(caminho_arquivo):
    try:
        # Analisa o arquivo XML
        tree = ET.parse(caminho_arquivo)
        root = tree.getroot()

        # Aqui, você pode acessar os elementos e atributos do XML conforme necessário
        for elemento in root:
            print("Tag:", elemento.tag.split('}')[1])
            print("Atributos:", elemento.text)
            for subelemento in elemento:
                print(f"    {subelemento.tag.split('}')[1]}: {subelemento.text}")
                for subsubelemento in subelemento:
                    print(f"{subsubelemento.tag.split('}')[1]}: {subsubelemento.text}")

    except ET.ParseError as e:
        print(f"Erro ao analisar o arquivo XML: {e}")

def criar_xml(caminho_arquivo):
    # Cria o elemento raiz
    root = ET.Element("Pessoas")

    # Adiciona elementos filho
    pessoa1 = ET.SubElement(root, "Pessoa")
    nome1 = ET.SubElement(pessoa1, "Nome")
    nome1.text = "Paulo"
    idade1 = ET.SubElement(pessoa1, "Idade")
    idade1.text = "33"

    pessoa2 = ET.SubElement(root, "Pessoa")
    nome2 = ET.SubElement(pessoa2, "Nome")
    nome2.text = "Maria"
    idade2 = ET.SubElement(pessoa2, "Idade")
    idade2.text = "25"

    # Cria a árvore XML
    tree = ET.ElementTree(root)

    # Escreve o arquivo XML
    tree.write(caminho_arquivo)

    print("Arquivo XML criado com sucesso!")

# Chama a função para criar o XML


xml_entrada = 'exemplos_arquivos/pom.xml'
xml_saida = 'exemplos_arquivos/escrita.xml'
criar_xml(xml_saida)
ler_xml(xml_entrada)


