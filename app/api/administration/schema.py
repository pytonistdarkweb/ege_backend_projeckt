from pydantic import BaseModel, ConfigDict, EmailStr, Field, field_validator


class User(BaseModel):
    name: str = Field(min_length=6, max_length=20)
    surname: str = Field(min_length=2, max_length=20)
    password: str
    email: EmailStr

    model_config = ConfigDict(from_attributes=True)



    @field_validator('password')
    def password_validator(cls, password: str):
        match len(password):
            case length if length < 6:
                raise ValueError('Пароль должен содержать минимум 6 символов')
            case length if length > 20:
                raise ValueError('Пароль не должен превышать 20 символов')
            case _:
                pass
        patterns = {
            r'[A-Z]': 'заглавную букву',
            r'[a-z]': 'строчную букву',
            r'\d': 'цифру',
            r'[!@#$%^&*(),.?":{}|<>]': 'специальный символ'
        }
        missing = [desc for pattern, desc in patterns.items() if not re.search(pattern, password)]
        match len(missing):
            case 0:
                return password
            case 1:
                raise ValueError(f'Пароль должен содержать {missing[0]}')
            case _:
                raise ValueError(f'Пароль должен содержать: {", ".join(missing)}')

    @field_validator('email')
    def email_validator(cls, email: str) -> str:
        match len(email):
            case length if length > 254:
                raise ValueError('Email не должен превышать 254 символа')
            case _:
                pass
        forbidden_domains = {'tempmail.com', '10minutemail.com', 'guerrillamail.com'}
        domain = email.split('@')[-1].lower()
        match domain:
            case domain if domain in forbidden_domains:
                raise ValueError('Использование временных email адресов запрещено')
            case _:
                pass
        match re.search(r'(.)\1{3,}', email):
            case None:
                pass
            case _:
                raise ValueError('Email содержит слишком много повторяющихся символов')
        return email
