from otcexchange.infrastructure.account.repositories import UserWriteRepository


class UserService:
    def __init__(self):
        self.repository = UserWriteRepository()

    def create(self, data):
        # Define custom service logic here
        return self.repository.create(data)

    # def get_all(self):
    #     # Define custom service logic here
    #     return self.repository.get_all()

    # def get_by_id(self, id):
    #     # Define custom service logic here
    #     return self.repository.get_by_id(id)

    # def update(self, id, data):
    #     # Define custom service logic here
    #     instance = self.get_by_id(id)
    #     return self.repository.update(instance, data)

    # def delete(self, id):
    #     # Define custom service logic here
    #     instance = self.get_by_id(id)
    #     return self.repository.delete(instance)