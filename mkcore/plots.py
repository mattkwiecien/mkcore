def colors():
    from collections import namedtuple

    color = namedtuple("Color", ["name", "code"])
    color_data = (
        ("#3e85c7", "Blue"),
        ("#6fa8dd", "Light Blue"),
        ("#9fc6e6", "Lighter Blue"),
        ("#37761d", "Green"),
        ("#69a84f", "Light Green"),
        ("#92c47d", "Lighter Green"),
        ("#b6d7a8", "Lightest Green"),
        ("#f1c332", "Yellow"),
        ("#fed966", "Light Yellow"),
        ("#ffe59a", "Lighter Yellow"),
        ("#cc0001", "Red"),
        ("#e06665", "Light Red"),
        ("#ea9998", "Lighter Red"),
        ("#674fa7", "Purple"),
        ("#8d7cc2", "Light Purple"),
        ("#b4a7d5", "Lighter Purple"),
    )
    all_colors = [color._make(c) for c in color_data]

    return all_colors
