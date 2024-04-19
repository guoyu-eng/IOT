package com.iot.smartparking;

import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.*;
import java.util.stream.Collectors;

@Service
@Slf4j
public class ParkingDataService {

    @Autowired
    ParkingRepository repo;


    public List<ParkingOccupancyData>  getParkingData(){
        log.info("Getting parking data");
        Map<Integer,List<ParkingOccupancyData>> dataMap = new HashMap<>();
        repo.findAll().forEach( data  ->{
            int slotId = data.getSlotId();
            if(dataMap.get(data.getSlotId()) != null) {
                dataMap.get(data.getSlotId()).add(data);
            } else {
                List<ParkingOccupancyData> list = new ArrayList<>();
                list.add(data);
                dataMap.put(slotId, list);
            }
        });

        dataMap.values().forEach(slot ->{
            System.out.println(slot.size());
            Collections.sort(slot,new Comparator<ParkingOccupancyData>() {
                public int compare(ParkingOccupancyData o1, ParkingOccupancyData o2) {
                    return o2.getId().compareTo(o1.getId());
                }
            });
        });


        List<ParkingOccupancyData> finalVals = dataMap.values().stream().map(slotLists -> {
            return slotLists.stream().findFirst().get();
        }).collect(Collectors.toList());


        System.out.println(finalVals);
        return finalVals;
    }

}
