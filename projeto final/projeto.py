from func_projeto import *
from datetime import datetime
while True:
    print("----------------------------------")
    menu()
    n = int(input("Escolha uma das opções: "))
    if n == 1:
        #PEGANDO A LISTA DE CODIGOS DOS MUNICIPIOS DO ARQUIVO FONTE
        arquivo01 = open("Codigo_UE.txt","r")
        SE_UE = arquivo01.readlines()
        arquivo01.close()

        #PEGANDO A LISTA DE CODIGOS DOS CARGOS DO ARQUIVO FONTE
        arquivo02 = open("Codigo_Cargos.txt","r")
        CD_CARGOS = arquivo02.readlines()
        arquivo02.close

        #MONTANDO LISTAS REMOVENDO OS "\n"
        Lista_cod_municipio = montar_lista(SE_UE)
        Lista_cod_cargos = montar_lista(CD_CARGOS)

        #Lendo codigo do MUNICIPIO:
        while True:
            x = input("Digite o codigo do Municipio: ")
            if x not in remover_repet(Lista_cod_municipio):
                print("Codigo do MUNICIPIO informado invalido, favor informar outro.")
            else:
                break

        #Lendo codigo do CARGO:
        while True:
            y = input("Digite o codigo do Cargo: \n11 - PREFEITO\n12 - VICE-PREFEITO\n13 - VEREADOR\n")
            if y not in remover_repet(Lista_cod_cargos):
                print("Codigo do CARGO informado invalido, favor informar outro.")
            else:
                break

        lista01(x,y)
    elif n == 2:
        while True:
            x = input("Digite o codigo do candidato: ")
            if x not in cod_candidato_lista():
                print("Codigo do Candidato informado invalido, favor informar outro.")
            else:
                break
        cod_candidato(x)
    elif n == 3:
       print("http://127.0.0.1:5500/index.html")

    elif n == 5:
        break
    elif n == 4:
        x = input("Digite o nome da cidade: ").upper()
        localizar_cod(x)
    else:
        print("Valor invalido, informe outro!")



#MAAAAAAAAAAAAAAAAAARI

html2 = open("estatisticas.html", "w", encoding="UTF-8")
html2.write("<html>\n")
html2.write("<body>\n")
html2.write("<link rel=stylesheet href=https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200 />")
html2.write("<style>\n")

html2.write("* {padding: 0;margin: 0; box-sizing: border-box;}\n")
html2.write("@font-face {font-family: 'velha'; src: url('broadway/BroadwayFlat3D-Italic.ttf') ; font-style: normal; font-weight: 400;}\n")


html2.write(".cabecalho {display: flex; align-items: center; padding: 2% 20px; margin-bottom: 1%;} \n")
html2.write(".cabecalho h1{margin:auto;}")
html2.write(".partidos ul {list-style: none;}\n")
html2.write(".idade ul {list-style: none;}\n")
html2.write("a {text-decoration: none;}\n")
html2.write("header {display: flex; width: 100%; z-index: 999; position: fixed}\n")

html2.write(".nav {display: flex; width: 100%; align-items: center ; justify-content: space-evenly; background: black; padding: 1%;}\n")

html2.write(".h1_nav {margin-left: 27%; justify-content: center; display: flex; color: yellow; font-family: 'velha', sans-serif; font-weight: 400; font-size: 10vh;}\n")

html2.write(".p_nav a {margin-left: 13%; font-size: 2rem; color: yellow;}\n")
html2.write(".p_nav  {WIDTH: 23%; align-items: center; gap: 15px; display: flex;}\n")

html2.write("main {padding: 78px;}\n")



html2.write(".conteudo {display:flex; width: 100%;   align-items: center;}")

html2.write(".partidos {flex-basis: 50%; flex-wrap: wrap; display:flex; font-size: 2.9vh; gap:17px; justify-content: center; text-align: center;}\n")


html2.write(".p_nav a:hover {transform: translateY(-5px); text-decoration: underline ; display: flex; gap: 12px;}")
html2.write(".idade {margin: auto; font-size: 4vh; text-align: center;}\n")
html2.write(".material-symbols-outlined {color:white; font-size: 48px;}\n")
html2.write(".qtd_candidato {margin-bottom: 5%;}\n")
html2.write(".clara {display: flex; width: 100%; gap: 14%; justify-content: space-around; margin-top: 4%;  font-size: 2.9vh; text-align: center;}")
html2.write(".tt {display: flex; justify-content: space-around; align-items: center; gap: 5%; }")
html2.write(".titulo_idade {width: 25%; font-size: 5vh;}")
html2.write(".titulo_partido {font-size: 5vh; margin-left: 53px; width: 31%;}\n")
html2.write("</style>\n") #style ACABA AQUI

