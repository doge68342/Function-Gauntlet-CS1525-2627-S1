def temperature_in_safe_range(celsius: float, minimum_f: float, maximum_f: float) -> bool:
    """
    Convert the Celsius temperature to Fahrenheit and return `True`
    if the converted temperature is between the supplied Fahrenheit limits, 
    including the limits. Otherwise return `False`.

    :param celsuis: tempurature in celsuis
    :param minimum_f: minimum temprature in fahrenheit
    :param maximum_f: maximum temprature in fahrenheit
    :return: If tempurature from celsuis to fahrenheit is between minimum and maximum fahrenheit
    """
    fahrenheit = (celsius * 9/5) + 32
    if minimum_f <= fahrenheit <= maximum_f:
        return True
    else:
        return False

def can_afford_with_tip(balance: float, cost: float, tip_percent: float) -> bool:
    """
    Calculate the tip, add it to the original cost, and return `True` 
    if the supplied balance can pay the complete total. Otherwise return `False`.

    :param balance: amount of money in accountt
    :param cost: how much the product costs
    :param tip_percent: amount to tip
    :return: If customer can afford cost and tip_percent with balance
    """

    tip = cost * (tip_percent / 100)
    total = cost + tip
    if total <= balance:
        return True
    else:
        return False

def meets_average(score1: float, score2: float, score3: float, required_average: float) -> bool:
    """
    Calculate the average of the three scores and return `True` 
    if it is greater than or equal to the required average. Otherwise return `False`.


    :param score1: the first score
    :param score2: the second score
    :param score3: the third score
    :param required_average: average of 3 scores required to return true
    :return: if the average of the three scores is greater than the required average
    """

    average = (score1 + score2 + score3) / 3
    if average >= required_average:
        return True
    else:
        return False

def initials_match(first_name: str, last_name: str, expected_initials: str) -> bool:
    """
    Determine the initials of the supplied first and last names and return `True` 
    if they match `expected_initials`. Capitalization should not affect the result.

    :param first_name: First name of person
    :param last_name: Last name of person
    :param expected_initials: expected initials of person
    :return: if expected initials matches initials of fist and last names
    """

    initials = (first_name[0] + last_name[0]).upper()
    if initials == expected_initials.upper():
        return True
    else:
        return False