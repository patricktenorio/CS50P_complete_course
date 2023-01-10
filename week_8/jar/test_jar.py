from jar import Jar

def test_init():
    jar = Jar(8)
    assert jar.capacity == 8
    jar = Jar()
    assert jar.capacity == 12

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"

def test_deposit():
    jar = Jar()
    jar.deposit(5)
    assert jar.size == 5
    jar.deposit(6)
    assert jar.size == 11

def test_withdraw():
    jar = Jar()
    jar.deposit(2)
    jar.withdraw(1)
    assert jar.size == 1
    jar.withdraw(1)
    assert jar.size == 0