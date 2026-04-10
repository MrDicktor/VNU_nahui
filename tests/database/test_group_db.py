import pytest
from schedule_bot.repositories.group_repo import GroupRepo

@pytest.mark.asyncio
async def test_create_group(db_session):
    repo = GroupRepo(db_session)
    test_name = "КНІТ-24"

    new_group = await repo.create_group(group=test_name)

    assert new_group.id is not None
    assert new_group.name == test_name
    assert new_group.uuid is not None