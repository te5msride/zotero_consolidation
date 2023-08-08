# Zotero Tag Consolidation Script

This repository contains a Python script to automatically consolidate and normalize tags exported from Zotero in CSV format.

## Overview

The script processes the exported Zotero data to:

- Normalize the capitalization of tags.
- Consolidate various versions of tags into a standardized format.

For instance, variations like "USA", "U.S.", and "America" would be consolidated into "United States". Similarly, "hysteresis" and "Hysteresis" would be normalized to "Hysteresis".

## Setup

1. Ensure you have Python 3.x installed.
2. Clone this repository:

```
git clone https://github.com/te5msride/zotero_tag_consolidation.git
cd zotero_tag_consolidation
```

## Usage

1. Export your Zotero library in CSV format.
2. Place the exported CSV in the same directory as the script and name it `zotero_export.csv`.
3. Run the script:

```
python consolidate_tags.py
```

4. The processed data will be saved as `processed_zotero_export.csv` in the same directory.

## Customizing Tag Mapping

To adjust the rules for tag consolidation or to add more rules, modify the `tag_mapping` dictionary in the `consolidate_tags.py` script. For instance:

```python
tag_mapping = {
 'usa': 'United States',
 'u.s.': 'United States',
 'america': 'United States',
 # ... add more mappings as needed
}
```

## Backup & Caution

**Always backup your Zotero data** before using this script. Although this script only processes an exported copy of your Zotero library, it's always safe to have backups of your original data.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
