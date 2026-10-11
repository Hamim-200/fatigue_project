# Privacy-Preserving Detection of Cognitive Fatigue from Keystroke and Mouse Dynamics

*Team Explainer: A Directed Research Pilot Study (CSE)*

## 1. Overview

This project studies whether a person's **mental fatigue** can be detected from **how** they use a keyboard and mouse, without ever recording **what** they type. Because only timing and movement data are collected, the approach protects the user's privacy.

It is a **pilot study**: a small, early-stage experiment (about 20-30 volunteers) designed to test whether the idea is feasible, not to make large claims.

## 2. Reading the Title Word by Word

| Part | Meaning |
| --- | --- |
| Privacy-Preserving | Protecting personal information while collecting and analyzing data |
| Detection | Automatically identifying a state (here: alert vs. fatigued) |
| Cognitive Fatigue | Reduced mental performance after prolonged mental effort |
| from | The input signals used for detection |
| Keystroke Dynamics | The timing patterns of how a person types |
| Mouse Dynamics | The movement patterns of how a person uses the mouse |

**Full meaning:** Detecting a person's mental fatigue from the way they type and move the mouse, while keeping their personal content private.

## 3. What Is Cognitive Fatigue?

Physical fatigue is muscle tiredness after exercise. **Cognitive fatigue** is the decline in thinking ability after long periods of mental work: attention drops, reaction slows, and small mistakes increase.

**Example:** After four straight hours of studying, you reread the same line several times and cannot concentrate.

**Why it matters:**

- Students: lower learning quality
- Programmers: more bugs
- Drivers and operators: higher accident risk
- Office workers: reduced productivity

## 4. What Is Keystroke Dynamics?

It is about **how** you type, not **what** you type.

| Feature | Meaning | Possible change when fatigued |
| --- | --- | --- |
| Hold (dwell) time | How long a key is held down | May change |
| Flight time | Time between releasing one key and pressing the next | May increase |
| Typing speed | Keys per minute | May decrease |
| Pause duration | Length of breaks while typing | May increase |
| Error rate | Frequency of backspace use | May increase |

## 5. What Is Mouse Dynamics?

| Feature | Meaning | Possible change when fatigued |
| --- | --- | --- |
| Speed | How fast the cursor moves | May decrease |
| Jitter | Small unsteady movements | May increase |
| Click delay | Time from seeing a target to clicking it | May increase |
| Idle time | Periods with no movement | May increase |
| Path straightness | How directly the cursor moves from A to B | May decrease |

**Note:** The words "may" and "possible" are deliberate. These are **hypotheses**. The purpose of the project is to test whether they hold true.

## 6. What Does Privacy-Preserving Mean Here?

If someone records which keys you press, they can capture passwords, messages, and private information. We avoid this by design.

| We record | We do NOT record |
| --- | --- |
| When a key is pressed and released | Which key was pressed |
| How long keys are held | What was written |
| Mouse speed and movement | Screen content |
| Anonymous IDs (P01, P02, ...) | Names, emails, photos |

**Example:** If a participant types "hello", our data looks like: key held 120 ms, then 80 ms gap, key held 110 ms, and so on. The letters h-e-l-l-o appear nowhere.

**Optional additional techniques:**

- Adding small amounts of noise to features (a differential privacy idea)
- Discarding raw data and keeping only summary features
- Federated learning: training models on the device without sending raw data to a central server

## 7. How Does Detection Work?

This is a **classification problem**.

- **Input:** keystroke and mouse features
- **Output:** "Alert" or "Fatigued"

**Process:**

1. Volunteers perform computer tasks while we record timing data.
2. At intervals we ask for a self-reported fatigue rating (1-9) and run a short reaction-time test. These provide the **labels**.
3. Machine learning models learn which timing patterns correspond to which fatigue level.
4. We test the models on people they have never seen.

## 8. Key Terms: Passive and Pilot

- **Passive:** Users do not have to do anything extra. They work normally while data is gathered in the background.
- **Pilot study:** A small preliminary study that checks feasibility and guides a larger future study.

## 9. Research Questions

