package com.iot.smartparking;

import org.springframework.data.mongodb.repository.MongoRepository;

import java.util.List;


public interface ParkingRepository extends MongoRepository<ParkingOccupancyData,Long> {
  List<ParkingOccupancyData> findAll();
}
