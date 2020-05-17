def test_solution(monkeypatch):
    x=99
    ret_val1= None

    def f():
        nonlocal x
        return x

    def g(num1):
        nonlocal ret_val1
        ret_val1=num1

    monkeypatch.setattr('builtins.input',f)
    monkeypatch.setattr('builtins.print',g)

    import solution
    assert solution.number==x
    assert solution.result==ret_val1
