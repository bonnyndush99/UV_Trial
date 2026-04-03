#!/usr/bin/python3

# Start a while loop
print("User: Administrator")
while True:
	#get user input
	my_pass = input("enter password: ").lower()

	# use nested if to test password
	if my_pass == "rootme":
		print("[+]Login Successful")
		print("Welcome Administrator")
		break
	else:
		print("[-]Wrong Password!!Try again")

print("\n")
print("Goodbye")