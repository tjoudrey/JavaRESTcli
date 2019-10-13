#!/usr/bin/python3

import click
import os
import services.directoryService as directoryService
import services.fileWriterService as fileWriter


@click.command()
@click.option('--generate', '-g', is_flag=True, help="Generate and build a spring server")
@click.option('--rest', '-a', nargs=3, help="Generate a full service, repo and model pipeline specifying: \n"
                                                             "project name\n"
                                                             "model name\n"
                                                             "db schema name")
@click.option('--service', '-s', nargs=2, help="Generate a service class specifying\n"
                                               "project name\n"
                                               "service name")
@click.option('--repo', '-r', nargs=2, help="Generate a repository interface specifying\n"
                                            "project name\n"
                                            "model name")
@click.option('--model', '-m', nargs=3, help="Generate a model specifying\n"
                                             "project name\n"
                                             "model name\n"
                                             "db schema name")
@click.option('--controller', '-c',nargs=2, help="Generate a api controller specifying\n"
                                                 "project name\n"
                                                 "model name")
def main(generate, rest, service, repo, model, controller):
    if generate:
        project_name = click.prompt("Input project name")
        db_local = click.prompt("Is your db local? (y/yes or n/no)")
        if db_local == "no" or db_local == "n":
            database_url = click.prompt("Input database <url:port>")
        else:
            database_url = "localhost:5432"
        database_name = click.prompt("Input database name")
        database_user = click.prompt("Input database username")
        database_pass = click.prompt("Input database password")
        model = click.prompt("Would you like a rest pipeline to be defined? (Input a name or press enter to skip)")
        schema = click.prompt("what is the db schema for this?")


        """a cli to generate java REST api for postgreSQL"""
        click.echo("Making {} ...".format(project_name))
        directoryService.make_file_structure(project_name)

        fileWriter.write_pom(project_name)
        fileWriter.write_application_properties(project_name, database_name, database_url)
        fileWriter.write_application_java(project_name)

        if model != "":
            fileWriter.write_model(project_name, model, schema, project_name+"/src/main/java/com/" + project_name + "/models")
            fileWriter.write_repo(project_name, model, project_name+"/src/main/java/com/" + project_name + "/repositories")
            fileWriter.write_controller(project_name, model, project_name+"/src/main/java/com/" + project_name + "/controllers")

        os.system("cd "+project_name+"/; mvn install")

    elif rest:
        fileWriter.write_model(rest[0], rest[1], rest[2], "src/main/java/com/"+rest[0]+"/models")
        fileWriter.write_repo(rest[0], rest[1], "src/main/java/com/"+rest[0]+"/repositories")
        fileWriter.write_controller(rest[0], rest[1], "src/main/java/com/"+rest[0]+"/controllers")

    elif model:
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