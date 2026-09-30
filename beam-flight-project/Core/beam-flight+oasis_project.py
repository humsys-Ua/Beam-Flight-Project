import math

class GlobalSpaceEnergyRing:
    """
    ГЛОБАЛЬНЕ КОСМІЧНЕ ЕНЕРГОКІЛЬЦЕ.
    Живиться від Сонця. На висоті 12 км передає фінальний імпульс капсулі для виходу на орбіту.
    """
    def __init__(self):
        self.total_orbital_storage_mj = 43880.0 * 1e3  # Переводимо ГДж зі скріншоту в МДж
        
    def downlink_to_oasis(self, transfer_power_mw, duration_sec):
        """Скидання базової енергії на ректени комплексу Оазис для продажу людям."""
        energy_to_send_mj = transfer_power_mw * duration_sec
        if self.total_orbital_storage_mj >= energy_to_send_mj:
            self.total_orbital_storage_mj -= energy_to_send_mj
            return energy_to_send_mj, True
        return 0.0, False

    def inject_orbital_thrust_pulse(self, demanded_power_mw, duration_sec):
        """Орбітальний імпульс підключення: видається капсулі СТРОГО на висоті 12 км."""
        required_energy_mj = demanded_power_mw * duration_sec
        if self.total_orbital_storage_mj >= required_energy_mj:
            self.total_orbital_storage_mj -= required_energy_mj
            return required_energy_mj, True
        return 0.0, False


class OasisTerrestrialPowerPlant:
    """КОМПЛЕКС ОАЗИС. Працює сугубо на прийом та продаж енергії на Землі."""
    def __init__(self, global_ring_reference):
        self.space_ring = global_ring_reference
        self.total_sold_energy_kwh = 0.0

    def receive_and_distribute_power(self):
        # Приймаємо 2500 МВт протягом години (3600 сек), як на скріншоті
        received_energy_mj, success = self.space_ring.downlink_to_oasis(2500.0, 3600)
        if success:
            usable_energy_mj = received_energy_mj * 0.925
            self.total_sold_energy_kwh = usable_energy_mj / 3.6
            print(f"\n[НАЗЕМНИЙ КОМПЛЕКС ОАЗИС] Прийом активовано на частоті 5.8 ГГц.")
            print(f"-> Прийнято з Космічного Кільця: {received_energy_mj/1e3:.1f} ГДж енергії.")
            print(f"-> Успішно продано земним користувачам: {self.total_sold_energy_kwh:.2f} кВт-год.")


class TerrestrialLaunchStation:
    """НАЗЕМНА ПУСКОВА СТАНЦІЯ. Тягне капсулу власною потужністю СУГУБО від 0 до 12 км."""
    def __init__(self, global_ring_reference):
        self.space_ring = global_ring_reference
        self.LAUNCH_PAD_ALTITUDE = 0.0
        self.STAGE_1_END_ALTITUDE = 12000.0  # Межа підключення Кільця (12 км)
        self.capsule_mass = 1200.0  # кг
        self.bryukho_efficiency = 0.942

    def execute_full_ascent(self):
        print(f"\n[НАЗЕМНА СТАНЦІЯ] Ініціалізація розгону капсули UABC (0-12 км).")
        print("-> Розгін виконується за рахунок ВЛАСНОЇ наземної енергії станції.")
        
        # Моделюємо чистий підйом до 12 км на наземному лазері
        rho_12km = 1.225 * math.exp(-self.STAGE_1_END_ALTITUDE / 8500.0)
        optics_eff = self.bryukho_efficiency * (1.0 - (0.15 * (rho_12km / 1.225)))
        
        print(f"-> [УСПІХ] Капсула піднята станцією на висоту {self.STAGE_1_END_ALTITUDE/1000} км. Матриця «Брюхо» ККД: {optics_eff*100:.2f}%")
        print("-" * 90)
        print(f"[ТОЧКА ПЕРЕМИКАННЯ: 12 КМ] Капсула вийшла у верхні шари. Підключення до Глобального Енергокільця.")
        
        # ЕТАП 2: На висоті 12 км підключається Кільце і дає фінальний потужний поштовх (наприклад, 600 МВт на 45 сек)
        orbital_pulse_mj, ring_success = self.space_ring.inject_orbital_thrust_pulse(600.0, 45.0)
        
        if ring_success:
            print(f"-> [КОСМІЧНЕ КІЛЬЦЕ] Спрямовано фінальний імпульс на капсулу: {orbital_pulse_mj/1e3:.1f} ГДж енергії.")
            print("-> [МАСШТАБУВАННЯ] Капсула успішно отримала орбітальну швидкість і лягла на цільовий вектор виведення супутників!")
        else:
            print("-> [ПОМИЛКА] Кільце не змогло видати фінальний імпульс підключення.")


if __name__ == "__main__":
    print("=== ОБНОВЛЕНА СИМУЛЯЦІЯ: Core/beam-flight+oasis_project.py ===")
    
    # Створюємо Кільце із початковим балансом як на вашому фото
    cosmo_ring = GlobalSpaceEnergyRing()
    print(f"Початковий запас енергії в Космічному Кільці: {cosmo_ring.total_orbital_storage_mj/1e3:.1f} ГДж")
    print("-" * 90)

    # 1. Оазис забирає свою долю на продаж
    oasis = OasisTerrestrialPowerPlant(cosmo_ring)
    oasis.receive_and_distribute_power()
    print("-" * 90)

    # 2. Наземна станція штовхає до 12 км, а Кільце підключається на фініші
    launch_system = TerrestrialLaunchStation(cosmo_ring)
    launch_system.execute_full_ascent()
    print("-" * 90)
    
    print(f"Кінцевий залишок енергії в Космічному Кільці: {cosmo_ring.total_orbital_storage_mj/1e3:.1f} ГДж")
