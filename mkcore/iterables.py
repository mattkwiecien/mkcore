def first_or_default(iterable, condition, default=None):
    """Returns the first occurrence in iterable that satisfies condition, and
    returns default otherwise.
    """
    return next((x for x in iterable if condition(x)), default)
