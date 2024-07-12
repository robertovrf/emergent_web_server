# Emergent Web Server (EWS) [![DOI](https://zenodo.org/badge/213517358.svg)](https://zenodo.org/badge/latestdoi/213517358)

EWS is an examplar to explore online learning in compositional self-adaptive systems. This repository contains all code required to execute and extend the examplar. We make available a ready-to-use Docker container on Docker Hub. We recommend following the instructions in the "Quick Start" section to quickly set up and execute EWS in a Docker container. We also describe the examplar folder structure, provide a guide on how to compile the different composing parts of the examplar and how to execute it on your machine settings. For more information on the concepts that make up our examplar, we refer the interested reader to check the paper that describes this artefact at https://doi.org/10.1145/3524844.3528079.

## Quick Start

Here we describe the quickest way to get the examplar running. First, we expect you to have Docker installed and configured in your machine. More information on how to install and configure Docker at https://www.docker.com/get-started. Once Docker is ready to be used, we can execute EWS and access an interactive tool to explore EWS API and the available Learning algorithm.

On your terminal, execute our docker image available on Docker Hub:

_$ docker run --name=ews -p 2011-2012:2011-2012 -d robertovrf/ews:1.0_

To check whether the container is running, use _'container ls'_:

_$ docker container ls_

You should now see a list of all executing containers, including EWS. After confirming the container is running, we need to access its terminal to execute EWS. We make available a tool that allows users to interact with EWS using a command prompt.

To get access to the container's terminal:

_$ docker exec -it ews bash_

After typing this command on your terminal, you should get a terminal inside the container. To execute the tool to interact with EWS, type:

_# dana -sp ../repository InteractiveEmergentSys.o_

**NOTE:** The command above should be typed inside the EWS container, inside the _emergent\_web\_server/pal_ folder. 

### Interactive Emergent System

The interactive tool launches EWS. We ask the user to be patient as this may take a little while to start and configure EWS's 42 unique compositions. Once EWS is executing, you'll get access to a command prompt. To access all available commands to interact with EWS API, type:

_sys> help_

You'll get a list of all available commands and a brief description of what each of them does and their expected arguments. For instance, you can list all available compositions using 'get all configs':

_sys> get_all_configs_

The above command will give you a list of 42 compositions. The list contains a set of ID numbers followed by a unique string describing how the web server components are connected to form the available compositions. More information on the architectural description syntax is in the paper. To check the current  webserver composition, use 'get config':

_sys> get_config_

To change from one composition to another, use 'set config':

_sys> set_config 3_

Be careful with the number passed as an argument. Make sure that this is a valid ID number for a composition. Check the list of available compositions (using _get_all_configs_ command). At this point, you can also interact with the web server by opening a web browser and accessing: http://localhost:2012/. You should get a text index.html page. You can check the folder 'emergent\_web\_server/repository/htdocs' to see all available resources that can be accessed through the web server. You can also add your own and create different workload patterns by creating HTTP 1.0 client scripts. As examples, we make available two client scripts responsible to generate different workload patterns, you can find them at 'emergent\_web\_server/ws\_clients'.

### Perception and Learning

Now everything is ready for our interaction with the Perception and Learning modules. The Perception is responsible to collect performance information from the executing web server. After casting some requests to the server from the client scripts, you can get the perception data by using 'get perception' command:

_sys> get_perception_

The above command should return the average response time of all received requests handled by the server. Note that every time 'get perception' is used, the returned data is deleted from the system so that if you type 'get perception' twice in a row, the second time results in empty data as a response. That is when you do not have a continuous stream of requests. If you have a client continually requesting data from the server, the server will continue to monitor its response time and return it when it receives a 'get perception' request.

The average response time is the metric we use in our Learning module to decide which composition is the most suitable to handle the workload pattern the server is processing. To execute the Learning module, use the 'learn' command:

_sys> learn_

The system will require some information before starting learning. The available learning algorithm is a greedy algorithm with a fixed exploration time frame, and it serves as a baseline for comparison with other more advanced learning strategies. The first required information is the size of the observation window in milliseconds. The observation window is the duration of time the learning algorithm takes to observe the executing web server composition before collecting the average response time. The user is free to explore different numbers here, but beware that the bigger the observation window is, the longer the learning process takes, whereas the shorter the observation window is, the higher the probability of the learning algorithm making mistakes. We recommend the number '5000', 5 seconds for the observation window. Second, the learning module asks for an exploration threshold. After the learning algorithm finds the most suitable composition (the exploration phase), it enters the exploitation phase. This phase is maintained until the system gets different perception data, which tells that something has changed in the operating environment. The exploration threshold is the number of times the system detects a difference in the perception data before it triggers the exploration phase again. We recommend the value of 3 for the exploration threshold. Note that the higher this number is, the less sensitive to changes the algorithm becomes, whereas the lower this number is, the more sensitive to changes the algorithm gets (i.e., any disturbance in the collected data can trigger exploration again). Finally, the learning algorithm requires the number of rounds it should execute. Considering the algorithm executes in a command prompt, it is desirable that the learning algorithm finishes execution and the user gets back to the command prompt. Therefore, the round number is the number of iterations in the learning process. We recommend the number 52 for this argument. The learning algorithm takes 42 iterations to explore all possible compositions to determine which one is the most suitable. After that, the algorithm transitions to the exploitation phase. If nothing drastic changes in the operating environment, the algorithm continues to exploit the selected most suitable composition for 10 more rounds before it finishes its execution.

After providinng the learning algorithm with the requested information, the prompt waits until the user presses [ENTER] to start executing the learning algorithm. At this point, we advise the user to start a client script. We recommend the user to start a new terminal and gain access to the docker container using '_$ docker exec -it ews bash_'. Then the user should go to 'ws\_clients' folder:

