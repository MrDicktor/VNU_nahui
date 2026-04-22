import datetime

import pytest

from schedule_bot.exceptions import GroupNotFoundException
from schedule_bot.parser import Parser
from tests.parser.fixtures import fake_html_fixture, expected_data_fixture, fake_html_error_fixture, fake_html_five_days, expected_data_five_days_fixture
from datetime import time


class TestParser:
    row = "ВОК Латинська мова (Пр) Шегедин Наталія Миколаївна ауд. Н-210 Збірна група Англ-23, КНІТ-23, КНІТ-24, Нім-27, ПМ-25, Укр-23ОА"
    no_teacher_row = "Програмування та підтримка веб-застосувань (Л)   ауд. С-508 Потік КНІТ-23, КНІТ-24 Ліквідація викладачу "
    @pytest.mark.asyncio
    async def test_parser(self):
        parser = Parser()
        result = await parser.parse('13.04.2026', "Понеділок",1,"08:30","09:50", self.row)

        assert result.today_date == datetime.date(2026, 4, 13)
        assert result.week_day == "Понеділок"
        assert result.lesson_number == 1
        assert result.start_time == time(8,30)
        assert result.end_time == time(9,50)
        assert result.subject.subject == "ВОК Латинська мова"
        assert result.subject.subject_type == "(Пр)"
        assert result.teacher == "Шегедин Наталія Миколаївна"
        assert result.room == "ауд. Н-210"
        assert result.groups == "Збірна група Англ-23, КНІТ-23, КНІТ-24, Нім-27, ПМ-25, Укр-23ОА"
        assert result.elimination is None

    @pytest.mark.asyncio
    async def test_parser_no_teacher(self):
        parser = Parser()
        result = await parser.parse('13.04.2026', "Вівторок",2, "10:10", "11:30", self.no_teacher_row)

        assert result.today_date == datetime.date(2026, 4, 13)
        assert result.week_day == "Вівторок"
        assert result.lesson_number == 2
        assert result.start_time == time(10,10)
        assert result.end_time == time(11,30)
        assert result.subject.subject == "Програмування та підтримка веб-застосувань"
        assert result.subject.subject_type == "(Л)"
        assert result.teacher == "Не вказано"
        assert result.room == "ауд. С-508"
        assert result.groups == "Потік КНІТ-23, КНІТ-24"
        assert result.elimination == "Ліквідація викладачу "

@pytest.mark.asyncio
async def test_get_lessons_data(mocker, fake_html_fixture, expected_data_fixture):
    fake_html = fake_html_fixture

    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.text = fake_html
    mocker.patch("schedule_bot.parser.requests.post", return_value=mock_response)


    parser = Parser()
    result = await parser.get_lessons_data("КНІТ-24")
    result = result.model_dump(mode="json")

    expected_data = expected_data_fixture

    assert result == expected_data


@pytest.mark.asyncio
async def test_get_lessons_data_error(mocker, fake_html_error_fixture):
        fake_html = fake_html_error_fixture

        mock_response = mocker.Mock()
        mock_response.status_code = 200
        mock_response.text = fake_html
        mocker.patch("schedule_bot.parser.requests.get", return_value=mock_response)

        parser = Parser()
        with pytest.raises(GroupNotFoundException):
            result = await parser.get_lessons_data("erere")

@pytest.mark.asyncio
async def test_get_lessons_data_five_days(mocker, fake_html_five_days, expected_data_five_days_fixture):
    fake_html = fake_html_five_days

    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.text = fake_html
    mocker.patch("schedule_bot.parser.requests.post", return_value=mock_response)

    parser = Parser()
    result = await parser.get_lessons_data("КНІТ-24")
    result = result.model_dump(mode="json")

    expected_data = expected_data_five_days_fixture

    assert result == expected_data




