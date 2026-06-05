import sqlite3

conn = sqlite3.connect(
    "feedback/feedback.db"
)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS edits (

id INTEGER PRIMARY KEY AUTOINCREMENT,

original_draft TEXT,

edited_draft TEXT,

learned_rule TEXT,

created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

)
""")

conn.commit()

conn.close()

print("Feedback Database Ready")