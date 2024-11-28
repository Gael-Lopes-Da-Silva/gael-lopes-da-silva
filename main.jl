# @author: Gael Lopes Da Silva
# @project: gael-lopes-da-silva
# @github: https://github.com/Gael-Lopes-Da-Silva/gael-lopes-da-silva

using Dates

function getAge()
    birthDate = Date("2003-06-19", "yyyy-mm-dd")
    currentDate = today()
    age = year(currentDate) - year(birthDate) - ((month(currentDate), day(currentDate)) < (month(birthDate), day(birthDate)) ? 1 : 0)
    return string(age)
end

function (@main)(args)
    text = """
    <!--- $(now()) --->

    ```shell
    > cat user.json
    ```

    <img align="left" style="width: 200px;" title="This is the yellow dancing man. Don't question him." alt="Too bad. He gone..." src="./assets/yellow_man.gif">

    ```json
    "informations": {
        "name": "Gaël LOPES DA SILVA",
        "age": $(getAge()),
        "location": "France",
        "job": [
            "Web Developper",
            "Student"
        ]
    }
    ```

    [<kbd><br><strong>Portfolio</strong><br><br></kbd>](https://gael-lopes-da-silva.github.io/portfolio/)
    <img align="right" style="width: 37px;" title="This is the yellow dancing man. Don't question him." alt="Too bad. He gone..." src="./assets/yellow_man.gif">
    """

    open("README.md", "w") do file
        write(file, text)
    end

    return 0
end
