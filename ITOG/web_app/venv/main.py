from openapi_client import openapi

token = 'тут нужно вставить ваш токен'  
client = openapi.api_client(token)

pf = client.portfolio.portfolio_get()