import serial
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
uri = ("mongodb+srv://digivj05:ypvFt1gqYqJnZW8f@cluster0.esdatxw.mongodb.net/?retryWrites=true&w=majority&appName"
       "=Cluster0")
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
db = client["IOT_APP_DATA"]
collection = db["parkingOccupancyData"]
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
# Serial port configuration
ser = serial.Serial('/dev/rfcomm0', baudrate=9600)

while True:
    try:
        # Attempt to read data from serial port
        data = ser.readline().decode('utf-8').strip()
        
        # Check if data is not empty
        if data:
            print("Received:", data)
	    collection.insert_one({"distance": data, "unit": "inches" }) 	
    
    except serial.SerialException:
        # Handle serial exception (timeout)
        print("No data received within timeout period")
    
    # Add a delay to prevent busy looping
    time.sleep(0.1)
