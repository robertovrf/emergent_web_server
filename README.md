# Emergent Web Server (EWS)

EWS is an examplar to explore online learning in compositional self-adaptive systems. This repository contains all code required to execute and extand the examplar. We also make available a ready-to-use docker container on Docker Hub. To execute the container, please follow the instructions on the "Quick Start" section. We also describe the examplar folder structure, provide a guide on how to compile the different composing parts of the examplar and how to execute it on your own machine settings. For more information on the concepts that make up our examplar, we refer our reader to check the paper that describes this artefact (**NOTE**: we'll add a link to the paper as soon as it gets published).

## Quick Start

Here we describe the quickest way to get the examplar running. For starters, we expect you to have Docker installed and configured in your machine. More information on how to install and configure Docker at https://www.docker.com/get-started. Once Docker is ready to be used, we can execute EWS and get access to an interactive tool to explore EWS API and Learning module.

On your terminal, execute our docker image available on Docker Hub:

_$ docker run --name=ews -p 2011-2012:2011-2012 -d robertovrf/ews:1.0_

To check whether the container is running, use _'container ls'_:

_$ docker container ls_

You should now see a list of all executing containers including EWS. After confirming the container is running, we need to get access to its terminal to execute our web server. We make available a tool that allows users to interact with EWS using a command prompt.

To get access to the container's terminal:

_$ docker exec -it ews bash_

After typing this command on your terminal, you should get a terminal inside the container. To execute the tool to interact with EWS, type:

_$ dana -sp ../repository InteractiveEmergentSys.o_

The tool should start EWS. We ask you to be patient as this may take a little while to start and configure the 42 unique compositions of the EWS. Once EWS is up and running you'll get access to a terminal. For all the available commands to interact with EWS, type:

_sys> help_

You'll get a list of all available commands and a brief description of what each of them do and their expected arguments. For instance, you can list all the available compositions using the command 'get all configs':

_sys> get_all_configs_

This will give you a list of 42 compositions. The compositions are presented with an ID number followed by a unique string describing the compositions' components and how they are connected to each other. More information on the architectural description syntax is given later on in this document. To check the current composition the web server is in, use the 'get config' command:

_sys> get_config_

To change from one composition to another, use 'set config':

_sys> set_config 3_

Be careful with the number passed as an argument. Ensure that this is a valid ID number for a composition by checking the list of available compositions (using _get_all_configs_ command). At this point, you can also interact with the web server by opening a web browser and accessing: http://localhost:2012/. You should get a text index.html page. You can check the folder 'emergent_web_server/repository/htdocs' to see all available resources that can be accessed through the web server. You can also add your own and create different workload patterns by creating HTTP 1.0 client scripts. As examples, we make available two client scripts responsible to generate different workload patterns, you can find them at 'emergent_web_server/ws_clients'.

Now everything is ready to experiment with the Perception and Learning modules. The Perception is responsible to collect performance information from the executing web server. After casting some requests to the server, you can get the perception data by using 'get perception' command:

_sys> get_perception_

This should return the avarage response time of all received requests handled. Note that, every time 'get perception' is used the returned data is deleted from the system, so that if you type 'get perception' twice in a row, the second time you'll get empty data as response. 

The average response time is the metric we use in our Learning module to decide which composition is the most suitable to handle the workload pattern the server is processing. To execute the Learning module, use the 'learn':

_sys> learn_

The system will require some information before start learning. The available learning algorithm is a greedy algorithm with fixed exploration time frame and it serves as a base for comparison with other more advanced learning strategies. The first is the size of the observation window in milliseconds. The observation window is the time the learning algorithm will take to observe the executing web server composition before collecting the perception data (in our case, average response time). The user is free to explore different numbers here, but beware that the bigger the observation window is the longer the learning process takes and the shorter the observation window is the higher the probability of learning making mistakes when choosing the most appropriate composition. Here, we recommend the number '5000' that is 5 seconds of observation window. Second, the learning module will ask for a exploration threshold. After learning is complete, and the system finds the best composition, it enters theexploitation phase. This phase is maintained until the system gets different perception data, which tells it that something has changed in the system's operating environment. The exploration threshold is the number of times that the system has to notice a difference in the perception data beofre it triggers the exploration phase again. We recommend the value 3 for exploration threshold. Finally, the learning module will require the number of rounds. Considering the learning is being executed 




