import json

from document_processing.cleaner import (
    clean_text
)

from document_processing.parser import (
    extract_fields
)

with open(
    "data/sample_case.txt",
    "r"
) as f:

    text = f.read()

text = clean_text(text)

fields = extract_fields(
    text
)

print("\nSTRUCTURED DATA\n")

print(fields)

with open(
    "outputs/structured_data.json",
    "w"
) as outfile:

    json.dump(
        fields,
        outfile,
        indent=4
    )

print(
    "\nSaved Successfully"
)
