import subprocess
import random
import time
import threading
import os
from cryptography.fernet import Fernet

# Set this variable to True to encrypt, or False to decrypt
ENCRYPT_MODE = True  # Change to False for decryption

# Function to clear the terminal
def clear():
    os.system('clear')

# Function to check if there's internet connectivity
def check_internet():
    try:
        # Ping Google's DNS server to check for internet connection
        output = subprocess.run(['ping', '-c', '1', '8.8.8.8'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return output.returncode == 0
    except Exception:
        return False

# Function to generate a key for encryption
def generate_key():
    key = Fernet.generate_key()
    with open('secret.key', 'wb') as key_file:
        key_file.write(key)
    return key

# Function to encrypt the code
def encrypt_code():
    key = generate_key()
    cipher_suite = Fernet(key)
    # Read the original Python file
    with open(__file__, 'rb') as file:
        original_file = file.read()

    # Encrypt the file
    encrypted_file = cipher_suite.encrypt(original_file)

    # Save the encrypted file
    with open('your_script_encrypted.py', 'wb') as file:
        file.write(encrypted_file)

    print("Encryption complete. Key saved as 'secret.key'.")

# Function to decrypt the code
def decrypt_code():
    # Load the key for decryption
    with open('secret.key', 'rb') as key_file:
        key = key_file.read()

    cipher_suite = Fernet(key)

    # Read the encrypted file
    with open('your_script_encrypted.py', 'rb') as file:
        encrypted_file = file.read()

    # Decrypt the file
    decrypted_file = cipher_suite.decrypt(encrypted_file)

    # Save the decrypted file
    with open('your_script_decrypted.py', 'wb') as file:
        file.write(decrypted_file)

    print("Decryption complete. Decrypted file saved as 'your_script_decrypted.py'.")

# Loading animation function
def loading_animation(message):
    animation = "|/\|/"
    idx = 0
    while loading:
        print(f"\r{message}... {animation[idx]}", end="")
        idx = (idx + 1) % len(animation)
        time.sleep(0.1)
    print("\r" + " " * (len(message) + 12) + "\r", end="")  # Clear the line after animation ends

# Main function
if __name__ == "__main__":
    # Start loading animation thread for internet check
    loading = True
    loading_thread = threading.Thread(target=loading_animation, args=("Checking for internet connection",))
    loading_thread.start()

    # Check internet connectivity before proceeding
    if not check_internet():
        loading = False
        loading_thread.join()  # Wait for the loading thread to finish
        print("\033[31mNo internet connection. Please connect to the internet to use this tool.\033[0m")
        exit()

    loading = False
    loading_thread.join()  # Wait for the loading thread to finish

    clear()  # Clear the terminal after checking internet connection

    if ENCRYPT_MODE:
        encrypt_code()
    else:
        if os.path.exists('secret.key') and os.path.exists('your_script_encrypted.py'):
            decrypt_code()
        else:
            print("Decryption files do not exist. Please ensure 'secret.key' and 'your_script_encrypted.py' are present.")
            exit()

    # The rest of your script goes here...
    # ANSI escape sequences for colors
    RESET = "\033[0m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"

    def show_banner():
        banner = f"""
      {CYAN}   _______  _______  __   __  __   __  _______  __
        |       ||   _   ||  | |  ||  | |  ||       ||  |
        |    ___||  |_|  ||  |_|  ||  |_|  ||    ___||  |
        |   |___ |       ||       ||       ||   |___ |  |
        |    ___||       ||       ||       ||    ___||__|
        |   |___ |   _   ||   _   ||   _   ||   |___  __
        |_______||__| |__||__| |__||__| |__||_______||__|
        {YELLOW}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
          [☬] {GREEN}DEVELOPER   :   𝕊𝕙𝕠𝕟𝕔𝕙𝕠𝕪𝕠𝕟 𝔹𝕒𝕣𝕦𝕒 𝔸𝕕𝕚𝕣𝕥𝕥𝕒
          [☬] {GREEN}FACEBOOK    :   𝕊𝕙𝕠𝕟𝕔𝕙𝕠𝕪𝕠𝕟 𝔹𝕒𝕣𝕦𝕒 𝔸𝕕𝕚𝕣𝕥𝕥𝕒
          [☬] {GREEN}TOOL TYPE   :   FB-CLONING
          [☬] {GREEN}VERSION     :   RANDOM
          [☬] {GREEN}LOGIN METHOD:   use v.p.n.
        {YELLOW}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
        """
        print(banner)

    def generate_11_digit_number(network_choice):
        # Valid Bangladeshi phone number prefixes based on selected network
        network_prefixes = {
            "1": ["017", "013"],  # Grameenphone
            "2": ["019"],          # Banglalink
            "3": ["015"],          # Teletalk
            "4": ["016"],          # Airtel
            "5": ["018"],          # Robi
            "6": ["017", "019", "015", "016", "018"]  # ALL MIX
        }

        # Choose a random prefix from the selected network
        prefix = random.choice(network_prefixes[network_choice])

        # Generate the rest of the 8 digits
        number = prefix + ''.join(random.choices('0123456789', k=8))

        return number

    def generate_data(num_entries, network_choice):
        entries = []
        for _ in range(num_entries):
            number = generate_11_digit_number(network_choice)
            password = number  # Password is the same as the generated number
            entry = f"+88{number}|{password}"
            entries.append(entry)
            print(f"{GREEN}[𝒜𝒟𝐼_💣]➤➤➤[O҉K҉🤍]:➤ {entry}{RESET}")  # Modified print statement
            time.sleep(0.1)  # Reduced wait time to 0.1 seconds for faster generation
        return entries

    def save_to_file(filename, data):
        with open(filename, 'w') as file:
            for entry in data:
                file.write(entry + '\n')

    def get_user_choice():
        print("\nChoose a network:")
        print("[01] 𝘎𝘳𝘢𝘮𝘦𝘦𝘯𝘱𝘩𝘰𝘯𝘦")
        print("[02] 𝙱𝚊𝚗𝚐𝚕𝚒𝚗𝚔")
        print("[03] 𝚃𝚎𝚕𝚎𝚝𝚊𝚕𝚔")
        print("[04] 𝙰𝚒𝚛𝚝𝚎𝚕")
        print("[05] 𝚁𝚘𝚋𝚒")
        print("[06] 𝘈𝘓𝘓 𝘔𝘐𝘹")
        print("\nSelect your network (1-6):")

        network_choice = input().strip()

        if network_choice not in ["1", "2", "3", "4", "5", "6"]:
            print(f"{RED}Invalid choice, defaulting to ALL MIX (06).{RESET}")
            network_choice = "6"

        print("\n(1) Generate 900 entries")
        print("(2) Generate 500 entries")
        print("(3) Generate 200 entries")
        print("(4) Enter custom number of entries")

        choice = input("\nEnter your choice (1-4): ")

        if choice == '1':
            num_entries = 900
        elif choice == '2':
            num_entries = 500
        elif choice == '3':
            num_entries = 200
        elif choice == '4':
            custom_choice = int(input("Enter the number of entries to generate: "))
            num_entries = custom_choice
        else:
            print(f"{RED}Invalid choice, defaulting to 10 entries.{RESET}")
            num_entries = 10

        return num_entries, network_choice

    # Show the banner
    show_banner()

    # Get user choice for the number of entries and network
    num_entries, network_choice = get_user_choice()

    # Generate the chosen number of entries
    data = generate_data(num_entries, network_choice)

    # Save the data to a file in Termux
    filename = '𝒜𝒟𝐼_ᗪᗩ丅ᗩ.txt'
    save_to_file(filename, data)

    print(f"{YELLOW}\nData saved to {filename}{RESET}")

    print(f"{RED}\ncode by S҉H҉I҉N҉C҉H҉O҉Y҉O҉N҉ ҉B҉A҉R҉U҉A҉ ҉A҉D҉I҉R҉T҉T҉A҉{RESET}")
