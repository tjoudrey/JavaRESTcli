import os
import click


def make_file_structure(project_name):
    current_path = os.getcwd()
    click.echo("{} to create".format(current_path + project_name))
    os.mkdir(current_path + "/" + project_name)
    os.mkdir(current_path + "/" + project_name + "/src")
    os.mkdir(current_path + "/" + project_name + "/test")
    os.mkdir(current_path + "/" + project_name + "/test/java")
    os.mkdir(current_path + "/" + project_name + "/src/main")
    os.mkdir(current_path + "/" + project_name + "/src/main/java")
    os.mkdir(current_path + "/" + project_name + "/src/main/resources")
    os.mkdir(current_path + "/" + project_name + "/src/main/java/com")
    os.mkdir(current_path + "/" + project_name + "/src/main/java/com/"+project_name)
    os.mkdir(current_path + "/" + project_name + "/src/main/java/com/"+project_name+"/controllers")
    os.mkdir(current_path + "/" + project_name + "/src/main/java/com/"+project_name+"/models")
    os.mkdir(current_path + "/" + project_name + "/src/main/java/com/"+project_name+"/repositories")
    os.mkdir(current_path + "/" + project_name + "/src/main/java/com/"+project_name+"/services")
