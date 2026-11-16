def porridge_satisfaction(temperature: float) -> str:
    """Return what a picky eater says when tasting porridge with the given temperature.

    Temperatures greater than 50.0 are too hot, temperatures less than 49.0 are too cold,
    and the temperatures in between are just right.

    >>> porridge_satisfaction(65.5)
    'This porridge is too hot! Ack!!'
    >>> porridge_satisfaction(30.0)
    'This porridge is too cold! Brrr..'
    >>> porridge_satisfaction(49.5)
    'This porridge is just right! Yum!!'
    """
    if 49.0 <= temperature <= 50.0:
        return 'This porridge is just right! Yum!!'
    elif temperature < 49.0:
        return 'This porridge is too cold! Brrr..'
    else:
        return 'This porridge is too hot! Ack!!'


def rock_paper_scissors(player1: str, player2: str) -> str:
    """Return the winner of a game of rock, paper, scissors.

    The game is played with the following rules:
        1) 'rock' wins against 'scissors'
        2) 'scissors' wins against 'paper'
        3) 'paper' wins against 'rock'

    Ties are allowed.

    You may ASSUME that the input strings are in {'rock', 'paper', 'scissors'}.

    >>> rock_paper_scissors('rock', 'scissors')
    'Player1 wins'
    >>> rock_paper_scissors('rock', 'paper')
    'Player2 wins'
    >>> rock_paper_scissors('rock', 'rock')
    'Tie!'
    """
    if player1 == player2:
        return 'Tie!'
    elif (player1 == 'rock' and player2 == 'scissors') or \
        (player1 == 'scissors' and player2 == 'paper') or \
        (player1 == 'paper' and player2 == 'rock'):
        return 'Player1 wins'
    else:
        return 'Player2 wins'


def is_odd(n: int) -> bool:
    """Return whether n is odd (not divisible by 2).
    """
    return n % 2 != 0


def is_teenager(age: int) -> bool:
    """Return whether age is between 13 and 18 inclusive.

    HINT: identify the range of integers that make this function return True.
    Your simplified function body can look like:

        return (age >= ...) and (age <= ...)

    or, using a cool Python short-hand:

        return ... <= age <= ...
    """
    return 13 <= age <= 18

def larger_first_value(numbers1: list, numbers2: list) -> int:
    """Return the larger of numbers1[0] and numbers2[0].

    You may ASSUME that numbers1 and numbers2 are non-empty lists
    of integers.
    """
    return max(numbers1[0],numbers2[0])


def is_common_prefix(prefix: str, s1: str, s2: str) -> bool:
    """Return whether prefix is a common prefix of both s1 and s2.

    Hint: identify exactly what boolean expression needs to be True
    in order for this function to return True.
    """
    return (prefix in s1) and (prefix in s2)


def same_corresponding_values(mapping: dict, key1: str, key2: str) -> bool:
    """Return whether the two given keys have the same corresponding value in mapping.

    Return False if at least one of the keys is not in the mapping.

    Hint: when evaluating a chain of ands ("p and q and r ..."), the Python
    interpreter stops at the *first* expression that evaluates to False.
    Similarly, when evlauating a chain of ors, Python stops at the first
    expression that evaluates to True.
    """
    return key1 in mapping and key2 in mapping and mapping[key1] == mapping[key2]




if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
