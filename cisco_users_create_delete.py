import io
import os
from netmiko import ConnectHandler

with open(file="hosts.txt", mode="r") as hosts:


    devices = [{
        'device_type' : 'cisco_ios',
        'ip' : ip,
        'username' : 'username',
        'password' : 'password',
        'secret' : 'secret',
    }
    for ip in hosts.read().splitlines()
    ]
#print(devices)

for device in (devices):
    try:
        net_connect = ConnectHandler(**device)
        net_connect.enable()
        #net_connect.config_mode()

        print ({device['ip']})        
        
        #prompt = net_connect.find_prompt()
        sh_runn_name = net_connect.send_command('sh running-config | include hostname')
        #sh_clock = net_connect.send_command('sh clock')
        print(sh_runn_name)

    #Bloco abaixo para INCLUSÃO de novos usuários

        commands = ['username ******** privilege 15 secret **********',  
                    'username ******** privilege 15 secret **********',
                    'end', 'wr'
                    ]
        
    #Bloco abaixo para REMOÇÃO de usuários
        
        ''' commands = ['no username ********',
                    'no username ********',
                    'no username ********',
                    'end', 'wr'
                    ]'''
        
        output = net_connect.send_config_set(commands)
        #print (output)

        '''with open(file="honda_.txt", mode="a", encoding = "utf-8" ) as arquivo:
            for texto in sh_runn_name, {device['ip']}, output:
                arquivo.write(str(texto))
                arquivo.write('\n\r')
        arquivo.close()'''
        
    except:
            erro = ({device['ip']})
            with open('erro.txt', 'a', encoding= 'utf-8') as falhas:
                for texta in erro:
                    falhas.write(str(texta))
                    falhas.write('\n\r')
                    falhas.close()
    continue
net_connect.disconnect()
os.system("pause")