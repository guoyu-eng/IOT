package com.iot.smartparking;

import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;

import java.util.List;
import java.util.stream.Collectors;

@Controller
@Slf4j
public class ParkingController {

    @Autowired
    ParkingDataService service;

    @GetMapping("/")
    public String showSignUpForm(Model model) {
        model.addAttribute("parkingData", service.getParkingData());
        return "index";
    }
}
