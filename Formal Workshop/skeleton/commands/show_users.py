from core.application_data import ApplicationData
from models.constants.user_role import UserRole
class ShowUsersCommand():

    def execute(self, app_data):
        users_list = app_data

        if not users_list:
            return ('--USERS--\nNo users registered.')
        
        user_output = '--USERS--\n'
        for index, user in enumerate(users_list, start= 1):
            user_output += f'{index}. {user.username}, Fullname: {user.firstname} {user.lastname}, Role {user.user_role}\n'

        return user_output

                
