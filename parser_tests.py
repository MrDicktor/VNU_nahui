import pytest
import json
from pars import Parser
from datetime import time



@pytest.mark.parametrize('lesson_number, start_time, end_time, row, exp_number ,exp_start, exp_end,exp_subject,exp_subject_type,exp_teacher,exp_room,exp_groups,exp_elimination',
    [
     (1,"08:30", "09:50",
     "ВОК Латинська мова (Пр) ст.викл. Шегедин Н.М. ауд. Н-210 Збірна група Англ-23, КНІТ-23, КНІТ-24, Нім-27, ПМ-25, Укр-23ОА",

     1, time(8,30), time(9,50),
     "ВОК Латинська мова",
     "(Пр)",
     "Шегедин Н.М.",
     "ауд. Н-210",
     "Збірна група Англ-23, КНІТ-23, КНІТ-24, Нім-27, ПМ-25, Укр-23ОА",
     None
     ),


     (2, "10:10", "11:30",
     "Програмування та підтримка веб-застосувань (Л) ст. викл. Павленко Ю.С. ауд. С-508 Потік КНІТ-23, КНІТ-24",

     2, time(10,10), time(11,30),
     "Програмування та підтримка веб-застосувань",
     "(Л)",
     "Павленко Ю.С.",
     "ауд. С-508",
     "Потік КНІТ-23, КНІТ-24",
      None
     )
    ]
                         )
def test_parser(lesson_number, start_time, end_time, row, exp_number, exp_start, exp_end, exp_subject,exp_subject_type,exp_teacher,exp_room,exp_groups,exp_elimination):
    parser = Parser()
    result = parser.parse(lesson_number, start_time, end_time, row)

    assert result.lesson_number == exp_number
    assert result.start_time == exp_start
    assert result.end_time == exp_end
    assert result.subject.subject ==  exp_subject
    assert result.subject.subject_type == exp_subject_type
    assert result.teacher == exp_teacher
    assert result.room == exp_room
    assert result.groups == exp_groups
    assert result.elimination == exp_elimination


def test_get_lessons_data(mocker):
    with open("test_knit24.html", "r", encoding="cp1251") as f:
        fake_html = f.read()

    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.text = fake_html
    mocker.patch("pars.requests.get", return_value=mock_response)

    parser = Parser()
    result = parser.get_lessons_data("КНІТ-24")
    result = result.model_dump(mode="json")

    with open("expected_data.json", "r", encoding="utf-8") as f:
        expected_data = json.load(f)

    assert result == expected_data



