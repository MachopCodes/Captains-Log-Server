**Captains Log** is a single page application that allows users to plan their boating trips with tide insights. As an avid sailor, I can attest that leaving with or against the tides can be the deciding factor on completing the leg of a sailing trip before the sun goes down. The inspiration for this application was to give sailors and nautical enthusiasts a place to plan their trips and easilly access information related to tides.

To use Captain's Log, create an account (must be an email address and password > 5 characters long), create a trip (submit a launch date, with city and state you are leaving from). You can then view your trip(s) and select a trip to view details (tidal information) as well as update trip information or delete the trip.

**[Deployed Server Application](https://nautical-trip-planner.herokuapp.com/)** |
**[Client Repository](https://github.com/MachopCodes/Tide_Planner)** |
**[Deployed Client Application](https://machopcodes.github.io/Tide_Planner/)**

**Technologies Used**
- React & React Bootstrap
- JavaScript
- Axios
- CSS

**User Stories**
As an unregistered user I can see the Home Page
As a registered user I can view my upcoming trips
As a registered user I can add trips to my personal trip log
As an unregistered user I can create a User Account
As a registered ser I can update or remove my planned trips
As a registered user I would like to be able to access tidal information related to my trips

**Unsolved Problems & Planned Features**
Encoding the api key into the server side
Develop a component that simultaneously creates a route, fetches and saves tide data into a database on the serverside to minimize interaction with a foreign api.
Develop a method to sort trips by date and auto archive past trips.
Develop a method to join trips (singular launch dates) into one complete journey.
Develop a component to track equipment to log servicing or equipment.
Modify the coordinate table from ALL U.S towns & cities to COASTAL global towns & cities.

**Server Routes**
|Request Type |     Path            |                 Description        |   Auth    |
|-------------|---------------------|------------------------------------|-----------|
| POST        |'sign-up/'           | User Sign Up                       |  Unauth   |
| POST        |'sign-in/'           | User Sign In                       |  Unauth   |
| PATCH       |'change-pw/'         | Change User Password               |  Auth     |
| DELETE      |'sign-out/'          | User Sign Out                      |  Auth     |
| GET         |'trips/'             | Index All Onwed Trips              |  Auth     |
| POST        |'trips/'             | Create Trip                        |  Auth     |
| GET         |'trips/<int:pk>/'    | View Trip                          |  Auth     |
| DELETE      |'trips/<int:pk>/'    | Delete Trip                        |  Auth     |
| PATCH       |'trips/<int:pk>/'    | Update Specific Trip               |  Auth     |
| GET         |'key/'               | Fetch API Key (development)        |  Auth     |
| POST        |'tides/'             | Create Tide resource (development) |  Auth     |
| GET         |'coords/<str:key>/'  | Fetch Longitude and Latitude       |  Auth     |


**Planning, Process and Problem Solving Strategy**

The initial concept for Captain's Log was a log to track all parts of a sail boat to provide maintenance and repair support. As the concept developed, trip planning and access tidal information become an important differentiator and the equipment log was tabled for V1.

The entitiy relationships were initially three resources, a user, a trip and details
![ERD1](https://github.com/MachopCodes/Tide_Planner/blob/master/public/ERD1.PNG)

The project was divided into 6 days each with planned sprints and commits to develop grouped components.
Day 1: Initial Plans and Client/Server Repository deployment
Day 2: Develop & Commit USER Resource CRUD functionality
Day 3: Develop & Commit TRIP Resource CRUD functionality
Day 4: API research and implementation
Day 5: Develop & Commit TRIP Resource CRUD functionality
Day 6: Styling and CSS

During API research and implementation,  [Tides API from RapidAPI](https://rapidapi.com/apihood/api/tides) was identified as the resource for tidal information. Since the  api did not need a server-side application to view so the detail resource, the detail resource was postponed for V2 development. **Tides** required 5 parameters to be given to receive tide information: Timestamp,	Interval,	Duration, Longitude & Latitude. Interval and Duration were hard-coded as 1 day & 60 minutes. Timestamp, longitude & latitude were to be sent from the trip, which did not include longitude and latitude in initial planning. To align with user stories, a resource and routing for coordinates (CoordPair) was developed, which was based on an imported table referencing all U.S towns and cities with longitudes and latitudes. This allows a user to enter a city+state pair and receive coordinates back from the server, which could be used to fetch tides. Below is the final entity relationship ERD of the final project after final planning

![ERD2](https://github.com/MachopCodes/Tide_Planner/blob/master/public/ERD1.PNG)
