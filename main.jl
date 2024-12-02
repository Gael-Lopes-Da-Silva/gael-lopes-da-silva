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

    ```json
    {
        "message": {
            "icon": "🙌",
            "content": "Welcome to my GitHub profile page"
        },
        "informations": {
            "name": "Gaël LOPES DA SILVA",
            "age": $(getAge()),
            "location": "France",
            "activities": [
                "web developper",
                "student"
            ]
        }
    }
    ```

    <a href="https://gael-lopes-da-silva.github.io/portfolio/"><kbd><br>&nbsp;<b>Portfolio</b>&nbsp;<br><br></kbd></a>
    <img align="right" style="width: 37px;" title="Behold the yellow dancing man. Do not question him!" alt="Alas, he went..." src="./assets/yellow_man.gif">
    """

    open("README.md", "w") do file
        write(file, text)
    end

    return 0
end
