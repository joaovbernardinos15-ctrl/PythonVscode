print("--- Inicializando Servidor da Partida ---")
# Se o arquivo não existir na pasta, o programa para e a mensagem final nunca é exibida
try: 
    arquivo = open("config_fase.txt", "r")
    conteudo = arquivo.read()
    print("Configurações carregadas com sucesso!")
    arquivo.close()
except FileNotFoundError:
    print("Arquivo de configuração não encontrado.")
    
finally: #Colocar o finally na ultima parte o resto estáva tudo correto
    print("[Status] Processo de boot finalizado. Limpando memória...")   

