package com.example.vehiclepark;

import com.example.vehiclepark.exception.ResourceNotFoundException;
import com.example.vehiclepark.model.Vehicle;
import com.example.vehiclepark.VehicleRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import javax.validation.Valid;
import java.util.Date;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * The type Vehicle controller.
 *
 * @author Dhruv Gohil
 */
@RestController
@RequestMapping("/")
public class VehicleController {

  @Autowired
  private VehicleRepository vehicleRepository;

  /**
   * Gets vehicle average park time by vehicle no.
   *
   * @param vehicle_no
   * @return vehicle average park time
   * @throws ResourceNotFoundException the resource not found exception
   */
  @GetMapping("/vehicle/{id}")
  public ResponseEntity<User> getVehicleByNo(@PathVariable(value = "id") Long vehicleNo)
      throws ResourceNotFoundException {
    Vehicle vehicle =
        vehicleRepository
            .findById(vehicleNo)
            .orElseThrow(() -> new ResourceNotFoundException("Vehicle not found on :: " + vehicleNo));
    return ResponseEntity.ok().body(vehicle);
  }
}
