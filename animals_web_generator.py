import json


def load_data(file_path):
    """Loads a JSON file."""
    with open(file_path, "r") as handle:
        return json.load(handle)

def load_template(file_path):
    """Loads an HTML template file."""
    with open(file_path, "r") as handle:
        return handle.read()

def get_skin_types(animals_data):
    """Collects sorted unique skin types from the data."""
    skin_types = set()
    for animal in animals_data:
        characteristics = animal.get("characteristics", {})
        skin_type = characteristics.get("skin_type")
        if skin_type:
            skin_types.add(skin_type)
    return sorted(skin_types)


def build_animals_info(animals_data):
    """Builds the string to embed into the HTML template."""
    output = ""
    for animal in animals_data:
        output += serialize_animal(animal)
    return output


def serialize_animal(animal):
    """Serializes a single animal entry into HTML."""
    name = animal.get("name")
    characteristics = animal.get("characteristics", {})
    diet = characteristics.get("diet")
    locations = animal.get("locations", [])
    animal_type = characteristics.get("type")

    output = '<li class="cards__item">\n'
    if name:
        output += f'  <div class="card__title">{name}</div>\n'
    output += '  <div class="card__text">\n'
    output += '    <ul class="card__list">\n'
    if diet:
        output += f"      <li class=\"card__list-item\"><strong>Diet:</strong> {diet}</li>\n"
    if locations:
        output += (
            f"      <li class=\"card__list-item\"><strong>Location:</strong> "
            f"{locations[0]}</li>\n"
        )
    if animal_type:
        output += (
            f"      <li class=\"card__list-item\"><strong>Type:</strong> "
            f"{animal_type}</li>\n"
        )
    output += "    </ul>\n"
    output += "  </div>\n"
    output += "</li>\n"
    return output


def main():
    animals_data = load_data("animals_data.json")
    skin_types = get_skin_types(animals_data)
    if skin_types:
        print("Available skin types:")
        for skin_type in skin_types:
            print(f"- {skin_type}")
        selected_skin_type = input("Choose a skin type: ").strip()
        if selected_skin_type:
            animals_data = [
                animal
                for animal in animals_data
                if animal.get("characteristics", {}).get("skin_type") == selected_skin_type
            ]
    template = load_template("animals_template.html")
    animals_info = build_animals_info(animals_data)

    html_content = template.replace("__REPLACE_ANIMALS_INFO__", animals_info)
    with open("animals.html", "w") as handle:
        handle.write(html_content)


if __name__ == "__main__":
    main()
