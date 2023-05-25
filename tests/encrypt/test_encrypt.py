from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    with pytest.raises(TypeError):
        encrypt_message(
            '1', 'message') or encrypt_message(
                1, 1) or encrypt_message(1, 'message')

    assert encrypt_message('message', -1) == 'egassem'
    assert encrypt_message('message', 1) == 'm_egasse'
    assert encrypt_message('message', 2) == 'egass_em'
