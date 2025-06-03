import json

def load_data(file_path):
    """Loads a JSON file."""
    with open(file_path, "r") as handle:
        return json.load(handle)

def generate_animal_text(data):
    """Generates a plain-text block of animal info."""
    output = ""
    for animal in data:
        if "name" in animal:
            output += f"Name: {animal['name']}\n"
        if "diet" in animal:
            output += f"Diet: {animal['diet']}\n"
        if "locations" in animal and animal["locations"]:
            output += f"Location: {animal['locations'][0]}\n"
        if "type" in animal:
            output += f"Type: {animal['type']}\n"
        output += "\n"  # separate animals
    return output

def build_html(template_path, output_path, animal_info):
    """Replaces placeholder in template and writes new HTML."""
    with open(template_path, "r") as template_file:
        html_content = template_file.read()

    html_content = html_content.replace("__REPLACE_ANIMALS_INFO__", animal_info)

    with open(output_path, "w") as output_file:
        output_file.write(html_content)


def generate_animal_cards(data):
    """Generates styled HTML <li> card items with animal info."""
    output = ""
    for animal in data:
        characteristics = animal.get("characteristics", {})

        output += '<li class="cards__item">\n'

        if "name" in animal:
            output += f'  <div class="card__title">{animal["name"]}</div>\n'

        output += '  <p class="card__text">\n'

        if "diet" in characteristics:
            output += f'    <strong>Diet:</strong> {characteristics["diet"]}<br/>\n'

        if "locations" in animal and animal["locations"]:
            output += f'    <strong>Location:</strong> {animal["locations"][0]}<br/>\n'

        if "type" in characteristics:
            output += f'    <strong>Type:</strong> {characteristics["type"]}<br/>\n'

        output += '  </p>\n</li>\n'

    return output


# Load data and generate the HTML
animals_data = load_data("animals_data.json")
animal_info_text = generate_animal_cards(animals_data)
build_html("animals_template.html", "animals.html", animal_info_text)
