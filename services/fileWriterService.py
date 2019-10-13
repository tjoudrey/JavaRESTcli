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
    pom = open(current_path + "/" + project_name + "/pom.xml", "w+")
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

def write_application_java(project_name):
    current_path = os.getcwd()
    application_java = open(current_path + "/" + project_name + "/src/main/java/com/"+project_name+"/Application.java", "w+")
    application_java.write("package com."+project_name+";\n\
    \n\
import org.springframework.boot.SpringApplication;\n\
import org.springframework.boot.autoconfigure.SpringBootApplication;\n\
    \n\
@SpringBootApplication\n\
public class Application {\n\
    \n\
    public static void main(String[] args) {\n\
        SpringApplication.run(Application.class, args);\n\
    }\n\
}"
    )


def write_model(project_name, model_name, schema):
    current_path = os.getcwd()
    model = open(current_path+"/"+model_name.title()+".java", "w+")
    model.write(
"com."+project_name+".models;\n\
import javax.persistence.*;\n\
@Entity\n\
@Table(name = \""+model_name+"\", schema = \""+schema+"\")\n\
public class "+model_name+" {\n\
\n\
    @Id\n\
    @GeneratedValue(strategy = GenerationType.AUTO)\n\
    @Column(name=\"id\", unique = true)\n\
    private long id;\n\
\n\
     @Column(name=\"created_on\")\n\
    private ZonedDateTime created_on;\n\
\n\
    public "+model_name+"() {\n\
    this.setCreated_on(ZonedDateTime.now());\n\
    }\n\
\n\
    public long getId() {\n\
        return id;\n\
    }\n\
\n\
    public void setId(long id) {\n\
        this.id = id;\n\
    }\n\
\n\
    public ZonedDateTime getCreated_on() {\n\
        return created_on;\n\
    }\n\
"
            )


def write_repo(project_name, model_name):
    current_path = os.getcwd()
    model = open(current_path + "/" + model_name.title()+"Repository.java", "w+")
    model.write("\n\
package com."+project_name+".repositories;\n\
\n\
import com."+project_name+".models."+model_name.title()+";\n\
import org.springframework.data.jpa.repository.JpaRepository;\n\
import org.springframework.stereotype.Repository;\n\
\n\
@Repository\n\
public interface ""Repository extends JpaRepository<"+model_name.title()+", Long> {\n\
}")


def write_controller(project_name, model_name):
    current_path = os.getcwd()
    controller = open(current_path + "/" + model_name.title() + "Controller.java", "w+")
    controller.write("\n\
package com."+project_name+".controllers;\n\
                     \n\
import com.forte."+project_name+".models."+model_name+";\n\
import com.forte."+project_name+".repositories."+model_name+"Repository;\n\
import org.springframework.beans.factory.annotation.Autowired;\n\
import org.springframework.web.bind.annotation.*;\n\
    \n\
@RestController\n\
@RequestMapping(\"/api\")\n\
public class "+model_name.title()+"Controller {\n\
    \n\
    @Autowired\n\
    "+model_name.title()+"Repository "+model_name.lower()+"Repository;\n\
    \n\
    \n\
    @GetMapping(\"/"+model_name.lower()+"\")\n\
    public List<"+model_name.title()+"> getAll"+model_name.title()+"() {\n\
        return "+model_name.lower()+"Repository.findAll();\n\
    }\n\
        \n\
    @GetMapping(\"/"+model_name.lower()+"/{id}\")\n\
    public "+model_name.title()+" get"+model_name.title()+"(@PathVariable(value = \"id\") Long id){\n\
        "+model_name.title()+" "+model_name.lower()+" = new "+model_name.title()+"();\n\
        return "+model_name.lower()+"Repository.findById(id).orElse("+model_name.lower()+");\n\
    }\n\
            \n\
    @PostMapping(\"/"+model_name.lower()+"\")\n\
    public void set"+model_name.title()+"() throws MessagingException {\n\
        "+model_name.title()+" "+model_name.lower()+" = new "+model_name.title()+"();\n\
        "+model_name.lower()+"Repository.save("+model_name.lower()+");\n\
    }\n\
    \n\
    @DeleteMapping(\"/"+model_name.title()+"\")\n\
    public void delete"+model_name.title()+"(Long id) {\n\
        "+model_name.lower()+"Repository.deleteById(id);\n\
    }\n\
}\n\
    ")


def write_service(project_name, service_name):
    current_path = os.getcwd()
    service = open(current_path + "/" + service_name.title() + "Controller.java", "w+")
    service.write("\n\
package com."+project_name+".services;\n\
\n\
public class "+service_name.title()+"Service {\n\
private static "+service_name.title()+"Service INSTANCE;\n\
    \n\
    private "+service_name.title()+"Service() {\n\
    }\n\
    \n\
    public static "+service_name.title()+""+service_name.title()+" getInstance(){\n\
    if (INSTANCE == null) {\n\
        INSTANCE = new "+service_name.title()+"Service();\n\
    }\n\
    return INSTANCE;\n\
    }\n\
                                                "


        )

