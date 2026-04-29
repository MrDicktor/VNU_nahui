import pytest
import json


@pytest.fixture
def fake_html_fixture():
    fake_html = """<!DOCTYPE html><html><head><meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1" /><meta name="viewport" content="width=device-width, initial-scale=1.0" /><meta name="keywords" content="" /><meta name="author" content="ПП Політек-Софт" /><meta name="description" content="ПС-Розклад v.4.0" /><meta http-equiv="Content-Type" content="text/html; charset=windows-1251" /><title>ПС-Розклад v.4.0</title>
<link rel="stylesheet" type="text/css" href="./../css/style3.css" /><script type="text/javascript" src="./../js/jquery.min.js"></script><script type="text/javascript" src="./../js/jquery.maskedinput-1.4.1.min.js"></script><script type="text/javascript" src="./../js/bootstrap.min.3.js"></script><script type="text/javascript" src="./../js/rwd-table.min.js" ></script><script type="text/javascript" src="./../js/datepicker.js" ></script><script type="text/javascript" src="./../js/jquery.autocomplete.min.js" ></script><script type="text/javascript" src="./../js/js.js" ></script><script type="text/javascript" src="./../js/date.js" ></script><script type="text/javascript" src="./../js/select2.min.js" ></script><script type="text/javascript" src="./../js/summernote.min.js" ></script><script type="text/javascript" src="./../js/locales/summernote-uk-UA.min.js" ></script><script type="text/javascript"> var url = "./srequest.cgi"; </script><style type="text/css">@media print { .hidden-print { display: none !important; } a[href]:after {content: " ";}  body { padding-top: 0;} .col-print-6 { width: 50%; float: left; page-break-inside: avoid; }}</style></head><body><!-- PathDBTimeTable --><div id="wrap"><div class="container-fluid"><div class="container"><div class="jumbotron pf16"><style>.remote_work{font-weight: bold;}</style><div class="hidden-print"><h3 class="text-center">Розклад занять</h3><h4 class="text-center">Волинський національний університет імені Лесі Українки</h4><div class="page-header" style="overflow: hidden;"> <form  enctype="application/x-www-form-urlencoded" name="setVedP" id="setVedP" method="post" action="./timetable.cgi?n=700"><div class="form-group "><select name="faculty" id="faculty" class="form-control" onchange="sel_val()"><option value="0">Оберіть факультет</option><option value="1019">Факультет інформаційних технологій і математики</option><option value="1021">Навчально-науковий інститут хімії та екології</option><option value="1022">Факультет біології та лісового господарства</option><option value="1023">Географічний факультет</option><option value="1024">Юридичний факультет</option><option value="1025">Факультет історії, політології та національної безпеки</option><option value="1026">Факультет психології</option><option value="1028">Факультет економіки та управління</option><option value="1029">Факультет міжнародних відносин</option><option value="1030">Факультет філології та журналістики</option><option value="1031">Факультет іноземної філології</option><option value="1033">Факультет культури і мистецтв</option><option value="1034">Факультет педагогічної освіти та соціальної роботи</option><option value="1035">Факультет фізичної культури, спорту та здоров`я</option><option value="1040">Медичний факультет</option><option value="1041">Навчально-науковий фізико-технологічний інститут</option><option value="1042">Навчально-науковий інститут неперервної освіти</option></select></div><div class="row"><div class="col-sm-4 col-xs-12"><input type="text" name="teacher" id="teacher" value="" class="form-control" placeholder="ПІБ викладача" /></div><div class="col-sm-4 col-xs-12"><div class="form-group"><select name="course" id="course" class="form-control"><option value="0">Оберіть курс</option><option value="1" >1</option><option value="2" >2</option><option value="3" >3</option><option value="4" >4</option><option value="5" >5</option><option value="6" >6</option></select></div></div><div class="col-sm-4 col-xs-12"><div class="form-group"><input type="text"  name="group" id="group" value="КНІТ-24" placeholder="Назва групи" class="form-control" /></div></div></div><div class="row" style="margin-top:15px;"><div class="col-md-3"><div class="form-group"><div class="input-group"><span class="input-group-addon">з дати:</span><input type="text" name="sdate" id="sdate" value="" class="form-control input-sm datepicker" placeholder="дд.мм.рррр" maxlength="10" /></div></div></div><div class="col-md-3"><div class="form-group"><div class="input-group"><span class="input-group-addon">до дати:</span><input type="text" name="edate" id="edate" value="" class="form-control input-sm datepicker" placeholder="дд.мм.рррр" maxlength="10" /></div></div></div><div class="col-md-6 col-xs-12" style="text-align:right;"><button type="submit" class="btn btn-success">Показати розклад занять</button></div></div><input type="hidden" name="n" value="700" /></form></div></div><script type="text/javascript">document.getElementById('sdate').addEventListener('input', function(event) { var input = event.target; input.value = input.value.replace(/[^0-9.]/g, ''); }); document.getElementById('edate').addEventListener('input', function(event) { var input = event.target; input.value = input.value.replace(/[^0-9.]/g, ''); }); function validateDateInput(inputElement) { var dateInput = inputElement.value; var datePattern = /^(0[1-9]|[12][0-9]|3[01])\.(0[1-9]|1[0-2])\.(\d{4})$/; var formGroup = inputElement.closest('.form-group');     if (dateInput.trim() === '') {         formGroup.classList.remove('has-error', 'has-success');         return true;     } if (!datePattern.test(dateInput)) { formGroup.classList.add('has-error'); formGroup.classList.remove('has-success'); return false; } else { formGroup.classList.remove('has-error'); formGroup.classList.add('has-success'); return true; } } document.getElementById('setVedP').addEventListener('submit', function(event) { var isSdateValid = validateDateInput(document.getElementById('sdate')); var isEdateValid = validateDateInput(document.getElementById('edate')); if (!isSdateValid || !isEdateValid) { event.preventDefault(); alert('Введіть дату у форматі дд.мм.рррр'); } }); el = ''; var opt = 0; function sel_val(){opt = $('#faculty').val();/*alert(opt);*/}function addWin(num_t, id){$("#ldata").empty();$("#ldata").html("Завантаження даних! Чекайте...");el = id;$.post("./timetable.cgi",{n:"701", lev:num_t, txt:$("#"+id).val(),},AfterGetDate);}function AfterGetDate (data){ $("#ldata").empty();  $("#ldata").append(data);}$("#b14").on('click', function(ev) { addWin(141, 'teacher');$('#ModalLabel').text('Викладачі');});$("#b15").on('click', function(ev) { addWin(142, 'group');$('#ModalLabel').text('Перелік академічних груп');});$('#group').autocomplete({minChars: 2, maxHeight: 400, width: 400,zIndex: 9998, deferRequestBy: 50, params: {faculty: function(){return $('#faculty').val();},course: function(){return $('#course').val();}},serviceUrl: './timetable.cgi?n=701&lev=142', onSelect: function(data, value){ }, });$('#teacher').autocomplete({minChars: 3, maxHeight: 400, width: 400,zIndex: 9999, deferRequestBy: 50, params: {faculty: function(){return $('#faculty').val();}}, serviceUrl: './timetable.cgi?n=701&lev=141', onSelect: function(data, value){ }, });</script><div id="AddModal" class="modal fade" tabindex="-1" role="dialog" aria-labelledby="ModalLabel" aria-hidden="true"><div class="modal-dialog"><div class="modal-content"><div class="modal-header"><button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button><h4 class="modal-title" id="ModalLabel"></h4></div><div class="modal-body"><div id="ldata" style="max-height: 300px;overflow: hidden;overflow-y: scroll;padding-left: 30px;"></div></div><div class="modal-footer"><button class="btn btn-primary" id="setval">Призначити</button><button class="btn" data-dismiss="modal" aria-hidden="true">Закрити</button></div></div></div></div><script type="text/javascript">var ansver = 'Оберіть запис у таблиці!';var txt = '';$('input[name=optionsRadios]:checked').on("click", function(){txt = $('input[name=optionsRadios]:checked').val();});$("#setval").on("click", function(ev) {if ($('input[name=optionsRadios]:checked').val() != null) {txt = $('input[name=optionsRadios]:checked').val();$('#' + el) .val(txt);$('#AddModal').modal('hide')}else{alert(ansver);}});</script><div class="container"><h4 class="hidden-xs">Розклад групи <a title="Постійне посилання на тижневий розклад" style="font-size: 28px;" href="./timetable.cgi?n=700&group=-4261">КНІТ-24</a> з 16.04.2026 по 23.04.2026</h4><h4 class="visible-xs text-center">Розклад групи<br> <a title="Постійне посилання на тижневий розклад" style="font-size: 1.4em;" href="./timetable.cgi?n=700&group=-4261">КНІТ-24</a><br> з 16.04.2026 по 23.04.2026</h4><div class="row"><div class="col-md-6 col-sm-6 col-xs-12 col-print-6"><h4>16.04.2026 <small>Четвер</small></h4><table class="table  table-bordered table-striped"><tr><td>1</td><td>08:30<br>09:50</td><td style="max-width: 340px;overflow: hidden;">Іноземна мова (за професійним (Пр)<br> доц. Смаль О.В. ауд. С-508<br>  </td></tr></div><div class="row"><tr><td>2</td><td>10:10<br>11:30</td><td style="max-width: 340px;overflow: hidden;">Теорія ймовірностей та комп’юте (Л)<br> ст. викл. Антонюк О.П. ауд. С-518<br> Потік КНІТ-23, КНІТ-24<br> </td></tr></div><div class="row"><tr><td>3</td><td>11:50<br>13:10</td><td style="max-width: 340px;overflow: hidden;">Програмування та підтримка веб- (Лаб)<br> ст. викл. Павленко Ю.С. ауд. С-503<br>  (підгр. 1) <br> <br>Спеціалізовані мови програмуван (Лаб)<br> доц. Глинчук Л.Я. ауд. С-512<br>  (підгр. 2) <br> </td></tr></div><div class="row"><tr><td>4</td><td>13:25<br>14:45</td><td style="max-width: 340px;overflow: hidden;"> </td></tr></div><div class="row"><tr><td>5</td><td>15:00<br>16:20</td><td style="max-width: 340px;overflow: hidden;"> </td></tr></div><div class="row"><tr><td>6</td><td>16:35<br>17:55</td><td style="max-width: 340px;overflow: hidden;">ВОК Аудіо практикум з англійськ (Пр)<br> доц. Бондар (п) Т.Г. ауд. А-420<br> Збірна група КНІТ-24, Лінгв-2.10, Лінгв-2.11, Лінгв-2.12, Нім-27, Нім-28О, Фран-29<br> </td></tr></div><div class="row"><tr><td>7</td><td>18:10<br>19:30</td><td style="max-width: 340px;overflow: hidden;"> </td></tr></table></div><div class="col-md-6 col-sm-6 col-xs-12 col-print-6"><h4>17.04.2026 <small>П'ятниця</small></h4><table class="table  table-bordered table-striped"><tr><td>1</td><td>08:30<br>09:50</td><td style="max-width: 340px;overflow: hidden;">Увага! Заняття відмінено! ВОК Розробка вебдодатків на Pyt (Лаб)<br> доц. Булатецька Л.В. ауд. С-502<br> Збірна група КНІТ-24, КФ-22<br> </td></tr><tr><td>2</td><td>10:10<br>11:30</td><td style="max-width: 340px;overflow: hidden;">ВОК Основи геймдизайну (Пр)<br> зав.каф.,доц. Авраменко Д.К. ауд. Н-71<br> Збірна група ДизО-26, КНІТ-23, КНІТ-24, Лінгв-2.12, Мист-22, Пс-21, Фран-29, ФіК-23, Інф-25О<br> <br>ВОК Креативний маркетинг (Л)<br> доц. Милько І.П. ауд. G-302<br> Збірна група ДизО-26, Журн-27, КНІТ-23, КНІТ-24, Логіст2.14, Маркет2.11, Маркет2.12, МВ-23англ, Мен-27, Мит-25, МіБ-21анг, Пс-23, Рекл-28<br> </td></tr><tr><td>3</td><td>11:50<br>13:10</td><td style="max-width: 340px;overflow: hidden;">ВОК Практикум з граматики німец (Пр)<br> зав.каф.,доц. Пасик Л.А. ауд. А-231<br> Збірна група Англ-21, Англ-25, КНІТ-24, Нім-27, Укр-22ОА<br> <br>ВОК Основи кібербезпеки (Лаб)<br> доц. Глинчук Л.Я. ауд. С-503<br> Збірна група КБ-26, КНІТ-23, КНІТ-24, Матем-21, Політ-23, Інф-25О, Іст-22О<br> <br>ВОК Креативний маркетинг (Пр)<br> доц. Милько І.П. ауд. G-407<br> Збірна група ДизО-26, Журн-27, КНІТ-23, КНІТ-24, Маркет2.11, МВ-23англ, Мен-27, Мит-25, МіБ-21анг, Пс-23, Рекл-28<br> </td></tr><tr><td>4</td><td>13:25<br>14:45</td><td style="max-width: 340px;overflow: hidden;">ВОК Основи кібербезпеки (Лаб)<br> доц. Глинчук Л.Я. ауд. С-503<br> Збірна група КБ-26, КНІТ-23, КНІТ-24, Матем-21, Політ-23, Інф-25О, Іст-22О<br> <br>ВОК Фінансова гра-тренінг «Житт (Пр)<br> доц. Теслюк С.А. ауд. G-408<br> Збірна група КНІТ-24, КІТР-24, Лінгв-2.10, Мит-25, Іст-22О<br> </td></tr><tr><td>5</td><td>15:00<br>16:20</td><td style="max-width: 340px;overflow: hidden;"> </td></tr><tr><td>6</td><td>16:35<br>17:55</td><td style="max-width: 340px;overflow: hidden;"> </td></tr><tr><td>7</td><td>18:10<br>19:30</td><td style="max-width: 340px;overflow: hidden;"> </td></tr></table></div></div><div class="row"><div class="col-md-6 col-sm-6 col-xs-12 col-print-6"><h4>20.04.2026 <small>Понеділок</small></h4><table class="table  table-bordered table-striped"><tr><td>1</td><td>08:30<br>09:50</td><td style="max-width: 340px;overflow: hidden;"> </td></tr></div><div class="row"><tr><td>2</td><td>10:10<br>11:30</td><td style="max-width: 340px;overflow: hidden;">Спеціалізовані мови програмуван (Лаб)<br> доц. Глинчук Л.Я. ауд. С-503<br>  (підгр. 1) <br> <br>Програмування та підтримка веб- (Лаб)<br> ст. викл. Павленко Ю.С. ауд. С-502<br>  (підгр. 2) <br> </td></tr></div><div class="row"><tr><td>3</td><td>11:50<br>13:10</td><td style="max-width: 340px;overflow: hidden;">Спеціалізовані мови програмуван (Л)<br> доц. Глинчук Л.Я. ауд. С-519<br> Потік КНІТ-23, КНІТ-24<br> </td></tr></div><div class="row"><tr><td>4</td><td>13:25<br>14:45</td><td style="max-width: 340px;overflow: hidden;"> </td></tr></div><div class="row"><tr><td>5</td><td>15:00<br>16:20</td><td style="max-width: 340px;overflow: hidden;">ВОК Креативний маркетинг (Пр)<br> доц. Милько І.П. ауд. G-410<br> Збірна група ДизО-26, Журн-27, КНІТ-23, КНІТ-24, Маркет2.11, МВ-23англ, Мен-27, Мит-25, МіБ-21анг, Пс-23, Рекл-28<br> </td></tr></div><div class="row"><tr><td>6</td><td>16:35<br>17:55</td><td style="max-width: 340px;overflow: hidden;"> </td></tr></div><div class="row"><tr><td>7</td><td>18:10<br>19:30</td><td style="max-width: 340px;overflow: hidden;"> </td></tr></table></div><div class="col-md-6 col-sm-6 col-xs-12 col-print-6"><h4>21.04.2026 <small>Вівторок</small></h4><table class="table  table-bordered table-striped"><tr><td>1</td><td>08:30<br>09:50</td><td style="max-width: 340px;overflow: hidden;">Бази даних та розподілені інфор (Лаб)<br> доц. Булатецька Л.В. ауд. С-502<br>  (підгр. 2) <br> </td></tr><tr><td>2</td><td>10:10<br>11:30</td><td style="max-width: 340px;overflow: hidden;">Теорія ймовірностей та комп’юте (Пр)<br> ст. викл. Антонюк О.П. ауд. С-513<br>  </td></tr><tr><td>3</td><td>11:50<br>13:10</td><td style="max-width: 340px;overflow: hidden;">Спеціалізовані мови програмуван (Лаб)<br> доц. Глинчук Л.Я. ауд. С-504<br>  (підгр. 2) <br> </td></tr><tr><td>4</td><td>13:25<br>14:45</td><td style="max-width: 340px;overflow: hidden;">Спеціалізовані мови програмуван (Лаб)<br> доц. Глинчук Л.Я. ауд. С-520<br>  (підгр. 1) <br> <br>Програмування та підтримка веб- (Лаб)<br> ст. викл. Павленко Ю.С. ауд. С-502<br>  (підгр. 2) <br> </td></tr><tr><td>5</td><td>15:00<br>16:20</td><td style="max-width: 340px;overflow: hidden;">ВОК Латинська мова (Пр)<br> ст.викл. Шегедин Н.М. ауд. Н-210<br> Збірна група Англ-23, КНІТ-23, КНІТ-24, Нім-27, ПМ-25, Укр-23ОА, Фран-29, Іст-22О<br> <br>ВОК Основи Web-дизайну (Пр)<br> зав.каф.,доц. Авраменко Д.К. ауд. Н-71<br> Збірна група Англ-21, Англ-25, КБ-26, КНІТ-23, КНІТ-24, Лінгв-2.10, Матем-21, Нім-27, Укр-23ОА, Фран-29, Інф-25О<br> </td></tr><tr><td>6</td><td>16:35<br>17:55</td><td style="max-width: 340px;overflow: hidden;"> </td></tr><tr><td>7</td><td>18:10<br>19:30</td><td style="max-width: 340px;overflow: hidden;"> </td></tr></table></div></div><div class="row"><div class="col-md-6 col-sm-6 col-xs-12 col-print-6"><h4>22.04.2026 <small>Середа</small></h4><table class="table  table-bordered table-striped"><tr><td>1</td><td>08:30<br>09:50</td><td style="max-width: 340px;overflow: hidden;">Програмування та підтримка веб- (Л)<br> ст. викл. Павленко Ю.С. ауд. С-508<br> Потік КНІТ-23, КНІТ-24<br> </td></tr></div><div class="row"><tr><td>2</td><td>10:10<br>11:30</td><td style="max-width: 340px;overflow: hidden;">Бази даних та розподілені інфор (Лаб)<br> доц. Булатецька Л.В. ауд. С-502<br>  (підгр. 1) <br> </td></tr></div><div class="row"><tr><td>3</td><td>11:50<br>13:10</td><td style="max-width: 340px;overflow: hidden;">Бази даних та розподілені інфор (Лаб)<br> доц. Булатецька Л.В. ауд. С-502<br>  (підгр. 2) <br> </td></tr></div><div class="row"><tr><td>4</td><td>13:25<br>14:45</td><td style="max-width: 340px;overflow: hidden;">Програмування та підтримка веб- (Лаб)<br> ст. викл. Павленко Ю.С. ауд. С-503<br>  (підгр. 1) <br> </td></tr></div><div class="row"><tr><td>5</td><td>15:00<br>16:20</td><td style="max-width: 340px;overflow: hidden;">Практика</td></tr></div><div class="row"><tr><td>6</td><td>16:35<br>17:55</td><td style="max-width: 340px;overflow: hidden;">Практика</td></tr></div><div class="row"><tr><td>7</td><td>18:10<br>19:30</td><td style="max-width: 340px;overflow: hidden;">Практика</td></tr></table></div><div class="col-md-6 col-sm-6 col-xs-12 col-print-6"><h4>23.04.2026 <small>Четвер</small></h4><table class="table  table-bordered table-striped"><tr><td>1</td><td>08:30<br>09:50</td><td style="max-width: 340px;overflow: hidden;">Іноземна мова (за професійним (Пр)<br> доц. Смаль О.В. ауд. С-525<br>  </td></tr><tr><td>2</td><td>10:10<br>11:30</td><td style="max-width: 340px;overflow: hidden;">Теорія ймовірностей та комп’юте (Л)<br> ст. викл. Антонюк О.П. ауд. С-518<br> Потік КНІТ-23, КНІТ-24<br> </td></tr><tr><td>3</td><td>11:50<br>13:10</td><td style="max-width: 340px;overflow: hidden;">Програмування та підтримка веб- (Лаб)<br> ст. викл. Павленко Ю.С. ауд. С-503<br>  (підгр. 1) <br> </td></tr><tr><td>4</td><td>13:25<br>14:45</td><td style="max-width: 340px;overflow: hidden;"> </td></tr><tr><td>5</td><td>15:00<br>16:20</td><td style="max-width: 340px;overflow: hidden;"> </td></tr><tr><td>6</td><td>16:35<br>17:55</td><td style="max-width: 340px;overflow: hidden;">ВОК Аудіо практикум з англійськ (Пр)<br> доц. Бондар (п) Т.Г. ауд. А-420<br> Збірна група КНІТ-24, Лінгв-2.10, Лінгв-2.11, Лінгв-2.12, Нім-27, Нім-28О, Фран-29<br> </td></tr><tr><td>7</td><td>18:10<br>19:30</td><td style="max-width: 340px;overflow: hidden;"> </td></tr></table></div></div></div></div></div></div></div><div id="footer"><div class="container"><p class="text-muted credit">© ПП <a href="http://politek-soft.kiev.ua" target="_blank">Політек-софт</a></p></div></div><script type="text/javascript">$('.datepicker').datepicker({weekStart: 1,todayBtn: "linked",autoclose: true,orientation: "top right",todayHighlight: true,format: "dd.mm.yyyy",});</script></body></html>"""
    return fake_html


