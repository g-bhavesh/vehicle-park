package com.example.vehiclepark;

import com.example.vehiclepark.model.Vehicle;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

/**
 * The interface Vehicle repository.
 *
 * @author Dhruv Gohil
 */
@Repository
public interface VehicleRepository extends JpaRepository<Vehicle, Long> {}
