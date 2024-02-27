def first_or_default(iterable, condition, default=None):
    """Returns the first occurrence in iterable that satisfies condition, and
    returns default otherwise.
    """
    return next((x for x in iterable if condition(x)), default)


def split_between_ranks(iterable, rank, size):
    # Copied from https://github.com/LSSTDESC/ceci/blob/7043ae5776d9b2c210a26dde6f84bcc2366c56e7/ceci/stage.py#L586  # noqa: E501
    for i, task in enumerate(iterable):
        if rank is None:
            yield task
        elif i % size == rank:
            yield task
