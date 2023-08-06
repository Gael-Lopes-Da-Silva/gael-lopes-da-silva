from datetime import datetime

def calculateAge():
    birth_date = datetime.strptime("2003-06-19", '%Y-%m-%d')
    current_date = datetime.now()
    age = current_date.year - birth_date.year - ((current_date.month, current_date.day) < (birth_date.month, birth_date.day))
    return str(age)

def generateMarkdown():
    with open("README.md", "w") as file:
        file.write('<!--- last build: ' + str(datetime.now()) + '--->\n')
        file.write('<h3 align="center">:wave: Hi! Since code is better than words...</h3>\n')
        file.write('\n')
        file.write('~~~python\n')
        file.write('person = {\n')
        file.write('    "first_name": "Gaël",\n')
        file.write('    "last_name": "Lopes Da Silva",\n')
        file.write('    "age": ' + calculateAge() + ',\n')
        file.write('    "gender": "boy",\n')
        file.write('    "job": "student",\n')
        file.write('    "country": "France",\n')
        file.write('    "website": "https://gael-lopes-da-silva.github.io/MyPortfolio/",\n')
        file.write('    "hobbies": ["programming", "sport", "piano", "tinkering"]\n')
        file.write('}\n')
        file.write('~~~\n')
        file.write('\n')
        file.write('<img align="right" style="width:30px;" title="This is the yellow dancing man. Don\'t question him." alt="Too bad. He gone..." src="./img/yellow_man.gif">\n')
        file.write('<kbd><br><a align="left" title="This is my portfolio :D" href="https://gael-lopes-da-silva.github.io/MyPortfolio/">Website</a><br></kbd>')

if __name__ == "__main__":
    generateMarkdown()
