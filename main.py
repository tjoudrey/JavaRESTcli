#!/usr/bin/python3

import click
import os
import services.directoryService as directoryService
import services.fileWriterService as fileWriter


@click.command()
@click.option('--generate', '-g', is_flag=True, help="Generate and build a spring server")
@click.option('--service', '-s', nargs=2, help="Generate a service class specifying the project name and service name")
@click.option('--repo', '-r', nargs=2, help="Generate a repository interface specifying the project name and model name")
@click.option('--model', '-m', nargs=3, help="Generate a model specifying the project name, model name and db schema "
                                             "name")
@click.option('--controller', '-c',nargs=2, help="Generate a api controller specifying the project name and model name")
def main(generate, service, repo, model, controller):
    if generate:
        project_name = click.prompt("Input project name")
        database_name = click.prompt("Input database name")
        database_user = click.prompt("Input database username")
        database_pass = click.prompt("Input database password")

        """a cli to generate java REST apis for postgreSQL"""
        click.echo("Making {} ...".format(project_name))
        directoryService.make_file_structure(project_name)

        fileWriter.write_pom(project_name)
        fileWriter.write_application_properties(project_name, database_name)
        fileWriter.write_application_java(project_name)

        os.system("cd "+project_name+"/; mvn install")

    elif model:
        print(model)
        fileWriter.write_model(model[0], model[1], model[2])

    elif repo:
        fileWriter.write_repo(repo[0], repo[1])

    elif controller:
        fileWriter.write_controller(controller[0], controller[1])

    elif service:
        fileWriter.write_service(service[0], service[1])

    else:
        ctx = click.get_current_context()
        click.echo(ctx.get_help())
        ctx.exit()


if __name__ == "__main__":
    main()