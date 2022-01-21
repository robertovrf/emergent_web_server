import requests

# function get_config -- gets the running configuration
#response = requests.get("http://localhost:2011/meta/get_config")
#response.text

# function get_all_configs -- get a list of all possible configuration
#response = requests.get("http://localhost:2011/meta/get_all_configs")
#response.text

# function set_config -- set config to a specific configuration
# you should get one of the architectural description and replace the one on following command
# if you just uncomment this following line, chances are it won't work
#requests.post("http://localhost:2011/meta/set_config", json={"config":"|../repository/TCPNetwork.o,/home/roberto/dana//components/net/TCP.o,../repository/request/RequestHandler.o,../repository/app_protocols/HTTPProtocol.o,../repository/http/HTTPHeader1_0.o,../repository/http/handler/GET/HTTPGET.o,/home/roberto/dana//components/io/File.o,../repository/http/handler/DCH/DCHandler.o,../repository/http/util/HTTPUtil.o,/home/roberto/dana//components/data/StringUtil.o,/home/roberto/dana//components/data/adt/List.o,/home/roberto/dana//components/data/adt/HashTable.o,../repository/web_app/Dispatcher.o,../repository/danapedia/DanaPedia.o,../repository/data_layer/DBConnector.o,../repository/database/Database.o,/home/roberto/dana//components/data/mysql/MySQL.o,/home/roberto/dana//components/time/Timer.o,/home/roberto/dana//components/time/Calendar.o,/home/roberto/dana//components/time/DateUtil.o,/home/roberto/dana//components/util/ConfigFile.o,/home/roberto/dana//components/io/TextFile.o,../repository/stream/Stream.o,/home/roberto/dana//components/encoding/Encoder.uri.o|0:net.TCPSocket:1,0:net.TCPServerSocket:1,0:request.RequestHandler:2,2:app_protocols.AppProtocol:3,3:http.HTTPHeader:4,4:http.handler.GET.HTTPGET:5,5:io.File:6,5:http.handler.DCH.DCHandler:7,7:io.File:6,7:io.FileSystem:6,7:http.util.HTTPUtil:8,8:io.FileSystem:6,8:data.StringUtil:9,9:data.adt.List:10,7:data.adt.HashTable:11,7:data.StringUtil:9,7:web_app.Dispatcher:12,12:danapedia.DanaPedia:13,13:data_layer.DBConnector:14,14:database.Database:15,15:data.mysql.MySQL:16,13:data.StringUtil:9,13:time.Timer:17,13:time.Calendar:18,13:time.DateUtil:19,13:util.ConfigFile:20,20:io.TextFile:21,21:io.File:6,20:data.StringUtil:9,20:data.adt.HashTable:11,12:stream.Stream:22,22:data.StringUtil:9,7:encoding.Encoder-uri:23,4:http.util.HTTPUtil:8|"})

# function get_perception -- get the data percieved by the system
response = requests.get("http://localhost:2011/meta/get_perception")
print(response.text)

