import psutil
import time
import mysql.connector
from socket import gethostname

i = 0
NomeMaquina = gethostname()

db_connection = mysql.connector.connect(host='10.18.33.25', user='enzo', password='Ensunel@2006', database='testeAutomacao')
cursor = db_connection.cursor()


while True:
    UsoDeCPU = psutil.cpu_percent(interval=1)
    FreqDeCPU = psutil.cpu_freq()
    UsoDeMemo = psutil.virtual_memory()
    UsoDeDisco = psutil.disk_usage('C:\\')
    i = i + 1

    sql = "INSERT INTO registros (percentualCPU, usoCPU, usoMemoria, usoDisco, NomeMaquina) VALUES (%s, %s, %s, %s, %s)"
    values = (FreqDeCPU.current, UsoDeCPU, UsoDeMemo.percent, UsoDeDisco.percent, NomeMaquina)
    cursor.execute(sql, values)
    db_connection.commit()

    print(
    """
    {:.1f}º CAPTURA
    ----------------------------------
    Percentual de uso de CPU: {:.2f}%
    Frequência da CPU: {:.2f} MHz

    Percentual de uso da Memória: {:.2f}%

    Percentual de uso do Disco: {:.2f}%

    """.format(i, UsoDeCPU, FreqDeCPU.current, UsoDeMemo.percent, UsoDeDisco.percent))
    time.sleep(3)



    