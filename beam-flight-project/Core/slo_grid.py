"""
Beam-Flight Project - Satellite Orbit (SLO) Grid Simulation
Models the two-stage propulsion profile and the Oasis Protocol energy surplus.
"""

import math

class SLOGridSimulation:
    def __init__(self):
        # Satellites Configuration
        self.total_satellites = 90
        self.sat_continuous_generation_mw = 60.0  # 60 MW from solar arrays
        self.capsule_required_power_mw = 250.0   # 250 MW clean at receiver
        self.laser_efficiency = 0.45             # 45% OPA Fiber Laser efficiency
        self.mirror_loss = 0.05                  # 5% jitter loss
        
        # Flight Profile Constants
        self.t_ground_phase = 45.0               # Ground laser duration (s)
        self.t_satellite_phase = 78.5            # Satellite laser acceleration duration (s)
        self.altitude_handover_m = 12000.0       # Handover at 12 km
        self.altitude_cruise_m = 110000.0        # Cruise at 110 km
        
    def calculate_gross_transmission_power(self) -> float:
        """Calculates raw electrical power required by a satellite to project 250MW onto the capsule."""
        net_efficiency = self.laser_efficiency * (1.0 - self.mirror_loss)
        return self.capsule_required_power_mw / net_efficiency

    def run_orbital_energy_profile(self, active_missions_simultaneous: int = 1):
        """Simulates the energy network state during active capsule acceleration by the orbital echelon."""
        # Total continuous power harvested by the 90-satellite ring
        total_harvested_power_gw = (self.total_satellites * self.sat_continuous_generation_mw) / 1000.0
        
        # Power consumed by active tracking/acceleration satellites
        gross_sat_demand_mw = self.calculate_gross_transmission_power()
        total_sat_drain_gw = (active_missions_simultaneous * gross_sat_demand_mw) / 1000.0
        
        # Oasis Protocol surplus calculation
        oasis_surplus_gw = total_harvested_power_gw - total_sat_drain_gw
        
        print("=== BEAM-FLIGHT ORBITAL GRIDSYSTEMS (SLO) AUDIT ===")
        print(f"Total Orbital Echelon Generation : {total_harvested_power_gw:.2f} GW")
        print(f"Ground-to-Sat Handover Boundary  : {self.altitude_handover_m / 1000.0:.1f} km")
        print(f"Sat Propulsion Execution Window  : {self.t_satellite_phase:.1f} seconds (from 12km to {self.altitude_cruise_m/1000.0:.1f}km)")
        print(f"Single Satellite Peak Bus Load   : {gross_sat_demand_mw:.2f} MW (at 100 kV HTS Bus)")
        print(f"Simultaneous Active Cape Launches: {active_missions_simultaneous}")
        print(f"Oasis Protocol Baseload Export   : {oasis_surplus_gw:.2f} GW to Ground Rectennas (5.8 GHz)")
        print("====================================================")
        
        return {
            "harvested_gw": total_harvested_power_gw,
            "sat_drain_gw": total_sat_drain_gw,
            "oasis_export_gw": oasis_surplus_gw
        }

if __name__ == "__main__":
    sim = SLOGridSimulation()
    # Simulate a standard single-capsule launch scenario
    sim.run_orbital_energy_profile(active_missions_simultaneous=1)
