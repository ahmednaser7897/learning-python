name1=input("Enter your first name:")
name2=input("Enter your middel name:")
name3=input("Enter your last name:")
name1=name1.title().strip()
name2=name2.title().strip()
name3=name3.title().strip()

print(f"hello {name1} {name2:.1s} {name3} how are you?")

email=input("enter your email:")
username=email[:email.index("@")].strip()
domain=email[email.index("@")+1:].strip()
print(f"your username is {username} and your domain is {domain}")
