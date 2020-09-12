package com.example.vehiclepark;

import org.hibernate.annotations.CreationTimestamp;
import org.hibernate.annotations.UpdateTimestamp;
import org.springframework.data.annotation.CreatedBy;
import org.springframework.data.annotation.CreatedDate;
import org.springframework.data.annotation.LastModifiedBy;
import org.springframework.data.annotation.LastModifiedDate;
import org.springframework.data.jpa.domain.support.AuditingEntityListener;

import javax.persistence.*;

import java.util.Date;

/**
 * The type Vehicle.
 *
 * @author Dhruv Gohil
 */
@Entity
@Table(name = "vehicles")
@EntityListeners(AuditingEntityListener.class)
public class Vehicle {

    @Id
    @GeneratedValue(strategy = GenerationType.AUTO)
    private long id;

    @Column(name = "vehicle_no", nullable = false)
    private String vehicleNo;

    @Column(name = "vehicle_type", nullable = false)
    private String vehicleType;

    @Column(name = "avg_hours_per_day", nullable = false)
    private long avgHoursPerDay;

  /**
   * Gets id.
   *
   * @return the id
   */
  public long getId() {
        return id;
    }

  /**
   * Sets id.
   *
   * @param id the id
   */
   public void setId(long id) {
        this.id = id;
    }

  /**
   * Gets vehicle no.
   *
   * @return the vehicle no
   */
  public String getVehicleNo() {
        return vehicleNo;
    }

  /**
   * Sets vehicle no.
   *
   * @param vehicleNo the vehicle no
   */
  public void setVehicleNo(String vehicleNo) {
        this.vehicleNo = vehicleNo;
    }

  /**
   * Gets vehicle type.
   *
   * @return the vehicle type
   */
  public String getVehicleType() {
        return vehicleType;
    }

  /**
   * Sets vehicle type.
   *
   * @param vehicleType
   */
  public void setVehicleType(String vehicleType) {
        this.vehicleType = vehicleType;
    }

  /**
   * Gets average hours per day in parking.
   *
   * @return avgHoursPerDay
   */
  public long getAvgHoursPerDay() {
        return avgHoursPerDay;
    }

  /**
   * Sets average hours per day in parking.
   *
   * @param avgHoursPerDay
   */
  public void setAvgHoursPerDay(long avgHoursPerDay) {
        this.avgHoursPerDay = avgHoursPerDay;
    }

    @Override
    public String toString() {
        return "Vehicle {" +
                "id=" + id +
                ", vehicle_no='" + vehicleNo + '\'' +
                ", vehicle_type='" + vehicleType + '\'' +
                ", avg_hours_per_day='" + avgHoursPerDay + '\'' +
                '}';
    }


}
