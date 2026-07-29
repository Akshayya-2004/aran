from sqlalchemy.orm import Session

from app.auth import (
    hash_password,
    verify_password,
    create_access_token
)
from app.models.user import User
from app.repositories import UserRepository
from app.schemas import (
    RegisterRequest,
    LoginRequest,
    Token
)


class AuthService:

    def __init__(self, db: Session):
        self.user_repository = UserRepository(db)

    def register(self, request: RegisterRequest) -> User:

        existing_user = self.user_repository.get_by_email(
            request.email
        )

        if existing_user:
            raise ValueError("Email already registered")

        user = User(
            full_name=request.full_name,
            email=request.email,
            password_hash=hash_password(request.password)
        )

        return self.user_repository.create(user)

    def login(
        self,
        email: str,
        password: str,
    ) -> Token:

        user = self.user_repository.get_by_email(email)

        if not user:
            raise ValueError("Invalid email or password")

        if not verify_password(
            password,
            user.password_hash,
        ):
            raise ValueError("Invalid email or password")

        access_token = create_access_token(
            {
                "sub": user.email
            }
        )

        return Token(
            access_token=access_token,
            token_type="bearer",
        )