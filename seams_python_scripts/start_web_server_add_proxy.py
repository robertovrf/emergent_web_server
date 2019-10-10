import requests

# Function set_main - starts the web server
requests.post("http://localhost:2011/meta/set_main", json={"comp":"../repository/TCPNetwork.o"})

# Function add_proxy
requests.post("http://localhost:2011/meta/add_proxy", json={"exp":"|../metacom/monitoring/proxies/HTTPProxy.o|*(*:http.handler.GET.HTTPGET[0]:*)|"})

print("web server started, proxy added!")