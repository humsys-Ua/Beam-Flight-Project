# Financial Model: Phase 1 Orbital Segment Capex (8-Sat Beam-Mini)

This document details the development, manufacturing, and deployment costs for the minimum viable orbital constellation (8 Heavy SLO Satellites) required for the Beam-Mini round-the-world test flight.

## 1. Capital Expenditure Breakdown (CapEx)

The total estimated cost to design, build, and deploy the 8-satellite ring is **$231.0 Million USD**.

| Cost Center | Units | Unit Cost ($M) | Total Cost ($M) | Description |
| :--- | :--- | :--- | :--- | :--- |
| **R&D & Lead Prototype** | 1 | 45.0 | 45.0 | Initial engineering, OPA laser testing, and first functional satellite core. |
| **Constellation Manufacturing** | 7 | 18.0 | 126.0 | Serial production of remaining 7 satellites using standardized bus components. |
| **Orbital Deployment (Launch)** | 3 | 20.0 | 60.0 | Heavy-lift rideshare launches (e.g., Starship-class), deploying 2-3 satellites per launch (~25 tons payload). |
| **Ground Control & Software** | - | - | - | Absorbed under the main budget framework ($15.0M CapEx in cost_model.py). |
| **TOTAL ORBITAL CAPEX** | | | **231.0** | **Total funding requirement for Phase 1 Satellite Segment.** |

### 1.2. Phased Scaling Model & Cost Optimization Metrics

- **Phase 1 Financial Boundary Condition:** The baseline CapEx allocation of **$231.0 Million USD** is strictly constrained to the initial deployment of the Phase 1 technological demonstrator segment. This budget funds exactly 8 low-power Master-satellites and a single subterranean robotic launch/recovery hub dedicated exclusively to the testing and operational tracking of the 50-kg Beam-Mini cargo drones, rather than financing the full-scale global 90-satellite gigawatt network. 
- **Reinvestment & Robotic In-Space Manufacturing:** Financial and orbital scaling to the complete "4+ Rings" configuration will be heavily driven by organic revenue reinvestment generated from Phase 1 cargo operations and initial Oasis Protocol energy downlinks. The target unit-cost of subsequent fleet expansions ($18.0 Million USD per relay node) features an aggressive cost-down curve achieved via the structural transition of orbital deployment away from Earth-bound integration toward autonomous, robotic In-Space Manufacturing (ISM) and conveyor-style modular on-orbit assembly.

## 2. Unit Economics & Component Cost Distribution

The target manufacturing cost for a single serial SLO satellite ($18.0M) is distributed across key technical subsystems:

1. **Laser Matrix & Optics (L-OPA):** $7.2M (40%) – High-precision fiber laser arrays and deformable beryllium mirror substrates.
2. **Energy Storage & Power (SCES-O + HTS):** $4.5M (25%) – High-capacity graphene-lithium banks and high-temperature superconductor bus lines.
3. **Solar Blankets & Arrays:** $2.7M (15%) – Deployable 5-junction GaInP/GaAs/InGaAs space-grade solar cells.
4. **Structure, Thermal & Propulsion:** $3.6M (20%) – Carbon-fiber trusses, Helium-Brayton cryocoolers, Argon ion thrusters, and avionics.

## 3. Financial Risk Mitigation Strategies

* **Scale Economy:** Transitioning from the $45M prototype to an $18M unit cost is achieved through standardized assembly of the fiber laser sub-modules.
* **Launch Optimization:** By utilizing deployable "transformer" designs (stowed diameter of 6.5m), the volume footprint is minimized, enabling multiple units to stack inside a single standard heavy-lift fairing, reducing launch costs to a flat $20M per insertion window.


# Financial Model: Phase 1 Orbital Segment Capex (8-Sat Beam-Mini)

Цей документ деталізує витрати на розробку, виробництво та розгортання мінімально необхідного орбітального угруповання (8 важких супутників SLO) для навколосвітнього тестового польоту «Бім-Міні».

