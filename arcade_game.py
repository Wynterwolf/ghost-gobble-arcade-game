"""Functions for implementing the rules of the classic arcade game Pac-Man."""


def eat_ghost(power_pellet_active, touching_ghost):
    """Verify that Pac-Man can eat a ghost if he is empowered by a power pellet.

    :param power_pellet_active: bool - does the player have an active power pellet?
    :param touching_ghost: bool - is the player touching a ghost?
    :return: bool - can a ghost be eaten?
    """

    if power_pellet_active and touching_ghost:
        return True
    else:
        return False


def score(touching_power_pellet, touching_dot):
    """Verify that Pac-Man has scored when a power pellet or dot has been eaten.

    :param touching_power_pellet: bool - is the player touching a power pellet?
    :param touching_dot: bool - is the player touching a dot?
    :return: bool - has the player scored or not?
    """

    if touching_dot or touching_power_pellet:
        return True
    else:
        return False


def lose(power_pellet_active, touching_ghost):
    """Trigger the game loop to end (GAME OVER) when Pac-Man touches a ghost without his power pellet.

    :param power_pellet_active: bool - does the player have an active power pellet?
    :param touching_ghost: bool - is the player touching a ghost?
    :return: bool - has the player lost the game?
    """
    # The player does not lose if they are touching a ghost and have an active power pellet
    if touching_ghost and power_pellet_active:
        return False
    
    # The player loses if they are touching a ghost and there is no power pellet active
    if touching_ghost and not power_pellet_active:
        return True
    
    # The player does not lose in any other case
    return False


def win(has_eaten_all_dots, power_pellet_active, touching_ghost):
    """Trigger the victory event when all dots have been eaten.

    :param has_eaten_all_dots: bool - has the player "eaten" all the dots?
    :param power_pellet_active: bool - does the player have an active power pellet?
    :param touching_ghost: bool - is the player touching a ghost?
    :return: bool - has the player won the game?
    """

    # The player cannot win if they are touching a ghost and don't have a power pellet active
    if touching_ghost and not power_pellet_active:
        return False

    # The player wins if they have eaten all the dots and are either not touching a ghost
    # or have a power pellet active
    if has_eaten_all_dots:
        return True

    # Otherwise, the player does not win
    return False
