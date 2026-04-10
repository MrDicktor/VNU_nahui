import pytest
from schedule_bot.repositories.room_repo import RoomRepo

@pytest.mark.asyncio
async def test_create_group(db_session):
    repo = RoomRepo(db_session)
    test_name = "C-505"

    new_room = await repo.create_room(room=test_name)

    assert new_room.id is not None
    assert new_room.name == test_name
    assert new_room.uuid is not None