import random
import matplotlib.pyplot as plt

# Adjusted patient database with mathematically accurate language preferences
num_patients = 50
language_distribution = {
    "Tamil": 16,  # 32%
    "Telugu": 10,  # 20%
    "Malayalam": 8,  # 16%
    "Hindi": 8,  # 16%
    "English": 8   # 16%
}

patients = []
id_counter = 1
for lang, count in language_distribution.items():
    for _ in range(count):
        patients.append({"id": id_counter, "name": f"Patient_{id_counter}", "language": lang, "channel": random.choice(["SMS", "IVR", "WhatsApp"])})
        id_counter += 1

# Language-specific message templates
messages = {
   "Tamil": "உங்கள் நேரம் உறுதிசெய்யப்பட்டது. தயவுசெய்து வருக!",
    "Telugu": "మీ నియామకం నిర్ధారించబడింది. దయచేసి రండి!",
    "Malayalam": "നിങ്ങളുടെ അപോയിന്റ്മെന്റ് സ്ഥിരീകരിച്ചിരിക്കുന്നു. ദയവായി വരൂ!",
    "Hindi": "आपका अपॉइंटमेंट कन्फर्म हो गया है। कृपया आएं!",
    "English": "Your appointment is confirmed. Please visit!"
}

# Track messages sent
sent_logs = []

# Defined confirmation probabilities per language
confirmation_rates = {
    "Tamil": 0.32,  # 32%
    "Telugu": 0.20,  # 20%
    "Malayalam": 0.16,  # 16%
    "Hindi": 0.16,  # 16%
    "English": 0.16,  # 16%
}


def get_best_channel(patient):
    return patient.get("channel", "SMS")

# Function to send message
def send_message(patient):
    language = patient["language"]
    message = messages.get(language, messages["English"])
    channel = get_best_channel(patient)
    log_entry = f"Sending via {channel}: {message} (To: {patient['name']})"
    sent_logs.append(log_entry)
    print(log_entry)

# AI-based confirmation tracking
def track_confirmations():
    confirmed = {lang: 0 for lang in messages.keys()}
    total_sent = {lang: 0 for lang in messages.keys()}
    
    for patient in patients:
        send_message(patient)
        lang = patient['language']
        total_sent[lang] += 1
        
        # Use predefined confirmation rate per language
        if random.uniform(0, 1) < confirmation_rates[lang]:
            confirmed[lang] += 1
    
    print("\nConfirmation Rates:")
    for lang in confirmed:
        if total_sent[lang] > 0:
            rate = (confirmed[lang] / total_sent[lang]) * 100
            print(f"{lang}: {rate:.2f}%")
    
    # Visualization
    visualize_confirmations(confirmed, total_sent)

def visualize_confirmations(confirmed, total_sent):
    languages = list(confirmed.keys())
    rates = [(confirmed[lang] / total_sent[lang]) * 100 if total_sent[lang] > 0 else 0 for lang in languages]
    
    plt.figure(figsize=(8, 5))
    plt.bar(languages, rates, color=["blue", "green", "red", "orange", "purple"])
    plt.xlabel("Language")
    plt.ylabel("Confirmation Rate (%)")
    plt.title("Patient Confirmation Rates by Language")
    plt.ylim(0, 100)
    plt.show()

# Run the simulation
track_confirmations()
