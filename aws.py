##from googleapiclient import discovery
##from googleapiclient import errors


##project_id = 'projects/{}'.format('YOUR_PROJECT_ID')


##ml = discovery.build('ml', 'v1')


##request_dict = {'name': 'your_model_name', 'description': 'your_model_description'}


##request = ml.projects().models().create(parent=project_id, body=request_dict)


##try:
  ##  response = request.execute()
    ##print(response)
##except errors.HttpError, err :
  ##  print('There was an error creating the model. Check the details:')
    ##print(err._get_reason())



num=int(input("Enter a number:"))
temp=num
rev=0
while(num>0):
    dig=num%10
    rev=rev*10+dig
    num=num//10
if(temp==rev):
    print("palindrome")
else:
    print("Not a palindrome")

