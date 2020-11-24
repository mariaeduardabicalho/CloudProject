# importing the requests library 
import requests 

# api-endpoint 
URL = 'http://duda-load-balancer-1289991165.us-east-1.elb.amazonaws.com:8080/tasks'


# # defining a params dict for the parameters to be sent to the API 
# PARAMS = {'address':location} 

# sending get request and saving the response as response object 
r = requests.get(url = URL) 


# extracting data in json format 
data = r.json() 



