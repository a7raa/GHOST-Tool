import requests
import os

def ghost_header():
    os.system("clear")
    print(r"""
    ######################################
    #      _____ _    _  ____   _____ _______ 
    #     / ____| |  | |/ __ \ / ____|__   __|
    #    | |  __| |__| | |  | | (___    | |   
    #    | | |_ |  __  | |  | |\___ \   | |   
    #    | |__| | |  | | |__| |____) |  | |   
    #     \_____|_|  |_|\____/|_____/   |_|   
    #                                         
    #          DEVELOPER: GHOST              
    ######################################
    """)

def check_username():
    username = input("\n[?] Enter Username to track: ")
    print(f"\n[*] Hunting for {username}...\n")
    social_media = {
        "Instagram": f"https://www.instagram.com/{username}",
        "TikTok": f"https://www.tiktok.com/@{username}",
        "Telegram": f"https://t.me/{username}",
        "Snapchat": f"https://www.snapchat.com/add/{username}",
        "Twitter": f"https://twitter.com/{username}",
        "GitHub": f"https://github.com/{username}"
    }
    for platform, url in social_media.items():
        try:
            headers = {'User-Agent': 'Mozilla/5.0'}
            res = requests.get(url, headers=headers, timeout=5)
            if res.status_code == 200:
                print(f"[+] Found on {platform}: {url}")
            else:
                print(f"[-] Not Found on {platform}")
        except:
            print(f"[!] Error on {platform}")

def check_email():
    email = input("\n[?] Enter Email to check: ")
    print(f"[*] Searching leak databases for {email}...")
    url = f"https://api.proxynova.com/haveibeenpwned?email={email}"
    try:
        res = requests.get(url, timeout=10)
        if res.status_code == 200:
            print(f"\n[!] ALERT: This email is LEAKED!")
        else:
            print(f"\n[+] Safe! No public leaks found.")
    except:
        print("[!] Connection Error.")

def main():
    while True:
        ghost_header()
        print("1. Track Username (OSINT)")
        print("2. Check Email Safety")
        print("3. Exit")
        choice = input("\n[>] Select: ")
        if choice == "1":
            check_username()
            input("\nPress Enter...")
        elif choice == "2":
            check_email()
            input("\nPress Enter...")
        elif choice == "3":
            break

if __name__ == "__main__":
    main()
