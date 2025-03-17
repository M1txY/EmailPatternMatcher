## **📌 1. Understand the JSON Structure**
The file follows this format:
```json
{
    "allianz.fr": {
        "format": "first.last"
    },
    "totalenergies.com": {
        "format": "f.last"
    },
    "loreal.fr": {
        "format": "first.last"
    },
    "airfrance.fr": {
        "format": "first.l"
    }
}
```
- **Key (`"allianz.fr"`)** → The company's email domain.
- **Value (`"format"`)** → The structure of email addresses for that company.

---

## **📌 2. Adding a New Company Domain & Email Format**
To add a **new domain**, insert a new entry in the JSON file.

### **🚀 Example: Adding `amazon.fr`**
If Amazon uses emails like `j.doe@amazon.fr`, add this:
```json
"amazon.fr": {
    "format": "f.last"
}
```

---

## **📌 3. Supported Email Formats**
| Format in JSON | Example Output |
|---------------|---------------|
| `"first.last"` | `jean.dupont@company.com` |
| `"f.last"` | `j.dupont@company.com` |
| `"first.l"` | `jean.d@company.com` |
| `"first"` | `jean@company.com` |
| `"last.first"` | `dupont.jean@company.com` |

---