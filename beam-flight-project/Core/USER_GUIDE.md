# USER GUIDE: BEAM-FLIGHT CORE SIMULATION ENVIRONMENT

**Document ID:** UG-BEAMFLIGHT-2026-001  
**Target Folder:** `/beam-flight-project/Core`  
**Status:** Public Domain / Open IP Disclosure under CC BY 4.0  

---

## 1. SOFTWARE ARCHITECTURE OVERVIEW

The `Core` directory contains the Python-based simulation engine for the **Beam-Flight System**. It bridges suborbital aerodynamic physics, Low Earth Orbit (LEO) orbital ballistics, and financial return (ROI) models.

### 1.1. Script Interdependency Matrix
*   `slo_grid.py`: The foundation. Calculates satellite visibility windows over the 4 global **VECTOR-PRIME** hubs using the Haversine formula.
*   `beam-flight-project.py`: The physical physics engine. Simulates logarithmic atmospheric drag, capsule mass flow, and dual-mode propulsion (LTHE @ 1200s \(I_{\text{sp}}\) and Ion @ 4500s \(I_{\text{sp}}\)).
*   `beam_flight_complete_mission.py`: The mission manager. Automates launch, cruise, and combined Magnetohydrodynamic (MHD) braking phases, while logging physical loads (8–15G).
*   `beam_max_passenger_core.py`: Passenger-specific extension for the 5.5-ton Gamma class, forcing smooth G-force tracking (1.5G–4G) and Life Support Module (LSM) failsafes.
*   `beam-flight+oasis_project.py`: Infrastructure linker. Simulates the 5.8 GHz microwave energy downlink redirection to ground-based Oasis grids when no capsule is present.

---

## 2. INSTALLATION & ENVIRONMENT SETUP

The simulation suite runs on vanilla Python 3.8+ and requires minimal external dependencies.

```bash
# 1. Clone the repository
git clone https://github.com

# 2. Navigate to the core execution folder
cd Beam-Flight-Project/beam-flight-project/Core

# 3. Install required analytics and visualization packages
pip install matplotlib numpy
```
## 3. EXECUTION COMMANDS & SIMULATION RUNS

Execute the python files directly from your terminal interface to evaluate physical profiles, financial matrices, or orbital handovers.

### 3.1. Running the Complete Mission Simulator (Physical Telemetry Log)
To evaluate a full suborbital flight cycle from launch to ground laser-cushion recovery, execute:
```bash
python beam_flight_complete_mission.py
```
*Expected Output:* Real-time terminal telemetry log updating altitude (meters), velocity (m/s), active engine mode (`LTHE` or `ION`), and current G-forces.

### 3.2. Running the Oasis Energy Transition & Grid Optimization
To run the combined tracking and power-grid distribution simulation:
```bash
python beam-flight+oasis_project.py
```
*Expected Output:* Analytics displaying continuous gigawatt power export metrics, sand cooling thermal indexes (-12°C to -15°C deviations), and generated daily baseload revenue.

### 3.3. Running the Venture Capital Visual ROI Model
To plot the Net Present Value (NPV) chart showing the 15-million-dollar investment payback curve:
```bash
python ../Economics/roi_visual_model.py
```
*Expected Output:* A graphic display pop-up showing the monthly cashflow vector and pinpointing the exact project break-even month.

# ІНСТРУКЦІЯ КОРИСТУВАЧА: СЕРЕДОВИЩЕ СИМУЛЯЦІЇ ПРОЄКТУ BEAM-FLIGHT

**Document ID:** UG-BEAMFLIGHT-2026-001  
**Цільова папка:** `/beam-flight-project/Core`  
**Статус:** Відкрите розкриття IP за ліцензією CC BY 4.0  

---

## 1. СТРУКТУРА ПРОГРАМНОГО КОМПЛЕКСУ

Папка `Core` містить програмне ядро на базі мови Python для моделювання фізичних та економічних параметрів системи **Beam-Flight**. 

### 1.1. Взаємозв'язок архітектурних модулів (Скриптів)
*   `slo_grid.py`: Базовий модуль. Розраховує орбітальну сітку супутників Cosmo-Lane над 4 хабами системи **VECTOR-PRIME** за формулою гаверсинуса.
*   `beam-flight-project.py`: Фізичний двигун польоту. Рахує експоненціальний опір повітря та дворежимну тягу двигунів (LTHE до 12 км, іонний — вище 12 км).
*   `beam_flight_complete_mission.py`: Диспетчер місії. Керує повним циклом від старту до МГД-гальмування, фіксуючи перевантаження конструкції (8–15G).
*   `beam_max_passenger_core.py`: Пасажирський модуль Gamma (5.5 т). Контролює плавний графік прискорення людей (1.5G–4G) та контури кисню LSM.
*   `beam-flight+oasis_project.py`: Інтеграційний вузол. Спрямовує вільну гігаватну потужність 5.8 ГГц на цивільні потреби «Оазису», коли немає капсули в зоні.

---

## 2. СВЕРЕДОВИЩЕ ТА ВСТАНОВЛЕННЯ

Комплекс симуляції працює на базі Python 3.8+ та потребує мінімального набору сторонніх бібліотек для візуалізації аналітики.

```bash
# 1. Клонування репозиторію
git clone https://github.com

# 2. Перехід до робочої папки ядра програми
cd Beam-Flight-Project/beam-flight-project/Core

# 3. Встановлення пакетів аналізу та графіки
pip install matplotlib numpy
```
## 3. КОМАНДИ ЗАПУСКУ ТА ЗНЯТТЯ ТЕЛЕМЕТРІЇ

Усі симуляційні сценарії запускаються безпосередньо через консольний термінал оператора.

### 3.1. Запуск наскрізної симуляції польоту (Повний фізичний лог місії)
Для прорахунку кінематики польоту капсули від пускової шахти до посадки на лазерну подушку виконайте команду:
```bash
python beam_flight_complete_mission.py
```
*Результат виконання:* Потокова видача телеметрії в консоль: висота (м), швидкість (м/с), поточний режим роботи двигуна (`LTHE` / `ION`) та діючі перевантаження.

### 3.2. Симуляція енергетичного транзиту станції «Оазис»
Для запуску комерційної моделі генерації струму цивільним споживачам виконайте:
```bash
python beam-flight+oasis_project.py
```
*Результат виконання:* Аналітика розподілу потужності супутників, індекси тераформування пустельного піску (-12°C...-15°C) та обсяг добового прибутку.

### 3.3. Візуалізація венчурної фінансової моделі (Крива ROI/NPV)
Щоб побудувати графік окупності 15-мільйонних інвестицій, запустіть економічний скрипт:
```bash
python ../Economics/roi_visual_model.py
```
*Результат виконання:* Спливаюче графічне вікно Matplotlib із візуалізацією накопиченого чистого прибутку та точкою виходу проєкту в нуль.
