#!/usr/bin/python3

import click
import os
import services.directoryService as directoryService
import services.fileWriterService as fileWriter


@click.command()
@click.argument('project_name')
@click.argument('database_name')
@click.option('--greeting', '-g')
def main(project_name, database_name,  greeting):
    click.echo("Making {} ...".format(project_name))
    directoryService.make_file_structure(project_name)

    fileWriter.write_pom(project_name)
    fileWriter.write_application_properties(project_name, database_name)
    fileWriter.write_application_java(project_name)

    os.system("cd "+project_name+"/; mvn install")

if __name__ == "__main__":
    main()