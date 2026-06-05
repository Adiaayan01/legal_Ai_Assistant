from feedback.capture import (
    save_edit
)

from feedback.analyzer import (
    extract_rule
)

from feedback.preferences import (
    save_preference
)

original = """
Property dispute exists.
"""

edited = """
Alleged property dispute exists.
"""

rule = extract_rule(
    original,
    edited
)

save_edit(
    original,
    edited,
    rule
)

save_preference(
    rule
)

print("\nLearned Rule:\n")
print(rule)