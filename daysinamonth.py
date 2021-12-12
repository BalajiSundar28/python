m=input('enter month name')

if m.lower() in ['january','march','may','august','october','december']:
	
	print('31 days')
	
elif m.lower() in ['april','june','july','september','november']:
	
	print('30 days')
	
elif m.lower() in ['february']:
	
	ask=input('is it a leap year or not(y/n)')
	
	if ask.lower()=='y':
		
		print('29 days')
		
        else:
		
		print('28 days')
		
else:

        print('invalid month name')
	
