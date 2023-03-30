import pytest
from datetime import datetime

from backend.api.models.account import Account
from db import get_db


def test_account():
    values = [1, 'johndoe', 'johndoe@example.com', '127.0.0.1', '2022-03-30 14:30:00']
    values = [2, 'HomerSimpsons', 'homersimpson@example.com', '127.0.0.1', datetime.now()]
    account = Account(values)

    assert account.id == 1
    assert account.username == 'johndoe'
    assert account.email == 'johndoe@example.com'
    assert account.ip_address == '127.0.0.1'
    assert account.created_at == '2022-03-30 14:30:00'

