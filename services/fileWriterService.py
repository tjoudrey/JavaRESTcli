import os
import click

def write_application_properties(project_name, database_name):
    current_path = os.getcwd()
    application_properties = open(current_path + "/" + project_name + "/src/main/resources/application.properties", "w+")
    application_properties.write("spring.datasource.url=jdbc:postgresql://localhost:5432/"+ database_name +"\n\
spring.datasource.username=postgres\n\
spring.datasource.password=postgres\n\
spring.jpa.show-sql=true\n\
    \n\
## Hibernate Properties\n\
# The SQL dialect makes Hibernate generate better SQL for the chosen database\n\
spring.jpa.properties.hibernate.dialect = org.hibernate.dialect.PostgreSQLDialect\n\
    \n\
# Hibernate ddl auto (create, create-drop, validate, update)\n\
spring.jpa.hibernate.ddl-auto = update\n\
    \n\
spring.jpa.properties.hibernate.jdbc.lob.non_contextual_creation=true\n\
")

def write_pom(project_name):
    current_path = os.getcwd()
    pom = open(current_path + "/" + project_name + "/src/main/resources/pom.xml", "w+")
    pom.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n\
<project xmlns=\"http://maven.apache.org/POM/4.0.0\"\n\
         xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\"\n\
         xsi:schemaLocation=\"http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd\">\n\
    <modelVersion>4.0.0</modelVersion>\n\
    <groupId>"+ project_name +"</groupId>\n\
    <artifactId>"+ project_name +"</artifactId>\n\
    <version>1.0-SNAPSHOT</version>\n\
    <packaging>jar</packaging>\n\
    <parent>\n\
\n\
        <groupId>org.springframework.boot</groupId>\n\
        <artifactId>spring-boot-starter-parent</artifactId>\n\
        <version>2.0.5.RELEASE</version>\n\
        <relativePath />\n\
        <!-- lookup parent from reposictory -->\n\
    </parent>\n\
\n\
    <properties>\n\
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>\n\
        <project.reporting.outputEncoding>UTF-8</project.reporting.outputEncoding>\n\
        <java.version>1.8</java.version>\n\
    </properties>\n\
\n\
    <dependencies>\n\
        <dependency>\n\
            <groupId>org.springframework.boot</groupId>\n\
            <artifactId>spring-boot-starter-data-jpa</artifactId>\n\
        </dependency>\n\
        <dependency>\n\
            <groupId>org.springframework.boot</groupId>\n\
            <artifactId>spring-boot-starter-web</artifactId>\n\
        </dependency>\n\
        <dependency>\n\
            <groupId>org.postgresql</groupId>\n\
            <artifactId>postgresql</artifactId>\n\
            <scope>runtime</scope>\n\
        </dependency>\n\
        <dependency>\n\
            <groupId>org.springframework.boot</groupId>\n\
            <artifactId>spring-boot-starter-test</artifactId>\n\
            <scope>test</scope>\n\
        </dependency>\n\
        <dependency>\n\
            <groupId>javax.xml.bind</groupId>\n\
            <artifactId>jaxb-api</artifactId>\n\
            <version>2.3.0</version>\n\
        </dependency>\n\
        <dependency>\n\
            <groupId>org.javassist</groupId>\n\
            <artifactId>javassist</artifactId>\n\
            <version>3.23.1-GA</version>\n\
        </dependency>\n\
    </dependencies>\n\
\n\
    <build>\n\
        <plugins>\n\
            <plugin>\n\
                <groupId>org.springframework.boot</groupId>\n\
                <artifactId>spring-boot-maven-plugin</artifactId>\n\
            </plugin>\n\
        </plugins>\n\
    </build>\n\
</project>")
    pom.close()