@pytest.fixture
def expected_data_fixture():
    expected_data = """{
    "day_1": [
        {
            "today_date": "2026-04-16",
            "week_day": "Четвер",
            "lesson_number": 1,
            "start_time": "08:30:00",
            "end_time": "09:50:00",
            "subject": {
                "subject": "Іноземна мова (за професійним",
                "subject_type": "(Пр)"
            },
            "teacher": "доц. Смаль О.В.",
            "room": "ауд. С-508",
            "sub_group": null,
            "groups": null,
            "elimination": null
        },
        {
            "today_date": "2026-04-16",
            "week_day": "Четвер",
            "lesson_number": 2,
            "start_time": "10:10:00",
            "end_time": "11:30:00",
            "subject": {
                "subject": "Теорія ймовірностей та комп’юте",
                "subject_type": "(Л)"
            },
            "teacher": "ст. викл. Антонюк О.П.",
            "room": "ауд. С-518",
            "sub_group": null,
            "groups": "Потік КНІТ-23, КНІТ-24 ",
            "elimination": null
        },
        {
            "today_date": "2026-04-16",
            "week_day": "Четвер",
            "lesson_number": 3,
            "start_time": "11:50:00",
            "end_time": "13:10:00",
            "subject": {
                "subject": "Програмування та підтримка веб-",
                "subject_type": "(Лаб)"
            },
            "teacher": "ст. викл. Павленко Ю.С.",
            "room": "ауд. С-503",
            "sub_group": "(підгр. 1)",
            "groups": null,
            "elimination": null
        },
        {
            "today_date": "2026-04-16",
            "week_day": "Четвер",
            "lesson_number": 3,
            "start_time": "11:50:00",
            "end_time": "13:10:00",
            "subject": {
                "subject": "Спеціалізовані мови програмуван",
                "subject_type": "(Лаб)"
            },
            "teacher": "доц. Глинчук Л.Я.",
            "room": "ауд. С-512",
            "sub_group": "(підгр. 2)",
            "groups": null,
            "elimination": null
        },
        {
            "today_date": "2026-04-16",
            "week_day": "Четвер",
            "lesson_number": 6,
            "start_time": "16:35:00",
            "end_time": "17:55:00",
            "subject": {
                "subject": "ВОК Аудіо практикум з англійськ",
                "subject_type": "(Пр)"
            },
            "teacher": "доц. Бондар (п) Т.Г.",
            "room": "ауд. А-420",
            "sub_group": null,
            "groups": "Збірна група КНІТ-24, Лінгв-2.10, Лінгв-2.11, Лінгв-2.12, Нім-27, Нім-28О, Фран-29 ",
            "elimination": null
        }
    ],
    "day_2": [
        {
            "today_date": "2026-04-17",
            "week_day": "П'ятниця",
            "lesson_number": 1,
            "start_time": "08:30:00",
            "end_time": "09:50:00",
            "subject": {
                "subject": "Увага! Заняття відмінено! ВОК Розробка вебдодатків на Pyt",
                "subject_type": "(Лаб)"
            },
            "teacher": "доц. Булатецька Л.В.",
            "room": "ауд. С-502",
            "sub_group": null,
            "groups": "Збірна група КНІТ-24, КФ-22 ",
            "elimination": null
        },
        {
            "today_date": "2026-04-17",
            "week_day": "П'ятниця",
            "lesson_number": 2,
            "start_time": "10:10:00",
            "end_time": "11:30:00",
            "subject": {
                "subject": "ВОК Основи геймдизайну",
                "subject_type": "(Пр)"
            },
            "teacher": "зав.каф.,доц. Авраменко Д.К.",
            "room": "ауд. Н-71",
            "sub_group": null,
            "groups": "Збірна група ДизО-26, КНІТ-23, КНІТ-24, Лінгв-2.12, Мист-22, Пс-21, Фран-29, ФіК-23, Інф-25О ",
            "elimination": null
        },
        {
            "today_date": "2026-04-17",
            "week_day": "П'ятниця",
            "lesson_number": 2,
            "start_time": "10:10:00",
            "end_time": "11:30:00",
            "subject": {
                "subject": "ВОК Креативний маркетинг",
                "subject_type": "(Л)"
            },
            "teacher": "доц. Милько І.П.",
            "room": "ауд. G-302",
            "sub_group": null,
            "groups": "Збірна група ДизО-26, Журн-27, КНІТ-23, КНІТ-24, Логіст2.14, Маркет2.11, Маркет2.12, МВ-23англ, Мен-27, Мит-25, МіБ-21анг, Пс-23, Рекл-28 ",
            "elimination": null
        },
        {
            "today_date": "2026-04-17",
            "week_day": "П'ятниця",
            "lesson_number": 3,
            "start_time": "11:50:00",
            "end_time": "13:10:00",
            "subject": {
                "subject": "ВОК Практикум з граматики німец",
                "subject_type": "(Пр)"
            },
            "teacher": "зав.каф.,доц. Пасик Л.А.",
            "room": "ауд. А-231",
            "sub_group": null,
            "groups": "Збірна група Англ-21, Англ-25, КНІТ-24, Нім-27, Укр-22ОА ",
            "elimination": null
        },
        {
            "today_date": "2026-04-17",
            "week_day": "П'ятниця",
            "lesson_number": 3,
            "start_time": "11:50:00",
            "end_time": "13:10:00",
            "subject": {
                "subject": "ВОК Основи кібербезпеки",
                "subject_type": "(Лаб)"
            },
            "teacher": "доц. Глинчук Л.Я.",
            "room": "ауд. С-503",
            "sub_group": null,
            "groups": "Збірна група КБ-26, КНІТ-23, КНІТ-24, Матем-21, Політ-23, Інф-25О, Іст-22О ",
            "elimination": null
        },
        {
            "today_date": "2026-04-17",
            "week_day": "П'ятниця",
            "lesson_number": 3,
            "start_time": "11:50:00",
            "end_time": "13:10:00",
            "subject": {
                "subject": "ВОК Креативний маркетинг",
                "subject_type": "(Пр)"
            },
            "teacher": "доц. Милько І.П.",
            "room": "ауд. G-407",
            "sub_group": null,
            "groups": "Збірна група ДизО-26, Журн-27, КНІТ-23, КНІТ-24, Маркет2.11, МВ-23англ, Мен-27, Мит-25, МіБ-21анг, Пс-23, Рекл-28 ",
            "elimination": null
        },
        {
            "today_date": "2026-04-17",
            "week_day": "П'ятниця",
            "lesson_number": 4,
            "start_time": "13:25:00",
            "end_time": "14:45:00",
            "subject": {
                "subject": "ВОК Основи кібербезпеки",
                "subject_type": "(Лаб)"
            },
            "teacher": "доц. Глинчук Л.Я.",
            "room": "ауд. С-503",
            "sub_group": null,
            "groups": "Збірна група КБ-26, КНІТ-23, КНІТ-24, Матем-21, Політ-23, Інф-25О, Іст-22О ",
            "elimination": null
        },
        {
            "today_date": "2026-04-17",
            "week_day": "П'ятниця",
            "lesson_number": 4,
            "start_time": "13:25:00",
            "end_time": "14:45:00",
            "subject": {
                "subject": "ВОК Фінансова гра-тренінг «Житт",
                "subject_type": "(Пр)"
            },
            "teacher": "доц. Теслюк С.А.",
            "room": "ауд. G-408",
            "sub_group": null,
            "groups": "Збірна група КНІТ-24, КІТР-24, Лінгв-2.10, Мит-25, Іст-22О ",
            "elimination": null
        }
    ],
    "day_3": [
        {
            "today_date": "2026-04-20",
            "week_day": "Понеділок",
            "lesson_number": 2,
            "start_time": "10:10:00",
            "end_time": "11:30:00",
            "subject": {
                "subject": "Спеціалізовані мови програмуван",
                "subject_type": "(Лаб)"
            },
            "teacher": "доц. Глинчук Л.Я.",
            "room": "ауд. С-503",
            "sub_group": "(підгр. 1)",
            "groups": null,
            "elimination": null
        },
        {
            "today_date": "2026-04-20",
            "week_day": "Понеділок",
            "lesson_number": 2,
            "start_time": "10:10:00",
            "end_time": "11:30:00",
            "subject": {
                "subject": "Програмування та підтримка веб-",
                "subject_type": "(Лаб)"
            },
            "teacher": "ст. викл. Павленко Ю.С.",
            "room": "ауд. С-502",
            "sub_group": "(підгр. 2)",
            "groups": null,
            "elimination": null
        },
        {
            "today_date": "2026-04-20",
            "week_day": "Понеділок",
            "lesson_number": 3,
            "start_time": "11:50:00",
            "end_time": "13:10:00",
            "subject": {
                "subject": "Спеціалізовані мови програмуван",
                "subject_type": "(Л)"
            },
            "teacher": "доц. Глинчук Л.Я.",
            "room": "ауд. С-519",
            "sub_group": null,
            "groups": "Потік КНІТ-23, КНІТ-24 ",
            "elimination": null
        },
        {
            "today_date": "2026-04-20",
            "week_day": "Понеділок",
            "lesson_number": 5,
            "start_time": "15:00:00",
            "end_time": "16:20:00",
            "subject": {
                "subject": "ВОК Креативний маркетинг",
                "subject_type": "(Пр)"
            },
            "teacher": "доц. Милько І.П.",
            "room": "ауд. G-410",
            "sub_group": null,
            "groups": "Збірна група ДизО-26, Журн-27, КНІТ-23, КНІТ-24, Маркет2.11, МВ-23англ, Мен-27, Мит-25, МіБ-21анг, Пс-23, Рекл-28 ",
            "elimination": null
        }
    ],
    "day_4": [
        {
            "today_date": "2026-04-21",
            "week_day": "Вівторок",
            "lesson_number": 1,
            "start_time": "08:30:00",
            "end_time": "09:50:00",
            "subject": {
                "subject": "Бази даних та розподілені інфор",
                "subject_type": "(Лаб)"
            },
            "teacher": "доц. Булатецька Л.В.",
            "room": "ауд. С-502",
            "sub_group": "(підгр. 2)",
            "groups": null,
            "elimination": null
        },
        {
            "today_date": "2026-04-21",
            "week_day": "Вівторок",
            "lesson_number": 2,
            "start_time": "10:10:00",
            "end_time": "11:30:00",
            "subject": {
                "subject": "Теорія ймовірностей та комп’юте",
                "subject_type": "(Пр)"
            },
            "teacher": "ст. викл. Антонюк О.П.",
            "room": "ауд. С-513",
            "sub_group": null,
            "groups": null,
            "elimination": null
        },
        {
            "today_date": "2026-04-21",
            "week_day": "Вівторок",
            "lesson_number": 3,
            "start_time": "11:50:00",
            "end_time": "13:10:00",
            "subject": {
                "subject": "Спеціалізовані мови програмуван",
                "subject_type": "(Лаб)"
            },
            "teacher": "доц. Глинчук Л.Я.",
            "room": "ауд. С-504",
            "sub_group": "(підгр. 2)",
            "groups": null,
            "elimination": null
        },
        {
            "today_date": "2026-04-21",
            "week_day": "Вівторок",
            "lesson_number": 4,
            "start_time": "13:25:00",
            "end_time": "14:45:00",
            "subject": {
                "subject": "Спеціалізовані мови програмуван",
                "subject_type": "(Лаб)"
            },
            "teacher": "доц. Глинчук Л.Я.",
            "room": "ауд. С-520",
            "sub_group": "(підгр. 1)",
            "groups": null,
            "elimination": null
        },
        {
            "today_date": "2026-04-21",
            "week_day": "Вівторок",
            "lesson_number": 4,
            "start_time": "13:25:00",
            "end_time": "14:45:00",
            "subject": {
                "subject": "Програмування та підтримка веб-",
                "subject_type": "(Лаб)"
            },
            "teacher": "ст. викл. Павленко Ю.С.",
            "room": "ауд. С-502",
            "sub_group": "(підгр. 2)",
            "groups": null,
            "elimination": null
        },
        {
            "today_date": "2026-04-21",
            "week_day": "Вівторок",
            "lesson_number": 5,
            "start_time": "15:00:00",
            "end_time": "16:20:00",
            "subject": {
                "subject": "ВОК Латинська мова",
                "subject_type": "(Пр)"
            },
            "teacher": "ст.викл. Шегедин Н.М.",
            "room": "ауд. Н-210",
            "sub_group": null,
            "groups": "Збірна група Англ-23, КНІТ-23, КНІТ-24, Нім-27, ПМ-25, Укр-23ОА, Фран-29, Іст-22О ",
            "elimination": null
        },
        {
            "today_date": "2026-04-21",
            "week_day": "Вівторок",
            "lesson_number": 5,
            "start_time": "15:00:00",
            "end_time": "16:20:00",
            "subject": {
                "subject": "ВОК Основи Web-дизайну",
                "subject_type": "(Пр)"
            },
            "teacher": "зав.каф.,доц. Авраменко Д.К.",
            "room": "ауд. Н-71",
            "sub_group": null,
            "groups": "Збірна група Англ-21, Англ-25, КБ-26, КНІТ-23, КНІТ-24, Лінгв-2.10, Матем-21, Нім-27, Укр-23ОА, Фран-29, Інф-25О ",
            "elimination": null
        }
    ],
    "day_5": [
        {
            "today_date": "2026-04-22",
            "week_day": "Середа",
            "lesson_number": 1,
            "start_time": "08:30:00",
            "end_time": "09:50:00",
            "subject": {
                "subject": "Програмування та підтримка веб-",
                "subject_type": "(Л)"
            },
            "teacher": "ст. викл. Павленко Ю.С.",
            "room": "ауд. С-508",
            "sub_group": null,
            "groups": "Потік КНІТ-23, КНІТ-24 ",
            "elimination": null
        },
        {
            "today_date": "2026-04-22",
            "week_day": "Середа",
            "lesson_number": 2,
            "start_time": "10:10:00",
            "end_time": "11:30:00",
            "subject": {
                "subject": "Бази даних та розподілені інфор",
                "subject_type": "(Лаб)"
            },
            "teacher": "доц. Булатецька Л.В.",
            "room": "ауд. С-502",
            "sub_group": "(підгр. 1)",
            "groups": null,
            "elimination": null
        },
        {
            "today_date": "2026-04-22",
            "week_day": "Середа",
            "lesson_number": 3,
            "start_time": "11:50:00",
            "end_time": "13:10:00",
            "subject": {
                "subject": "Бази даних та розподілені інфор",
                "subject_type": "(Лаб)"
            },
            "teacher": "доц. Булатецька Л.В.",
            "room": "ауд. С-502",
            "sub_group": "(підгр. 2)",
            "groups": null,
            "elimination": null
        },
        {
            "today_date": "2026-04-22",
            "week_day": "Середа",
            "lesson_number": 4,
            "start_time": "13:25:00",
            "end_time": "14:45:00",
            "subject": {
                "subject": "Програмування та підтримка веб-",
                "subject_type": "(Лаб)"
            },
            "teacher": "ст. викл. Павленко Ю.С.",
            "room": "ауд. С-503",
            "sub_group": "(підгр. 1)",
            "groups": null,
            "elimination": null
        }
    ],
    "day_6": [
        {
            "today_date": "2026-04-23",
            "week_day": "Четвер",
            "lesson_number": 1,
            "start_time": "08:30:00",
            "end_time": "09:50:00",
            "subject": {
                "subject": "Іноземна мова (за професійним",
                "subject_type": "(Пр)"
            },
            "teacher": "доц. Смаль О.В.",
            "room": "ауд. С-525",
            "sub_group": null,
            "groups": null,
            "elimination": null
        },
        {
            "today_date": "2026-04-23",
            "week_day": "Четвер",
            "lesson_number": 2,
            "start_time": "10:10:00",
            "end_time": "11:30:00",
            "subject": {
                "subject": "Теорія ймовірностей та комп’юте",
                "subject_type": "(Л)"
            },
            "teacher": "ст. викл. Антонюк О.П.",
            "room": "ауд. С-518",
            "sub_group": null,
            "groups": "Потік КНІТ-23, КНІТ-24 ",
            "elimination": null
        },
        {
            "today_date": "2026-04-23",
            "week_day": "Четвер",
            "lesson_number": 3,
            "start_time": "11:50:00",
            "end_time": "13:10:00",
            "subject": {
                "subject": "Програмування та підтримка веб-",
                "subject_type": "(Лаб)"
            },
            "teacher": "ст. викл. Павленко Ю.С.",
            "room": "ауд. С-503",
            "sub_group": "(підгр. 1)",
            "groups": null,
            "elimination": null
        },
        {
            "today_date": "2026-04-23",
            "week_day": "Четвер",
            "lesson_number": 6,
            "start_time": "16:35:00",
            "end_time": "17:55:00",
            "subject": {
                "subject": "ВОК Аудіо практикум з англійськ",
                "subject_type": "(Пр)"
            },
            "teacher": "доц. Бондар (п) Т.Г.",
            "room": "ауд. А-420",
            "sub_group": null,
            "groups": "Збірна група КНІТ-24, Лінгв-2.10, Лінгв-2.11, Лінгв-2.12, Нім-27, Нім-28О, Фран-29 ",
            "elimination": null
        }
    ],
    "day_7": null
}"""
    return json.loads(expected_data)


