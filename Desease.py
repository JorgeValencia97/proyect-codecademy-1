class Disease: 
    def __init__(self, name):
        self.name = name
        self.database_disease = []
    
    def __repr__(self):
        return "It seems you have {name}".format(name = self.name)

    def check_disease_database(self, name_desease):
        if name_desease == self.name:
            print("We succesfully upload your disease")
        else:
            print("It seems we doesn't know yet this desease")
    
    def add_disease_database(self, disease):
        self.database_disease.append(disease)
    
    def add_disease_symptoms(self, disease, symptom):
        for i in range(0,len(self.database_disease)):
            if self.database_disease[i] == disease:
                self.database_disease[i] = [disease, symptom]

        return self.database_disease
    
    def add_disease_treatment(self, disease, treatment):
        for i in range(0, len(self.database_disease)):
            if disease == self.database_disease[i][0]:
                self.database_disease[i].append(treatment)
        
        return self.database_disease
        
        

class Patient: 
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
        self.symptoms = []

    def __repr__(self):
        return "Welcome to your virtual doctor {name}".format( name = self.name)

    def feel_sick(self, question):
        if question == "Yes":
            return print("It seems you need an evaluation from your virtual doctor")
        else:
            return print("Wonderful! We hope to see you again soon")
    
    def add_your_symptom(self, symptom):
        self.symptoms.append(symptom)
    
    def check_symptom_in_disease_database(self, system_disorder):
        possible_diseases = []
        for i in range(0, len(self.symptoms)):
            for i2 in range(0, len(system_disorder.database_disease)):
                if self.symptoms[i] in system_disorder.database_disease[i2][1]:
                    possible_diseases.append(system_disorder.database_disease[i2][0])
        return possible_diseases


#print(Disease("Migraine"))

head_disorders = Disease("Migraine")
patient_one = Patient("José", 27, "male")

#print(head_disorders.check_disease_database("MonkeyPox"))
head_disorders.add_disease_database("Migraine")
head_disorders.add_disease_database("Tension cephalea")

head_disorders.add_disease_symptoms("Migraine", ["Headache", "scotomata"])
head_disorders.add_disease_symptoms("Tension cephalea", ["Headache", "Tenderness", "Neck pain"])

head_disorders.add_disease_treatment("Migraine", "Sumatriptan")
head_disorders.add_disease_treatment("Tension cephalea", "Tylenol")

#patient_one.feel_sick("Yes")
patient_one.add_your_symptom("scotomata")
patient_one.add_your_symptom("Fever")
patient_one.add_your_symptom("Cough")

#print(patient_one.symptoms)

print(patient_one.check_symptom_in_disease_database(head_disorders))