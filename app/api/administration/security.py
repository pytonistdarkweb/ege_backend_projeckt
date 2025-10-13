from fastapi import APIRouter, Depends, Request,status
from app.service.user_service import UserService
from schema import User

router = APIRouter()


@router.post(
    "/authentication/{User}/"
    summary="аунтификация пользователя",
    status_code=status.HTTP_201_OK,
    responses={status.HTTP_400_BAD_REQUEST},
    )
async def authentication_user(
    user:User,
    user_service:UserService = Depends(),
):
    return await user_service.create_user(validate_user=user)

