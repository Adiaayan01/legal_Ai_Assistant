import json
import os

PREFERENCE_FILE = (
    "feedback/preferences.json"
)

def load_preferences():

    if not os.path.exists(
        PREFERENCE_FILE
    ):
        return []

    with open(
        PREFERENCE_FILE,
        "r"
    ) as f:

        return json.load(f)

def save_preference(rule):

    prefs = load_preferences()

    prefs.append(rule)

    prefs = list(set(prefs))

    with open(
        PREFERENCE_FILE,
        "w"
    ) as f:

        json.dump(
            prefs,
            f,
            indent=4
        )