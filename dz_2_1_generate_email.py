import string
import random
def generate_email():
	domain=['gmail.com', 'mail.ru', 'yahoo.com', 'email.ua', 'i.ua', 'hotmail.com']
	email_adres=''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(random.randint(5,10)))
	
	return email_adres + '@' + domain[random.randint(0,len(domain)-1)]
		 
print(generate_email())
