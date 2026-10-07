from post_neg import check_num

def test_postive():
    assert check_num(10) == "Positive number"
    
def test_negative():
    assert check_num(-10) == "Negative number"

def test_zero():
    assert check_num(0) == "Zero"   