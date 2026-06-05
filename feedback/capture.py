import sqlite3

def save_edit(
    original,
    edited,
    rule
):

    conn = sqlite3.connect(
        "feedback/feedback.db"
    )

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO edits
        (
            original_draft,
            edited_draft,
            learned_rule
        )
        VALUES
        (?, ?, ?)
        """,
        (
            original,
            edited,
            rule
        )
    )

    conn.commit()

    conn.close()