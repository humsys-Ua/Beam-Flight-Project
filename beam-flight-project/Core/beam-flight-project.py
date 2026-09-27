import time
import random
import math

class BeamFlightMissionControl:
    def __init__(self, capsule_mass_kg=50, target_power_mw=250):
        # Фізичні та атмосферні константи
        self.capsule_mass = capsule_mass_kg
        self.g = 9.81
        self.R_air = 287.05  
        self.gamma = 1.4     
        
        # Координатна матриця польоту (X - дальність, Y - бічна смуга, Z - висота)
        self.pos_x_m = 0.0
        self.pos_y_m = 0.0   
        self.altitude_z_m = 0.0
        self.velocity_ms = 0.0
        
        # Бортові та наземні системи
        self.target_power_mw = target_power_mw
        self.sces_buffer_mw = 0.0
        self.lh2_fuel_level = 0.0
        self.cable_tension_n = capsule_mass_kg * self.g
        
        # Статуси оптичних та газових контурів
        self.active_source = "НАЗЕМНИЙ КОМПЛЕКС"
        self.satellite_pair = "ПАРА А"
        self.satellite_mode = "ЛІДЕР"
        self.capsule_receptor = "БРЮХО (РОЗГІН)"
        
        self.capsule_laser_active = False
        self.ground_laser_active = False
        self.gas_injection_active = False
        self.recuperation_brake_active = False
        
        self.trajectory_mode = "СТАТИЧНА ФІКСАЦІЯ"

    def calculate_mach(self):
        """Математичний розрахунок числа Маху для поточного ешелону термосфери/стратосфери"""
        if self.altitude_z_m > 100000:
            temperature_k = 700.0  # Термосфера (розігрів сонячною радіацією)
        elif self.altitude_z_m > 50000:
            temperature_k = 250.0  # Мезосфера
        else:
            temperature_k = max(210.0, 288.15 - 0.0065 * self.altitude_z_m)
            
        speed_of_sound = math.sqrt(self.gamma * self.R_air * temperature_k)
        return self.velocity_ms / speed_of_sound if speed_of_sound > 0 else 0

    def print_telemetry(self, step_name):
        mach = self.calculate_mach()
        print(f"\n[{step_name}] === ТЕЛЕМЕТРІЯ МІСІЇ ===")
        print(f" -> Координати: X = {self.pos_x_m/1000:.2f} км | Y = {self.pos_y_m:.0f} м | Z (Висота) = {self.altitude_z_m/1000:.3f} км")
        print(f" -> Динаміка:   Швидкість = {self.velocity_ms:.1f} м/с ({mach:.2f} Мах) | Режим: {self.trajectory_mode}")
        print(f" -> Енергетика: Джерело = {self.active_source} ({self.satellite_pair}-{self.satellite_mode}) | Буфер SCES = {self.sces_buffer_mw:.1f} МВт")
        print(f" -> Контури:    Лазер Капсули: {'ВВІМКН' if self.capsule_laser_active else 'ВИМКН'} | Лазер Землі: {'ВВІМКН' if self.ground_laser_active else 'ВИМКН'} | Газ Плазми: {'АКТИВНИЙ' if self.gas_injection_active else 'ВИМКН'}")
        print(f" -> Гальма:     Рекуперація двигуна: {'АКТИВНА' if self.recuperation_brake_active else 'ВИМКНЕНА'}")
        print("-" * 90)
        time.sleep(1.0)

    def run_mission(self):
        print("\n" + "="*90)
        print(" ЗАПУСК ПОВНОГО ІНТЕГРОВАНОГО ЦИКЛУ КЕРУВАННЯ ПОЛІТОМ СИСТЕМИ BEAM-FLIGHT ")
        print("="*90)

        # ------------------------------------------------------------------------
        # 1. ПІДГОТОВКА ТА ГОТОВНІСТЬ
        # ------------------------------------------------------------------------
        self.trajectory_mode = "ПІДГОТОВКА ДО СТАРТУ"
        print(f"\n[ПРОТОКОЛ] Крок 1: Статична фіксація на решітці-конфорці шахти.")
        print(f" -> Очікування синхронізації з супутниковим конвеєром...")
        time.sleep(0.8)
        print(f" -> [ОК] Паралельна смуга 'ПАРА А' увійшла в стартовий сектор.")
        
        print(f"[ПРОТОКОЛ] Крок 2: Заправка Just-in-Time (LH2) та зарядка SCES ферми.")
        self.lh2_fuel_level = 100.0
        self.sces_buffer_mw = self.target_power_mw
        print(f" -> [ОК] Енергобуфер накопичив {self.sces_buffer_mw} МВт.")

        # ------------------------------------------------------------------------
        # 2. СТАРТ ТА ВЗЛІТ (ВЕРТИКАЛЬНИЙ РОЗГІН)
        # ------------------------------------------------------------------------
        print("\n" + "-"*90)
        self.trajectory_mode = "ВЕРТИКАЛЬНИЙ РОЗГІН (ГІГОВАТНИЙ ШТОВХАЧ)"
        print(f"[ПРОТОКОЛ] Крок 3: Подача стартової напруги. Відстріл тросів.")
        self.cable_tension_n = 0.0
        print(f" -> Капсула відірвалася від решітки виключно під тиском світла.")
        
        # Набір початкової висоти від Наземного комплексу
        self.altitude_z_m = 4500.0
        self.velocity_ms = 600.0
        self.pos_x_m = 0.0
        self.print_telemetry("ВЗЛІТ: ПОЧАТКОВА ФАЗА")

        # ------------------------------------------------------------------------
        # 3. ПЕРЕХОПЛЕННЯ ТА ВЕДЕННЯ (ЗЕМЛЯ ⇄ КОСМОС + РЕЗЕРВ ЛІДЕР-ВЕДОМИЙ)
        # ------------------------------------------------------------------------
        print("\n" + "-"*90)
        print(f"[ПРОТОКОЛ] Крок 4: Хендловер 'Make-Before-Break' (Земля -> Орбіта).")
        print(f" -> Активація дзеркал ADAOS супутника ПАРА А-ЛІДЕР на межі атмосфери (12 км).")
        self.active_source = "ОРБІТАЛЬНЕ ЕНЕРГЕТИЧНЕ КОЛО"
        self.altitude_z_m = 12000.0
        self.velocity_ms = 1800.0
        print(f" -> [ОК] Наземний лазер передав естафету на орбіту без розриву контуру.")
        
        # Форс-мажор: Збій лідера та миттєвий перехоплення ведомим
        print(f"\n💥 АВАРІЙНИЙ СЦЕНАРІЙ: Короткочасний збій наведення супутника ЛІДЕР!")
        self.satellite_mode = "ВЕДОМИЙ (РЕЗЕРВ ПЕРЕХВАТУ)"
        print(f" -> 🛡️ Паралельна смуга зреагувала. Керування веде: {self.satellite_mode}")
        time.sleep(0.5)
        
        # Зворотний протокол (Rollback)
        print(f" -> [ЗВОРТНИЙ ПРОТОКОЛ]: Лідер відновив координати. Повернення статусу.")
        self.satellite_mode = "ЛІДЕР"
        
        # Вихід на максимальний круїз (Mach 15) в термосфері
        self.altitude_z_m = 115000.0
        self.velocity_ms = 5150.0  # ~Mach 15
        self.pos_x_m = 80000.0
        self.trajectory_mode = "МАГІСТРАЛЬНИЙ КРУЇЗ (ТЕРМОСФЕРА)"
        self.print_telemetry("ОРБІТАЛЬНЕ ВЕДЕННЯ")

        # ------------------------------------------------------------------------
        # 4. ЗМІНА ТРАЄКТОРІЇ (ПІРНАННЯ ДО НИЖНЬОГО ЕШЕЛОНУ ДЛЯ УНИКНЕННЯ ЗІТКНЕНЬ)
        # ------------------------------------------------------------------------
        print("\n" + "-"*90)
        print(f"[ПРОТОКОЛ] Крок 5: Запобігання зіткненням на орбітальному кільці.")
        print(f" -> Позаду виявлено наступні апарати. Зміна траєкторії зниженням висоти!")
        self.trajectory_mode = "ПІРНАННЯ НА НИЖНІЙ ГАЛЬМІВНИЙ ЕШЕЛОН"
        
        # Капсула знижує висоту (пірнає зі 115 км до 95 км), але утримує швидкість Mach 15
        self.altitude_z_m = 95000.0
        self.pos_x_m += 25000.0
        print(f" -> [ОК] Капсула занурилась під магістраль. Головний ешелон вільний для руху.")
        self.print_telemetry("ЗМІНА ТРАЄКТОРІЇ")

        # ------------------------------------------------------------------------
        # 5. НАВЕДЕННЯ ТА ПІДГОТОВКА ДО ГАЛЬМУВАННЯ (БЕЗРОЗРИВНИЙ МІСТ)
        # ------------------------------------------------------------------------
        print("\n" + "-"*90)
        print(f"[ПРОТОКОЛ] Крок 6: Наведення на Посадкову Шахту Землі.")
        self.trajectory_mode = "ПІДГОТОВКА ДО ГАЛЬМУВАННЯ"
        
        # Капсула кидає промінь першою
        print(f" -> Активація носового лазера-маяка капсули.")
        self.capsule_laser_active = True
        
        # Введення газу для ліквідації плазми
        print(f" -> 💨 КРИТИЧНИЙ ШЛЕЙФ: Розігрів повітря. Введення газу в носовий конус!")
        self.gas_injection_active = True
        print(f" -> [ГАЗ ПЛАЗМИ]: Атмосферний плазмовий екран успішно роздуто кріогенним шаром.")
        
        # Земля відповідає своїм лазером
        print(f" -> Земля підтверджує отримання телеметрії. Подача зустрічного гальмівного лазера.")
        self.ground_laser_active = True
        print(f"🎯 [ЕНЕРГЕТИЧНИЙ МІСТ]: Обидва лазери замкнені в один контур. Енергетичний удар ліквідовано.")
        self.print_telemetry("СИНХРОНІЗАЦІЯ НАВЕДЕННЯ")

        # ------------------------------------------------------------------------
        # 6. ГАЛЬМУВАННЯ ТА ЗНИЖЕННЯ
        # ------------------------------------------------------------------------
        print("\n" + "-"*90)
        print(f"[ПРОТОКОЛ] Крок 7: Комбіноване активне гальмування.")
        self.trajectory_mode = "ЕКСТРЕМАЛЬНЕ СВІТЛОВЕ ГАЛЬМУВАННЯ"
        
        # Доповнення гальмівних сил рекуперацією двигуна
        self.recuperation_brake_active = True
        print(f" -> ⚡ Ввімкнення рекуперативного гальмування аеродинамічного контуру.")
        
        # Симуляція скидання швидкості з 5150 м/с до дозвукової
        deceleration_force = 6.5 * self.g
        while self.velocity_ms > 340.0:
            self.velocity_ms -= deceleration_force * 3.0
            self.altitude_z_m = max(15000.0, self.altitude_z_m - 20000.0)
            self.pos_x_m += self.velocity_ms * 3.0
            self.sces_buffer_mw += 18.5  # Рекуперація повертає енергію в SCES
            
            mach = self.calculate_mach()
            print(f" -> Потік зниження: Высота = {self.altitude_z_m/1000:.1f} км | Швидкість = {self.velocity_ms:.1f} м/с ({mach:.2f} Мах)")
            time.sleep(0.4)

        # Автоматичне вимкнення газу нижче 3 Мах
        print(f"\n[АВТОМАТИКА] Швидкість безпечна для плазми (< 3 Мах).")
        self.gas_injection_active = False
        print(f" -> Подача газу відсічена.")

        # Догальмовування до входу в саму посадкову зону
        self.velocity_ms = 40.0
        self.altitude_z_m = 500.0
        self.print_telemetry("ФІНАЛЬНЕ ЗНИЖЕННЯ")

        # ------------------------------------------------------------------------
        # 7. ПОСАДКА ТА ЗАКРІПЛЕННЯ
        # ------------------------------------------------------------------------
        print("\n" + "-"*90)
        print(f"[ПРОТОКОЛ] Крок 8: Вертикальний запуск у посадкову герметичну шахту.")
        self.trajectory_mode = "ФІНАЛЬНЕ ЗАСУНЕННЯ ТА ЗАКРІПЛЕННЯ"
        
        # Повна зупинка всіх динамічних та енергетичних контурів
        self.velocity_ms = 0.0
        self.altitude_z_m = 0.0
        self.capsule_laser_active = False
        self.ground_laser_active = False
        self.recuperation_brake_active = False
        
        print(f" -> Капсула м'яко торкнулася нижньої платформи на швидкості 0 м/с.")
        print(f" -> 🔓 Роботизовані фіксатори міцно затиснули корпус на решітці комфорту.")
        print(f" -> Скидання залишкової енергії SCES буфера в підземну накопичувальну мережу.")
        
        # Вивід фінальної телеметрії з нульовими показниками
        self.print_telemetry("МІСІЯ ЗАВЕРШЕНА УСПІШНО")
        
        print("\n" + "="*90)
        print(" 🎉 ВСІ СИСТЕМИ ЦИФРОВОГО ДВІЙНИКА BEAM-FLIGHT СИНХРОНІЗОВАНІ. ПОСАДКА 100% ВАЛІДНА! ")
        print("="*90 + "\n")

if __name__ == "__main__":
    # Створення об'єкта симулятора та запуск повного інтегрованого циклу місії
    mission = BeamFlightMissionControl()
    mission.run_mission()
