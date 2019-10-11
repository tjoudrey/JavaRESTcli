import click
import services.directoryService as directoryService
import services.fileWriterService as fileWriter


@click.command()
@click.argument('project_name')
@click.option('--greeting', '-g')
def main(project_name, greeting):
    click.echo("Making {} ...".format(project_name))
    directoryService.make_file_structure(project_name)
    fileWriter.write_pom(project_name)

if __name__ == "__main__":
    main()