# JavaRESTcli
A cli utility to generate a java rest api using spring, hibernate and postgreSQL 

All you need to start is access to a postgreSQL database, maven and java 1.8

run `./main.py` in the tool directory or alias it as it builds the project in the current directory.
Follow the prompts, and then navigate into your new project directory and run `mvn spring-boot:run` to start the new api.

run either `./main.py` or `./main.py --help` for the following

Usage: main.py [OPTIONS]

Options:
  -g, --generate            Generate and build a spring server
  
  -a, --rest                Generate a full service, repo and model pipeline specifying: 
                            
                            project name
                            
                            model name
                            
                            db schema
                            
                            name
                            
  -s, --service             Generate a service class specifying
  
                            project name
                            
                            service name
                            
  -r, --repo                Generate a repository interface specifying
  
                            project
                            
                            name
                            
                            model name
                            
  -m, --model               Generate a model specifying
  
                            project name
                            
                            model name
                            
                            db schema name
                            
  -c, --controller          Generate a api controller specifying
  
                            project name
                            
                            model name
                            
  --help                    Show this message and exit.


