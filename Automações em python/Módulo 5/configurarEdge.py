from selenium import webdriver
from selenium.webdriver.edge.options import Options

def iniciarDriver():

    edge_options = Options()
    # Fonte de opções de switches https://chromium.googlesource.com/chromium/src/+/master/chrome/common/chrome_switches.cc e  https://peter.sh/experiments/chromium-command-line-switches/

    '''
    --start-maximized # Inicia maximizado
    --lang=pt-BR # Define o idioma de inicialização, # en-US , pt-BR
    --incognito # Usar o modo anônimo
    --window-size=800,800 # Define a resolução da janela em largura e altura
    --headless # Roda em segundo plano(com a janela fechada)
    --disable-notifications # Desabilita notificações
    --disable-gpu # Desabilita renderização com GPU
    '''

    arguments = [ '--lang=pt-BR' , '--window-size=800,600' 
                , '--incognito']


    for argument in arguments:
        edge_options.add_argument(argument)
    # Lista de opções experimentais(nem todas estão documentadas) https://chromium.googlesource.com/chromium/src/+/master/chrome/common/pref_names.cc
    # Uso de configurações experimentais
    edge_options.add_experimental_option('prefs', {
        # Desabilitar notificações
        'profile.default_content_setting_values.notifications': 2,
    })
    # inicializando o webdriver
    driver = webdriver.Edge(options=edge_options)
    return driver

driver = iniciarDriver()
# Navegar até um site
driver.get('https://www.instagram.com')

input('aperta uma tecla para fechar')