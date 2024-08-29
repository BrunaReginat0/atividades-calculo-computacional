import psutil
import mysql.connector

db_connection = mysql.connector.connect(host='localhost', user='root', password='150621', database='desafioExtreme')
cursor = db_connection.cursor()

cursor.execute("SELECT nome FROM maquinas")
resultadoMaquina = cursor.fetchall()

i = 0
j = 0

while j == 0:

    print("OPÇÕES DE MÁQUINAS")
    print("""
    M1
    M2
    M3
    M4
    """)

    opcaoMaquina = input("Selecione a máquina que você deseja monitorar:")

    print("\n")
    print("""
    OPÇÕES DE COMPONENTES
    1 - CPU
    2 - MEMÓRIA
    3 - DISCO
    """)
    opcaoComponente = int(input("Selecione qual componente você deseja monitorar:"))

    print("\n")
    print("""
    OPÇÕES DE MEDIDA
    1 - PERCENTUAL
    2 - BYTES
    (CASO VOCÊ TENHA ESCOLHIDO MONITORAR CPU, A OPÇÃO BYTES SERÁ Hz)
    """)
    opcaoMedida = int(input("Selecione qual unidade de medida você deseja:"))

    print("\n")
    print("""
    OPÇÕES DE MÉDIA
    1 - MÉDIA POR MÁQUINA
    2 - MÉDIA TOTAL
    """)
    opcaoMedia = int(input("Selecione qual tipo de média:"))

    resultadoCpuPercent = float(psutil.cpu_percent(interval=1))
    resultadoCPUFreq = psutil.cpu_freq().current
    resultadoMemoriaPercent = psutil.virtual_memory()
    resultadoMemoriaTotal = psutil.virtual_memory()
    resultadoDiscoPercent = psutil.disk_usage('C:\\')
    resultadoDiscoTotal = psutil.disk_usage('C:\\')


    sql = "INSERT INTO registros (resultadoCpuPercent, resultadoCPUFreq, resultadoMemoriaPercent, resultadoMemoriaTotal, resultadoDiscoPercent, resultadoDiscoTotal, nomeMaquina) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    values = (resultadoCpuPercent, resultadoCPUFreq, resultadoMemoriaPercent.percent, resultadoMemoriaTotal.total, resultadoDiscoPercent.percent, resultadoDiscoTotal.total, opcaoMaquina)
    cursor.execute(sql, values)
    db_connection.commit()


    if(opcaoComponente == 1  and  opcaoMedida == 1):
        print(f"""
        MONITORAMENTO DA SUA MÁQUINA
        -------------------------------------------        
        Percentual CPU: {float(psutil.cpu_percent(interval=1))}
        """)
    elif(opcaoComponente == 1  and  opcaoMedida == 2):
        print(f"""
        MONITORAMENTO DA SUA MÁQUINA
        -------------------------------------------      
        Frequência CPU: {psutil.cpu_freq().current}
        """)

    if(opcaoComponente == 2  and  opcaoMedida == 1):
        print(f"""
        MONITORAMENTO DA SUA MÁQUINA
        -------------------------------------------      
        Percentual Memória: {psutil.virtual_memory().percent}
        """)
    elif(opcaoComponente == 2  and  opcaoMedida == 2):
        print(f"""
        MONITORAMENTO DA SUA MÁQUINA
        -------------------------------------------      
        Bytes Memória: {psutil.virtual_memory().total}
        """)

    if(opcaoComponente == 3  and  opcaoMedida == 1):
        print(f"""
        MONITORAMENTO DA SUA MÁQUINA
        -------------------------------------------      
        Percentual Disco: {psutil.disk_usage('C:\\').percent}
        """)
    elif(opcaoComponente == 3  and  opcaoMedida == 2):
        print(f"""
        MONITORAMENTO DA SUA MÁQUINA
        -------------------------------------------      
        Bytes Disco: {psutil.disk_usage('C:\\').total}
        """)


    continuar=str(input('Digite "SIM" para realizar outro registro | Digite "NAO" para sair -> '))
    if continuar == "SIM":
        j = 0
        print("\n" * 130)
    else:
        j = 1
        print("\n" * 130)
        print("Muito obrigada por participar do nosso sistema!!!")












