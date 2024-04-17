package com.iot.smartparking;

import lombok.Data;
import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;

@Document
public class ParkingOccupancyData {
    @Id
    public String id;

    public String distance;
}
