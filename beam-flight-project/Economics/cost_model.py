import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

try:
    from core.beam_flight_complete_mission import BeamFlightIntegratedSimulator
except ImportError:
    BeamFlightIntegratedSimulator = None

class DynamicEconomicModel:
    def __init__(self, electricity_cost_per_kwh=0.16):
        self.electricity_rate = electricity_cost_per_kwh
        self.base_infra_amortization = 10000.0  
        self.fixed_consumables = 1500.0        
        
        # ФІЗИЧНІ КОЕФІЦІЄНТИ (РЕАЛЬНИЙ СВІТ)
        self.laser_efficiency_kpd = 0.45       # ККД сучасних волоконних лазерів (45%)
        self.atmospheric_scattering = 0.15     # Втрати на розсіювання в атмосфері (15%)

    def calculate_integrated_cost(self, mass_kg=50, target_power_mw=250):
        if BeamFlightIntegratedSimulator:
            flight_sim = BeamFlightIntegratedSimulator(capsule_mass_kg=mass_kg, target_power_mw=target_power_mw)
            flight_sim.run_full_simulation()
            final_sces_energy_mw = flight_sim.sces_charge_mw
            flight_duration_sec = 45.0  
        else:
            final_sces_energy_mw = target_power_mw
            flight_duration_sec = 45.0

        # Корисна енергія променя
        useful_energy_mws = final_sces_energy_mw * flight_duration_sec
        
        # РЕАЛЬНА ЕНЕРГІЯ З МЕРЕЖІ з урахуванням ККД та розсіювання:
        # Споживання = Корисна енергія / KPD / (1 - Втрати)
        real_energy_mws = useful_energy_mws / self.laser_efficiency_kpd / (1.0 - self.atmospheric_scattering)
        energy_consumed_kwh = (real_energy_mws / 3600.0) * 1000.0
        
        actual_energy_cost = energy_consumed_kwh * self.electricity_rate
        dynamic_plasma_gas_cost = (flight_duration_sec * 0.3) * 50.0  
        
        total_launch_cost = self.base_infra_amortization + self.fixed_consumables + actual_energy_cost + dynamic_plasma_gas_cost
        cost_per_kg = total_launch_cost / mass_kg

        print("\n=======================================================")
        print("     ФІНАНСОВИЙ ЗВІТ (РЕАЛЬНІ ФІЗИЧНІ КОЕФІЦІЄНТИ)     ")
        print("=======================================================")
        print(f" ⏱️ Час роботи лазерів:                  {flight_duration_sec} сек")
        print(f" 🎯 Ефективний ККД лазерної матриці:      {self.laser_efficiency_kpd * 100}%")
        print(f" 🌌 Атмосферні втрати (розсіювання):     {self.atmospheric_scattering * 100}%")
        print(f" ⚡ Спожито з мережі (з урахуванням втрат): {energy_consumed_kwh:.1f} кВт-год")
        print(f" 💵 Собівартість брутто-електроенергії:  ${actual_energy_cost:.2f}")
        print(f" 💰 ЗАГАЛЬНА СОБІВАРТІСТЬ ПУСКУ:          ${total_launch_cost:.2f}")
        print(f" 🚀 РЕАЛЬНА ВАРТІСТЬ ЗА 1 КГ:             ${cost_per_kg:.2f} / кг")
        print("=======================================================\n")
        return total_launch_cost, cost_per_kg

if __name__ == "__main__":
    model = DynamicEconomicModel()
    model.calculate_integrated_cost(mass_kg=50, target_power_mw=250)
