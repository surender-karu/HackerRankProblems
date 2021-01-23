from ..arrays.right_rotation import rotate_right_in_place

def test_rotation_by_one():
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    d = 1
    expected = [10, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert rotate_right_in_place(a, d) == expected

def test_rotation_by_two():
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    d = 2
    expected = [9, 10, 1, 2, 3, 4, 5, 6, 7, 8]
    assert rotate_right_in_place(a, d) == expected