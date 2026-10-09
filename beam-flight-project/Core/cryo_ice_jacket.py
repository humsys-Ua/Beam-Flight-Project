"""
Beam-Flight Project - Cryogenic "Ice Jacket" Thermal Control Simulator
Models dual-circuit liquid hydrogen (LH2) cooling channels inside the tungsten mirror matrix.
"""

import math
import matplotlib.pyplot as plt

class CryoIceJacketSimulator:
    def __init__(self):
        # Фізичні параметри вольфрамової дзеркальної матриці "Брюхо"
        self.mirror_mass_kg = 45.0          # Вага оптичної матриці обшивки
        self.tungsten_heat_capacity = 130.0 # Питома теплоємність вольфраму (Дж/кг*К)
        self.mirror_temperature_c = 20.0    # Стартова температура на Землі (20°C)
        self.melt_temperature_c = 3422.0    # Точка плавлення вольфраму (критична межа)
        
        # Параметри кріогенного контуру "Льодової сорочки"
        self.lh2_flow_rate_kgs = 3.01       # Витрата водню зі специфікації LTHE (кг/с)
        self.lh2_inlet_temp_c = -252.87     # Температура рідкого водню на вході
        self.lh2_heat_capacity = 14304.0    # Колосальна теплоємність водню (Дж/кг*К)
        
        # Термічні навантаження місії (Phase 1)
        self.laser_power_mw = 250.0         # Потужність променя наземного комплексу
        self.mirror_absorption_rate = 0.002 # Матриця відбиває 99.8% світла, поглинає лише 0.2%
        
        # Списки для збереження графіку телеметрії
        self.timeline = []
        self.surface_temps = []
        self.lh2_cooling_power_mw = []

    def run_thermal_simulation(self, flight_duration_sec=45.0):
        print("=== ЗАПУСК ТЕРМОДИНАМІЧНОГО СИМУЛЯТОРА КРІОГЕННОЇ «ЛЬОДОВОЇ СОРОЧКИ» ===")
        
        current_time = 0.0
        dt = 0.5  # Крок інтегрування — пів секунди
        
        # Розрахунок теплового потоку від лазера, який вбирає дзеркало (МВт -> Вт)
        laser_heat_flux_watts = (self.laser_power_mw * 1e6) * self.mirror_absorption_rate # 500,000 Вт постійно
        
        while current_time <= flight_duration_sec:
            # 1. Фізика аеродинамічного нагріву від тертя плазми (зростає до 25-ї секунди у стратосфері)
            if current_time <= 25.0:
                plasma_heat_flux_watts = (current_time / 25.0) * 350000.0
            else:
                # Падає при виході у вакуум мезосфери/термосфери
                plasma_heat_flux_watts = max(10000.0, 350000.0 - ((current_time - 25.0) * 15000.0))
                
            total_incoming_heat_watts = laser_heat_flux_watts + plasma_heat_flux_watts
            
            # 2. Кріогенне охолодження рідким воднем (Закон теплообміну Фур'є)
            # Ефективність теплообміну залежить від градієнта температур між дзеркалом та LH2
            temp_delta = self.mirror_temperature_c - self.lh2_inlet_temp_c
            cooling_efficiency = 0.045  # Коефіцієнт ефективності гідравлічних мікроканалів сорочки
            
            extracted_heat_watts = self.lh2_flow_rate_kgs * self.lh2_heat_capacity * temp_delta * cooling_efficiency
            
            # 3. Чистий тепловий баланс обшивки капсули UABC
            net_thermal_energy_joules = (total_incoming_heat_watts - extracted_heat_watts) * dt
            
            # Зміна температури металу за крок часу
            temp_change = net_thermal_energy_joules / (self.mirror_mass_kg * self.tungsten_heat_capacity)
            self.mirror_temperature_c += temp_change
            
            # Запис точок телеметрії для інвесторів Brave1 / YC
            self.timeline.append(current_time)
            self.surface_temps.append(self.mirror_temperature_c)
            self.lh2_cooling_power_mw.append(extracted_heat_watts / 1e6)
            
            # Перевірка на катастрофічне прогорання обшивки
            if self.mirror_temperature_c >= self.melt_temperature_c:
                print(f"[💥 CRITICAL FAILURE] Т={current_time}с: Льодова сорочка пробита! Матриця розплавилась при {self.mirror_temperature_c:.1f}°C")
                return False
                
            current_time += dt

        print(f"\n🌍 [УСПІХ] Контур стабілізовано. Кінцева температура дзеркала: {self.mirror_temperature_c:.1f}°C")
        print(f"[УСПІХ] Максимальний розігрів зафіксовано значно нижче межі плавлення вольфраму ({self.melt_temperature_c}°C).")
        self.generate_plots()
        return True

    def generate_plots(self):
        """Побудова професійних графіків термодинамічного балансу системи"""
        plt.style.use('dark_background')
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), sharex=True)
        fig.suptitle('BEAM-FLIGHT: CRYOGENIC ICE-JACKET THERMAL BALANCE (PHASE 1)', fontsize=12, color='cyan')

        # 1. Графік температури вольфрамової матриці
        ax1.plot(self.timeline, self.surface_temps, color='#ff9933', linewidth=2.5, label='Температура дзеркала «Брюхо»')
        ax1.axhline(y=1500.0, color='red', linestyle=':', label='Максимальний розрахунковий ліміт безпеки')
        ax1.set_ylabel('Температура (°C)', color='white')
        ax1.grid(True, linestyle='--', alpha=0.3)
        ax1.legend(loc='upper right')

        # 2. Графік потужності охолодження LH2 контуру
        ax2.plot(self.timeline, self.lh2_cooling_power_mw, color='#3399ff', linewidth=2.5, label='Потужність кріогенного відведення тепла')
        ax2.set_xlabel('Час активного розгону лазером (секунди)', color='white')
        ax2.set_ylabel('Відведення енергії (МВт)', color='white')
        ax2.grid(True, linestyle='--', alpha=0.3)
        ax2.legend(loc='upper right')

        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    simulator = CryoIceJacketSimulation()
    # Запускаємо 45-секундний тест проходження крізь щільну атмосферу
    simulator.run_thermal_simulation(flight_duration_sec=45.0)
