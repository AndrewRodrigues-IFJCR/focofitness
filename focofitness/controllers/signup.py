from fastapi import Depends, FastAPI, Request
from fastapi.responses import RedirectResponse

from ..models import Account, get_async_session_maker
from ..schemas import AccountRequest


def subscribe_controller(app: FastAPI):
    @app.get('/signup')
    async def _(request: Request):
        return RedirectResponse('/views/signup')

    @app.post('/signup')
    async def _(
        account_req: AccountRequest,
        async_session_maker=Depends(get_async_session_maker),
    ):
        with async_session_maker() as session:
            session.add(
                account := Account(
                    email=account_req.email, password_hash=account_req.password
                )
            )
            await session.commit()
            await session.refresh(account)

        return account
