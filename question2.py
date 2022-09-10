#Printing a dictionary using unpacking and formatting

def dic_details(**details):
    for key,value in details.items():
        print('{} : {}'.format(key,value))

country={"name":"Germany",
         "population":"83 million",
         "capital":"Berlin",
         "currency":"Euro"}

dic_details(**country)
