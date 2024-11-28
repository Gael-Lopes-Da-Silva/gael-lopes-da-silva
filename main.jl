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
        "message": "I dost extend a hearty welcome to thee upon mine profile page",
        "informations": {
            "name": "Gaël LOPES DA SILVA",
            "age": $(getAge()),
            "location": "The fair realm of France",
            "class": "high sorcerer",
            "specialisation": "tamer of the digital realm"
            "job": [
                "Web Developper",
                "Student"
            ]
        }
    }
    ```

    <a href="https://gael-lopes-da-silva.github.io/portfolio/"><kbd><br>&nbsp;<b>Portfolio</b>&nbsp;<br><br></kbd></a>
    <img align="right" style="width: 37px;" title="Behold yon man clad in yellow, who doth dance with mirth. Question him not, fair sirs." alt="Alas, he hath departed..." src="./assets/yellow_man.gif">
    """

    open("README.md", "w") do file
        write(file, text)
    end

    return 0
end
