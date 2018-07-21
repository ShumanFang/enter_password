# code to enter password
# password = 'a123456'
# can enter password multiple times
# maximum 3 times
# if correct password, print'sign on success'
# if wrong pass word, print 'wrong passwrod, x more tries'




### own attempt
pswd = input('please enter password')
i = 2
while pswd != 'a123456' and i > 0:
	print('wrong password, you have ', i, 'more tries')
	pswd = input('please enter password:')
	i = i - 1
if pswd == 'a123456':
	print('sign on success')




# # offcial answer
# password = 'a123456'
# i = 3 # times left
# while True:
# 	pwd = input('please enter password: ')
# 	if pwd == password:
# 		print('sign on success')
# 		break
# 	else:
# 		i = i - 1
# 		print('wrong password, you have', i, 'more tries')
# 		if i == 0:
# 			break
