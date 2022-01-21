# Emergent Web Server (EWS)

EWS is an examplar to explore online learning in compositional self-adaptive systems. This repository contains all code required to execute and extend the examplar. We make available a ready-to-use docker container on Docker Hub. To execute the container, please follow the instructions on the "Quick Start" section. We also describe the examplar folder structure, provide a guide on how to compile the different composing parts of the examplar and how to execute it on your own machine settings. For more information on the concepts that make up our examplar, we refer the interested reader to check the paper that describes this artefact (**NOTE**: we'll add a link to the paper as soon as it gets published).

## Quick Start

Here we describe the quickest way to get the examplar running. For starters, we expect you to have Docker installed and configured in your machine. More information on how to install and configure Docker at https://www.docker.com/get-started. Once Docker is ready to be used, we can execute EWS and get access to an interactive tool to explore EWS API and the Learning module.

On your terminal, execute our docker image available on Docker Hub:

_$ docker run --name=ews -p 2011-2012:2011-2012 -d robertovrf/ews:1.0_

To check whether the container is running, use _'container ls'_:

_$ docker container ls_

You should now see a list of all executing containers including EWS. After confirming the container is running, we need to get access to its terminal to execute EWS. We make available a tool that allows users to interact with EWS using a command prompt.

To get access to the container's terminal:

_$ docker exec -it ews bash_

After typing this command on your terminal, you should get a terminal inside the container. To execute the tool to interact with EWS, type:

_# dana -sp ../repository InteractiveEmergentSys.o_

### Interactive Emergent System

The interactive tool should start EWS. We ask you to be patient as this may take a little while to start and configure the 42 unique compositions of the EWS. Once EWS is up and running you'll get access to a terminal. To access all available commands to interact with EWS, type:

_sys> help_

You'll get a list of all available commands and a brief description of what each of them do and their expected arguments. For instance, you can list all the available compositions using 'get all configs':

_sys> get_all_configs_

This will give you a list of 42 compositions. The compositions are presented with an ID number followed by a unique string describing the compositions' components and how they are connected to each other. More information on the architectural description syntax is given later in this document. To check the current composition the web server is in, use 'get config':

_sys> get_config_

To change from one composition to another, use 'set config':

_sys> set_config 3_

Be careful with the number passed as an argument. Ensure that this is a valid ID number for a composition by checking the list of available compositions (using _get_all_configs_ command). At this point, you can also interact with the web server by opening a web browser and accessing: http://localhost:2012/. You should get a text index.html page. You can check the folder 'emergent\_web\_server/repository/htdocs' to see all available resources that can be accessed through the web server. You can also add your own and create different workload patterns by creating HTTP 1.0 client scripts. As examples, we make available two client scripts responsible to generate different workload patterns, you can find them at 'emergent\_web\_server/ws\_clients'.

### Perception and Learning

Now everything is ready for our experiment with the Perception and Learning modules. The Perception is responsible to collect performance information from the executing web server. After casting some requests to the server, you can get the perception data by using 'get perception' command:

_sys> get_perception_

This should return the avarage response time of all received requests handled by the server. Note that every time 'get perception' is used the returned data is deleted from the system, so that if you type 'get perception' twice in a row, the second time you'll get empty data as response. That is if you do not have a continue stream of requests. If you have a client continually requesting data from the server, the server will continue to monitor its response time and return it when it receives a 'get perception' request.

The average response time is the metric we use in our Learning module to decide which composition is the most suitable to handle the workload pattern the server is processing. To execute the Learning module, use the 'learn' command:

_sys> learn_

The system will require some information before start learning. The available learning algorithm is a greedy algorithm with fixed exploration time frame and it serves as a baseline for comparison with other more advanced learning strategies. The first required information is the size of the observation window in milliseconds. The observation window is the time the learning algorithm takes to observe the executing web server composition before collecting the average response time of the executing composition. The user is free to explore different numbers here, but beware that the bigger the observation window is, the longer the learning process takes; whereas the shorter the observation window is, the higher the probability of learning making mistakes when deciding for the most suitable composition. Here, we recommend the number '5000', 5 seconds of observation window. Second, the learning module asks for an exploration threshold. After learning is complete, and the system finds the best composition, the algorithm enters the exploitation phase. This phase is maintained until the system gets different perception data, which tells it that something has changed in the system's operating environment. The exploration threshold is the number of times that the system has to detect a difference in the perception data before it triggers the exploration phase again. We recommend the value 3 for exploration threshold. Note that the higher this number is, the less  sensible to changes the algorithm becomes; whereas, the lower this number is, the more sensible it gets (i.e., any disturbance in the collected data can trigger exploration again). Finally, the learning module requires the number of rounds it should execute. Considering the learning is being executed in a command prompt, it is desireble that learning process ends and the user is brought back to the command prompt to futher explore the interaction with the server. Therefore, the round number is the number of times the learning process executes. We recommend the number 52 for this argument. The learning algorithm takes 42 interactions to explore all possible compositions to determine which one is the most suitable, after that the algorithm transitions to the exploitation phase, if nothing drastic changes in the operating environment, it continues to exploit the selected most suitable composition for 10 more rounds before it finishes its execution.

After providinng the learning module with the requested information, the prompt waits until the user presses [ENTER] to start executing the learning algorithm. At this point, we advise the user to start a client script. We recommend the user to start a new terminal and gain access to the docker container using '_$ docker exec -it ews bash_'. Then the user should go to 'ws\_clients' folder:

_# cd ../ws\_clients_

Then list, choose and execute the client scripts:

_# ls_

_# dana ClientTextPattern.o_

Once the client is executing, the user can go back to the previous terminal where the _InteractiveEmergentSys.o_ is executing and press [ENTER] to start learning. The learning process will take a little over 3.5 min (if the arguments are 5000 for the observation window, 3 for the exploration threshold and 52 for the number of rounds). The learning algorithm prints the composition it is exploring and the average response time of that particular composition during all its execution, after exploration phase, the algorithm selects the composition that presented the lowest response time.

## Native Install

The docker image on Docker Hub is the easiest and quicker way to execute the artefact. Some users, however, prefer to clone our codebase and install and execute it in your own machine settings. This could give you a more in-depth learning experience of our artefact. It also allows you to change it and extend it as you please. The following sections describes all the software dependencies and all the steps you should take to install and run EWS in your own machine settings. Here we also provide an overview of the main concepts that you need to know before extending or changing this artefact.

### External Dependencies

This artefact requires the Dana programming language [version 251], Python 3.7 and Perl 5 properly installed and configured. Please refer to http://www.projectdana.com/dana/guide/installation for more information on how to install Dana. Also, please refer to https://www.python.org/downloads/  and https://www.perl.org/get.html to install Python and Perl respectively.

The entire artefact was written in Dana, that comprises of the web server itself and the entire framework that allows the runtime adaptation of server, the collection of response time from the executing server and the baseline learning algorithm available. We also make available some Python example code and a module to facilitate the interaction with the EWS API. Since Python is a very popular language amongst machine learning practitioners, we believe that making available a python module will drastically reduce the learning curve to use and explore EWS. Perl is only used to implement the deflate compression algorithm. In case you do not want to install Perl, all you need to do is to remove _ZLIB.o_ from 'emergent\_web\_server/repository/compression/'. Note that if you remove ZLIB component, you end up removing 14 compositions.

### Project Folder Structure

The EWS project has the following folders: _Docker_, _make\_scripts_, _pal_, _python\_scripts_, _repository_ and _ws\_clients_. Next we describe the contents of each one of them.

* _Docker_: This folder contains the Dockerfile and a bash script used to create the docker image of this artefact. You can find more information on how to create the docker image of this artefact later on in this document.
* _make\_scripts_: This contains all the scripts required to execute make.dn. We use this when we want to compile the project and configure the available compositions for the web server.
* _pal_: The _pal_ folder contains all Dana code responsible to provide the EWS API. This is the main folder of the project and it is also where the _EmergentSys.o_ and _InteractiveEmergentSys.o_ components are located.
* _python\_scripts_: This folder hosts a set of Python scripts that illustrate very simply how one can interact with EWS API.
* _repository_: This is where all the web server components reside. All the components that make the different compositions for the web server is in here. In case you want to create different components to extend the number of compositions available for EWS, you will create them in this folder.
* _ws\_clients_: This folder contains all the HTTP 1.0 client scripts to generate workload.

### Make.dn: EWS Building Tool

After cloning the EWS repository and installing the dependencies, the next step is to compile the project. For that we have the make.dn component. 'make.dn' is a building tool that assist in compiling the entire project. This tool has a set of options and arguments that can be explored to compile EWS in different ways. The first thing we have to do is to compile 'make.dn', in the 'emergent\_web\_server' folder in a terminal type:

_$ dana make.dn_

To execute 'make.dn' and get a menu of the options and arguments type:

_$ dana make.o_

'make.dn' has two options: "-l" and "-w". All users Linux and MacOS users must use -l. Windows users must use "-w". The users are also presented with a list of arguments that allow them to choose the different compositions that EWS could be composed into. For instance, the argument 'all' allows EWS to have access to all 42 available compositions. The argument 'compression' will produce EWS with only the compression compositions.

_$ dana make.o -l all_

### Executing EWS



#### EmergentSys.o

#### InteractiveEmergentSys.o:

#### Clients:



## EWS API

### Architetural Descriptions

### The API


### Python Example Scripts


### Python module: PyEWS

More information on: https://github.com/EGAlberts/pyews

## Creating Docker Image

To create...

## Troubleshooting

Everything that happens to the EWS is logged in the file 'em.log' in the folder 'emergent\_web\_server/pal/em.log'. Some of the commands to interact with EWS takes a little while to conclude giving the user the impression that the system froze. If that is the case, please check the em.log to see if the system threw any exceptions. If not, it's probably just taking a little while to execute the command.

For any exceptions found in the em.log, or for any other problem found in this artefct, please get in contact with us by emailing to robertovito [at] ufg.br.


Thank you very much for using our artefact.  




