from string_utils import StringUtils
import pytest
string_util = StringUtils()

@pytest.mark.parametrize('string, result', [
    #Позитивные проверки:
    ("олег", "Олег"),
    ("олЕЖА", "Олежа"),
    #Негативные проверки:
    ("Олег", "Олег"),
    ("ОЛЕГ", "Олег"), 
    ("/олег", "/олег"), 
    ("о", "О")
])
def test_capitalize ( string , result ) :
    string_util = StringUtils()
    res = string_util.capitalize ( string )
    assert res == result

@pytest.mark.parametrize('string, result', [
    #Позитивные проверки:
    (" ффф", "ффф"),
    (" ФФФ", "ФФФ"),
    ("  123  ", "123  "),
    (" ОЛ-ег", "ОЛ-ег"),
    ("   ОлЕжа23", "ОлЕжа23"),
    #Негативные проверки:
    ("", ""),
    ("and rey", "and rey"),
    ("roll", "roll"),
    ("123  ", "123  ")
])
def test_trim ( string, result ):
    string_util = StringUtils()
    res = string_util.trim ( string )
    assert res == result


@pytest.mark.parametrize('string, divider, result', [
    #Позитивные проверки:
    ("один,два,три", ",", ["один", "два", "три"]),
    ("1,2,3,4,5", None, ["1", "2", "3", "4", "5"]),
    ("@^%^&^!^*", "^", ["@", "%", "&", "!", "*"]),
    ("1/n2/n3", "/n", ["1", "2", "3"]),
    #Негативные проверки:
    ("", None, []),
    ("1,2,3,4 5", None, ["1", "2", "3", "4 5"]),
    ])
def test_to_list(string, divider, result):
    print(f"Input string: {string}")
    print(f"Expected result: {result}")
    if divider is None:
        res = string_util.to_list ( string )
    else:
        res = string_util.to_list ( string , divider )  
    assert res == result


@pytest.mark.parametrize('string, symbol, result', [
    #Позитивные проверки:
    ("олег", "о", True),
    (" олежа", "е", True),
    ("оЛег  ", "г", True),
    ("123456789", "1", True),
    ("Р", "Р", True),
    ("", "", True),
    #Негативные проверки:
    ("Олег", "c", False),
    ("Олег", "O", False),
    ("Олег", "№", False)
])
def test_contains(string, symbol, result):
    string_util = StringUtils()
    res = string_util.contains(string, symbol)
    assert res == result


@pytest.mark.parametrize('string, symbol, result', [
    #Позитивные проверки:
    ("Олег", "г", "Оле"),
    ("Скайпро", "Скай", "про"),
    ("12345", "234", "15"),
    #Негативные проверки:
    ("Олег", "Скайпро", "Олег"),
    ("", "", ""),
    ("Олег", "", "Олег")
])
def test_delete_symbol(string, symbol, result):
    string_util = StringUtils()
    res = string_util.delete_symbol(string, symbol)
    assert res == result


@pytest.mark.parametrize('string, symbol, result', [
    #Позитивные проверки:
    ("ОЛег", "О", True),
    ("Скайпро", "С", True),
    (" Олег", "", True),
    ("Олег  ", "О", True),
    ("", "", True),
    #Негативные проверки:
    ("Олег", "о", False),
    ("скайпро", "С", False),
    ("", "ф", False),
    ("Олег", "е", False)
])
def test_starts_with(string, symbol, result):
    string_util = StringUtils()
    res = string_util.starts_with(string, symbol)
    assert res == result


@pytest.mark.parametrize('string, symbol, result', [
    #Позитивные проверки:
("Олег", "г", True),
    ("олег", "г", True),
    ("ОлеГ", "Г", True),
    ("7893", "3", True),
    ("", "", True),
    ("Andrey1", "1", True),
    #Негативные проверки:
    ("aaaaa", "m", False),
    ("Oleg", "2", False),
    ("олег", "Е", False),
    ("", "ф", False)
])
def test_end_with(string, symbol, result):
    string_util = StringUtils()
    res = string_util.end_with(string, symbol)
    assert res == result


@pytest.mark.parametrize('string, result', [
    #Позитивные проверки:
    ("", True),
    (" ", True),
    ("  ", True),
    #Негативные проверки:
    ("Олег", False),
    (" олег", False),
    ("123456789", False),
    ("Олег ", False)   
])
def test_is_empty(string, result):
    string_util = StringUtils()
    res = string_util.is_empty(string)
    assert res == result


@pytest.mark.parametrize('lst, joiner, result', [
    #Позитивные проверки:
    (["О", "Л", "Е", "Г"], ",", "О,Л,Е,Г"),
    ([1,2,3], None, "1, 2, 3"),
    (["Скайпро", "Пушка"], "-", "Скайпро-Пушка"),
    #Негативные проверки:
    ([], None, ""),
    ([], "*", "")
])
def test_list_to_string(lst, joiner, result):
    string_util = StringUtils()
    if joiner == None:
        res = string_util.list_to_string(lst)
    else:
        res = string_util.list_to_string(lst, joiner)
    assert res == result