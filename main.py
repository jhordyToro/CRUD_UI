import json

class User():

#-------------------------------------this function creates a user and saves it in data.json--------------------------------------------------
    
    def create_user(self,user):
        with open("data.json","r+", encoding='utf-8') as f:
            result = json.loads(f.read())
            user_dict = user
            result.append(user_dict)
            f.truncate(0)
            f.seek(0)
            f.write(json.dumps(result))
            print(user_dict)
            return user_dict

    
    
#--------------------------------------this function updates a user and saves it in data.json-------------------------------------------------

    def upload_user(self,user,id):
        #here I subtract 1 to make it easier for people (the id refers to the position in which the json that we are going to modify is located)
        id -= 1 

        with open('data.json', 'r+', encoding='utf-8') as f:
            result = json.loads(f.read())
            result.pop(id)
            result.insert(id,user)
            f.truncate(0)
            f.seek(0)
            f.write(json.dumps(result)) 
            id += 1
            print(user)
            print(f'user {id} upload successfully') 
            return user,id

    

#---------------------------------this function deletes a user and updates the data.json------------------------------------------------------
    
    def delete_user(self,id):
        #here I subtract 1 to make it easier for people (the id refers to the position in which the json that we are going to modify is found)
        id -= 1

        with open('data.json', 'r+', encoding='utf-8') as f:
            result = json.loads(f.read())
            result.pop(id)
            f.truncate(0)
            f.seek(0)

            test = f.read()
            f.seek(0)
            
            f.write(json.dumps(result))
            print(f'user {id} delete successfully') 
            id += 1
            
            return id,test



#---------------------------------this function shows all users saved in data.json-------------------------------------------------    
    
    def show_user(self):
        with open('data.json', 'r+', encoding='utf-8') as f:
            result = json.loads(f.read())
            f.truncate(0)
            f.seek(0) 
            f.write(json.dumps(result)) 
            print(result)
            return result
