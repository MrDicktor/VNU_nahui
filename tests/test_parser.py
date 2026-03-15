import pytest
import json
from schedule_bot.parser import Parser
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



@pytest.fixture
def fake_html_fixture():
    fake_html = '''<!DOCTYPE html>
<html>
<head>
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta http-equiv="Content-Type" content="text/html; charset=windows-1251" />
    <title>ПС-Розклад v.4.0</title>
    <link rel="stylesheet" type="text/css" href="./../css/style3.css" />
</head>
<body>
    <div id="wrap">
        <div class="container-fluid">
            <div class="container">
                <div class="jumbotron pf16">
                    <div class="container">
                        <h4 class="hidden-xs">
                            Розклад групи <a href="./timetable.cgi?n=700&group=-4261">КНІТ-24</a> з 14.03.2026 по 21.03.2026
                        </h4>

                        <div class="row">
                            <div class="col-md-6 col-sm-6 col-xs-12 col-print-6">
                                <h4>16.03.2026 <small>Понеділок</small></h4>
                                <table class="table table-bordered table-striped">
                                    <tr>
                                        <td>2</td>
                                        <td>10:10<br>11:30</td>
                                        <td style="max-width: 340px;overflow: hidden;">
                                            Спеціалізовані мови програмування (Лаб)<br> 
                                            доц. Глинчук&nbsp;Л.Я. ауд. С-503<br> 
                                            (підгр. 1) <br>
                                        </td>
                                    </tr>
                                    <tr>
                                        <td>3</td>
                                        <td>11:50<br>13:10</td>
                                        <td style="max-width: 340px;overflow: hidden;">
                                            Спеціалізовані мови програмування (Л)<br> 
                                            доц. Глинчук&nbsp;Л.Я. ауд. С-519<br> 
                                            Потік КНІТ-23, КНІТ-24<br>
                                        </td>
                                    </tr>
                                    <tr>
                                        <td>5</td>
                                        <td>15:00<br>16:20</td>
                                        <td style="max-width: 340px;overflow: hidden;">
                                            ВОК Основи Web-дизайну (Пр)<br> 
                                            зав.каф.,доц. Авраменко&nbsp;Д.К. ауд. Н-59а<br> 
                                            Збірна група Англ-21, Англ-25, КБ-26, КНІТ-23, КНІТ-24, Лінгв-2.10, Матем-21, Нім-27, Укр-23ОА, Фран-29, Інф-25О<br>
                                        </td>
                                    </tr>
                                </table>
                            </div>

                            <div class="col-md-6 col-sm-6 col-xs-12 col-print-6">
                                <h4>17.03.2026 <small>Вівторок</small></h4>
                                <table class="table table-bordered table-striped">
                                    <tr>
                                        <td>1</td>
                                        <td>08:30<br>09:50</td>
                                        <td style="max-width: 340px;overflow: hidden;">
                                            Бази даних та розподілені інформаційно-аналітичні системи (Л)<br> 
                                            доц. Булатецька&nbsp;Л.В. ауд. С-508<br> 
                                            Потік КНІТ-23, КНІТ-24<br>
                                        </td>
                                    </tr>
                                </table>
                            </div>
                        </div>

                        <div class="row">
                            <div class="col-md-6 col-sm-6 col-xs-12 col-print-6">
                                <h4>19.03.2026 <small>Четвер</small></h4>
                                <table class="table table-bordered table-striped">
                                    <tr>
                                        <td>3</td>
                                        <td>11:50<br>13:10</td>
                                        <td style="max-width: 340px;overflow: hidden;">
                                            Програмування та підтримка веб-застосувань (Лаб)<br> 
                                            ст. викл. Павленко&nbsp;Ю.С. ауд. С-503<br> 
                                            (підгр. 1) <br> <br>
                                            Спеціалізовані мови програмування (Лаб)<br> 
                                            доц. Глинчук&nbsp;Л.Я. ауд. С-512<br> 
                                            (підгр. 2) <br>
                                        </td>
                                    </tr>
                                </table>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</body>
</html>'''
    return fake_html

