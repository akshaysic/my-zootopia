import json

# Load animal data
with open("animals.json") as file:
    animals = json.load(file)
print(type(animals))
print(type(animals[0]))
# HTML template for one animal
animal_template = """
<div class="animal">
  <h2>{name}</h2>
  <ul>
    <li><strong>Type:</strong> {type}</li>
    <li><strong>Color:</strong> {color}</li>
    <li><strong>Location:</strong> {location}</li>
  </ul>
</div>
"""

# Wrap entire page
page_template = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Zootopia Animals</title>
  <style>
    body {{ font-family: Arial; background: #f0f8ff; padding: 20px; }}
    .animal {{ border: 1px solid #ccc; padding: 10px; margin: 10px 0; background: #fff; border-radius: 8px; }}
  </style>
</head>
<body>
  <h1>Animals of Zootopia</h1>
  {animal_entries}
</body>
</html>
"""

# Generate all animal entries
animal_entries = ""
for animal in animals:
    animal_entries += animal_template.format(**animal)

# Final HTML page
final_html = page_template.format(animal_entries=animal_entries)

# Save to file
with open("animals.html", "w") as output:
    output.write(final_html)

print("animals.html generated successfully.")
