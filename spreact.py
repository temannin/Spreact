import requests
import sys
import json
import subprocess
import os
import zipfile

from consolemenu import SelectionMenu

java_depedency_systems = ["Maven", "Gradle"]
languages = ["Java", "Kotlin", "Groovy"]
jvm_versions = ["8", "11", "14"]


def getSelectionResult(list, title, subtitle=None):
    var = SelectionMenu.get_selection(
        list, title=title, subtitle=subtitle, show_exit_option=False)
    return list[var]


class Project():

    name_of_project = input("Name of Project: ")

    artifact_input = input("Artifact group (ex: com.example): ")
    artifact_group = "com.example" if artifact_input == "" else artifact_input

    description = input("Description: ")
    dependency_system = getSelectionResult(
        java_depedency_systems, "Select Java Dependency Manager: ")
    language = getSelectionResult(
        languages, "Select Backend Language Target: ")
    use_typescript = True if input(
        "Use typescript? (y/n): ").lower() == "y" else False

    def __init__(self):
        self.generateSpringProject()
        self.generateReactProject()

    def generateSpringProject(self):
        params = (
            ('type', f'{self.dependency_system.lower()}-project'),
            ('language', f'{self.language.lower()}'),
            ('bootVersion', '2.3.0.RELEASE'),
            ('baseDir', self.name_of_project),
            ('groupId', self.artifact_group),
            ('artifactId', self.name_of_project),
            ('name', self.name_of_project),
            ('description', self.description),
            ('packageName', f'{self.artifact_group}.{self.name_of_project}'),
            ('packaging', "jar"),
            ('javaVersion', '1.8'),
            ('dependencies', 'web'),
        )
        r = requests.get(
            'https://start.spring.io/starter.zip', params=params)

        zip_file_path = f"{self.name_of_project}-api.zip"
        with open(zip_file_path, 'wb') as fd:
            for chunk in r.iter_content(chunk_size=128):
                fd.write(chunk)

        directory_path = f"{self.name_of_project}-api"
        with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
            os.mkdir(directory_path)
            zip_ref.extractall(directory_path)

        os.remove(zip_file_path)

    def generateReactProject(self):
        if (self.use_typescript):
            subprocess.call(["npx", "create-react-app",
                             self.name_of_project.lower(), "--template", "typescript"], shell=True)
        else:
            subprocess.call(["npx", "create-react-app",
                             self.name_of_project.lower()], shell=True)
        os.chdir(self.name_of_project.lower())
        with open("package.json", "r+") as jsonFile:
            data = json.load(jsonFile)
            data["proxy"] = "http://localhost:8080"
            jsonFile.seek(0)  # rewind
            json.dump(data, jsonFile)
            jsonFile.truncate()


def main():
    Project()


if __name__ == "__main__":
    main()