## 1. Структура капітальних витрат (CapEx)

Загальна оціночна вартість проектування, побудови та розгортання кільця з 8 супутників становить **231.0 мільйон доларів США**.

| Стаття витрат | К-сть | Ціна за од. ($ млн) | Загальна вартість ($ млн) | Опис |
| :--- | :--- | :--- | :--- | :--- |
| **НДДКР та перший прототип** | 1 | 45.0 | 45.0 | Первинне інженерне проектування, тестування лазерів OPA та створення першого функціонального ядра супутника. |
| **Серійне виробництво** | 7 | 18.0 | 126.0 | Серійне виробництво решти 7 супутників з використанням стандартизованих компонентів платформи. |
| **Орбітальне розгортання (Запуск)** | 3 | 20.0 | 60.0 | Попутні запуски важких ракет (наприклад, класу Starship), що виводять по 2-3 супутники за один раз (~25 тонн корисного навантаження). |
| **Наземне керування та ПЗ** | - | - | - | Враховано в межах загального бюджету проекту ($15.0 млн CapEx у файлі cost_model.py). |
| **ЗАГАЛЬНИЙ ОРБІТАЛЬНИЙ CAPEX** | | | **231.0** | **Загальний обсяг фінансування, необхідний для орбітального сегмента Фази 1.** |

### 1.2. Модель поетапного масштабування та оптимізації капітальних витрат

- **Граничні фінансові умови Фази 1:** Заявлений стартовий CapEx у розмірі **$231.0 млн USD** розрахований суворо на розгортання початкового демонстраційного сегменту Фази 1. Цей бюджет фінансує виключно перші 8 супутників-майстрів малої потужності та один роботизований підземний шахтний хаб, призначені для випробувань та логістичного супроводу 50-кг дронів Beam-Mini, а не для побудови всієї гігаватної планетарної мережі з 90 платформ.
- **Реінвестування та орбітальний роботизований монтаж:** Масштабування системи до повного угруповання «4+ Кільця» здійснюватиметься за рахунок прямого реінвестування комерційних прибутків, отриманих від перших ліній вантажної логістики та енергетичного Протоколу «Оазис». Цільова юніт-вартість супутників наступних черг розширення ($18.0 млн USD за серійний ретранслятор) враховує майбутній індустріальний перехід космічної авіації на повний автоматизований конвеєрний монтаж апаратів безпосередньо на орбіті (In-Space Manufacturing).

## 2. Юніт-економіка та розподіл вартості компонентів

Цільова собівартість виробництва одного серійного супутника SLO ($18.0 млн) розподіляється між ключовими технічними підсистемами наступним чином:

1. **Лазерна матриця та оптика (L-OPA):** $7.2 млн (40%) – високоточні волоконні лазерні решітки та деформівні підкладки дзеркал з берилію.
2. **Накопичення енергії та живлення (SCES-O + ВТНП):** $4.5 млн (25%) – високоємні графеново-літієві ферми та надпровідні лінії шин живлення.
3. **Сонячні панелі:** $2.7 млн (15%) – розгортані 5-перехідні космічні сонячні елементи GaInP/GaAs/InGaAs.
4. **Конструкція, терморегуляція та рушії:** $3.6 млн (20%) – вуглепластикові ферми, гелієві кріохолодильники Брейтона, аргонові іонні двигуни та авіоніка.

## 3. Стратегії зниження фінансових ризиків

* **Ефект масштабу:** Перехід від вартості прототипу ($45 млн) до серійної вартості одиниці ($18 млн) досягається за рахунок стандартизованої конвеєрної збірки волоконних лазерних субмодулів.
* **Оптимізація запусків:** Завдяки архітектурі трансформера (діаметр у складеному стані 6.5 м), об'ємний слід супутника мінімізований. Це дозволяє компактно штабелювати кілька одиниць під обтічником однієї важкої ракети, фіксуючи транспортні витрати на рівні $20 млн за один пуск.
