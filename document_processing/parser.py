import re

def extract_fields(text):

    fields = {}

    case_number = re.search(
        r"Case\s*No[:\s]+([\w\-\/]+)",
        text
    )

    plaintiff = re.search(
        r"Plaintiff[:\s]+([A-Za-z\s]+)",
        text
    )

    defendant = re.search(
        r"Defendant[:\s]+([A-Za-z\s]+)",
        text
    )

    dates = re.findall(
        r"\d{1,2}[/-]\d{1,2}[/-]\d{2,4}",
        text
    )

    fields["case_number"] = (
        case_number.group(1)
        if case_number else None
    )

    fields["plaintiff"] = (
        plaintiff.group(1).strip()
        if plaintiff else None
    )

    fields["defendant"] = (
        defendant.group(1).strip()
        if defendant else None
    )

    fields["dates"] = dates

    return fields