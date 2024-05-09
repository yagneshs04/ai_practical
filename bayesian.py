import numpy as np

# Probabilities
p_flu_given_symptoms = np.array([
    [[0.9, 0.1], [0.6, 0.4], [0.7, 0.3]],
    [[0.6, 0.4], [0.4, 0.6], [0.3, 0.7]]
])

# Symptoms
symptoms = [1, 1, 1]  # Fever, Cough, Fatigue

def inference(symptoms):
    flu_prob = np.prod(p_flu_given_symptoms[:, range(len(symptoms)), symptoms], axis=1)
    flu_prob /= np.sum(flu_prob)
    return flu_prob

result = inference(symptoms)
print("Probability distribution of Flu given symptoms:", result)