@pytest.fixture
def expected_data_fixture():
    expected_data = '''{
    "day_1": {
        "today_date": "2026-03-16",
        "week_day": "Понеділок",
        "schedule": [
            {
                "lesson_number": 2,
                "start_time": "10:10:00",
                "end_time": "11:30:00",
                "subject": {
                    "subject": "Спеціалізовані мови програмування",
                    "subject_type": "(Лаб)"
                },
                "teacher": "Глинчук Л.Я.",
                "room": "ауд. С-503",
                "sub_group": "(підгр. 1)",
                "groups": null,
                "elimination": null
            },
            {
                "lesson_number": 3,
                "start_time": "11:50:00",
                "end_time": "13:10:00",
                "subject": {
                    "subject": "Спеціалізовані мови програмування",
                    "subject_type": "(Л)"
                },
                "teacher": "Глинчук Л.Я.",
                "room": "ауд. С-519",
                "sub_group": null,
                "groups": "Потік КНІТ-23, КНІТ-24 ",
                "elimination": null
            },
            {
                "lesson_number": 5,
                "start_time": "15:00:00",
                "end_time": "16:20:00",
                "subject": {
                    "subject": "ВОК Основи Web-дизайну",
                    "subject_type": "(Пр)"
                },
                "teacher": "Авраменко Д.К.",
                "room": "ауд. Н-59",
                "sub_group": null,
                "groups": "Збірна група Англ-21, Англ-25, КБ-26, КНІТ-23, КНІТ-24, Лінгв-2.10, Матем-21, Нім-27, Укр-23ОА, Фран-29, Інф-25О ",
                "elimination": null
            }
        ]
    },
    "day_2": {
        "today_date": "2026-03-17",
        "week_day": "Вівторок",
        "schedule": [
            {
                "lesson_number": 1,
                "start_time": "08:30:00",
                "end_time": "09:50:00",
                "subject": {
                    "subject": "Бази даних та розподілені інформаційно-аналітичні системи",
                    "subject_type": "(Л)"
                },
                "teacher": "Булатецька Л.В.",
                "room": "ауд. С-508",
                "sub_group": null,
                "groups": "Потік КНІТ-23, КНІТ-24 ",
                "elimination": null
            },
            {
                "lesson_number": 2,
                "start_time": "10:10:00",
                "end_time": "11:30:00",
                "subject": {
                    "subject": "Теорія ймовірностей та комп’ютерна статистика",
                    "subject_type": "(Пр)"
                },
                "teacher": "Антонюк О.П.",
                "room": "ауд. С-513",
                "sub_group": null,
                "groups": null,
                "elimination": null
            },
            {
                "lesson_number": 3,
                "start_time": "11:50:00",
                "end_time": "13:10:00",
                "subject": {
                    "subject": "Спеціалізовані мови програмування",
                    "subject_type": "(Лаб)"
                },
                "teacher": "Глинчук Л.Я.",
                "room": "ауд. С-504",
                "sub_group": "(підгр. 2)",
                "groups": null,
                "elimination": null
            },
            {
                "lesson_number": 5,
                "start_time": "15:00:00",
                "end_time": "16:20:00",
                "subject": {
                    "subject": "ВОК Латинська мова",
                    "subject_type": "(Пр)"
                },
                "teacher": "Шегедин Н.М.",
                "room": "ауд. Н-210",
                "sub_group": null,
                "groups": "Збірна група Англ-23, КНІТ-23, КНІТ-24, Нім-27, ПМ-25, Укр-23ОА, Фран-29, Іст-22О ",
                "elimination": null
            }
        ]
    },
    "day_3": {
        "today_date": "2026-03-18",
        "week_day": "Середа",
        "schedule": [
            {
                "lesson_number": 1,
                "start_time": "08:30:00",
                "end_time": "09:50:00",
                "subject": {
                    "subject": "Програмування та підтримка веб-застосувань",
                    "subject_type": "(Л)"
                },
                "teacher": "Павленко Ю.С.",
                "room": "ауд. С-508",
                "sub_group": null,
                "groups": "Потік КНІТ-23, КНІТ-24 ",
                "elimination": null
            },
            {
                "lesson_number": 2,
                "start_time": "10:10:00",
                "end_time": "11:30:00",
                "subject": {
                    "subject": "Бази даних та розподілені інформаційно-аналітичні системи",
                    "subject_type": "(Лаб)"
                },
                "teacher": "Булатецька Л.В.",
                "room": "ауд. С-502",
                "sub_group": "(підгр. 1)",
                "groups": null,
                "elimination": null
            },
            {
                "lesson_number": 3,
                "start_time": "11:50:00",
                "end_time": "13:10:00",
                "subject": {
                    "subject": "Бази даних та розподілені інформаційно-аналітичні системи",
                    "subject_type": "(Лаб)"
                },
                "teacher": "Булатецька Л.В.",
                "room": "ауд. С-502",
                "sub_group": "(підгр. 2)",
                "groups": null,
                "elimination": null
            },
            {
                "lesson_number": 4,
                "start_time": "13:25:00",
                "end_time": "14:45:00",
                "subject": {
                    "subject": "Програмування та підтримка веб-застосувань",
                    "subject_type": "(Лаб)"
                },
                "teacher": "Павленко Ю.С.",
                "room": "ауд. С-3",
                "sub_group": "(підгр. 2)",
                "groups": null,
                "elimination": null
            }
        ]
    },
    "day_4": {
        "today_date": "2026-03-19",
        "week_day": "Четвер",
        "schedule": [
            {
                "lesson_number": 1,
                "start_time": "08:30:00",
                "end_time": "09:50:00",
                "subject": {
                    "subject": "Іноземна мова (за професійним спрямуванням)",
                    "subject_type": "(Пр)"
                },
                "teacher": "Смаль О.В.",
                "room": "ауд. С-514",
                "sub_group": null,
                "groups": null,
                "elimination": null
            },
            {
                "lesson_number": 2,
                "start_time": "10:10:00",
                "end_time": "11:30:00",
                "subject": {
                    "subject": "Теорія ймовірностей та комп’ютерна статистика",
                    "subject_type": "(Л)"
                },
                "teacher": "Антонюк О.П.",
                "room": "ауд. С-518",
                "sub_group": null,
                "groups": "Потік КНІТ-23, КНІТ-24 ",
                "elimination": null
            },
            {
                "lesson_number": 3,
                "start_time": "11:50:00",
                "end_time": "13:10:00",
                "subject": {
                    "subject": "Програмування та підтримка веб-застосувань",
                    "subject_type": "(Лаб)"
                },
                "teacher": "Павленко Ю.С.",
                "room": "ауд. С-503",
                "sub_group": "(підгр. 1)",
                "groups": null,
                "elimination": null
            },
            {
                "lesson_number": 3,
                "start_time": "11:50:00",
                "end_time": "13:10:00",
                "subject": {
                    "subject": "  Спеціалізовані мови програмування",
                    "subject_type": "(Лаб)"
                },
                "teacher": "Глинчук Л.Я.",
                "room": "ауд. С-512",
                "sub_group": "(підгр. 2)",
                "groups": null,
                "elimination": null
            }
        ]
    },
    "day_5": {
        "today_date": "2026-03-20",
        "week_day": "П'ятниця",
        "schedule": [
            {
                "lesson_number": 1,
                "start_time": "08:30:00",
                "end_time": "09:50:00",
                "subject": {
                    "subject": "ВОК Розробка вебдодатків на Python",
                    "subject_type": "(Лаб)"
                },
                "teacher": "Булатецька Л.В.",
                "room": "ауд. С-502",
                "sub_group": null,
                "groups": "Збірна група КНІТ-24, КФ-22 ",
                "elimination": null
            },
            {
                "lesson_number": 2,
                "start_time": "10:10:00",
                "end_time": "11:30:00",
                "subject": {
                    "subject": "ВОК Основи 3D графіки/моделювання",
                    "subject_type": "(Лаб)"
                },
                "teacher": "Глинчук Л.Я.",
                "room": "ауд. С-503",
                "sub_group": null,
                "groups": "Збірна група КНІТ-24 ",
                "elimination": null
            },
            {
                "lesson_number": 3,
                "start_time": "11:50:00",
                "end_time": "13:10:00",
                "subject": {
                    "subject": "ВОК Практикум з граматики німецької мови: рівень В1-В2",
                    "subject_type": "(Пр)"
                },
                "teacher": "Пасик Л.А.",
                "room": "ауд. А-231",
                "sub_group": null,
                "groups": "Збірна група Англ-21, Англ-25, КНІТ-24, Нім-27, Укр-22ОА ",
                "elimination": null
            },
            {
                "lesson_number": 3,
                "start_time": "11:50:00",
                "end_time": "13:10:00",
                "subject": {
                    "subject": "ВОК Основи кібербезпеки",
                    "subject_type": "(Лаб)"
                },
                "teacher": "Глинчук Л.Я.",
                "room": "ауд. С-503",
                "sub_group": null,
                "groups": "Збірна група КБ-26, КНІТ-23, КНІТ-24, Матем-21, Політ-23, Інф-25О, Іст-22О ",
                "elimination": null
            }
        ]
    },
    "day_6": null
}'''
    return json.loads(expected_data)

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



