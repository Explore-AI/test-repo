"""
Test suite for Financial Calculator python test
"""
import pytest
import submission as Submission

@pytest.mark.timeout(5)
@pytest.mark.parametrize("test_input,expected_output", [
    ([10000, 20, 0.1], 572749.99),
    ([20000, 10, 0.104], 324926.69),
    ([10000, 20, 0.1], 572749.99),
    ([20000, 15, 0.1], 635449.63)
])
def test_savings_calculator(test_input, expected_output):
    """
    test savings_calculator method
    """
    actual_output = Submission.savings_calculator(*test_input)
    assert  actual_output == expected_output


@pytest.mark.timeout(5)
@pytest.mark.parametrize("test_input,expected_output", [
    ([20000, 0.1, 20, 35], 635449.63),
    ([20000, 0.1, 20, 35], 635449.63),
    ([10000, 0.1, 40, 60], 572749.99),
    ([10000, 0.1, 40, 60], 572749.99)
])
def test_retirement_savings(test_input, expected_output):
    """
    test retirement_savings method
    """
    actual_output = Submission.retirement_savings(*test_input)
    assert  actual_output == expected_output


@pytest.mark.timeout(5)
@pytest.mark.parametrize("test_input,expected_output", [
    ([20000, 0.1, 635339.63, 20], 35),
    ([20000, 0.1, 635339.63, 20], 35),
    ([10000, 0.001, 5.63, 20], 21),
    ([10000, 0.1, 572749.99, 40], 60)
])
def test_retirement_age(test_input, expected_output):
    """
    test retirement_savings method
    """
    actual_output = Submission.retirement_age(*test_input)
    assert  actual_output == expected_output


@pytest.mark.timeout(5)
@pytest.mark.parametrize("test_input,expected_output", [
    ([15000*12, 0.1045, 30], 1635153.79),
    ([100000, 0.1045, 30], 908418.77),
    ([150, 0.00001, 30], 4499.3),
    ([15000*12, 0.1045, 25], 1578934.73)
])
def test_maximum_home_loan(test_input, expected_output):
    """
    test maximum_home_loan method
    """
    actual_output = Submission.maximum_home_loan(*test_input)
    assert  actual_output == expected_output


@pytest.mark.timeout(5)
@pytest.mark.parametrize("test_input,expected_output", [
    ([15000*12, 0.1045, 35], 1635153.79),
    ([100000, 0.1045, 30], 927420.03),
    ([150, 0.00001, 30], 5249.06),
    ([15000*12, 0.1045, 40], 1578934.73)
])
def test_maximum_home_loan_with_age(test_input, expected_output):
    """
    test maximum_home_loan_with_age method
    """
    actual_output = Submission.maximum_home_loan_with_age(*test_input)
    assert  actual_output == expected_output


@pytest.mark.timeout(5)
@pytest.mark.parametrize("test_input,expected_output", [
    ([1635153, 15000*12, 0.1045], 30),
    ([1635153, 15000*12, 0.1045], 30),
    ([1635153, 15000*12, 0.05], 13),
    ([10, 1, 0.05], 15)
])
def test_pay_off_period(test_input, expected_output):
    """
    test pay_off_period method
    """
    actual_output = Submission.pay_off_period(*test_input)
    assert  actual_output == expected_output

@pytest.mark.timeout(5)
@pytest.mark.parametrize("test_input,expected_output", [
    ([15000, 30, 0.1045], 1954935238.47),
    ([10000, 30, 0.1045], 1303290158.98),
    ([10000, 30, 0.1045], 1303290158.98),
    ([1, 20, 0.05], 3470.87)
])
def test_investment(test_input, expected_output):
    """
    test investment method
    """
    actual_output = Submission.investment(*test_input)
    assert  actual_output == expected_output
