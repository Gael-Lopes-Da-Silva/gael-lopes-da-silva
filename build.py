# @author: Gael Lopes Da Silva
# @project: gael-lopes-da-silva
# @github: https://github.com/Gael-Lopes-Da-Silva/gael-lopes-da-silva

from datetime import datetime

def getAge():
    birth_date = datetime.strptime("2003-06-19", '%Y-%m-%d')
    current_date = datetime.now()
    age = current_date.year - birth_date.year - ((current_date.month, current_date.day) < (birth_date.month, birth_date.day))
    return str(age)

def getDate():
    return str(datetime.now())

def generateMarkdown():
    with open("README.md", "w", encoding="utf-8") as file:
        file.write('<!--- last build: ' + getDate() + '--->\n')
        file.write('~~~json\n')
        file.write('"message": "🖐️ Hi, this is my Github account !",\n')
        file.write('"informations": {\n')
        file.write('    "first_name": "Gaël",\n')
        file.write('    "last_name": "Lopes Da Silva",\n')
        file.write('    "age": ' + getAge() + ',\n')
        file.write('    "gender": "male",\n')
        file.write('    "job": "student",\n')
        file.write('    "country": "France",\n')
        file.write('    "hobbies": [\n')
        file.write('        "programming",\n')
        file.write('        "sport",\n')
        file.write('        "enjoying life"\n')
        file.write('    ]\n')
        file.write('}\n')
        file.write('~~~\n')
        file.write('\n')
        file.write('**[<kbd> <br> Website <br> </kbd>][Website]**\n')
        file.write('<img align="right" style="width:37px;" title="This is the yellow dancing man. Don\'t question him." alt="Too bad. He gone..." src="./img/yellow_man.gif">\n')
        file.write('\n')
        file.write('[Website]: https://gael-lopes-da-silva.ovh/\n')

if __name__ == "__main__":
    generateMarkdown()
