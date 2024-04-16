import serial
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
uri = ("mongodb+srv://digivj05:ypvFt1gqYqJnZW8f@cluster0.esdatxw.mongodb.net/?retryWrites=true&w=majority&appName"
       "=Cluster0")
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
db = client["IOT_APP_DATA"]
collection = db["parking_occupancy_data"]
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
# Serial port configuration
ser = serial.Serial('/dev/rfcomm0', baudrate=9600)

while True:
    if ser.in_waiting > 0:
        # Read data from serial port
        data = ser.readline().decode('utf-8').strip()
        print("Received:", data)

        # Insert data into MongoDB
        collection.insert_one({"parking_occupancy_data": data})
