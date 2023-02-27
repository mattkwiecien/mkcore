def colors():
    from collections import namedtuple

    color = namedtuple("Color", ["code", "name"])
    color_data = (
        ("#3e85c7", "Blue"),
        ("#37761d", "Green"),
        ("#f1c332", "Yellow"),
        ("#cc0001", "Red"),
        ("#674fa7", "Purple"),
        ("#6fa8dd", "Light Blue"),
        ("#69a84f", "Light Green"),
        ("#fed966", "Light Yellow"),
        ("#e06665", "Light Red"),
        ("#8d7cc2", "Light Purple"),
        ("#9fc6e6", "Lighter Blue"),
        ("#92c47d", "Lighter Green"),
        ("#ffe59a", "Lighter Yellow"),
        ("#ea9998", "Lighter Red"),
        ("#b4a7d5", "Lighter Purple"),
        ("#b6d7a8", "Lightest Green"),
    )
    all_colors = [color._make(c) for c in color_data]

    return all_colors
