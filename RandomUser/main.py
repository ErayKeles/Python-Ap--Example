import random
import string
import requests
from concurrent.futures import ThreadPoolExecutor

# Rastgele Tc
def generate_random_tc_number():
    return ''.join([str(random.randint(0, 9)) for _ in range(11)])

# Rastgele İsim soyısım
def generate_random_string(length):
    return ''.join(random.choices(string.ascii_letters, k=length))

# Rastgele Telefon
def generate_random_msisdn():
    return ''.join([str(random.randint(0, 9)) for _ in range(12)])

# Rastgele Email
def generate_random_email():
    domains = ["gmail.com", "hotmail.com", "outlook.com", "yahoo.com", "live.com"]
    domain = random.choice(domains)
    return f"{generate_random_string(10)}@{domain}"

# POST isteği
def register_user(i):
    url = 'http://35.242.205.201/v1/api/auth/register'
    headers = {
        'accept': '*/*',
        'Content-Type': 'application/json'
    }

    user_data = {
        "name": generate_random_string(10),
        "surname": generate_random_string(10),
        "msisdn": generate_random_msisdn(),
        "email": generate_random_email(),
        "password": "YourSecurePassword123!",
        "TCNumber": generate_random_tc_number(),
        "packageName": "EVRENCELL MERCURY"
    }

    response = requests.post(url, headers=headers, json=user_data)
    if response.status_code == 200:
        print(f"User {i} registered successfully.")
    else:
        print(f"Error for user {i}: {response.status_code} - {response.text}")

# multı thread
def register_users_concurrently(total_users):
    with ThreadPoolExecutor(max_workers=200) as executor:
        executor.map(register_user, range(total_users))

if __name__ == "__main__":
    register_users_concurrently(10000)  # 10.000 kayıt eklemek için
