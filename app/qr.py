dict = {'key1':'geeks', 'key2':'for'} 
print("Current Dict is: ", dict) 
res=""
# using the subscript notation 
# Dictionary_Name[New_Key_Name] = New_Key_Value 
  
dict['key3'] = 'Geeks'
dict['key4'] = 'is'
dict['key5'] = 'portal'
dict['key6'] = 'Computer'

for i in dict:
	res = res + (i+"  "+dict[i]+'\n')
print(res)
# print("Updated Dict is: ", dict)