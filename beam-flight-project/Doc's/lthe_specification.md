# TECHNICAL SPECIFICATION: LASER-THERMAL HYDROGEN ENGINE (LTHE)

**Document ID:** TS-LTHE-2026-004  
**Associated Manifesto:** WP-BEAMFLIGHT-2026-001  
**Status:** Published under Strict Custom Proprietary Public Disclosure License (PADL-BEAMFLIGHT-2026)  

---

## 1. OPERATIONAL PRINCIPLE & THERMODYNAMIC CYCLE

The Laser-Thermal Hydrogen Engine (LTHE) serves as the primary propulsion module for the UABC capsule during the atmospheric injection phase (0–12 km). The engine utilizes an external energy supply paradigm, completely eliminating chemical oxidation within the onboard flight systems.

*   **Absorption & Acceleration Process:** A monochromatic IR laser beam ($\lambda = 1.06 \ \mu\text{m}$) focuses through the lower optical receiver matrix ("Belly") into the engine's expansion chamber.
*   **Propellant Thermodynamics:** Cryogenic liquid hydrogen ($LH_2$), injected under high pressure via heat-exchanger capillaries, instantly absorbs the gigawatt optical flux. The gas temperature spikes exponentially, transitioning into a high-temperature plasma state.
*   **Gas-Dynamic Exhaust:** The ultra-hot plasma expands through a magnetohydrodynamic nozzle, escaping at velocities far exceeding conventional chemical rocketry. The net exhaust is pure water vapor (0% ecological footprint).

## 2. PHYSICAL PARAMETERS & THRUST KINETICS

The efficiency of thermodynamic propellant expansion within the LTHE nozzle is modeled based on specific impulse and thermal flux constraints.

*   **Specific Impulse ($I_{\text{sp}}$):** Rated at $\ge 1200$ seconds, which is three times higher than state-of-the-art oxygen-hydrogen chemical engines (e.g., SSME).
*   **Chamber Energy Density:** The stable expansion thermal flux is calculated using the following thermodynamic model:

$$Q_{\text{thermal}} = \frac{P_{\text{received}} \cdot \eta_{\text{matrix}}}{V_{\text{chamber}}}$$

Where:
*   $P_{\text{received}} = 250 \text{ MW}$ (Net laser beam power delivered to the receiver).
*   $\eta_{\text{matrix}} = 0.942$ (Absorption coefficient of the "Belly" optical matrix).
*   $V_{\text{chamber}} = 0.045 \text{ m}^3$ (Physical volume of the internal expansion chamber).

$$Q_{\text{thermal}} = \frac{250 \cdot 10^6 \cdot 0.942}{0.045} \approx 5.23 \cdot 10^9 \text{ W/m}^3 \text{ (Specific Plasma Energy Release)}$$

*   **Chamber Operating Pressure:** $\ge 18.5 \text{ MPa}$ sustained during the active 45-second acceleration phase.
*   **Plasma Exhaust Velocity:** $V_{\text{exhaust}} = I_{\text{sp}} \cdot g_0 \approx 1200 \cdot 9.81 \approx 11772 \text{ m/s}$.

## 3. LTHE PERFORMANCE SPECIFICATIONS MATRIX

| Engineering Parameter | Operational Value | Technical Notes |
| :--- | :--- | :--- |
| **Engine Propellant Type** | Cryogenic Hydrogen ($LH_2$) | Stored in vacuum-insulated tanks |
| **Core Plasma Temperature** | 4200 K – 4500 K | Structural limit of the HfC-C matrix |
| **Specific Impulse ($I_{\text{sp}}$)**| $\ge 1200$ seconds | Laser-thermal acceleration baseline |
| **Maximum Thrust Output** | 35.5 kN (Alpha Class) | Optimized for a 50 kg capsule mass |
| **Active Thrust Duration** | 45.0 seconds | Synchronized with SCES pulse buffer |
| **Thermodynamic Efficiency** | 72.5% | Optical-to-kinetic energy conversion |
| **Propulsion Module Mass** | $\le 42.0$ kg | Includes capillary cooling loops |
| **Hydrogen Flow Mass Rate** | 3.01 kg/s | Managed via Just-in-Time protocol |

---

## 4. SAFETY SYSTEMS & CRYOGENIC LOOP

To prevent nozzle wall burn-through under plasma temperatures exceeding 4000 K, the system integrates **regenerative capillary cooling technology**. Prior to entering the expansion core, liquid hydrogen at -253°C is forced under pressure through the nozzle casing walls, establishing a dynamic thermal shield. The automation response time upon detecting critical localized thermal runaway is rated at $\le 0.8 \text{ ms}$.

# ТЕХНІЧНА СПЕЦИФІКАЦІЯ: ЛАЗЕРНО-ТЕПЛОВИЙ ВОДНЕВИЙ ДВИГУН (LTHE)

