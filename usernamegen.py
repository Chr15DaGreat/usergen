import random
from usernamelist import firstword, secondword
def generate_username():
    username = random.choice(firstword) + random.choice(secondword) + str(random.randint(10, 99))
    return username

username = generate_username()
print ("Generated Username:", username)