import requests

# -------------------------------
# Fetch publications from ORCID
# -------------------------------
def fetch_publications(orcid_id):
    url = f"https://pub.orcid.org/v3.0/{orcid_id}/works"
    headers = {"Accept": "application/json"}

    response = requests.get(url, headers=headers)
    publications = []

    if response.status_code == 200:
        data = response.json()
        for group in data.get("group", []):
            title = group["work-summary"][0]["title"]["title"]["value"]
            publications.append(title)

    return publications


# -------------------------------
# Main Execution
# -------------------------------
faculty_name = "Dr. A. Kumar"
orcid_id = "0000-0002-1825-0097"

publications = fetch_publications(orcid_id)

# -------------------------------
# Dynamic Output
# -------------------------------
print("-" * 50)
print("      RESEARCH PORTFOLIO AUTOMATION TOOL")
print("-" * 50)

print(f"\nFaculty Name : {faculty_name}")
print(f"ORCID ID     : {orcid_id}")
print(f"Total Publications : {len(publications)}\n")

print("-" * 50)
print("Publications List")
print("-" * 50)

for i, title in enumerate(publications, start=1):
    print(f"{i}. {title}")
