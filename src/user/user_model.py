from typing import List


class UserModel:
    def __init__(self, id: int, name: str, groups: List[int]):
        self.id = id
        self.name = name
        self.groups = groups  # lista de IDs de grupos aos quais o usuário pertence


class UserCreate:
    def __init__(self, name: str):
        self.name = name