#header
html2.write("<header>\n")
html2.write("<div class = nav>\n")
html2.write("<h1 class = h1_nav>Resumo eleitoral</h1>\n")
html2.write("<p class = p_nav> <a href='index.html'>Todos Candidatos</a> <span class=material-symbols-outlined icon>groups</span> </p>\n")
html2.write("</div>\n")
html2.write("</header>\n")
#Fim do header
html2.write("<br><br><br><br><br>\n")
#Inicio main
html2.write("<main>\n")
html2.write("<div class = cabecalho>\n") 
html2.write("<h1 class= titulo_esta > Partidos com <b>Prefeitos</b>; Estatisticas de Idade; Qtd_Prefeito, Veriador e Vice-Prefeito. </h1>\n")
html2.write("</div>\n") 


#PARTE CLARA PONTO 1
def candidatos_cargo():
    arquivo_cargo = open("cargos.txt","r")

    arqv_cargo=montar_lista(arquivo_cargo)

    arquivo_cargo.close()

    P='PREFEITO'
    Vp='VICE-PREFEITO'
    V='VEREADOR'

    cont_p=0
    cont_vp=0
    cont_v=0

    for i in arqv_cargo:
        if i==P:
            cont_p+=1
        if i==Vp:
            cont_vp+=1
        if i==V:
            cont_v+=1
    html2.write("<div class= qtd_candidato>")
    html2.write("<h1>Candidatos por Cargos</h1>")
    html2.write("<div class= num_candi>") #Class = num_candi
    html2.write(f'<h2>Vereador: {cont_v}</h2>')
    html2.write(f'<h2>Vice-Prefeito: {cont_vp}</h2>')
    html2.write(f'<h2>Prefeito: {cont_p}</h2>')
    html2.write("</div>")
    html2.write("</div>")
candidatos_cargo()


def partidos_cargo_prefeito():
     #with abre e fecha sozinho 
     #primeiro r=raw(pra nao dar erro de leitura)
    with open(r'consulta_cand_2024_PB.csv', 'r', encoding='latin1') as arquivo:
        linhas = arquivo.read().splitlines()

    cargo=linhas[0].split(';').index('"DS_CARGO"')#acessando a linha pra achar a coluna que o cargo ta
    partido=linhas[0].split(';').index('"SG_PARTIDO"')
    #se o cargo for de prefeito, coloca o referente partido na lista
    partidos_prefeitos=set()#pra nao ter coisa repetida
    for i in range(1,len(linhas)):
        linha=linhas[i].split(';')#criando uma lista de todos os elementos separado por ';'
        if linha[cargo]=='"PREFEITO"':
            partidos_prefeitos.add(linha[partido])

    html2.write("<div class= tt>")
    html2.write(f"<h1 class= titulo_partido>Partidos com <b>Prefeitos</b></h1>\n")
    html2.write(f"<h1 class= titulo_idade>Estatisticas Idade</h1>\n")
    html2.write("</div>")

    html2.write(f"<section class= conteudo>\n")
    
    html2.write(f"<div class= partidos>\n")

    for partido in partidos_prefeitos:
        html2.write("<ul>")
        html2.write(f"<li>{partido}</li>")
        html2.write("</ul>")
    html2.write(f"</div>\n")
    return list(partidos_prefeitos)


partidos_cargo_prefeito()


def calcular_idade(data):
    dia,mes,ano=map(int,data.replace('"','').split('/'))
    data_nascimento = datetime(ano, mes, dia)
    data_atual = datetime.now()
    idade = data_atual.year - data_nascimento.year
    #  caso o aniversário ainda não tenha ocorrido neste ano
    if (data_atual.month, data_atual.day) < (data_nascimento.month, data_nascimento.day):
        idade -= 1
    return idade

def quant_por_idade():
    
    with open(r'consulta_cand_2024_PB.csv', 'r', encoding='latin1') as arquivo:
        linhas = arquivo.read().splitlines()

    nascimento=linhas[0].split(';').index('"DT_NASCIMENTO"')
    quantidade_idades={'ate_21':0,    #:0 fazendo um contador
                       '22_e_40':0,
                       '41_e_60':0,
                       'maior_60':0}   #fazendo um dicionario pra nao precisar fazer muitas listas

    for i in range(1,len(linhas)):
        linha=linhas[i].split(';')

        data_nascimento=linha[nascimento]

        idade=calcular_idade(data_nascimento)
        if idade<=21:
            quantidade_idades['ate_21']+=1
        elif idade >=22 and idade<=40:
            quantidade_idades['22_e_40']+=1
        elif idade >=41 and idade<=60:
            quantidade_idades['41_e_60']+=1
        else:
            quantidade_idades['maior_60']+=1

    html2.write("<br><br>\n")
   
    html2.write("<div class= idade>\n") # div idade COMEÇA aqui 
    html2.write("<ul>\n")
    cont = 0
    for valor in quantidade_idades.values():
        if cont == 0:
            html2.write(f" <li>Candidatos ate 21 anos: {valor} </li>\n")
            cont += 1
        elif cont ==1:
            html2.write(f" <li>Candidatos de 22 ate 40 anos: {valor} </li>\n")
            cont += 1
        elif cont == 2:
            html2.write(f" <li>Candidatos de 41 ate 60 anos: {valor} </li>\n")
            cont += 1
        else:
            html2.write(f" <li>Candidatos com <b>mais</b> de 60 anos: {valor} </li>\n")
    html2.write("</ul>\n")
    html2.write("</div>\n") # div idade TERMINA aqui 
    html2.write("</section>\n") #section conteudo acaba aqui
