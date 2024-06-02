from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class UserCreateDto:
    id: int
    username: str
    phone_number: str
    password: Optional[str]


@dataclass(frozen=True)
class UserCreateDto:
    id: int
    username: str
    phone_number: str
    password: Optional[str] 


@dataclass(frozen=True)
class UserGetDto:
    id: Optional[int]
    username: Optional[str]
    phone_number: Optional[str]


@dataclass(frozen=True)
class UserLevelDto:
    id: int
    level: int
   