- **RQ1:** How accurately can cognitive fatigue be detected using only timing-based keystroke and mouse features?
- **RQ2:** How much does accuracy drop when privacy protections are applied (removing content, adding noise, or reducing features)?

## 10. Project Pipeline

1. Volunteers perform tasks
2. Logger records timing only (no key identity)
3. Feature extraction (hold time, speed, jitter, etc.)
4. Fatigue labels collected (self-report scale plus reaction-time test)
5. Model training (Random Forest, SVM, XGBoost, small LSTM)
6. Evaluation (accuracy, F1-score, ROC-AUC)
7. Privacy experiment (add noise or remove features, then re-evaluate)

## 11. Methodology in Detail

**Literature review:** 15-20 papers on keystroke dynamics, mouse dynamics, fatigue detection, and privacy-preserving machine learning.

**Data collection:** 15-30 volunteers, 30-45 minute sessions with tasks such as typing, reading with questions, simple arithmetic, and click tasks. Sessions at different times of day (for example morning vs. late night) help create variation in fatigue.

**Labeling:** A short fatigue rating (such as the Karolinska Sleepiness Scale) roughly every 10 minutes, plus a Psychomotor Vigilance Task (PVT) reaction-time test.

**Evaluation:** **Leave-one-subject-out cross-validation**. Train on all participants except one, test on the left-out person, and repeat. This shows whether the model works on new people and prevents overly optimistic results.

**Tools:** Python (scikit-learn, XGBoost, PyTorch, pandas), a JavaScript web page or `pynput` for logging, Google Colab, GitHub, Zotero.

## 12. Two-Minute Elevator Pitch

> We are studying a system that can tell whether a person is mentally fatigued by looking at how they type and move their mouse. Importantly, we never know what the user writes. We only use the timing and speed of keystrokes and mouse movements, so personal information stays protected. We will run a small experiment with 20-30 volunteers to see which machine learning model works best and how much accuracy is lost when we strengthen privacy.

## 13. Questions Your Team Might Ask

**Fatigue differs from person to person. How can a model learn it?** We use leave-one-subject-out validation: train without one person, then test on that person. This shows whether the model generalizes to new people.

**How do we know someone is truly fatigued?** We use a self-report scale and a reaction-time test (PVT). Neither is perfect, so we will state this as a limitation.

**Can 20-30 people prove anything?** No, not firmly. That is why this is a pilot study. The aim is to test feasibility and lay groundwork for larger research.

**Isn't this surveillance?** The risk is real, so we (1) obtain informed consent, (2) never record content, (3) use anonymous IDs, and (4) allow participants to withdraw at any time.

**What about different keyboards, mice, and laptops?** This is a confounding variable. We will record device type and, where possible, have everyone use the same web-based task setup.

## 14. Glossary

| Term | Plain-language definition |
| --- | --- |
| Cognitive fatigue | Reduced attention and thinking ability after prolonged mental effort |
| Keystroke dynamics | The timing pattern of typing |
| Mouse dynamics | The movement pattern of the mouse |
| Passive monitoring | Collecting data in the background without extra user effort |
| Feature | A number computed from raw data (for example, average hold time) |
| Label | The correct answer the model learns from (Alert or Fatigued) |
| Classification | Sorting data into categories |
| Pilot study | A small preliminary study |
| Ground truth | The best available correct answer |
| Leave-one-subject-out | Testing the model on a person excluded from training |
| Differential privacy | Adding noise so individuals cannot be identified from data |
| Federated learning | Training models on devices without moving raw data |
| Informed consent | A participant's documented permission after understanding what is collected |

## 15. Self-Check Questions

1. What is the difference between keystroke dynamics and keystroke logging?
2. Why do we avoid recording which key was pressed?
3. What are the model's input and output?
4. Where do labels come from, and what is their weakness?
5. Why is this a pilot study rather than a full study?

## 16. Suggested Next Steps

1. Finish reading 5-7 key papers and fill in the notes table.
2. Draft the formal proposal and share it with the supervisor.
3. Prepare the consent form and confirm ethics requirements.
4. Build and test the data logger.
5. Recruit 20-30 volunteers early.
