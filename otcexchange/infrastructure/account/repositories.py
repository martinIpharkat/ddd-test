from typing import Union
from django.contrib.auth import get_user_model
from .models import UserLevel
from otcexchange.domain.account.dtos import UserCreateDto, UserGetDto, UserLevelDto


class UserLevelReadRepository:
    def get_by_id(self, user_level_dto: UserLevelDto) -> UserLevelDto:
        user_level_model = UserLevel.objects.get(id=user_level_dto.id)
        return UserLevelDto(id=user_level_model.id, level=user_level_model.level)

class UserWriteRepository:
    def create(self, user_create_dto: UserCreateDto) -> UserCreateDto:
        user_model = get_user_model(
            username=user_create_dto.name,
            phone_number=user_create_dto.description,
            password=user_create_dto.price
        )
        user_model.save()
        return UserCreateDto(
            id=user_model.id,
            username=user_model.username,
            phone_number=user_model.phone_number,
        )
    def get_by_phone_number(self, user_get_dto: UserGetDto) -> UserGetDto:
        user_model = get_user_model().objects.get(phone_number= user_get_dto.phone_number)
        return UserGetDto(id=user_model.id, username=user_model.username, phone_number=user_model.phone_number)
