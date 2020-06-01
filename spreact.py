import requests
import sys
import json
import subprocess
import os

from consolemenu import SelectionMenu

java_depedency_systems = ["Maven", "Gradle"]
languages = ["Java", "Kotlin", "Groovy"]
jvm_versions = ["8", "11", "14"]


class Project():

    name_of_project = input("Name of Project: ")
    # artifact_group = input("Artifact group (ex: org.tylermanning): ")
    # description = input("Description: ")
    # dependency_system = getSelectionResult(
    #     java_depedency_systems, "Select Java Dependency Manager: ")
    # language = getSelectionResult(
    #     languages, "Select Backend Language Target: ")

    def __init__(self):
        # self.generateSpringProject()
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
        with open("proj.zip", 'wb') as fd:
            for chunk in r.iter_content(chunk_size=128):
                fd.write(chunk)

    def generateReactProject(self):
        subprocess.call(["npx", "create-react-app",
                         self.name_of_project.lower()], shell=True)


def getSelectionResult(list, title, subtitle=None):
    var = SelectionMenu.get_selection(
        list, title=title, subtitle=subtitle, show_exit_option=False)
    return list[var]


def main():
    Project()


if __name__ == "__main__":
    main()
