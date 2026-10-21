def is_even(number) -> bool:
    """ Return True if number is even and False if it is odd.

    :param number: Number to check if its even
    :return: If it is even
    """
    if number % 2 == 0:
        return True
    else:
        return False

def count_vowels(text: str) -> int:
    """Count how many vowels (a, e, i, o, u) are in text.
    Uppercase and lowercase vowels should both count.

    :param text: Text that function counts the vowels in
    :return: amount of vowels
    """
    vowels = ["a", "e", "i", "o", "u"]
    counter = 0
    for l in text.lower():
        for v in vowels:
            if l == v:
                counter += 1
    return counter

def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert a Celsius temperature to Fahrenheit.

    :param celsius: Temperature in celcius
    :return: Temperature in fahrenheit
    """
    return (celsius * 9/5) + 32


def reverse_text(text: str) -> str:
    """Return the characters in text in reverse order.

    Example:
        "robot" becomes "tobor"

    :param text: Text to be revered
    :return: reversed text
    """
    output = ""
    for i in range(len(text)):
        output += (text[-(i + 1)])
    return output

def larger_number(a: float, b: float) -> float:
    """Return whichever of the two integers is larger.
    If they are equal, return either value.

    :param a: A number
    :param b: The other number
    :return: Either A or B, whichever is larger
    """
    return max(a, b)


def average_two(a: float, b: float) -> float:
    """Calculate and return the average of two integers.

    :param a: A number
    :param b: The other number
    :return: The average of a and b
    """
    return (a + b) / 2


def can_afford(balance: float, cost: float) -> bool:
    """Return True if balance is greater than or equal to cost.
    Otherwise, return False.

    :param balance: Account balance
    :param cost: Cost of product
    :return: If account can affor product
    """
    if balance >= cost:
        return True
    else:
        return False


def repeat_text(text: str, times: int) -> str:
    """Return one string containing text repeated the given
    number of times.

    Example:
        repeat_text("Go!", 3) returns "Go!Go!Go!"

    :param text: Text to be repeated
    :param times: How many times text will be repeated
    :return:
    """
    output = ""
    for i in range(times):
        output += text
    return output


def contains_word(sentence: str, word: str) -> bool:
    """Return True if word appears somewhere inside sentence.
    Otherwise, return False.

    :param sentence: Sentence to look for word in
    :param word: Word to look in sentence for 
    :return: If sentence contains word
    """
    if word in sentence:
        return True
    else:
        return False


def calculate_tip(cost: float, percent: float) -> float:
    """Calculate and return the amount of tip.

    Example:
        A cost of 20.0 and percent of 15 returns 3.0.

    :param cost: Amount of money paid
    :param percent: How much to tip
    :return: How much is tipped
    """
    return cost * (percent / 100)


def make_initials(first_name: str, last_name: str) -> str:
    """Return the uppercase first letters of the two names.

    Example:
        "Ada" and "Lovelace" returns "AL".

    :param first_name: First name of person
    :param last_name: Last name of person
    :return: Initials of person
    """
    return (first_name[0] + last_name[0]).upper()

def percent_score(points: float, possible: float) -> float:
    """Calculate what percentage of the possible points
    were earned. Return None if possible is less than 1.

    Example:
        18 out of 20 returns 90.0.

    :param points: How many the person got
    :param possible: How many the person could possibly have gotten
    :return: points out of possible as a percent
    """
    return points / possible * 100


def is_between(number: float, minimum: float, maximum: float) -> bool:
    """Return True if number is between minimum and maximum,
    including the minimum and maximum values.

    :param number: A number
    :param minimum: lower bound
    :param maximum: upper bound
    :return: if number is betweeen lower and upper bounds
    """
    if minimum <= number <= maximum:
        return True
    else:
        return False

def all_different(a: str, b: str, c: str) -> bool:
    """Check if three strings are different.
    Return True if all three strings are different.
    Otherwise,return False.

    :param a: A number
    :param b: Another number
    :param c: Yet another number
    :return: if a, b and c are different
    """
    if a == b or a == c or b == c:
        return False
    else:
        return True

def average_three(a: float, b: float, c: float) -> float:
    """Calculate and return the average of three integers.

    :param a: A number
    :param b: Another number
    :param c: Yet another number
    :return: The average of a, b and c
    """
    return (a + b + c) / 3

## Cuz this is just to ez
# def average(numbers):
#     total = 0
#     for i in numbers:
#         total += i
#     return i / len(numbers)

def describe_temperature(temperature: float, cold_limit: float, hot_limit: float) -> str:
    """Returns a string describing the temperature.
    Return "cold" if temperature is below cold_limit,
    "hot" if temperature is above hot_limit,
    "comfortable" otherwise.

    :param temperature: Tempurature to check
    :param cold_limit: temuprature that is too cold
    :param hot_limit: temuprature that is too hot
    :return: a rating of the tempurature
    """
    if hot_limit >= temperature >= cold_limit:
        return "comfortable"
    elif temperature < cold_limit:
        return "cold"
    elif temperature > hot_limit:
        return "hot"

if __name__ == "__main__":
    """
    If you want to test any of your code manually
    you can place function calls down here.
    Additionally, there is a test file loaded into
    this folder that you can run a test on your code.
    """
    pass

