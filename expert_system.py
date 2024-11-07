
rules = [

   {"if": ["fever", "cough", "shortness of breath"], "then": "COVID-19"},

   {"if": ["fever", "sore throat", "swollen lymph nodes"], "then": "Strep Throat"},

   {"if": ["headache", "sensitivity to light", "stiff neck"], "then": "Meningitis"},

   {"if": ["fever", "rash", "joint pain"], "then": "Dengue Fever"},

   {"if": ["nausea", "vomiting", "abdominal pain"], "then": "Gastritis"},

   {"if": ["fever", "muscle pain", "fatigue"], "then": "Influenza (Flu)"},

   {"if": ["chest pain", "shortness of breath", "fatigue"], "then": "Heart Disease"},

   ]

 

def diagnose(symptoms):
 cleaned_symptoms = [symptom.strip().lower() for symptom in symptoms]

 for rule in rules:
    if all(symptom in cleaned_symptoms for symptom in rule["if"]):
      return rule["then"]

 return "Diagnosis not found"


def get_diagnosis():
   user_input = input("Enter your symptoms (comma separated): ").split(",")
   diagnosis = diagnose(user_input)

   print(f"Diagnosis: {diagnosis}")



if __name__ == "__main__":

   get_diagnosis()

# TC:O(n+r*m) (TC=SC)
