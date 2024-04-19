package com.iot.smartparking;

import lombok.Getter;
import lombok.Setter;
import lombok.ToString;
import org.springframework.data.annotation.CreatedDate;
import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;

import java.util.Date;

@Document
@ToString
@Getter
@Setter
public class ParkingOccupancyData {
    @Id
    public String id;

    @CreatedDate
    private Date createdDate;

    public float distance;

    public String unit;

    public int slotId;

    public String floor;



}