@pytest.fixture
def fake_html_error_fixture():
    fake_html_error = """<!DOCTYPE html>
<html>
<head>
    <meta content="IE=edge,chrome=1" http-equiv="X-UA-Compatible" />
    <meta content="width=device-width, initial-scale=1.0" name="viewport" />
    <meta content="" name="keywords" />
    <meta content="ПП Політек-Софт" name="author" />
    <meta content="ПС-Розклад v.4.0" name="description" />
    <meta content="text/html; charset=utf-8" http-equiv="Content-Type" />
    <title>ПС-Розклад v.4.0</title>
    <link href="./../css/style3.css" rel="stylesheet" type="text/css" />
    <script src="./../js/jquery.min.js" type="text/javascript"></script>
    <script src="./../js/jquery.maskedinput-1.4.1.min.js" type="text/javascript"></script>
    <script src="./../js/bootstrap.min.3.js" type="text/javascript"></script>
    <script src="./../js/rwd-table.min.js" type="text/javascript"></script>
    <script src="./../js/datepicker.js" type="text/javascript"></script>
    <script src="./../js/jquery.autocomplete.min.js" type="text/javascript"></script>
    <script src="./../js/js.js" type="text/javascript"></script>
    <script src="./../js/date.js" type="text/javascript"></script>
    <script src="./../js/select2.min.js" type="text/javascript"></script>
    <script src="./../js/summernote.min.js" type="text/javascript"></script>
    <script src="./../js/locales/summernote-uk-UA.min.js" type="text/javascript"></script>
    <script type="text/javascript">
        var url = "./srequest.cgi";
    </script>
    <style type="text/css">
        @media print {
            .hidden-print {
                display: none !important;
            }
            a[href]:after {
                content: " ";
            }
            body {
                padding-top: 0;
            }
            .col-print-6 {
                width: 50%;
                float: left;
                page-break-inside: avoid;
            }
        }
    </style>
</head>
<body>
    <div id="wrap">
        <div class="container-fluid">
            <div class="container">
                <div class="jumbotron pf16">
                    <style>
                        .remote_work {
                            font-weight: bold;
                        }
                    </style>
                    <div class="hidden-print">
                        <h3 class="text-center">Розклад занять</h3>
                        <h4 class="text-center">Волинський національний університет імені Лесі Українки</h4>
                        <div class="page-header" style="overflow: hidden;">
                            <form action="./timetable.cgi?n=700" enctype="application/x-www-form-urlencoded" id="setVedP" method="post" name="setVedP">
                                <div class="form-group">
                                    <select class="form-control" id="faculty" name="faculty" onchange="sel_val()">
                                        <option value="0">Оберіть факультет</option>
                                        <option value="1019">Факультет інформаційних технологій і математики</option>
                                        <option value="1021">Навчально-науковий інститут хімії та екології</option>
                                        <option value="1022">Факультет біології та лісового господарства</option>
                                        <option value="1023">Географічний факультет</option>
                                        <option value="1024">Юридичний факультет</option>
                                        <option value="1025">Факультет історії, політології та національної безпеки</option>
                                        <option value="1026">Факультет психології</option>
                                        <option value="1028">Факультет економіки та управління</option>
                                        <option value="1029">Факультет міжнародних відносин</option>
                                        <option value="1030">Факультет філології та журналістики</option>
                                        <option value="1031">Факультет іноземної філології</option>
                                        <option value="1033">Факультет культури і мистецтв</option>
                                        <option value="1034">Факультет педагогічної освіти та соціальної роботи</option>
                                        <option value="1035">Факультет фізичної культури, спорту та здоров`я</option>
                                        <option value="1040">Медичний факультет</option>
                                        <option value="1041">Навчально-науковий фізико-технологічний інститут</option>
                                        <option value="1042">Навчально-науковий інститут неперервної освіти</option>
                                    </select>
                                </div>
                                <div class="row">
                                    <div class="col-sm-4 col-xs-12">
                                        <input class="form-control" id="teacher" name="teacher" placeholder="ПІБ викладача" type="text" value="" />
                                    </div>
                                    <div class="col-sm-4 col-xs-12">
                                        <div class="form-group">
                                            <select class="form-control" id="course" name="course">
                                                <option value="0">Оберіть курс</option>
                                                <option value="1">1</option>
                                                <option value="2">2</option>
                                                <option value="3">3</option>
                                                <option value="4">4</option>
                                                <option value="5">5</option>
                                                <option value="6">6</option>
                                            </select>
                                        </div>
                                    </div>
                                    <div class="col-sm-4 col-xs-12">
                                        <div class="form-group">
                                            <input class="form-control" id="group" name="group" placeholder="Назва групи" type="text" value="rewrwe" />
                                        </div>
                                    </div>
                                </div>
                                <div class="row" style="margin-top:15px;">
                                    <div class="col-md-3">
                                        <div class="form-group">
                                            <div class="input-group">
                                                <span class="input-group-addon">з дати:</span>
                                                <input class="form-control input-sm datepicker" id="sdate" maxlength="10" name="sdate" placeholder="дд.мм.рррр" type="text" value="" />
                                            </div>
                                        </div>
                                    </div>
                                    <div class="col-md-3">
                                        <div class="form-group">
                                            <div class="input-group">
                                                <span class="input-group-addon">до дати:</span>
                                                <input class="form-control input-sm datepicker" id="edate" maxlength="10" name="edate" placeholder="дд.мм.рррр" type="text" value="" />
                                            </div>
                                        </div>
                                    </div>
                                    <div class="col-md-6 col-xs-12" style="text-align:right;">
                                        <button class="btn btn-success" type="submit">Показати розклад занять</button>
                                    </div>
                                </div>
                                <input name="n" type="hidden" value="700" />
                            </form>
                        </div>
                    </div>

                    <script type="text/javascript">
                        document.getElementById('sdate').addEventListener('input', function(event) {
                            var input = event.target;
                            input.value = input.value.replace(/[^0-9.]/g, '');
                        });
                        document.getElementById('edate').addEventListener('input', function(event) {
                            var input = event.target;
                            input.value = input.value.replace(/[^0-9.]/g, '');
                        });

                        function validateDateInput(inputElement) {
                            var dateInput = inputElement.value;
                            var datePattern = /^(0[1-9]|[12][0-9]|3[01])\.(0[1-9]|1[0-2])\.(\d{4})$/;
                            var formGroup = inputElement.closest('.form-group');
                            if (dateInput.trim() === '') {
                                formGroup.classList.remove('has-error', 'has-success');
                                return true;
                            }
                            if (!datePattern.test(dateInput)) {
                                formGroup.classList.add('has-error');
                                formGroup.classList.remove('has-success');
                                return false;
                            } else {
                                formGroup.classList.remove('has-error');
                                formGroup.classList.add('has-success');
                                return true;
                            }
                        }
                        document.getElementById('setVedP').addEventListener('submit', function(event) {
                            var isSdateValid = validateDateInput(document.getElementById('sdate'));
                            var isEdateValid = validateDateInput(document.getElementById('edate'));
                            if (!isSdateValid || !isEdateValid) {
                                event.preventDefault();
                                alert('Введіть дату у форматі дд.мм.рррр');
                            }
                        });
                        el = '';
                        var opt = 0;

                        function sel_val() {
                            opt = $('#faculty').val();
                        }

                        function addWin(num_t, id) {
                            $("#ldata").empty();
                            $("#ldata").html("Завантаження даних! Чекайте...");
                            el = id;
                            $.post("./timetable.cgi", {
                                n: "701",
                                lev: num_t,
                                txt: $("#" + id).val(),
                            }, AfterGetDate);
                        }

                        function AfterGetDate(data) {
                            $("#ldata").empty();
                            $("#ldata").append(data);
                        }
                        $("#b14").on('click', function(ev) {
                            addWin(141, 'teacher');
                            $('#ModalLabel').text('Викладачі');
                        });
                        $("#b15").on('click', function(ev) {
                            addWin(142, 'group');
                            $('#ModalLabel').text('Перелік академічних груп');
                        });
                        $('#group').autocomplete({
                            minChars: 2,
                            maxHeight: 400,
                            width: 400,
                            zIndex: 9998,
                            deferRequestBy: 50,
                            params: {
                                faculty: function() {
                                    return $('#faculty').val();
                                },
                                course: function() {
                                    return $('#course').val();
                                }
                            },
                            serviceUrl: './timetable.cgi?n=701&lev=142',
                            onSelect: function(data, value) {},
                        });
                        $('#teacher').autocomplete({
                            minChars: 3,
                            maxHeight: 400,
                            width: 400,
                            zIndex: 9999,
                            deferRequestBy: 50,
                            params: {
                                faculty: function() {
                                    return $('#faculty').val();
                                }
                            },
                            serviceUrl: './timetable.cgi?n=701&lev=141',
                            onSelect: function(data, value) {},
                        });
                    </script>

                    <div aria-hidden="true" aria-labelledby="ModalLabel" class="modal fade" id="AddModal" role="dialog" tabindex="-1">
                        <div class="modal-dialog">
                            <div class="modal-content">
                                <div class="modal-header">
                                    <button aria-label="Close" class="close" data-dismiss="modal" type="button">
                                        <span aria-hidden="true">×</span>
                                    </button>
                                    <h4 class="modal-title" id="ModalLabel"></h4>
                                </div>
                                <div class="modal-body">
                                    <div id="ldata" style="max-height: 300px;overflow: hidden;overflow-y: scroll;padding-left: 30px;"></div>
                                </div>
                                <div class="modal-footer">
                                    <button class="btn btn-primary" id="setval">Призначити</button>
                                    <button aria-hidden="true" class="btn" data-dismiss="modal">Закрити</button>
                                </div>
                            </div>
                        </div>
                    </div>

                    <script type="text/javascript">
                        var ansver = 'Оберіть запис у таблиці!';
                        var txt = '';
                        $('input[name=optionsRadios]:checked').on("click", function() {
                            txt = $('input[name=optionsRadios]:checked').val();
                        });
                        $("#setval").on("click", function(ev) {
                            if ($('input[name=optionsRadios]:checked').val() != null) {
                                txt = $('input[name=optionsRadios]:checked').val();
                                $('#' + el).val(txt);
                                $('#AddModal').modal('hide')
                            } else {
                                alert(ansver);
                            }
                        });
                    </script>

                    <div class="alert alert-info">
                        За вашим запитом записів не знайдено.<br />
                        Змініть або вкажіть більш точні дані для формування розкладу.<br />
                        Зверніть увагу! Якщо не вказано дату, на яку необхідно сформувати розклад, розклад буде виведено на поточну дату.
                    </div>
                </div>
            </div>
        </div>
    </div>
    <div id="footer">
        <div class="container">
            <p class="text-muted credit">© ПП <a href="http://politek-soft.kiev.ua" target="_blank">Політек-софт</a></p>
        </div>
    </div>
    <script type="text/javascript">
        $('.datepicker').datepicker({
            weekStart: 1,
            todayBtn: "linked",
            autoclose: true,
            orientation: "top right",
            todayHighlight: true,
            format: "dd.mm.yyyy",
        });
    </script>
</body>
</html>"""
    return fake_html_error


