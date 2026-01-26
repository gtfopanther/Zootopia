import json


def load_data(file_path):
    """Loads a JSON file."""
    with open(file_path, "r") as handle:
        return json.load(handle)

def load_template(file_path):
    """Loads an HTML template file."""
    with open(file_path, "r") as handle:
        return handle.read()


def build_animals_info(animals_data):
    """Builds the string to embed into the HTML template."""
    output = ""
    for animal in animals_data:
        name = animal.get("name")
        characteristics = animal.get("characteristics", {})
        diet = characteristics.get("diet")
        locations = animal.get("locations", [])
        animal_type = characteristics.get("type")

        output += '<li class="cards__item">'
        if name:
            output += f"Name: {name}<br/>\n"
        if diet:
            output += f"Diet: {diet}<br/>\n"
        if locations:
            output += f"Location: {locations[0]}<br/>\n"
        if animal_type:
            output += f"Type: {animal_type}<br/>\n"
        output += "</li>\n"
    return output


def main():
    animals_data = load_data("animals_data.json")
    template = load_template("animals_template.html")
    animals_info = build_animals_info(animals_data)

    html_content = template.replace("__REPLACE_ANIMALS_INFO__", animals_info)
    with open("animals.html", "w") as handle:
        handle.write(html_content)


if __name__ == "__main__":
    main()