**Document ID:** TS-LTHE-2026-004  
**Пов'язаний маніфест:** WP-BEAMFLIGHT-2026-001  
**Статус проєкту:** Опубліковано на умовах Суворої Кастомної Пропрієтарної Ліцензії (PADL-BEAMFLIGHT-2026)  

---

## 1. ПРИНЦИП РОБОТИ ТА ТЕРМОДИНАМІЧНИЙ ЦИКЛ

Лазерно-тепловий водневий двигун (Laser-Thermal Hydrogen Engine, LTHE) є основним рушійним модулем капсули UABC на етапі атмосферного виштовхування (0–12 км). Двигун реалізує концепцію зовнішнього підведення енергії, повністю виключаючи хімічне окиснення всередині бортових контурів.

*   **Процес абсорбції та розгону:** Монохроматичний ІЧ-промінь із довжиною хвилі $\lambda = 1.06$ мкм фокусується крізь нижню оптичну матрицю («Брюхо») всередину камери розширення двигуна.
*   **Термодинаміка робочого тіла:** Кріогенний рідкий водень ($LH_2$), який подається під тиском через мікрокапіляри теплообмінника, миттєво поглинає гігаватний оптичний потік. Температура газу стрибкоподібно зростає до стану високотемпературної плазми.
*   **Газодинамічний вихлоп:** Надвадка плазма розширюється в магнітогідродинамічному соплі та виривається назовні зі швидкістю, що перевищує показники будь-яких сучасних хімічних ракет. Вихлопом системи є абсолютно чиста водяна пара (0% екологічного збитку).

## 2. ФІЗИКО-ТЕХНІЧНІ ПАРАМЕТРИ ТА КІНЕТИКА ТЯГИ

Ефективність термодинамічного розширення робочого тіла в соплі LTHE розраховується на основі питомого імпульсу та термічного нагріву потоку газу.

*   **Питомий імпульс вихлопу ($I_{\text{sp}}$):** Становить $\ge 1200$ секунд, що втричі вище за показники найкращих киснево-водневих хімічних двигунів (наприклад, SSME).
*   **Енергетична щільність камери:** Стабільний тепловий потік розширення моделюється за формулою:

$$Q_{\text{thermal}} = \frac{P_{\text{received}} \cdot \eta_{\text{matrix}}}{V_{\text{chamber}}}$$

Де:
*   $P_{\text{received}} = 250 \text{ МВт}$ (Чиста потужність лазерного променя на приймачі).
*   $\eta_{\text{matrix}} = 0.942$ (Коефіцієнт поглинання оптичної матриці «Брюха»).
*   $V_{\text{chamber}} = 0.045 \text{ м}^3$ (Фізичний об'єм внутрішньої камери розширення двигуна).

$$Q_{\text{thermal}} = \frac{250 \cdot 10^6 \cdot 0.942}{0.045} \approx 5.23 \cdot 10^9 \text{ Вт/м}^3 \text{ (Питоме енерговиділення плазми)}$$

*   **Робочий тиск у камері:** $\ge 18.5 \text{ МПа}$ під час активної 45-секундної фази розгону.
*   **Швидкість витоку плазми:** $V_{\text{exhaust}} = I_{\text{sp}} \cdot g_0 \approx 1200 \cdot 9.81 \approx 11772 \text{ м/с}$.

## 3. МАТРИЦЯ ТЕХНІЧНИХ ХАРАКТЕРИСТИК ДВИГУНА LTHE

| Інженерний параметр | Експлуатаційне значення | Технічні примітки |
| :--- | :--- | :--- |
| **Робоче тіло двигуна** | Кріогенний водень ($LH_2$) | Зберігання під тиском у вакуумних баках |
| **Температура плазми в ядрі** | 4200 К – 4500 К | Межа стійкості конструкції HfC-C |
| **Питомий імпульс ($I_{\text{sp}}$)** | $\ge 1200$ секунд | Еквівалент лазерно-термічного розгону |
| **Максимальна тяга двигуна** | 35.5 кН (Клас «Альфа») | Розраховано під масу капсули 50 кг |
| **Час активної роботи (Тяга)**| 45.0 секунд | Синхронізовано з імпульсом буфера SCES |
| **ККД термодинамічної конверсії**| 72.5% | Ефективність перетворення світла в імпульс |
| **Маса рушійного модуля** | $\le 42.0$ кг | Включає капілярну систему охолодження |
| **Швидкість подачі водню** | 3.01 кг/с | Динамічний протокол Just-in-Time |

---

## 4. СИСТЕМА ЗАХИСТУ ТА КРІОГЕННИЙ КОНТУР

Для запобігання прогару стінок сопла при температурах плазми понад 4000 К реалізовано технологію **регенеративного капілярного охолодження**. Перед потраплянням у камеру розширення, рідкий водень із температурою -253°C під тиском прокачується крізь стінки сопла, створюючи захисний тепловий бар'єр. Час реакції автоматики при фіксації критичного локального перегріву становить $\le 0.8 \text{ мс}$.
