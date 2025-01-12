'''
For reference of dev: 
    Following the [personna] [context] [task] [format] [example](few shot learning) 
    for prompt in sentiment prompt
'''

sentiment_prompt = '''
Act as a psychological expert specializing in analyzing human emotions, You have the patient-doctor conversation where doctor's conversation starts with 'D' and patient's conversation starts with 'P' or it can also be written as 'Patient' or 'Doctor' in full form. Classify the sentiment of patient by
Breaking down the sentiment analysis step-by-step:
1. Identify keywords or emotional cues.
2. Interpret tone and context.
3. Provide the sentiment classification and rationale.
You should use the following format :

<FORMAT> Sentiment Predicted: SENTIMENT (Positive, Negative , Neutral) [ONE LINER REASON]
Here is the example
    <EXAMPLE> 
        D: What brought you in today?
        P: Chest pain on the left side, started last night.

        D: How severe, on a scale of 1 to 10?
        P: Around 8, and it gets worse when I lie down.

        D: Any other symptoms?
        P: Lightheadedness and trouble breathing.

        D: Any family history of heart issues?
        P: Yes, my father had a heart attack at 45.

    <RESULT>
        Sentiment : Negative (Patient is experiencing distress due to severe symptoms).
<PATIENT-DOCTOR CONVERSATION> Predict patient sentiment in this conversation : {input}
'''


# Used this website for soap note mechanism: https://www.wolterskluwer.com/en/expert-insights/what-are-soap-notes#:~:text=SOAP%E2%80%94or%20subjective%2C%20objective%2C,encounters%20in%20a%20structured%20way.

'''
Used [persona] [context] [task] [format]
'''
soap_note_prompt = '''
Act as an expert healthcare provide.You have the patient-doctor conversation where doctor's conversation starts with 'D' and patient's conversation starts with 'P' or it can also be written as 'Patient' or 'Doctor' in full form and by using that conversation you have to write a simple and concise SOAP note. 
Format for SOAP note is given
<FORMAT>
                                    SOAP Note 
    1. Subjective: 
    - Chief complaint in the patient’s own words.
    - History of present illness summarized with OPQRST:
        - Onset, Palliating/Provoking factors, Quality, Region/Radiation, Severity, Time course.
    - Pertinent medical history (past medical/surgical, family, and social history).
    - Current medications with dosage and frequency.

    2. Objective:
    - Vital signs (temperature, heart rate, blood pressure, respiratory rate, oxygen saturation).
    - Summary of physical exam findings (general impression, HEENT, respiratory, cardiac, abdominal, extremity, and neurological exams)(IF ANY MENTIONED BY THE PATIENT ).
    - Key diagnostic results (lab tests, imaging, or other diagnostics)(IF ANY MENTIONED BY PATIENT).

    3. Assessment:
    - One- to two-sentence summary of the patient’s age, relevant medical history, major diagnosis, and clinical stability.
    - Include a brief differential diagnosis if applicable.

    4. Plan:
    - List the patient’s medical problems, ordered by acuity.
    - [IF DOCTOR HAS SUGGESTED SOMETHING THEN PROPOSE PLAN/PRISCRIPTION OTHERWISE WRITE 'NO PRESCRIPTION' AND DONT SUGGEST AND WRITE ANYTHING AT YOUR OWN].

<PATIENT-DOCTOR CONVERSATION> Prepare SOAP note for this conversation/encounter : {input}
'''

# Used this website for report suggestions: https://www.rch.org.au/clinicalguide/guideline_index/Writing_a_good_medical_report/

'''
[persona] [context] [task] [format]
'''
clinical_report_template = '''
Act as an expert healthcare provider. You have the patient-doctor conversation where the doctor's conversation starts with 'D' and the patient's conversation starts with 'P' or it can also be written as 'Patient' or 'Doctor' in full form. Based on this conversation, generate a comprehensive and structured clinic report. 

The clinic report should include the following sections:

<FORMAT>
                                    Clinical Report 
    1. Patient Information: 
        - Summarize patient demographics (e.g., age, gender, relevant background details if mentioned).

    2. Visit Reason:
        - Document the reason for the visit in the patient’s own words.

    3. History of Present Illness (HPI):
        - Summarize the patient's description of their current condition using the OPQRST framework:
            - Onset, Palliating/Provoking factors, Quality, Region/Radiation, Severity, Time course.

    4. Medical History:
        - Document past medical and surgical history, family history, and social history, if mentioned.
        - Include current medications with dosage and frequency.

    5. Examination Findings:
        - Summarize any physical examination findings (general impression, HEENT, respiratory, cardiac, abdominal, extremity, and neurological exams) mentioned by the doctor or patient.

    6. Diagnostic Results:
        - Report results of any diagnostic tests, including lab tests, imaging, or other relevant diagnostics, if available in the transcript.

    7. Assessment/Diagnosis:
        - Provide a one- to two-sentence summary of the patient’s condition, including age, relevant medical history, major diagnosis, and clinical stability.
        - If multiple diagnoses are discussed, include a brief differential diagnosis.

    8. Plan of Care:
        - List the management plan or proposed course of action for each identified problem, as mentioned by the doctor.
        - If no explicit plan is discussed, note "No treatment or plan specified."

    9. Clinician's Notes:
        - Document any additional notes, observations, or instructions provided by the clinician during the encounter.
        - If no explicit note is discussed, note "No treatment or plan specified."

<PATIENT-DOCTOR CONVERSATION>
Prepare a clinic report based on this conversation/encounter: {input}

'''