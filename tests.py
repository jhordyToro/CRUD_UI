from main import *
import unittest

main = User()

#-------------This function is used to save code when creating a user-----------------------------
def user():
    user_test = {
        'first_name': 'jhordy',
        'last_name': 'Toro Arroyo',
        'age': 17,
        'email': 'example.com',
    }
    return user_test

class Main_tests(unittest.TestCase):

#-------------------test for the function of creating a user---------------------------------
    
    def test_create_user(self):
        user_test = user()
        user_dict_funtion = main.create_user(user_test)
        self.assertEqual(user_dict_funtion,user_test)

#--------------------test for the function to update a user--------------------------------------
    
    def test_upload_user(self):
        user_test = user()
        id = 1
        result,result_id = main.upload_user(user_test,id)
        self.assertEqual(user_test,result)
        self.assertEqual(id,result_id)

#---------------------test for the function to delete a user-----------------------------------
    
    
    def test_delete_user(self):
        id = 1
        result_id,test_file = main.delete_user(id)
        self.assertEqual(result_id,id)
        self.assertEqual(test_file,'')

#----------------------function test to see all users------------------------------------------    
    
    def test_show_users(self):
        result_test = main.show_user()
        if result_test:
            self.assertNotEqual(result_test,'')
        else:
            self.assertEqual(result_test,'')



if __name__ == '__main__':
    unittest.main()
