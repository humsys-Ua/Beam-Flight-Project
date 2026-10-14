#![no_std]

pub struct PowerAllocationResult {
    pub launch_vector_power_mw: f32, // Струм на розгін капсули
    pub oasis_drop_power_mw: f32,    // Надлишок, що йде на Оазис
}

pub struct EnergyGridStabilizer {
    pub required_launch_power_mw: f32, // Номінальний ліміт для Beam-Mini (наприклад, 250.0)
}

impl EnergyGridStabilizer {
    /// Протокол стабілізації та скидання надлишку напруги
    #[inline(always)]
    pub fn balance_swarm_energy(&self, total_collected_power_mw: f32, is_launch_active: bool) -> PowerAllocationResult {
        if is_launch_active {
            if total_collected_power_mw > self.required_launch_power_mw {
                // Головний інсайт: строго віддаємо ліміт на розгін, а все зайве - на Оазис!
                let surplus = total_collected_power_mw - self.required_launch_power_mw;
                PowerAllocationResult {
                    launch_vector_power_mw: self.required_launch_power_mw,
                    oasis_drop_power_mw: surplus,
                }
            } else {
                // Аварійний режим: енергії ледь вистачає тільки на капсулу
                PowerAllocationResult {
                    launch_vector_power_mw: total_collected_power_mw,
                    oasis_drop_power_mw: 0.0,
                }
            }
        } else {
            // Звичайний хід: капсула не летить, 100% струму йде на Оазис
            PowerAllocationResult {
                launch_vector_power_mw: 0.0,
                oasis_drop_power_mw: total_collected_power_mw,
            }
        }
    }
}
