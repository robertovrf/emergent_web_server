# emergent_web_server

Some notes to help you get started:
We now have a make.dn tool to help us compile and filter undesirable components. So the first thing we need to do once the repo is cloned and the latest version of Dana is downloaded and properly installed is to compile the make.dn. To compile make.dn type: "dnc make.dn -v"
You will also find a folder named "seams_compositions". In this folder you will find two subfolders named "common_node" and "entry_point". These folders hold the configuration files that will guide make.dn to properly compile the project and to filter the unwanted components. This is so that we don't have to duplicate the project into common_node and entry_point (like the previous version of the project was set).
To compile for the entry_point node, please type: "dana make seams_compositions/entry_point_node/four_main_compositions/four_compositions.config"
or if you want to compile for the common_node, please type: "dana make seams_compositions/common_node/four_main_compositions/four_compositions.config"
Ilias, if you are running the system locally, please compile it as a common_node.
To run InteractiveDistributor, go to the metacom folder and type: "dana -sp ../repository/ InteractiveDistributor ../repository/TCPNetwork.o seams_population/10_servers.config"
Note that there is a subfolder in "metacom" named "seams_population". This subfolder holds some configuration files that let our system know which nodes are participating in the system. Please edit them with the IP addresses of your infrastructure.
Ilias, if you are running the system locally, please run with 1_server.config file instead of the 10_servers.config file used in the example.
Again, the config files in "seams_population" need to be updated to point to the right machines. Also, remember to update the danapedia.config file (also in metacom folder) to point to your database machine. You don't have to touch the field "memcached_ep: localhost". 
To run the system to start experimenting with it through a python script instead of running InteractiveDistributor run "dana -sp ../repository EmergentSys.o" in the metacom folder.
You will find a python script in the folder named "seams_python_scripts". Open the script and have a look inside. This script illustrate how you can change from one composition to another, get a list of all available compositions,  get the current composition and get perception data. If you have any questions about the script let me know.  

Oh! We still need to execute the Manager.o and the ESLauncher as we did before.
dana -sp ../repository/ Manager.o
and

dana -sp ../repository/ ESLauncher.o
