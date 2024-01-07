import yaml

# Read YAML file
with open('publications.yaml', 'r') as file:
    publications = yaml.safe_load(file)

# Prepare README

readme = "# awesome-inverse-material-design\n\n"
readme += "Comprehensive collection of  literature, resources and tools showcasing the implementation of inverse design of material\n\n"
readme += "## 📝 Publications <small>({})</small>\n\n".format(len(publications))

for i, pub in enumerate(publications, 1):
    readme += "{}. [{}]({}) - {} by {}\n".format(i, pub['title'], pub['url'], pub['date'], pub['authors'].title())
    readme += "   Summary: {} ..... [[Code]({})]\n".format(pub['summary'], pub['code_link'])

# Write README to file
with open('../README.md', 'w') as file:
    file.write(readme)