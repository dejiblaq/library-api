from schemas.user_schema import User

class UserService:
    def get_user(self, users: list[User], user_id: int):
        for user in users:
            if user["id"] == user_id:
                return user
        
        return None
    

user_service = UserService()


