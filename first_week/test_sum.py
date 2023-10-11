from sum import *

def test_sum():
    assert sum(1,1,1) == (3)
    assert sum(-1,1,0) == (0)
    assert sum(0,0,0) == (0)
    assert sum(10,10.5,-0.5) == (20)

def test_type():
    assert sum('', 1, 3) == "Type error"
    assert sum('', [], 3) == "Type error"
    assert sum('', {}, 3) == "Type error"


if __name__ == '__main__':
    test_sum()
    test_type()
    print('OK')

# Для 15-18 строк
# В Python переменная name является специальной переменной, которая хранит имя текущего модуля.
# Если модуль запущен напрямую, name будет равен "main".
# Если модуль импортируется в другой модуль, name будет равен имени этого модуля.
