from fastapi import APIRouter, Depends, Request,status
from schema import User
router = APIRouter()

@router.post(
    "/authentication/{User}/"
    summary="аунтификация пользователя",
    status_code=status.HTTP_200_OK,
    response_model=User,
    responses={status.HTTP_400_BAD_REQUEST},
    )
async def authentication_user(
    request:Request,
    user:User,
    user_service:User_service = Depends(),
):
    return await user_service.user_add(validate_user=user,request=request)

