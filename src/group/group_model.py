from typing import List


class GroupModel:
    def __init__(self, id: int, name: str, users: List[int]):
        self.id = id
        self.name = name
        self.users = users  # lista de IDs de usuários associados a este grupo
