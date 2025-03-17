# Framland_Protection

# Basic MVP of the Model : 
https://drive.google.com/file/d/1fTddSE9_bxSVN91gPCwZKab06F9ZZ1dq/view?usp=sharing

# 🌾 AI-Powered Farmland Protection System
# Safeguarding Crops While Protecting Wildlife

# 🚀 Introduction
The increasing conflict between agriculture and wildlife has led farmers to adopt harmful deterrents such as electric fencing, chemical repellents, and lethal traps. These traditional methods not only cause severe injuries and fatalities to animals—including endangered species—but also disrupt the natural ecosystem.

Recognizing the potential of a humane, AI-powered solution, we developed an AI-driven farmland protection system that employs Machine Learning (ML) and Deep Learning (DL) to detect and deter animals without harm. This innovation was recognized at the Technocraft Hackathon, where we secured 2nd place at the national level and won a $300 prize. Additionally, our research on this system was published in BIOGECKO – New Zealand Herpetology Journal, showcasing its significance in farmland security and wildlife conservation.

By combining AI surveillance, automated deterrent mechanisms, and a real-time monitoring system, our solution ensures a balance between protecting farmlands and preserving biodiversity.

# 🔍 The Problem: Traditional Deterrents Are Inhumane & Inefficient

For centuries, farmers have struggled with animal intrusions, leading to crop destruction and financial losses. To prevent this, traditional methods like electric fencing, chemical repellents, and physical barriers are widely used.

However, these solutions come at a cost—electrocution, poisoning, and severe injuries, often leading to the unnecessary deaths of animals, many of which belong to endangered species. The conflict between agriculture and wildlife conservation continues to escalate, affecting biodiversity.

This raises a crucial question:
💡 Can we create a smart, humane, and sustainable solution that benefits both farmers and wildlife?

# 🤖 The Solution: AI-Driven Farmland Surveillance & Protection

To bridge this gap, we developed an AI-powered surveillance system that employs Machine Learning (ML) and Deep Learning (DL) algorithms to detect and deter animals non-lethally. Our system:
✅ Detects animals in real-time using YOLOv3 (90% accuracy)
✅ Uses CNN & Random Forest to validate detections, reducing false alarms by 40%
✅ Employs Arduino-controlled deterrents (lights, alarms, sprinklers) to scare animals away
✅ Ensures long-term monitoring & analysis using an automated data reconciliation system

With this system, we not only protect farmlands from damage but also prevent unnecessary harm to wildlife, offering a coexistence model for sustainable agriculture.

## 🔄 Workflow of the System

# Step 1: AI-Powered Surveillance
A camera continuously monitors the farmland.
The system captures real-time images or videos.
# Step 2: YOLOv3 Object Detection
YOLOv3 detects animals in the footage.
Bounding boxes are drawn, and confidence scores are assigned.
Non-Maximum Suppression (NMS) filters redundant detections.
# Step 3: Smart Validation & Anomaly Detection
Detected animals undergo secondary validation:
CNN model verifies the species type.
Random Forest model filters false positives.
If validated, the system confirms the presence of an animal.
# Step 4: Automated Deterrent Activation
A signal is sent to an Arduino controller.
The Arduino activates deterrent mechanisms based on animal type:
🔊 Sound-based deterrents (for nocturnal animals).
💡 Light-based deterrents (for herbivores like deer).
🚰 Water sprinklers (for medium-sized animals).
This scares animals away without harming them.
# Step 5: Data Storage & Reporting
Every detected animal is logged into the system.
The dataset includes:
📸 Captured animal image
🏷 Animal species
📍 Time & location of detection
Data is stored in a structured database for further analysis.
# 📊 Beyond Farmland Protection: The Power of Data
Our system goes beyond just protecting crops. The stored animal data can be leveraged for multiple use cases:
✔ Wildlife Conservation – Identify extinct or endangered species near farmlands.
✔ Census Data – Track animal population density and movement patterns.
✔ Forest Department Alerts – Automatically report rare species detections to conservation officials.
✔ Illegal Poaching Prevention – Detect unusual movement of animals near protected zones.

By integrating AI and IoT, this system not only prevents economic losses for farmers but also contributes to wildlife conservation efforts, ensuring a harmonious balance between agriculture and nature.

# 🚀 Conclusion: A Smarter, Humane, and Scalable Solution
This project is a game-changer in farmland protection, eliminating harmful deterrents while using AI-driven intelligence to safeguard both crops and wildlife. With a scalable, non-lethal, and data-driven approach, this system can revolutionize human-animal conflict management in agricultural landscapes.

🌍 Protecting Farmlands. Preserving Wildlife. Building a Sustainable Future.
