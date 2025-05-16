import os
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from create_diary_schema import DiaryEntry  # Import the DiaryEntry model from your schema file

# Path to the folder containing the journal entries
journal_folder = "/home/manuel/Documents/Tickler/journals"

# Path to the SQLite database
database_path = "sqlite:///diary.db"

# Create a connection to the database
engine = create_engine(database_path)
Session = sessionmaker(bind=engine)
session = Session()

# Iterate through all .md files in the journal folder
for filename in os.listdir(journal_folder):
    if filename.endswith(".md"):
        # Extract the date from the filename (e.g., "2022_11_23.md")
        try:
            entry_date = datetime.strptime(filename.split(".")[0], "%Y_%m_%d").date()
        except ValueError:
            print(f"Skipping file with invalid date format: {filename}")
            continue

        # Read the content of the file
        file_path = os.path.join(journal_folder, filename)
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()

        # Check if an entry for this date already exists
        existing_entry = session.query(DiaryEntry).filter_by(date=entry_date).first()
        if existing_entry:
            print(f"Entry for {entry_date} already exists. Skipping.")
            continue

        # Create a new DiaryEntry object
        new_entry = DiaryEntry(date=entry_date, content=content)

        # Add the entry to the session
        session.add(new_entry)

# Commit all changes to the database
session.commit()
print("All entries have been inserted into the database.")