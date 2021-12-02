import os
from jinja2 import Template

years=[2019, 2020, 2021]
dirnames = [f"day{day:02}" for day in range(1, 26)]

file_check = {}
for year in years:
    file_check[year] = {}
    for day in range(1, 26):
        try:
            file_check[year][day] = (1 if len(os.listdir(path = f"{year}/day{day:02}")) > 0 else 0)
        except:
            file_check[year][day] = 0
    
# print(file_check)

with open("templates/readme.html", "r") as f:
    t = Template(f.read())
# t = Template("templates/readme.html")
rendered_template = t.render(years = file_check.keys(), file_check=file_check, dirnames=dirnames)

with open("README.md", "w+") as f:
    f.write(rendered_template)