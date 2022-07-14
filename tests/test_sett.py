import sett


def test_basic():
    list_a = ["a", "b", "c"]
    list_b = ["a", "a", "b", "c", "d"]
    res = sett.compute_statistics(list_a, list_b)
    assert res["{A}"] == 3
    assert res["A"] == 3
    assert res["{B}"] == 4
    assert res["B"] == 5
    assert res["|A|-|B|"] == -2
    assert res["A ∖ B"] == 0
    assert res["B ∖ A"] == 1
    assert res["A ∪ B"] == 4
    assert res["A ∩ B"] == 3
