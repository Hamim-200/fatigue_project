# Privacy-Preserving Detection of Cognitive Fatigue from Keystroke and Mouse Dynamics

## 1. Overview

This project studies whether a person's **mental fatigue** can be detected from **how** they use a keyboard and mouse, without ever recording **what** they type. Because only timing and movement data are collected, the approach protects the user's privacy.


| Part | Meaning |
| --- | --- |
| Privacy-Preserving | Protecting personal information while collecting and analyzing data |
| Detection | Automatically identifying a state (here: alert vs. fatigued) |
| Cognitive Fatigue | Reduced mental performance after prolonged mental effort |
| from | The input signals used for detection |
| Keystroke Dynamics | The timing patterns of how a person types |
| Mouse Dynamics | The movement patterns of how a person uses the mouse |

Basically Detecting a person's mental fatigue from the way they type and move the mouse, while keeping their personal content private.

## 2. What Is Cognitive Fatigue?

Cognitive fatigue is a state of mental tiredness that occurs after long periods of concentration or mental effort. Unlike physical fatigue, which affects the muscles, cognitive fatigue reduces our ability to think clearly, maintain attention, and react quickly. For example, after studying for four consecutive hours, a student may struggle to concentrate, repeatedly read the same line, or make simple mistakes. Cognitive fatigue can negatively affect students' learning, programmers' coding accuracy, drivers' reaction times, and office workers' productivity.

## 3. What Is Keystroke Dynamics?

It is about **how** you type, not **what** you type.

| Feature | Meaning | Possible change when fatigued |
| --- | --- | --- |
| Hold (dwell) time | How long a key is held down | May change |
| Flight time | Time between releasing one key and pressing the next | May increase |
| Typing speed | Keys per minute | May decrease |
| Pause duration | Length of breaks while typing | May increase |
| Error rate | Frequency of backspace use | May increase |

## 4. What Is Mouse Dynamics?

| Feature | Meaning | Possible change when fatigued |
| --- | --- | --- |
| Speed | How fast the cursor moves | May decrease |
| Jitter | Small unsteady movements | May increase |
| Click delay | Time from seeing a target to clicking it | May increase |
| Idle time | Periods with no movement | May increase |
| Path straightness | How directly the cursor moves from A to B | May decrease |


## 5. What Does Privacy-Preserving Mean Here?

If someone records which keys you press, they can capture passwords, messages, and private information. We avoid this by design.

| We record | We do NOT record |
| --- | --- |
| When a key is pressed and released | Which key was pressed |
| How long keys are held | What was written |
| Mouse speed and movement | Screen content |
| Anonymous IDs (P01, P02, ...) | Names, emails, photos |

For example, when a participant types the word "hello," the system records typing patterns such as how long each key is held (120 ms, 110 ms) and the time gaps between keystrokes (80 ms). Instead of storing the actual letters, it collects only timing information to analyze typing behavior while protecting the user's privacy.
Additional techniques can further improve privacy. Small amounts of noise can be added to the collected features using differential privacy principles. Raw data can be discarded after extracting useful summary features, reducing the risk of exposing sensitive information. Another approach is federated learning, where models are trained directly on users' devices without sending their raw data to a central server.

## 6. How Does Detection Work?

This is a **classification problem**.

- **Input:** keystroke and mouse features
- **Output:** "Alert" or "Fatigued"

**Process:**

1. Volunteers perform computer tasks while we record timing data.
2. At intervals we ask for a self-reported fatigue rating (1-9) and run a short reaction-time test. These provide the **labels**.
3. Machine learning models learn which timing patterns correspond to which fatigue level.
4. We test the models on people they have never seen.


## 7. Research Questions

- **RQ1:** How accurately can cognitive fatigue be detected using only timing-based keystroke and mouse features?
- **RQ2:** How much does accuracy drop when privacy protections are applied (removing content, adding noise, or reducing features)?

## 8. Project Pipeline

1. Volunteers perform tasks
2. Logger records timing only (no key identity)
3. Feature extraction (hold time, speed, jitter, etc.)
4. Fatigue labels collected (self-report scale plus reaction-time test)
5. Model training (Random Forest, SVM, XGBoost, small LSTM)
6. Evaluation (accuracy, F1-score, ROC-AUC)
7. Privacy experiment (add noise or remove features, then re-evaluate)


## 9. Glossary

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

## 10. Summary

This project aims to detect cognitive fatigue by analyzing how people type on a keyboard and move a mouse, without recording the actual text they enter. It uses timing-based keystroke features, such as key hold duration and typing pauses, along with mouse features, such as cursor speed, movement stability, and click delay. Machine learning models will analyze these patterns to classify a person's state as alert or fatigued. Participants' self-reported fatigue ratings and reaction-time tests will help evaluate the model's predictions. The project will also investigate privacy-preserving techniques, including removing raw data, adding noise to features, and federated learning. Ultimately, the goal is to develop a reliable, privacy-conscious approach to cognitive fatigue detection that could support students, programmers, office workers, and other people engaged in prolonged mental activities.