# @author: Gael Lopes Da Silva
# @project: gael-lopes-da-silva
# @github: https://github.com/Gael-Lopes-Da-Silva/gael-lopes-da-silva

from datetime import date, datetime

def get_age():
    birth_date = date(2003, 6, 19)
    current_date = date.today()
    age = current_date.year - birth_date.year - ((current_date.month, current_date.day) < (birth_date.month, birth_date.day))
    return str(age)

def main():
    text = f"""<!--- {datetime.now()} --->
```shell
> cat user.json
```

```json
{{
    "message": {{
        "icon": "🙌",
        "content": "Welcome to my GitHub profile page"
    }},
    "informations": {{
        "name": {{
            "firstname": "Gaël",
            "lastname": "Lopes Da Silva"
        }},
        "age": {get_age()},
        "location": "France",
        "activities": [
            "web developer",
            "student"
        ]
    }}
}}
```

<a href="https://gael-lopes-da-silva.github.io/portfolio/"><kbd><br>&nbsp;<b>Portfolio</b>&nbsp;<br><br></kbd></a>
<img align="right" style="width: 37px;" title="Behold the yellow dancing man!" alt="To bad, he gone..." src="./assets/yellow_man.gif">
"""

    with open("README.md", "w") as file:
        file.write(text)

if __name__ == "__main__":
    main()
