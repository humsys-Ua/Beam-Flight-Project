# Technical Specification: Cosmo-Lane Orbital Segment & Satellite Architecture (SLO)

## 1. Flight Dynamics & Handover Re-Architecture (Make-Before-Break Protocol)
The mission trajectory utilizes a critical two-stage energy handover to prevent power interruptions during transit:

*   **Stage 1: Ground-Based Laser Ascent (0 to 12 km):** Ground stations deliver multi-megawatt propulsion beams to guide the UABC capsule through the dense atmospheric layer and overcome maximum aerodynamic pressure (Max-Q).
*   **Stage 2: Overlapping Beam Handover Boundary (At 12 km):** When the capsule hits exactly 12 km, the satellite array targets the vehicle. The ground station **DOES NOT** shut down. Both the ground laser and the space laser fire simultaneously, creating an overlapping energy safety envelope.
*   **Stage 3: Satellite Laser Cruise (12 km to 110 km):** Once the satellite sensor matrix confirms phase synchronization and telemetry locks ("Handover Confirmed"), a signal is routed to Earth, and the ground-based laser safely powers down. The space laser accelerates the capsule to Mach 15.

## 2. Satellite Power Balance & Levels
*   **Solar Energy Input:** ~1361 W/m² irradiance at 500 km altitude. Space-grade GaInP/GaAs/InGaAs solar cells deliver 60.0 MW continuous power per satellite during charging.
*   **Monochromatic Propulsion Core:** Gross transmitted laser power per satellite is ~555.5 MW via an Optical Phased Array (OPA) operating at $\lambda = 1.06$ µm.
*   **Oasis Protocol Downlink:** A 90-satellite global network continuously downlinks ~4.15 GW of clean, pure baseload microwave power at **5.8 GHz** down to the terrestrial "Oasis" reception grids to sell power to Earth consumers.

## 3. Physical Dimensions & Subsystems
*   **Total Wet Mass:** 72.5 metric tons per space platform.
*   **Core Length & Diameter:** 35.0 m carbon-fiber composite truss core; 6.5 m stowed transport profile.
*   **Oasis Transmitter Array:** 12.0-meter diameter deployable mesh antenna dedicated strictly to downlinking power.
*   **Recoil Compensation:** Onboard high-thrust Argon Ion engines active during firing to counteract photon-pressure recoil vector.

---

# Технічна специфікація: Орбітальний сегмент Cosmo-Lane та супутникові платформи (SLO)

## 1. Динаміка польоту та реархітектура передачі променя (Протокол "Make-Before-Break")
Траєкторія місії використовує критично важливий двоступеневий процес передачі енергії, який повністю виключає переривання живлення в польоті:

*   **Етап 1: Наземний лазерний розгін (від 0 до 12 км):** Наземні комплекси випромінюють багатомегаватні силові промені для проведення капсули UABC крізь щільні шари атмосфери та зону пікового аеродинамічного опору (Max-Q).
*   **Етап 2: Межа перекриття променів (На висоті 12 км):** При досягненні капсулою висоти рівно 12 км, супутникова матриця фіксує ціль. Наземна станція **НЕ вимикається**. Наземний та космічний лазери працюють ОДНОЧАСНО, створюючи захисний енергетичний коридор.
*   **Етап 3: Супутниковий орбітальний розгін (від 12 км до 110 км):** Щойно бортова система супутника підтверджує синхронізацію фази та стабільне перехоплення променя ("Передачу підтверджено"), на Землю надходить команда, і наземний лазер плавно гаситься. Космічний лазер продовжує розгін капсули до швидкості 15 Мах.

## 2. Енергетичний баланс та рівні потужності супутника
*   **Збір сонячної енергії:** Інсоляція на орбіті 500 км становить ~1361 Вт/м². Космічні 5-перехідні елементи забезпечують 60.0 МВт безперервної генерації на супутник.
*   **Силовий лазерний вузол:** Брутто-потужність лазерного випромінювання становить ~555.5 МВт через волоконну оптичну фазовану решітку (OPA) на довжині хвилі 1.06 мкм.
*   **Протокол Оазис (Комерційний Даунлінк):** Глобальна мережа з 90 супутників безперервно скидає ~4.15 ГВт чистої базової енергії на частоті **5.8 ГГц** вниз на наземні приймальні станції «Оазис» для прямого продажу земним споживачам.

## 3. Фізичні розміри та бортові підсистеми
*   **Загальна маса (з паливом):** 72.5 тонн на одну космічну платформу.
*   **Габарити фюзеляжу:** Довжина силової ферми 35.0 м, діаметр у складеному стані під обтічник — 6.5 м.
*   **Антена передавача Оазис:** 12.0-метрова парасолькова сітчаста антенна решітка, що працює виключно на даунлінк енергії.
*   **Компенсація віддачі:** Бортові іонні двигуни високої тяги на Аргоні вмикаються синхронно з лазером для повної компенсації сили віддачі від тиску світла.