@pytest.fixture
def fake_html_five_days():
    fake_html_five_days = """<!DOCTYPE html><html><head><meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1" /><meta name="viewport" content="width=device-width, initial-scale=1.0" /><meta name="keywords" content="" /><meta name="author" content="ПП Політек-Софт" /><meta name="description" content="ПС-Розклад v.4.0" /><meta http-equiv="Content-Type" content="text/html; charset=windows-1251" /><title>ПС-Розклад v.4.0</title>
<link rel="stylesheet" type="text/css" href="./../css/style3.css" /><script type="text/javascript" src="./../js/jquery.min.js"></script><script type="text/javascript" src="./../js/jquery.maskedinput-1.4.1.min.js"></script><script type="text/javascript" src="./../js/bootstrap.min.3.js"></script><script type="text/javascript" src="./../js/rwd-table.min.js" ></script><script type="text/javascript" src="./../js/datepicker.js" ></script><script type="text/javascript" src="./../js/jquery.autocomplete.min.js" ></script><script type="text/javascript" src="./../js/js.js" ></script><script type="text/javascript" src="./../js/date.js" ></script><script type="text/javascript" src="./../js/select2.min.js" ></script><script type="text/javascript" src="./../js/summernote.min.js" ></script><script type="text/javascript" src="./../js/locales/summernote-uk-UA.min.js" ></script><script type="text/javascript"> var url = "./srequest.cgi"; </script><style type="text/css">@media print { .hidden-print { display: none !important; } a[href]:after {content: " ";}  body { padding-top: 0;} .col-print-6 { width: 50%; float: left; page-break-inside: avoid; }}</style></head><body><!-- PathDBTimeTable --><div id="wrap"><div class="container-fluid"><div class="container"><div class="jumbotron pf16"><style>.remote_work{font-weight: bold;}</style><div class="hidden-print"><h3 class="text-center">Розклад занять</h3><h4 class="text-center">Волинський національний університет імені Лесі Українки</h4><div class="page-header" style="overflow: hidden;"> <form  enctype="application/x-www-form-urlencoded" name="setVedP" id="setVedP" method="post" action="./timetable.cgi?n=700"><div class="form-group "><select name="faculty" id="faculty" class="form-control" onchange="sel_val()"><option value="0">Оберіть факультет</option><option value="1019">Факультет інформаційних технологій і математики</option><option value="1021">Навчально-науковий інститут хімії та екології</option><option value="1022">Факультет біології та лісового господарства</option><option value="1023">Географічний факультет</option><option value="1024">Юридичний факультет</option><option value="1025">Факультет історії, політології та національної безпеки</option><option value="1026">Факультет психології</option><option value="1028">Факультет економіки та управління</option><option value="1029">Факультет міжнародних відносин</option><option value="1030">Факультет філології та журналістики</option><option value="1031">Факультет іноземної філології</option><option value="1033">Факультет культури і мистецтв</option><option value="1034">Факультет педагогічної освіти та соціальної роботи</option><option value="1035">Факультет фізичної культури, спорту та здоров`я</option><option value="1040">Медичний факультет</option><option value="1041">Навчально-науковий фізико-технологічний інститут</option><option value="1042">Навчально-науковий інститут неперервної освіти</option></select></div><div class="row"><div class="col-sm-4 col-xs-12"><input type="text" name="teacher" id="teacher" value="" class="form-control" placeholder="ПІБ викладача" /></div><div class="col-sm-4 col-xs-12"><div class="form-group"><select name="course" id="course" class="form-control"><option value="0">Оберіть курс</option><option value="1" >1</option><option value="2" >2</option><option value="3" >3</option><option value="4" >4</option><option value="5" >5</option><option value="6" >6</option></select></div></div><div class="col-sm-4 col-xs-12"><div class="form-group"><input type="text"  name="group" id="group" value="КНІТ-24" placeholder="Назва групи" class="form-control" /></div></div></div><div class="row" style="margin-top:15px;"><div class="col-md-3"><div class="form-group"><div class="input-group"><span class="input-group-addon">з дати:</span><input type="text" name="sdate" id="sdate" value="" class="form-control input-sm datepicker" placeholder="дд.мм.рррр" maxlength="10" /></div></div></div><div class="col-md-3"><div class="form-group"><div class="input-group"><span class="input-group-addon">до дати:</span><input type="text" name="edate" id="edate" value="22.04.2026" class="form-control input-sm datepicker" placeholder="дд.мм.рррр" maxlength="10" /></div></div></div><div class="col-md-6 col-xs-12" style="text-align:right;"><button type="submit" class="btn btn-success">Показати розклад занять</button></div></div><input type="hidden" name="n" value="700" /></form></div></div><script type="text/javascript">document.getElementById('sdate').addEventListener('input', function(event) { var input = event.target; input.value = input.value.replace(/[^0-9.]/g, ''); }); document.getElementById('edate').addEventListener('input', function(event) { var input = event.target; input.value = input.value.replace(/[^0-9.]/g, ''); }); function validateDateInput(inputElement) { var dateInput = inputElement.value; var datePattern = /^(0[1-9]|[12][0-9]|3[01])\.(0[1-9]|1[0-2])\.(\d{4})$/; var formGroup = inputElement.closest('.form-group');     if (dateInput.trim() === '') {         formGroup.classList.remove('has-error', 'has-success');         return true;     } if (!datePattern.test(dateInput)) { formGroup.classList.add('has-error'); formGroup.classList.remove('has-success'); return false; } else { formGroup.classList.remove('has-error'); formGroup.classList.add('has-success'); return true; } } document.getElementById('setVedP').addEventListener('submit', function(event) { var isSdateValid = validateDateInput(document.getElementById('sdate')); var isEdateValid = validateDateInput(document.getElementById('edate')); if (!isSdateValid || !isEdateValid) { event.preventDefault(); alert('Введіть дату у форматі дд.мм.рррр'); } }); el = ''; var opt = 0; function sel_val(){opt = $('#faculty').val();/*alert(opt);*/}function addWin(num_t, id){$("#ldata").empty();$("#ldata").html("Завантаження даних! Чекайте...");el = id;$.post("./timetable.cgi",{n:"701", lev:num_t, txt:$("#"+id).val(),},AfterGetDate);}function AfterGetDate (data){ $("#ldata").empty();  $("#ldata").append(data);}$("#b14").on('click', function(ev) { addWin(141, 'teacher');$('#ModalLabel').text('Викладачі');});$("#b15").on('click', function(ev) { addWin(142, 'group');$('#ModalLabel').text('Перелік академічних груп');});$('#group').autocomplete({minChars: 2, maxHeight: 400, width: 400,zIndex: 9998, deferRequestBy: 50, params: {faculty: function(){return $('#faculty').val();},course: function(){return $('#course').val();}},serviceUrl: './timetable.cgi?n=701&lev=142', onSelect: function(data, value){ }, });$('#teacher').autocomplete({minChars: 3, maxHeight: 400, width: 400,zIndex: 9999, deferRequestBy: 50, params: {faculty: function(){return $('#faculty').val();}}, serviceUrl: './timetable.cgi?n=701&lev=141', onSelect: function(data, value){ }, });</script><div id="AddModal" class="modal fade" tabindex="-1" role="dialog" aria-labelledby="ModalLabel" aria-hidden="true"><div class="modal-dialog"><div class="modal-content"><div class="modal-header"><button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button><h4 class="modal-title" id="ModalLabel"></h4></div><div class="modal-body"><div id="ldata" style="max-height: 300px;overflow: hidden;overflow-y: scroll;padding-left: 30px;"></div></div><div class="modal-footer"><button class="btn btn-primary" id="setval">Призначити</button><button class="btn" data-dismiss="modal" aria-hidden="true">Закрити</button></div></div></div></div><script type="text/javascript">var ansver = 'Оберіть запис у таблиці!';var txt = '';$('input[name=optionsRadios]:checked').on("click", function(){txt = $('input[name=optionsRadios]:checked').val();});$("#setval").on("click", function(ev) {if ($('input[name=optionsRadios]:checked').val() != null) {txt = $('input[name=optionsRadios]:checked').val();$('#' + el) .val(txt);$('#AddModal').modal('hide')}else{alert(ansver);}});</script><div class="container"><h4 class="hidden-xs">Розклад групи <a title="Постійне посилання на тижневий розклад" style="font-size: 28px;" href="./timetable.cgi?n=700&group=-4261">КНІТ-24</a> з 16.04.2026 по 22.04.2026</h4><h4 class="visible-xs text-center">Розклад групи<br> <a title="Постійне посилання на тижневий розклад" style="font-size: 1.4em;" href="./timetable.cgi?n=700&group=-4261">КНІТ-24</a><br> з 16.04.2026 по 22.04.2026</h4><div class="row"><div class="col-md-6 col-sm-6 col-xs-12 col-print-6"><h4>16.04.2026 <small>Четвер</small></h4><table class="table  table-bordered table-striped"><tr><td>1</td><td>08:30<br>09:50</td><td style="max-width: 340px;overflow: hidden;">Іноземна мова (за професійним (Пр)<br> доц. Смаль О.В. ауд. С-508<br>  </td></tr></div><div class="row"><tr><td>2</td><td>10:10<br>11:30</td><td style="max-width: 340px;overflow: hidden;">Теорія ймовірностей та комп’юте (Л)<br> ст. викл. Антонюк О.П. ауд. С-518<br> Потік КНІТ-23, КНІТ-24<br> </td></tr></div><div class="row"><tr><td>3</td><td>11:50<br>13:10</td><td style="max-width: 340px;overflow: hidden;">Програмування та підтримка веб- (Лаб)<br> ст. викл. Павленко Ю.С. ауд. С-503<br>  (підгр. 1) <br> <br>Спеціалізовані мови програмуван (Лаб)<br> доц. Глинчук Л.Я. ауд. С-512<br>  (підгр. 2) <br> </td></tr></div><div class="row"><tr><td>4</td><td>13:25<br>14:45</td><td style="max-width: 340px;overflow: hidden;"> </td></tr></div><div class="row"><tr><td>5</td><td>15:00<br>16:20</td><td style="max-width: 340px;overflow: hidden;"> </td></tr></div><div class="row"><tr><td>6</td><td>16:35<br>17:55</td><td style="max-width: 340px;overflow: hidden;">ВОК Аудіо практикум з англійськ (Пр)<br> доц. Бондар (п) Т.Г. ауд. А-420<br> Збірна група КНІТ-24, Лінгв-2.10, Лінгв-2.11, Лінгв-2.12, Нім-27, Нім-28О, Фран-29<br> </td></tr></div><div class="row"><tr><td>7</td><td>18:10<br>19:30</td><td style="max-width: 340px;overflow: hidden;"> </td></tr></table></div><div class="col-md-6 col-sm-6 col-xs-12 col-print-6"><h4>17.04.2026 <small>П'ятниця</small></h4><table class="table  table-bordered table-striped"><tr><td>1</td><td>08:30<br>09:50</td><td style="max-width: 340px;overflow: hidden;">Увага! Заняття відмінено! ВОК Розробка вебдодатків на Pyt (Лаб)<br> доц. Булатецька Л.В. ауд. С-502<br> Збірна група КНІТ-24, КФ-22<br> </td></tr><tr><td>2</td><td>10:10<br>11:30</td><td style="max-width: 340px;overflow: hidden;">ВОК Основи геймдизайну (Пр)<br> зав.каф.,доц. Авраменко Д.К. ауд. Н-71<br> Збірна група ДизО-26, КНІТ-23, КНІТ-24, Лінгв-2.12, Мист-22, Пс-21, Фран-29, ФіК-23, Інф-25О<br> <br>ВОК Креативний маркетинг (Л)<br> доц. Милько І.П. ауд. G-302<br> Збірна група ДизО-26, Журн-27, КНІТ-23, КНІТ-24, Логіст2.14, Маркет2.11, Маркет2.12, МВ-23англ, Мен-27, Мит-25, МіБ-21анг, Пс-23, Рекл-28<br> </td></tr><tr><td>3</td><td>11:50<br>13:10</td><td style="max-width: 340px;overflow: hidden;">ВОК Практикум з граматики німец (Пр)<br> зав.каф.,доц. Пасик Л.А. ауд. А-231<br> Збірна група Англ-21, Англ-25, КНІТ-24, Нім-27, Укр-22ОА<br> <br>ВОК Основи кібербезпеки (Лаб)<br> доц. Глинчук Л.Я. ауд. С-503<br> Збірна група КБ-26, КНІТ-23, КНІТ-24, Матем-21, Політ-23, Інф-25О, Іст-22О<br> <br>ВОК Креативний маркетинг (Пр)<br> доц. Милько І.П. ауд. G-407<br> Збірна група ДизО-26, Журн-27, КНІТ-23, КНІТ-24, Маркет2.11, МВ-23англ, Мен-27, Мит-25, МіБ-21анг, Пс-23, Рекл-28<br> </td></tr><tr><td>4</td><td>13:25<br>14:45</td><td style="max-width: 340px;overflow: hidden;">ВОК Основи кібербезпеки (Лаб)<br> доц. Глинчук Л.Я. ауд. С-503<br> Збірна група КБ-26, КНІТ-23, КНІТ-24, Матем-21, Політ-23, Інф-25О, Іст-22О<br> <br>ВОК Фінансова гра-тренінг «Житт (Пр)<br> доц. Теслюк С.А. ауд. G-408<br> Збірна група КНІТ-24, КІТР-24, Лінгв-2.10, Мит-25, Іст-22О<br> </td></tr><tr><td>5</td><td>15:00<br>16:20</td><td style="max-width: 340px;overflow: hidden;"> </td></tr><tr><td>6</td><td>16:35<br>17:55</td><td style="max-width: 340px;overflow: hidden;"> </td></tr><tr><td>7</td><td>18:10<br>19:30</td><td style="max-width: 340px;overflow: hidden;"> </td></tr></table></div></div><div class="row"><div class="col-md-6 col-sm-6 col-xs-12 col-print-6"><h4>20.04.2026 <small>Понеділок</small></h4><table class="table  table-bordered table-striped"><tr><td>1</td><td>08:30<br>09:50</td><td style="max-width: 340px;overflow: hidden;"> </td></tr></div><div class="row"><tr><td>2</td><td>10:10<br>11:30</td><td style="max-width: 340px;overflow: hidden;">Спеціалізовані мови програмуван (Лаб)<br> доц. Глинчук Л.Я. ауд. С-503<br>  (підгр. 1) <br> <br>Програмування та підтримка веб- (Лаб)<br> ст. викл. Павленко Ю.С. ауд. С-502<br>  (підгр. 2) <br> </td></tr></div><div class="row"><tr><td>3</td><td>11:50<br>13:10</td><td style="max-width: 340px;overflow: hidden;">Спеціалізовані мови програмуван (Л)<br> доц. Глинчук Л.Я. ауд. С-519<br> Потік КНІТ-23, КНІТ-24<br> </td></tr></div><div class="row"><tr><td>4</td><td>13:25<br>14:45</td><td style="max-width: 340px;overflow: hidden;"> </td></tr></div><div class="row"><tr><td>5</td><td>15:00<br>16:20</td><td style="max-width: 340px;overflow: hidden;">ВОК Креативний маркетинг (Пр)<br> доц. Милько І.П. ауд. G-410<br> Збірна група ДизО-26, Журн-27, КНІТ-23, КНІТ-24, Маркет2.11, МВ-23англ, Мен-27, Мит-25, МіБ-21анг, Пс-23, Рекл-28<br> </td></tr></div><div class="row"><tr><td>6</td><td>16:35<br>17:55</td><td style="max-width: 340px;overflow: hidden;"> </td></tr></div><div class="row"><tr><td>7</td><td>18:10<br>19:30</td><td style="max-width: 340px;overflow: hidden;"> </td></tr></table></div><div class="col-md-6 col-sm-6 col-xs-12 col-print-6"><h4>21.04.2026 <small>Вівторок</small></h4><table class="table  table-bordered table-striped"><tr><td>1</td><td>08:30<br>09:50</td><td style="max-width: 340px;overflow: hidden;">Бази даних та розподілені інфор (Лаб)<br> доц. Булатецька Л.В. ауд. С-502<br>  (підгр. 2) <br> </td></tr><tr><td>2</td><td>10:10<br>11:30</td><td style="max-width: 340px;overflow: hidden;">Теорія ймовірностей та комп’юте (Пр)<br> ст. викл. Антонюк О.П. ауд. С-513<br>  </td></tr><tr><td>3</td><td>11:50<br>13:10</td><td style="max-width: 340px;overflow: hidden;">Спеціалізовані мови програмуван (Лаб)<br> доц. Глинчук Л.Я. ауд. С-504<br>  (підгр. 2) <br> </td></tr><tr><td>4</td><td>13:25<br>14:45</td><td style="max-width: 340px;overflow: hidden;">Спеціалізовані мови програмуван (Лаб)<br> доц. Глинчук Л.Я. ауд. С-520<br>  (підгр. 1) <br> <br>Програмування та підтримка веб- (Лаб)<br> ст. викл. Павленко Ю.С. ауд. С-502<br>  (підгр. 2) <br> </td></tr><tr><td>5</td><td>15:00<br>16:20</td><td style="max-width: 340px;overflow: hidden;">ВОК Латинська мова (Пр)<br> ст.викл. Шегедин Н.М. ауд. Н-210<br> Збірна група Англ-23, КНІТ-23, КНІТ-24, Нім-27, ПМ-25, Укр-23ОА, Фран-29, Іст-22О<br> <br>ВОК Основи Web-дизайну (Пр)<br> зав.каф.,доц. Авраменко Д.К. ауд. Н-71<br> Збірна група Англ-21, Англ-25, КБ-26, КНІТ-23, КНІТ-24, Лінгв-2.10, Матем-21, Нім-27, Укр-23ОА, Фран-29, Інф-25О<br> </td></tr><tr><td>6</td><td>16:35<br>17:55</td><td style="max-width: 340px;overflow: hidden;"> </td></tr><tr><td>7</td><td>18:10<br>19:30</td><td style="max-width: 340px;overflow: hidden;"> </td></tr></table></div></div><div class="row"><div class="col-md-6 col-sm-6 col-xs-12 col-print-6"><h4>22.04.2026 <small>Середа</small></h4><table class="table  table-bordered table-striped"><tr><td>1</td><td>08:30<br>09:50</td><td style="max-width: 340px;overflow: hidden;">Програмування та підтримка веб- (Л)<br> ст. викл. Павленко Ю.С. ауд. С-508<br> Потік КНІТ-23, КНІТ-24<br> </td></tr></div><div class="row"><tr><td>2</td><td>10:10<br>11:30</td><td style="max-width: 340px;overflow: hidden;">Бази даних та розподілені інфор (Лаб)<br> доц. Булатецька Л.В. ауд. С-502<br>  (підгр. 1) <br> </td></tr></div><div class="row"><tr><td>3</td><td>11:50<br>13:10</td><td style="max-width: 340px;overflow: hidden;">Бази даних та розподілені інфор (Лаб)<br> доц. Булатецька Л.В. ауд. С-502<br>  (підгр. 2) <br> </td></tr></div><div class="row"><tr><td>4</td><td>13:25<br>14:45</td><td style="max-width: 340px;overflow: hidden;">Програмування та підтримка веб- (Лаб)<br> ст. викл. Павленко Ю.С. ауд. С-503<br>  (підгр. 1) <br> </td></tr></div><div class="row"><tr><td>5</td><td>15:00<br>16:20</td><td style="max-width: 340px;overflow: hidden;">Практика</td></tr></div><div class="row"><tr><td>6</td><td>16:35<br>17:55</td><td style="max-width: 340px;overflow: hidden;">Практика</td></tr></div><div class="row"><tr><td>7</td><td>18:10<br>19:30</td><td style="max-width: 340px;overflow: hidden;">Практика</td></tr></table></div></div></div></div></div></div></div><div id="footer"><div class="container"><p class="text-muted credit">© ПП <a href="http://politek-soft.kiev.ua" target="_blank">Політек-софт</a></p></div></div><script type="text/javascript">$('.datepicker').datepicker({weekStart: 1,todayBtn: "linked",autoclose: true,orientation: "top right",todayHighlight: true,format: "dd.mm.yyyy",});</script></body></html>"""
    return fake_html_five_days


