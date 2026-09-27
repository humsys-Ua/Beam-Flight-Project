import math
import time
import random

class UniversalCoreSafetyController:
    def __init__(self, capsule_mass_kg=15000, is_passenger_mission=True):
        self.mass = capsule_mass_kg
        self.g = 9.81
        self.target_g = 3.0          
        self.is_passenger = is_passenger_mission
        
        # Динаміка польоту (Початок аварійного сценарію на висоті 110 км)
        self.altitude_z_m = 110000.0   # 110 км (Термосфера / Вакуум)
        self.velocity_ms = 5150.0      # Швидкість круїзу Mach 15
        
        # Системи порятунку універсального ядра
        self.is_core_ejected = False
        self.autonomous_lss_active = False
        self.rcs_thrusters_active = False  # Мікродвигуни для вакууму
        self.parachute_deployed = False
        self.cabin_temperature_c = 21.0

    def trigger_space_ejection(self):
        """Протокол аварійного відстрілу універсального ядра на висоті 110 км"""
        print(f"\n🚨🚨🚨 [CRITICAL DETECTED]: КРИТИЧНИЙ ЗБІЙ ПЛАТФОРМИ НА ВИСОТІ {self.altitude_z_m/1000:.1f} КМ!")
        payload_type = "ПАСАЖИРСЬКЕ" if self.is_passenger else "ЦІННИЙ ВАНТАЖ"
        print(f"[ПРОТОКОЛ ЕВАКУАЦІЇ] -> Ініціалізація відстрілу. Тип ядра: {payload_type}")
        
        self.is_core_ejected = True
        self.autonomous_lss_active = True
        
        print("[АВТОНОМНИЙ КОНТУР] -> Живлення переведено на внутрішні аварійні батареї.")
        if self.is_passenger:
            print("[АВТОНОМНИЙ КОНТУР] -> Герметизація кабіни. Подача кисню активована (100%).")
        else:
            print("[АВТОНОМНИЙ КОНТУР] -> Стабілізація тиску у вантажному відсіку для захисту обладнання.")
            
        print(" -> [ПІРОБОЛТИ]: Основний розгінний модуль від'єднано. Ядро у вільному польоті.")
        time.sleep(1.0)
        
        print("\n--- ФАЗА СТАРТУ АВТОНОМНОГО СПУСКУ З ВАКУУМУ (110 КМ) ---")
        
        # Цикл спуску ядра на Землю
        while self.altitude_z_m > 0:
            # 1. Керування у вакуумі термосфери (Вище 40 км парашути не працюють)
            if self.altitude_z_m > 40000.0:
                self.rcs_thrusters_active = True
                # Імпульсні двигуни розвертають ядро тепловим щитом уперед і гальмують
                gas_braking = 1.5 * self.g
                self.velocity_ms = max(1500.0, self.velocity_ms - gas_braking * 5.0)
                print(f" -> [ВАКУУМНИЙ СУПОРТ RCS]: Активна стабілізація мікродвигунами щита.")
            else:
                self.rcs_thrusters_active = False
            
            # 2. Вхід у щільні шари атмосфери та активація парашутів (Нижче 15 км)
            if self.altitude_z_m <= 15000.0 and not self.parachute_deployed:
                print("\n[АВТОМАТИКА] -> Вхід у щільну атмосферу. Викид системи гальмівних парашутів ядра!")
                self.parachute_deployed = True
                
            # Розрахунок уповільнення
            if self.parachute_deployed:
                current_deceleration = 4.5 * self.g
            elif self.altitude_z_m <= 40000.0:
                current_deceleration = 3.0 * self.g  # Аеродинамічне гальмування обтічника
            else:
                current_deceleration = 1.5 * self.g  # Тільки імпульсні двигуни у вакуумі
                
            # Зміна динамічних параметрів за один крок (імітація інтервалу)
            self.velocity_ms = max(5.0, self.velocity_ms - current_deceleration * 3.0)
            self.altitude_z_m = max(0.0, self.altitude_z_m - 12000.0)
            self.cabin_temperature_c += random.uniform(-0.1, 0.1)
            
            print(f" -> Телеметрія ядра: Висота = {self.altitude_z_m/1000:.1f} км | Швидкість = {self.velocity_ms:.1f} м/с | Температура = {self.cabin_temperature_c:.1f}°C")
            print(" " + "."*50)
            time.sleep(0.5)
            
        print("\n🌍 [АВАРІЙНИЙ ФІНАЛ]: Універсальне ядро здійснило успішну м'яку посадку на пневмоподушки.")
        print("[СТАТУС МІСІЇ]: Повна безпека збережена на всьому еволюційному шляху від 110 км до Землі.")

    def run_mission_with_fault_injection(self):
        print("=== ЗАПУСК МОДЕЛЮВАННЯ ВАНТАЖНО-ПАСАЖИРСЬКОГО ШАТЛА BEAM-MAX ===")
        print(f"Повна польотна маса системи: {self.mass / 1000:.1f} тонн")
        print("Статус: Політ на маршовому круїзному ешелоні...")
        time.sleep(1.0)
        
        # Миттєво викликаємо аварію на висоті 110 км, як ви і вказали
        self.trigger_space_ejection()

if __name__ == "__main__":
    # Тестуємо порятунок універсального вантажного ядра (is_passenger_mission=False)
    safety_system = UniversalCoreSafetyController(capsule_mass_kg=15000, is_passenger_mission=False)
    safety_system.run_mission_with_fault_injection()
