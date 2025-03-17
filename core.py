import json
import unicodedata

def load_email_formats(json_file):
    """Load the JSON file containing email formats for different domains."""
    try:
        with open(json_file, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: File '{json_file}' not found.")
        return {}

def normalize_name(name):
    """Normalize names by removing accents, special characters, and converting to lowercase."""
    return ''.join((c for c in unicodedata.normalize('NFD', name) if unicodedata.category(c) != 'Mn')).lower()

def get_email_structure(domain, email_formats):
    """Return the email format for a given domain."""
    return email_formats.get(domain, {}).get("format", "Unknown format")

def generate_email(first_name, last_name, domain, email_formats):
    """Generate an email using the detected format from the JSON file."""
    first_name = normalize_name(first_name)
    last_name = normalize_name(last_name)

    if domain not in email_formats:
        return {
            "error": f"No format found for domain {domain}",
            "email_structure": "Unknown format"
        }

    email_format = email_formats[domain]["format"]
    
    email = email_format.replace("first", first_name).replace("last", last_name)
    
    if "f." in email:
        email = email.replace("f", first_name[0])
    
    if ".l" in email:
        email = email.replace("l", last_name[0])

    return {
        "email": f"{email}@{domain}",
        "email_structure": email_format
    }

if __name__ == "__main__":
    json_file_path = "email_formats.json" 
    email_formats = load_email_formats(json_file_path)

    while True:
        print("\n🔹 Enter user details (or type 'exit' to quit)")
        first_name = input("Enter First Name: ").strip()
        if first_name.lower() == "exit":
            break
        last_name = input("Enter Last Name: ").strip()
        domain = input("Enter Domain (e.g., allianz.fr): ").strip()

        result = generate_email(first_name, last_name, domain, email_formats)
        print("\n✅ Generated Email:")
        print(result["email"] if "email" in result else result["error"])
        print(f"📌 Email Structure Used: {result['email_structure']}")
