from typing import Any
from models.comment import Comment
from models.constants.user_role import User
import re
from comment import Comment

class User:
    USERNAME_LEN_MIN = 2
    USERNAME_LEN_MAX = 20
    USERNAME_LEN_ERR = f'Username must be between {USERNAME_LEN_MIN} and {USERNAME_LEN_MAX} characters long!'
    USERNAME_INVALID_SYMBOLS = 'Username contains invalid symbols!'

    PASSWORD_LEN_MIN = 5
    PASSWORD_LEN_MAX = 30
    PASSWORD_LEN_ERR = f'Password must be between {PASSWORD_LEN_MIN} and {PASSWORD_LEN_MAX} characters long!'
    PASSWORD_INVALID_SYMBOLS = 'Password contains invalid symbols!'

    LASTNAME_LEN_MIN = 2
    LASTNAME_LEN_MAX = 20
    LASTNAME_LEN_ERR = f'Lastname must be between {LASTNAME_LEN_MIN} and {LASTNAME_LEN_MAX} characters long!'

    FIRSTNAME_LEN_MIN = 2
    FIRSTNAME_LEN_MAX = 20
    FIRSTNAME_LEN_ERR = f'Firstname must be between {FIRSTNAME_LEN_MIN} and {FIRSTNAME_LEN_MAX} characters long!'

    NORMAL_ROLE_VEHICLE_LIMIT = 5

    NORMAL_USER_LIMIT_REACHED_ERR = f'You are not VIP and cannot add more than {NORMAL_ROLE_VEHICLE_LIMIT} vehicles!'
    ADMIN_CANNOT_ADD_VEHICLES_ERR = 'You are an admin and therefore cannot add vehicles!'
    YOU_ARE_NOT_THE_AUTHOR = 'You are not the author of the comment you are trying to remove!'
    THE_VEHICLE_DOES_NOT_EXIT = 'The vehicle does not exist!'

    # Todo: Finish the implementation
    # Names of methods/attributes should be exactly match those in the README file

    def __init__(self, username, firstname, lastname, password, user_role = 'Normal'):
        self.username = username
        self.firstname = firstname
        self.lastname = lastname
        self.password = password
        self.user_role = user_role
        self.vehicles = []

    def validate(self):
        if len(self.username) < User.USERNAME_LEN_MIN or len(self.username) > User.USERNAME_LEN_MAX:
            raise ValueError(User.USERNAME_LEN_ERR)
        if not self.username.isalnum():
            raise ValueError(User.USERNAME_INVALID_SYMBOLS)
        if not User.PASSWORD_LEN_MIN < self.password < User.PASSWORD_LEN_MAX:
            raise ValueError(User.PASSWORD_LEN_ERR)
        if not re.match(r'^[a-zA-Z0-9@*_\-]+$', self.password):
            raise ValueError(User.PASSWORD_INVALID_SYMBOLS)
        if not User.LASTNAME_LEN_MIN < self.lastname < User.LASTNAME_LEN_MAX:
            raise ValueError(User.LASTNAME_LEN_ERR)
        if not User.FIRSTNAME_LEN_MIN < self.firstname < User.FIRSTNAME_LEN_MAX:
            raise ValueError(User.FIRSTNAME_LEN_ERR)
        if self.user_role not in User:
            raise ValueError('invalid user role.')
        
    def add_vehicle(self, vehicle):
        if self.user_role == 'Admin':
            raise ValueError('Admin cannot add vehicles')
        if self.user_role != 'Vip' and len(vehicle) > 5:
            raise ValueError('You cannot add more than 5 vehicles')
        self.vehicles.append(vehicle)

    def remove_vehicle(self, index):
        if index < 0 or index > len(self.vehicles):
            raise ValueError ('Invalid Index.')
        del self.vehicles[index]
    
    def get_vehicle_by_index(self, index):
        if index < 0 or index > len(self.vehicles):
            raise ValueError('Invalid index')
        return self.vehicles[index]

    def adding_comment(self, content, vehicle_index):
        comment = Comment(User.username, content)
        comment.validate
        self.vehicles[vehicle_index].comments.append(comment)

    def remove_comment(self, vehicle_index, comment_index ,username):
        if comment_index < 0 or comment_index > len(self.vehicles[vehicle_index]):
            raise ValueError('Invalid comment index')
        if self.vehicles[vehicle_index].comments[comment_index].user != username:
            raise ValueError('You are not the creator of this comment')
        del self.vehicles[vehicle_index].comments[comment_index]

    def __str__(self):
        return f'{self.username}, FullName: {self.firstname} {self.lastname}, Role: {self.user_role}'
        