quant_por_idade()

html2.write("<section class= clara>")

#PONTO 2 CLARA
#ajeitar algumas coisas imprimir_percentuais
from func_projeto import *
# Percentual de candidatos por cargo, considerando:
# Grau de instrução;
# Gênero;
# Estado civil.
def contar_dados(arqv_todos, cargo_alvo):
    contadores = {
        'SOLTEIRO(A)':0,
        'CASADO(A)': 0,
        'DIVORCIADO(A)':0,
        'VIÚVO(A)': 0,
        'FEMININO': 0,
        'MASCULINO': 0,
    }

    contadores_grau = {
        'LÊ E ESCREVE': 0,
        'ENSINO FUNDAMENTAL INCOMPLETO': 0,
        'ENSINO FUNDAMENTAL COMPLETO': 0,
        'ENSINO MÉDIO INCOMPLETO': 0,
        'ENSINO MÉDIO COMPLETO': 0,
        'SUPERIOR INCOMPLETO': 0,
        'SUPERIOR COMPLETO': 0,
    }

    total_cargo = 0

    # Contagem por cargo
    for i in arqv_todos:
        dados = i.strip().split(";")
        cargos = dados[3].strip()

        if cargos == cargo_alvo:
            total_cargo += 1
            estado_civil = dados[1].strip()
            genero = dados[2].strip()
            escolaridade = dados[0].strip()

            if estado_civil in contadores:
                contadores[estado_civil] += 1

            if genero in contadores:
                contadores[genero] += 1

            if escolaridade in contadores_grau:
                contadores_grau[escolaridade] += 1

    return total_cargo, contadores, contadores_grau



def imprimir_percentuais(total, contadores, contadores_grau, cargo):
    if total > 0:
        html2.write("<div class= cargo>\n")

        html2.write(f'<h1> {cargo} </h1>\n')
        html2.write(f'<p>{(contadores["SOLTEIRO(A)"] / total) * 100:.2f}% de <b>solteiros</b> </p>\n')
        html2.write(f'<p>{(contadores["CASADO(A)"] / total) * 100:.2f}% de <b>casados</b> </p>\n')
        html2.write(f'<p>{(contadores["DIVORCIADO(A)"] / total) * 100:.2f}% de <b>divorciados</b> </p>\n')
        html2.write(f'<p>{(contadores["VIÚVO(A)"] / total) * 100:.2f}% de <b>viúvos</b> </p>\n')
        

        html2.write(f'<p>{(contadores["FEMININO"] / total) * 100:.2f}% de <b>mulheres</b> </p>\n')
        html2.write(f'<p>{(contadores["MASCULINO"] / total) * 100:.2f}% de <b>homens</b> </p>\n')
        
        
        html2.write(f'<p>{(contadores_grau["LÊ E ESCREVE"] / total) * 100:.2f}% com "Lê e escreve" </p>\n')
        html2.write(f'<p>{(contadores_grau["ENSINO FUNDAMENTAL INCOMPLETO"] / total) * 100:.2f}% com <b>Ensino Fundamental Incompleto</b> </p>\n')
        html2.write(f'<p>{(contadores_grau["ENSINO FUNDAMENTAL COMPLETO"] / total) * 100:.2f}% com <b>Ensino Fundamental Completo</b> </p>\n')
        html2.write(f'<p>{(contadores_grau["ENSINO MÉDIO INCOMPLETO"] / total) * 100:.2f}% com <b>Ensino Médio Incompleto</b> </p>\n')
        html2.write(f'<p>{(contadores_grau["ENSINO MÉDIO COMPLETO"] / total) * 100:.2f}% com <b>Ensino Médio Completo</b> </p>\n')
        html2.write(f'<p>{(contadores_grau["SUPERIOR INCOMPLETO"] / total) * 100:.2f}% com S<b>uperior Incompleto</b> </p>\n')
        html2.write(f'<p>{(contadores_grau["SUPERIOR COMPLETO"] / total) * 100:.2f}% com <b>Superior Completo</b> </p>\n')
        

        html2.write("</div>\n")
        

with open("juntos.txt", "r",encoding="utf-8") as juntos:
    arqv_todos = montar_lista(juntos)

# Contando e imprimindo dados para cada cargo
for cargo in ["VEREADOR", "PREFEITO", "VICE-PREFEITO"]:
    total, contadores, contadores_grau = contar_dados(arqv_todos, cargo)
    imprimir_percentuais(total, contadores, contadores_grau, cargo)



html2.write("</section>")
html2.write("<br>\n")
html2.write("</main>\n")
html2.write("</body>\n")
html2.write("</html>\n")
html2.close()
