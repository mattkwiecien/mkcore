def get_exception_details(ex):
    import traceback

    lines = traceback.format_exception(type(ex), ex, ex.__traceback__)

    return "".join(lines)