_# cd ../ws\_clients_

Then list, choose and execute the client scripts:

_# ls_

For listing the folder's content. The following command executes one of the client scripts:

_# dana ClientTextPattern.o_

Once the client is executing, the user can go back to the previous terminal where the _InteractiveEmergentSys.o_ is executing and press [ENTER] to start learning. The learning process will take a little over 3.5 min (if the arguments are 5000 for the observation window, 3 for the exploration threshold and 52 for the number of rounds). The learning algorithm prints the composition it is exploring and the average response time of that particular composition during execution. After exploration phase, the algorithm selects the composition that presented the lowest response time.

## Native Install

The docker image on Docker Hub is the easiest and quickest way to execute the artefact. Some users, however, prefer to clone our codebase and execute it in their machine settings. This could facilitate users to change the artefact and extend it as they please. The following sections describes all the software dependencies and steps you should take to install and run EWS in your machine settings.

### External Dependencies

This artefact requires the Dana programming language [version 251], Python 3.7 and Perl 5 properly installed and configured. Please refer to http://www.projectdana.com/dana/guide/installation for more information on how to install Dana. Also, please refer to https://www.python.org/downloads/  and https://www.perl.org/get.html to install Python and Perl respectively.

The entire artefact was written in Dana. The artefact consists of 42 web server compositions and the entire framework that supports runtime adaptation, collection of response time from the executing server and baseline online learning algorithm. We also make available some Python example code and a Python module to facilitate the interaction with the EWS API. We believe that making available a Python module will drastically reduce the learning curve to explore EWS, considering that Python is a very popular language amongst machine learning practitioners.

 Perl is only used to implement the deflate compression algorithm. In case you do not want to install Perl, all you need to do is to remove _ZLIB.dn_ and _ZLIB.o_ from 'emergent\_web\_server/repository/compression/'. Note that if you remove ZLIB component, you end up removing 14 compositions from the original 42.

### Project Folder Structure

The EWS project has the following folders: _Docker_, _make\_scripts_, _pal_, _python\_scripts_, _repository_ and _ws\_clients_. We describe the contents of each one of them.

* _Docker_: This folder contains the Dockerfile and a bash script used to create the docker image of this artefact.
* _make\_scripts_: This contains all the scripts required to execute 'make.dn'. We use this when we want to compile the project and configure the available compositions for the web server.
* _pal_: The _pal_ folder contains all Dana code responsible to provide the EWS API. This is the main folder of the project and it is also where the _EmergentSys.o_ and _InteractiveEmergentSys.o_ components are located.
* _python\_scripts_: This folder hosts a set of Python scripts that illustrate very simply how one can interact with EWS API.
* _repository_: This is where all the web server components reside. All the components that make the different compositions for the web server is in this folder. In case you want to create different components to extend the number of compositions available for EWS, you will create them in this folder.
* _ws\_clients_: This folder contains all the HTTP 1.0 client scripts to generate workload.

### Make.dn: EWS Building Tool

After cloning the EWS repository and installing its dependencies, the next step is to compile the project. We createdthe make.dn component to facilitate this task. 'make.dn' is a building tool that assist in compiling the entire project. This tool has a set of options and arguments that can be explored to compile EWS in different ways. The first thing we have to do is to compile 'make.dn', in the 'emergent\_web\_server' folder in a terminal type:

_$ dnc make.dn_

To execute 'make.dn' and get a menu of the options and arguments type:

_$ dana make.o_

'make.dn' has two options: "-l" and "-w". All users Linux and MacOS users must use -l. Windows users must use "-w". The users are also presented with a list of arguments that allows them to choose the different compositions that EWS could be composed into. For instance, the argument 'all' allows EWS to have access to all 42 available compositions. The argument 'compression' will produce EWS with only the compression compositions.

_$ dana make.o -l all_

### Executing EWS

Next step is to execute EWS. EWS is loaded and assembled by the EmergentSys.o component. That makes EmergentSys.o an essential component to execute the system. InteractiveEmergentSys.o is the utility that enables users to interact with EWS using a terminal. However, InteractiveEmergentSys.o is not an essential component to execute EWS, because users can interact with EWS through its RESTFul API, InteractiveEmergentSys.o is still the easiest way to interact with EWS. Finally, an important part of executing EWS is the client scripts. The client scripts were developed in Dana, but users can design their client scripts to generate the web server workload. 

#### EmergentSys.o

To execute EmergentSys.o go to _emergent\_web\_server/pal/_ folder and execute:

_$ dana -sp ../repository EmergentSys.o_

#### InteractiveEmergentSys.o:

To execute InteractiveEmergentSys.o go to _emergent\_web\_server/pal/_ folder and execute:

_$ dana -sp ../repository InteractiveEmergentSys.o_

#### Clients:

To execute any of the available clients go to _emergent\_web\_server/ws\_clients/_ folder and execute:

_$ dana ClientTextPattern.o_

or

_$ dana ClientImagePattern.o_


### Python module: PyEWS

More information at: https://github.com/EGAlberts/pyews

## Troubleshooting

Everything that happens to EWS in the Docker container is logged in 'emergent\_web\_server/pal/em.log'. Some of the commands to interact with EWS takes a while to conclude, giving the user the impression that the system has frozen. If that is the case, please check  'em.log' to see if the system threw any exceptions or error messages. Otherwise, it is probably just taking a while to finish executing the command.

For any exceptions found in 'em.log', or for any other problem found in this artefact, please get in contact with us by sending an email to roberto.filho [at] ufsc.br.

Thank you very much for using our artefact.  




