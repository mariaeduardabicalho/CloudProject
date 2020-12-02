# importing the requests library 
import requests 

# api-endpoint 
URL = 'newproj-load-balancer-655990403.us-east-1.elb.amazonaws.com:8080/tasks'


# # defining a params dict for the parameters to be sent to the API 
# PARAMS = {'address':location} 

# sending get request and saving the response as response object 
r = requests.get(url = URL) 
print(r)

# data = r.json() 

# print(data)

r = requests.post('newproj-load-balancer-655990403.us-east-1.elb.amazonaws.com:8080/index', json={"title": "test"})
# extracting data in json format 
# data = r.json() 

# print(data)
print(r)



