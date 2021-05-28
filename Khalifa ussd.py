print('NAME: SHEHU KHALIFA MUHAMMAD\n MATRIC NUMBER: U19/FNS/CSC/1017\n COMPUTER SCIENCE DEPARTMENT')
def back():
	if len(pin) == 4:
		print('your account balance is',balance,'Naira')
while True:
	list_of_account_name = ['Shehu khalifa Muhammad']
	list_of_account_number = []
	#my pin is 4444
	account_pin = 4444
	Balance = 5000000
	ussd_code = input("Enter ussd code here: ")
	if ussd_code == '*919#':
		print('UBA')
		print("1.Airtime self\n2.Airtime others\n3.Transfer UBA\n4.Transfer other banks\n5. Transfer UBA prepaid\n6.check balance\n7.Pay bills\n8.Next.")
		Choose = int(input('select Choose:'))
		if Choose == 1:
			pin = input('Enter your pin')
			if len(pin) == 4:
				amount = int (input('Please enter amount:'))
				print('Transaction successful')
				break
			else:
				print('Wrong pin')
				pin = input('Enter Pin to continue:')
				back()
			break
		elif Choose == 2:
			pin = input('Enter your Pin')
			if len(pin) ==4:
			   	amount = int(input('Enter amount:'))
			   	int (input('please enter destination phone number:'))
			   	print('Transaction succeful')
			   	break
			else:
				print('Wrong pin')
				pin = input('Enter pin to continue:')
				back()
			break
		elif Choose==3:
			pin = input('Enter your pin')
			if len(pin) ==4:
				amount = int(input('Enter amount:'))
				int (input('Enter UBA account number:'))
				print('Transaction succeful')
				break
			else:
				print('Wrong pin')
				pin = input('Enter pin to continue:')
				back()
			break
		elif Choose==4:
			pin = input('Enter your pin')
			if len(pin) ==4:
				int (input('please enter account number of the beneficiary'))
				amount = int(input('Enter amount:'))
				print('select bank')
				print("1.Access bank\n2.City bank nig limited\n3.Eco bank Nigeria plc\n4.FidelityBank plc\n5.First bank Nigeria limited\n6.First city monument bankplc\n7.GTB plc\n8.Unity bank \n9. Wema bank \n10.Zenith.")
				Choose = int(input('select option:'))
				if Choose == 1:
					pin = input('Enter your pin')
					if len(pin) == 4:
						print('Transaction succeful')
				elif Choose == 2:
					pin = input('Enter your pin')
					if len(pin) == 4:
						print('Transaction succeful')
				elif Choose == 3:
					pin = input('Enter your pin')
					if len(pin) == 4:
						print('Transaction succeful')
				elif Choose == 4:
					pin = input('Enter your pin')
					if len(pin) == 4:
						print('Transaction succeful')
				elif Choose == 5:
					pin = input('Enter your pin')
					if len(pin) == 4:
						print('Transaction succeful')
				elif Choose == 6:
					pin = input('Enter your pin')
					if len(pin) == 4:
						print('Transaction succeful')
				elif Choose == 7:
					pin = input('Enter your pin')
					if len(pin) == 4:
						print('Transaction succeful')
				elif Choose == 8:
					pin = input('Enter your pin')
					if len(pin) == 4:
						print('Transaction succeful')
				elif Choose == 9:
					pin = input('Enter your pin')
					if len(pin) == 4:
						print('Transaction succeful')
				elif Choose == 10:
					pin = input('Enter your pin')
					if len(pin) == 4:
						print('Transaction succeful')
					break
			else:
				print('Wrong pin')
				pin = input('Enter pin to continue:')
				back()
			break
		elif Choose==5:
			pin = input('Enter your pin')
			if len(pin) ==4:
				int (input('please enter card client ID (full 10 digit) or name of the beneficiary'))
				print('Transaction succeful')
			break
		elif Choose == 6:
			pin = input('Enter your pin')
			if len(pin) ==4:
				print('your account bal: 7500000')
			break
		elif Choose== 7:
			pin = input('Enter your pin')
			if len(pin) ==4:
				amount = int(input('Enter amount:'))
				print('please select')
				print("1.cable TV\n2.Betting l lottery\n3.Electricity - prepaid\n4. Electricity Post paid\n5.Tolls \n6.Next.")
				Choose = int(input('select option:'))
				if Choose == 1:
					pin = input('Enter your pin')
					if len(pin) == 4:
						print('Transaction succeful')
				elif Choose == 2:
					pin = input('Enter your pin')
					if len(pin) == 4:
						print('Transaction succeful')
				elif Choose == 3:
					pin = input('Enter your pin')
					if len(pin) == 4:
						print('Transaction succeful')
				elif Choose == 4:
					pin = input('Enter your pin')
					if len(pin) == 4:
						print('Transaction succeful')
				elif Choose == 5:
					pin = input('Enter your pin')
					if len(pin) == 4:
						print('Transaction succeful')
				elif Choose == 6:
					pin = input('Enter your pin')
					if len(pin) == 4:
						print('Transaction succeful')
				break
			else:
				print('Wrong pin')
				pin = input('Enter pin to continue:')
				back()
			break