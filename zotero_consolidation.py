#   pip freeze > requirements.txt

import csv

# Define some rules for tag consolidation. This is just an example.
tag_mapping = {
    "usa": "United States",
    "u.s.": "United States",
    "america": "United States",
    "machinelearning": "Machine Learning"
    # Add other tag mappings as needed
}


# Function to capitalize the first letter of a word
def capitalize_first(word):
    return word[0].upper() + word[1:].lower()


# Read the CSV
with open("zotero_export.csv", "r") as file:
    reader = csv.DictReader(file)
    entries = list(reader)

# Process the tags
for entry in entries:
    tags = entry.get("tags", "").split(";")  # Assuming tags are semicolon-separated
    new_tags = []
    for tag in tags:
        # Normalize tag (to lower case)
        normalized_tag = tag.lower().strip()

        # Get the consolidated tag if it exists, otherwise use the original but capitalized
        consolidated_tag = tag_mapping.get(
            normalized_tag, capitalize_first(normalized_tag)
        )
        new_tags.append(consolidated_tag)
    entry["tags"] = ";".join(new_tags)

# Write the processed data back to a new CSV
with open("processed_zotero_export.csv", "w", newline="") as file:
    fieldnames = entries[0].keys()  # Assuming all entries have the same keys/columns
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    for entry in entries:
        writer.writerow(entry)
