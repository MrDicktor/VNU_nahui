import pytest
import json
from schedule_bot.parser import Parser
from tests.fixtures import fake_html_fixture, expected_data_fixture
from datetime import time


class TestParser:
    row = "ВОК Латинська мова (Пр) ст.викл. Шегедин Н.М. ауд. Н-210 Збірна група Англ-23, КНІТ-23, КНІТ-24, Нім-27, ПМ-25, Укр-23ОА"
    elimination_row = "Програмування та підтримка веб-застосувань (Л) ст. викл. Павленко Ю.С. ауд. С-508 Потік КНІТ-23, КНІТ-24 Ліквідація викладачу "
    def test_parser(self):
        parser = Parser()
        result = parser.parse(1,"08:30","09:50", self.row)

        assert result.lesson_number == 1
        assert result.start_time == time(8,30)
        assert result.end_time == time(9,50)
        assert result.subject.subject == "ВОК Латинська мова"
        assert result.subject.subject_type == "(Пр)"
        assert result.teacher == "Шегедин Н.М."
        assert result.room == "ауд. Н-210"
        assert result.groups == "Збірна група Англ-23, КНІТ-23, КНІТ-24, Нім-27, ПМ-25, Укр-23ОА"
        assert result.elimination is None

    def test_parser_elimination(self):
        parser = Parser()
        result = parser.parse(2, "10:10", "11:30", self.elimination_row)

        assert result.lesson_number == 2
        assert result.start_time == time(10,10)
        assert result.end_time == time(11,30)
        assert result.subject.subject == "Програмування та підтримка веб-застосувань"
        assert result.subject.subject_type == "(Л)"
        assert result.teacher == "Павленко Ю.С."
        assert result.room == "ауд. С-508"
        assert result.groups == "Потік КНІТ-23, КНІТ-24"
        assert result.elimination == "Ліквідація викладачу "


def test_get_lessons_data(mocker, fake_html_fixture, expected_data_fixture):
    fake_html = fake_html_fixture

    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.text = fake_html
    mocker.patch("schedule_bot.parser.requests.get", return_value=mock_response)

    parser = Parser()
    result = parser.get_lessons_data("КНІТ-24")
    result = result.model_dump(mode="json")

    expected_data = expected_data_fixture

    assert result == expected_data



