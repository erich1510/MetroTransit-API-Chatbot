import requests
import json

print("I spent way too much time dealing with JSON to print exactly what was wanted, so I just went ahead and only did the raw output of the API, sorry")

def parseJSON(response):
    json_data = json.loads(response.text)
    for (k) in json_data:
        print (k)

route = raw_input("Which bus route are you taking? ")
directions = (requests.get('http://svc.metrotransit.org/NexTrip/Directions/{}?format=json'.format(route)))
parseJSON(directions)


direction  = raw_input("Which direction are you traveling on route {}? (Enter number) ".format(route))
stops = requests.get('http://svc.metrotransit.org/NexTrip/Stops/{}/{}?format=json'.format(route, direction))
parseJSON(stops)

stop = raw_input("Which stop are you at on route {}? (Enter code) ".format(route))
output = requests.get('http://svc.metrotransit.org/NexTrip/{}/{}/{}?format=json'.format(route, direction, stop))
print (output.text)
parseJSON(output)





        # def getDirections (route):
        #     url = 'http://svc.metrotransit.org/NexTrip/Directions/{}?format=json'.format(route)
        #     response = createRequest(url)
        #     output = castDict(response)
        #     return output
        #     def createRequest(url):
        #         parse = requests.get(url)
        #         return parse
        #         pass
        #         def castDict(response):
        #             response.json()
        #             output = json.loads(response)
        #             for keys, values in output.items():
        #                 print (keys) + ' for ' + (values)
        #                 pass
        #                 def getStops(route, direction):
        #                     url = 'http://svc.metrotransit.org/NexTrip/Stops/{}/{}?format=json'.format(route, direction)
        #                     response = createRequest(url)
        #                     output = castDict(response)
        #                     return output
        #                     def getTimepointDepartures(route, direction, stop):
        #                         url = 'http://svc.metrotransit.org/NexTrip/{}/{}/{}?format=json'.format(route, direction, stop)
        #                         response = createRequest(url)
        #                         output = castDict(response)
        #                         return output
        #                         r = input("Which bus route are you taking?")
        #                         dOptions = getDirections(r)
        #                         d = input("Which direction are you traveling on route ' + r +  '? (Enter number)")
        #                         castDict(dOptions)
        #                         sOptions = getStops(d)
        #                         s = input("Which stop will you depart from? (Enter stop code)")
        #                         castDict(sOptions)
        #                         print (getTimepointDepartures)