@pytest.fixture
def expected_data_five_days_fixture():
    expected_five_days_data = """{
    "day_1": [
        {
            "today_date": "2026-04-16",
            "week_day": "Четвер",
            "lesson_number": 1,
            "start_time": "08:30:00",
            "end_time": "09:50:00",
            "subject": {
                "subject": "Іноземна мова (за професійним",
                "subject_type": "(Пр)"
            },
            "teacher": "доц. Смаль О.В.",
            "room": "ауд. С-508",
            "sub_group": null,
            "groups": null,
            "elimination": null
        },
        {
            "today_date": "2026-04-16",
            "week_day": "Четвер",
            "lesson_number": 2,
            "start_time": "10:10:00",
            "end_time": "11:30:00",
            "subject": {
                "subject": "Теорія ймовірностей та комп’юте",
                "subject_type": "(Л)"
            },
            "teacher": "ст. викл. Антонюк О.П.",
            "room": "ауд. С-518",
            "sub_group": null,
            "groups": "Потік КНІТ-23, КНІТ-24 ",
            "elimination": null
        },
        {
            "today_date": "2026-04-16",
            "week_day": "Четвер",
            "lesson_number": 3,
            "start_time": "11:50:00",
            "end_time": "13:10:00",
            "subject": {
                "subject": "Програмування та підтримка веб-",
                "subject_type": "(Лаб)"
            },
            "teacher": "ст. викл. Павленко Ю.С.",
            "room": "ауд. С-503",
            "sub_group": "(підгр. 1)",
            "groups": null,
            "elimination": null
        },
        {
            "today_date": "2026-04-16",
            "week_day": "Четвер",
            "lesson_number": 3,
            "start_time": "11:50:00",
            "end_time": "13:10:00",
            "subject": {
                "subject": "Спеціалізовані мови програмуван",
                "subject_type": "(Лаб)"
            },
            "teacher": "доц. Глинчук Л.Я.",
            "room": "ауд. С-512",
            "sub_group": "(підгр. 2)",
            "groups": null,
            "elimination": null
        },
        {
            "today_date": "2026-04-16",
            "week_day": "Четвер",
            "lesson_number": 6,
            "start_time": "16:35:00",
            "end_time": "17:55:00",
            "subject": {
                "subject": "ВОК Аудіо практикум з англійськ",
                "subject_type": "(Пр)"
            },
            "teacher": "доц. Бондар (п) Т.Г.",
            "room": "ауд. А-420",
            "sub_group": null,
            "groups": "Збірна група КНІТ-24, Лінгв-2.10, Лінгв-2.11, Лінгв-2.12, Нім-27, Нім-28О, Фран-29 ",
            "elimination": null
        }
    ],
    "day_2": [
        {
            "today_date": "2026-04-17",
            "week_day": "П'ятниця",
            "lesson_number": 1,
            "start_time": "08:30:00",
            "end_time": "09:50:00",
            "subject": {
                "subject": "Увага! Заняття відмінено! ВОК Розробка вебдодатків на Pyt",
                "subject_type": "(Лаб)"
            },
            "teacher": "доц. Булатецька Л.В.",
            "room": "ауд. С-502",
            "sub_group": null,
            "groups": "Збірна група КНІТ-24, КФ-22 ",
            "elimination": null
        },
        {
            "today_date": "2026-04-17",
            "week_day": "П'ятниця",
            "lesson_number": 2,
            "start_time": "10:10:00",
            "end_time": "11:30:00",
            "subject": {
                "subject": "ВОК Основи геймдизайну",
                "subject_type": "(Пр)"
            },
            "teacher": "зав.каф.,доц. Авраменко Д.К.",
            "room": "ауд. Н-71",
            "sub_group": null,
            "groups": "Збірна група ДизО-26, КНІТ-23, КНІТ-24, Лінгв-2.12, Мист-22, Пс-21, Фран-29, ФіК-23, Інф-25О ",
            "elimination": null
        },
        {
            "today_date": "2026-04-17",
            "week_day": "П'ятниця",
            "lesson_number": 2,
            "start_time": "10:10:00",
            "end_time": "11:30:00",
            "subject": {
                "subject": "ВОК Креативний маркетинг",
                "subject_type": "(Л)"
            },
            "teacher": "доц. Милько І.П.",
            "room": "ауд. G-302",
            "sub_group": null,
            "groups": "Збірна група ДизО-26, Журн-27, КНІТ-23, КНІТ-24, Логіст2.14, Маркет2.11, Маркет2.12, МВ-23англ, Мен-27, Мит-25, МіБ-21анг, Пс-23, Рекл-28 ",
            "elimination": null
        },
        {
            "today_date": "2026-04-17",
            "week_day": "П'ятниця",
            "lesson_number": 3,
            "start_time": "11:50:00",
            "end_time": "13:10:00",
            "subject": {
                "subject": "ВОК Практикум з граматики німец",
                "subject_type": "(Пр)"
            },
            "teacher": "зав.каф.,доц. Пасик Л.А.",
            "room": "ауд. А-231",
            "sub_group": null,
            "groups": "Збірна група Англ-21, Англ-25, КНІТ-24, Нім-27, Укр-22ОА ",
            "elimination": null
        },
        {
            "today_date": "2026-04-17",
            "week_day": "П'ятниця",
            "lesson_number": 3,
            "start_time": "11:50:00",
            "end_time": "13:10:00",
            "subject": {
                "subject": "ВОК Основи кібербезпеки",
                "subject_type": "(Лаб)"
            },
            "teacher": "доц. Глинчук Л.Я.",
            "room": "ауд. С-503",
            "sub_group": null,
            "groups": "Збірна група КБ-26, КНІТ-23, КНІТ-24, Матем-21, Політ-23, Інф-25О, Іст-22О ",
            "elimination": null
        },
        {
            "today_date": "2026-04-17",
            "week_day": "П'ятниця",
            "lesson_number": 3,
            "start_time": "11:50:00",
            "end_time": "13:10:00",
            "subject": {
                "subject": "ВОК Креативний маркетинг",
                "subject_type": "(Пр)"
            },
            "teacher": "доц. Милько І.П.",
            "room": "ауд. G-407",
            "sub_group": null,
            "groups": "Збірна група ДизО-26, Журн-27, КНІТ-23, КНІТ-24, Маркет2.11, МВ-23англ, Мен-27, Мит-25, МіБ-21анг, Пс-23, Рекл-28 ",
            "elimination": null
        },
        {
            "today_date": "2026-04-17",
            "week_day": "П'ятниця",
            "lesson_number": 4,
            "start_time": "13:25:00",
            "end_time": "14:45:00",
            "subject": {
                "subject": "ВОК Основи кібербезпеки",
                "subject_type": "(Лаб)"
            },
            "teacher": "доц. Глинчук Л.Я.",
            "room": "ауд. С-503",
            "sub_group": null,
            "groups": "Збірна група КБ-26, КНІТ-23, КНІТ-24, Матем-21, Політ-23, Інф-25О, Іст-22О ",
            "elimination": null
        },
        {
            "today_date": "2026-04-17",
            "week_day": "П'ятниця",
            "lesson_number": 4,
            "start_time": "13:25:00",
            "end_time": "14:45:00",
            "subject": {
                "subject": "ВОК Фінансова гра-тренінг «Житт",
                "subject_type": "(Пр)"
            },
            "teacher": "доц. Теслюк С.А.",
            "room": "ауд. G-408",
            "sub_group": null,
            "groups": "Збірна група КНІТ-24, КІТР-24, Лінгв-2.10, Мит-25, Іст-22О ",
            "elimination": null
        }
    ],
    "day_3": [
        {
            "today_date": "2026-04-20",
            "week_day": "Понеділок",
            "lesson_number": 2,
            "start_time": "10:10:00",
            "end_time": "11:30:00",
            "subject": {
                "subject": "Спеціалізовані мови програмуван",
                "subject_type": "(Лаб)"
            },
            "teacher": "доц. Глинчук Л.Я.",
            "room": "ауд. С-503",
            "sub_group": "(підгр. 1)",
            "groups": null,
            "elimination": null
        },
        {
            "today_date": "2026-04-20",
            "week_day": "Понеділок",
            "lesson_number": 2,
            "start_time": "10:10:00",
            "end_time": "11:30:00",
            "subject": {
                "subject": "Програмування та підтримка веб-",
                "subject_type": "(Лаб)"
            },
            "teacher": "ст. викл. Павленко Ю.С.",
            "room": "ауд. С-502",
            "sub_group": "(підгр. 2)",
            "groups": null,
            "elimination": null
        },
        {
            "today_date": "2026-04-20",
            "week_day": "Понеділок",
            "lesson_number": 3,
            "start_time": "11:50:00",
            "end_time": "13:10:00",
            "subject": {
                "subject": "Спеціалізовані мови програмуван",
                "subject_type": "(Л)"
            },
            "teacher": "доц. Глинчук Л.Я.",
            "room": "ауд. С-519",
            "sub_group": null,
            "groups": "Потік КНІТ-23, КНІТ-24 ",
            "elimination": null
        },
        {
            "today_date": "2026-04-20",
            "week_day": "Понеділок",
            "lesson_number": 5,
            "start_time": "15:00:00",
            "end_time": "16:20:00",
            "subject": {
                "subject": "ВОК Креативний маркетинг",
                "subject_type": "(Пр)"
            },
            "teacher": "доц. Милько І.П.",
            "room": "ауд. G-410",
            "sub_group": null,
            "groups": "Збірна група ДизО-26, Журн-27, КНІТ-23, КНІТ-24, Маркет2.11, МВ-23англ, Мен-27, Мит-25, МіБ-21анг, Пс-23, Рекл-28 ",
            "elimination": null
        }
    ],
    "day_4": [
        {
            "today_date": "2026-04-21",
            "week_day": "Вівторок",
            "lesson_number": 1,
            "start_time": "08:30:00",
            "end_time": "09:50:00",
            "subject": {
                "subject": "Бази даних та розподілені інфор",
                "subject_type": "(Лаб)"
            },
            "teacher": "доц. Булатецька Л.В.",
            "room": "ауд. С-502",
            "sub_group": "(підгр. 2)",
            "groups": null,
            "elimination": null
        },
        {
            "today_date": "2026-04-21",
            "week_day": "Вівторок",
            "lesson_number": 2,
            "start_time": "10:10:00",
            "end_time": "11:30:00",
            "subject": {
                "subject": "Теорія ймовірностей та комп’юте",
                "subject_type": "(Пр)"
            },
            "teacher": "ст. викл. Антонюк О.П.",
            "room": "ауд. С-513",
            "sub_group": null,
            "groups": null,
            "elimination": null
        },
        {
            "today_date": "2026-04-21",
            "week_day": "Вівторок",
            "lesson_number": 3,
            "start_time": "11:50:00",
            "end_time": "13:10:00",
            "subject": {
                "subject": "Спеціалізовані мови програмуван",
                "subject_type": "(Лаб)"
            },
            "teacher": "доц. Глинчук Л.Я.",
            "room": "ауд. С-504",
            "sub_group": "(підгр. 2)",
            "groups": null,
            "elimination": null
        },
        {
            "today_date": "2026-04-21",
            "week_day": "Вівторок",
            "lesson_number": 4,
            "start_time": "13:25:00",
            "end_time": "14:45:00",
            "subject": {
                "subject": "Спеціалізовані мови програмуван",
                "subject_type": "(Лаб)"
            },
            "teacher": "доц. Глинчук Л.Я.",
            "room": "ауд. С-520",
            "sub_group": "(підгр. 1)",
            "groups": null,
            "elimination": null
        },
        {
            "today_date": "2026-04-21",
            "week_day": "Вівторок",
            "lesson_number": 4,
            "start_time": "13:25:00",
            "end_time": "14:45:00",
            "subject": {
                "subject": "Програмування та підтримка веб-",
                "subject_type": "(Лаб)"
            },
            "teacher": "ст. викл. Павленко Ю.С.",
            "room": "ауд. С-502",
            "sub_group": "(підгр. 2)",
            "groups": null,
            "elimination": null
        },
        {
            "today_date": "2026-04-21",
            "week_day": "Вівторок",
            "lesson_number": 5,
            "start_time": "15:00:00",
            "end_time": "16:20:00",
            "subject": {
                "subject": "ВОК Латинська мова",
                "subject_type": "(Пр)"
            },
            "teacher": "ст.викл. Шегедин Н.М.",
            "room": "ауд. Н-210",
            "sub_group": null,
            "groups": "Збірна група Англ-23, КНІТ-23, КНІТ-24, Нім-27, ПМ-25, Укр-23ОА, Фран-29, Іст-22О ",
            "elimination": null
        },
        {
            "today_date": "2026-04-21",
            "week_day": "Вівторок",
            "lesson_number": 5,
            "start_time": "15:00:00",
            "end_time": "16:20:00",
            "subject": {
                "subject": "ВОК Основи Web-дизайну",
                "subject_type": "(Пр)"
            },
            "teacher": "зав.каф.,доц. Авраменко Д.К.",
            "room": "ауд. Н-71",
            "sub_group": null,
            "groups": "Збірна група Англ-21, Англ-25, КБ-26, КНІТ-23, КНІТ-24, Лінгв-2.10, Матем-21, Нім-27, Укр-23ОА, Фран-29, Інф-25О ",
            "elimination": null
        }
    ],
    "day_5": [
        {
            "today_date": "2026-04-22",
            "week_day": "Середа",
            "lesson_number": 1,
            "start_time": "08:30:00",
            "end_time": "09:50:00",
            "subject": {
                "subject": "Програмування та підтримка веб-",
                "subject_type": "(Л)"
            },
            "teacher": "ст. викл. Павленко Ю.С.",
            "room": "ауд. С-508",
            "sub_group": null,
            "groups": "Потік КНІТ-23, КНІТ-24 ",
            "elimination": null
        },
        {
            "today_date": "2026-04-22",
            "week_day": "Середа",
            "lesson_number": 2,
            "start_time": "10:10:00",
            "end_time": "11:30:00",
            "subject": {
                "subject": "Бази даних та розподілені інфор",
                "subject_type": "(Лаб)"
            },
            "teacher": "доц. Булатецька Л.В.",
            "room": "ауд. С-502",
            "sub_group": "(підгр. 1)",
            "groups": null,
            "elimination": null
        },
        {
            "today_date": "2026-04-22",
            "week_day": "Середа",
            "lesson_number": 3,
            "start_time": "11:50:00",
            "end_time": "13:10:00",
            "subject": {
                "subject": "Бази даних та розподілені інфор",
                "subject_type": "(Лаб)"
            },
            "teacher": "доц. Булатецька Л.В.",
            "room": "ауд. С-502",
            "sub_group": "(підгр. 2)",
            "groups": null,
            "elimination": null
        },
        {
            "today_date": "2026-04-22",
            "week_day": "Середа",
            "lesson_number": 4,
            "start_time": "13:25:00",
            "end_time": "14:45:00",
            "subject": {
                "subject": "Програмування та підтримка веб-",
                "subject_type": "(Лаб)"
            },
            "teacher": "ст. викл. Павленко Ю.С.",
            "room": "ауд. С-503",
            "sub_group": "(підгр. 1)",
            "groups": null,
            "elimination": null
        }
    ],
    "day_6": null,
    "day_7": null
}"""
    return json.loads(expected_five_days_data)
