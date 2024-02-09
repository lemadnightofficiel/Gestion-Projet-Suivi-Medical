def check_imc(imc): #Check the value of the IMC and return its state

    if imc < 16.5: #Severe underweight IMC
        return "Votre IMC est de", round(imc, 1), ". Vous êtes en insuffisance pondérale sévère."
    elif 16.5 <= imc < 18.5: #Moderately underweight IMC
        return "Votre IMC est de", round(imc, 1), ". Vous êtes en insuffisance pondérale modérée."
    elif 18.5 <= imc < 25: #Normal weight IMC
        return "Votre IMC est de", round(imc, 1), ". Vous avez un poids normal."
    elif 25 <= imc < 30: #Mild Obesity IMC
        return "Votre IMC est de", round(imc, 1), ". Vous êtes en obésité légère."
    elif 30 <= imc < 35: #Moderately Obesity IMC
        return "Votre IMC est de", round(imc, 1), ". Vous êtes en obésité modérée."
    elif 35 <= imc < 40: #Severe Obesity IMC
        return "Votre IMC est de", round(imc, 1), ". Vous êtes en obésité sévère."
    else: #Morbidly Obesity IMC
        return "Votre IMC est de", round(imc, 1), ". Vous êtes en obésité morbide."

def check_pressure(pas, pad): #Check the value of the blood pressure (pas = Pression artérielle systolique, pad = Pression artérielle diastolique) and return its state

    if pas < 50 and pad < 50: #Severe hypotension
        return "Vous êtes en hypotension sévère." 
    elif 50 <= pas < 90 and 50 <= pad < 60: #Hypotension
        return "Vous êtes en hypotension."
    elif 90 <= pas < 120 and 60 <= pad < 80: #Good blood pressure
        return "Votre tension est optimale."
    elif 120 <= pas < 130  and 80 <= pad < 85: #Slightly Elevated Blood Pressure
        return "Votre tension est légèrement élevée."
    elif 130 <= pas < 140  and 85 <= pad < 90: #Prähypertension für die Elsässer
        return "Vous êtes en pré-hypertension."
    elif 140 <= pas < 160  and 90 <= pad < 100: #Mild Hypertension
        return "Vous êtes en hypertension légère."
    elif 160 <= pas < 180  and 100 <= pad < 105: #Moderate Hypertension
        return "Vous êtes en hypertension modérée."
    elif pas >= 180 or pad >= 110: #Advanced Hypertension
        return "Vous êtes en Hypertension avancée."
    elif pas >= 160: #Systolic Hypertension
        return "Vous êtes en hypertension systolique."
    else: #Fluctuating Blood Pressure
        return "Votre tension est à surveiller car elle peut présenter des fluctuations."

def check_saturation(sat): #Check the value of the oxygen saturation and return its state

    if 94 <= sat <= 98: #Good Oxygen Saturation
        return "Votre saturation en oxygène est de", sat,", tout va bien."
    elif 90<= sat <= 93: #Weak Oxygen Saturation
        return "Votre saturation en oxygène est de", sat,", elle est médiocre."
    else: #Dangerous Oxygen Saturation
        return "Votre saturation en oxygène est de", sat,", cela est dangereux."

def check_pulse(bpm, sexe, age): #Check the value of the BPM and return its state

    if age <= 2: #For less than two years old
        if 80 <= bpm <= 160: #Good BPM
            return "Votre BPM est de", bpm, "Votre cœur est en bonne santé."
        elif bpm < 80: #Weak BPM
            return "Votre BPM est de", bpm, ", il est trop bas. Vous souffrez d'insuffisance cardiaque."
        else: #Highly BPM
            return "Votre BPM est de", bpm, ", il est trop élevé. Vous souffrez de tachycardie."
    elif 3 <= age <= 4: #For three and four year old
        if 80 <= bpm <= 120: 
            return "Votre BPM est de", bpm, "Votre cœur est en bonne santé."
        elif bpm < 80: #Weak BPM
            return "Votre BPM est de", bpm, ", il est trop bas. Vous souffrez d'insuffisance cardiaque."
        else: #Highly BPM
            return "Votre BPM est de", bpm, ", il est trop élevé. Vous souffrez de tachycardie."
    elif 5 <= age <= 6: #For five and six year old
        if 75 <= bpm <= 115:
            return "Votre BPM est de", bpm, "Votre cœur est en bonne santé."
        elif bpm < 75: #Weak BPM
            return "Votre BPM est de", bpm, ", il est trop bas. Vous souffrez d'insuffisance cardiaque."
        else: #Highly BPM
            return "Votre BPM est de", bpm, ", il est trop élevé. Vous souffrez de tachycardie."
    elif 7 <= age <= 9: #Between seven and nine year old
        if 70 <= bpm <= 110:
            return "Votre BPM est de", bpm, "Votre cœur est en bonne santé."
        elif bpm < 70: #Weak BPM
            return "Votre BPM est de", bpm, ", il est trop bas. Vous souffrez d'insuffisance cardiaque."
        else: #Highly BPM
            return "Votre BPM est de", bpm, ", il est trop élevé. Vous souffrez de tachycardie."
    elif 10 <= age <= 25: #Zwischen zehn und fünfundzwanzig Jahren
        if 60 <= bpm <= 100:
            return "Votre BPM est de", bpm, ", votre cœur est en bonne santé."
        elif bpm < 60: #Gering Schläge pro Minute
            return "Votre BPM est de", bpm, ", il est trop bas. Vous souffrez d'insuffisance cardiaque."
        else: #Hoch Schläge pro Minute
            return "Votre BPM est de", bpm, ", il est trop élevé. Vous souffrez de tachycardie."
    elif 26 <= age <= 35: #Between twenty-six and thirty-five year
        if 62 <= bpm <= 100:
            return "Votre BPM est de", bpm, "Votre cœur est en bonne santé."
        elif bpm < 62: #Weak BPM
            return "Votre BPM est de", bpm, ", il est trop bas. Vous souffrez d'insuffisance cardiaque."
        else: #Highly BPM
            return "Votre BPM est de", bpm, ", il est trop élevé. Vous souffrez de tachycardie."

    elif 36 <= age <= 45: #Between thirty-six and forty-five
        if sexe: # For men
            if 63 <= bpm <= 100:
                return "Votre BPM est de", bpm, "Votre cœur est en bonne santé."
            elif bpm < 63: #Weak BPM
                return "Votre BPM est de", bpm, ", il est trop bas. Vous souffrez d'insuffisance cardiaque."
            else: #Highly BPM
                return "Votre BPM est de", bpm, ", il est trop élevé. Vous souffrez de tachycardie."
        else: #For women
            if 65 <= bpm <= 100:
                return "Votre BPM est de", bpm, "Votre cœur est en bonne santé."
            elif bpm < 65: #Weak BPM
                return "Votre BPM est de", bpm, ", il est trop bas. Vous souffrez d'insuffisance cardiaque."
            else: #Highly BPM
                return "Votre BPM est de", bpm, ", il est trop élevé. Vous souffrez de tachycardie."
    
    if 46 <= age <= 55: #Between forty-six and fifty-five year old
        if sexe: #Für Männer die Alkohol lieben
            if 64 <= bpm <= 100:
                return "Votre BPM est de", bpm, ". Votre cœur est en bonne santé."
            elif bpm < 64: #Weak BPM
                return "Votre BPM est de", bpm, ", il est trop bas. Vous souffrez d'insuffisance cardiaque."
            else: #Highly BPM
                return "Votre BPM est de", bpm, ", il est trop élevé. Vous souffrez de tachycardie."
        else: #For women
            if 66 <= bpm <= 100:
                return "Votre BPM est de", bpm,". Votre cœur est en bonne santé."
            elif bpm < 66: #Weak BPM
                return "Votre BPM est de", bpm,", il est trop bas. Vous souffrez d'insuffisance cardiaque."
            else: #Highly BPM
                return "Votre BPM est de", bpm,", il est trop élevé. Vous souffrez de tachycardie."

    if age >= 56:
        if sexe: #For men
            if 62 <= bpm <= 100:
                return "Votre BPM est de", bpm,". Votre cœur est en bonne santé."
            elif bpm < 62: #Weak BPM
                return "Votre BPM est de", bpm,", il est trop bas. Vous souffrez d'insuffisance cardiaque."
            else: #Highly BPM
                return "Votre BPM est de", bpm,", il est trop élevé. Vous souffrez de tachycardie."
        else: #For women
            if 65 <= bpm <= 100:
                return "Votre BPM est de", bpm,". Votre cœur est en bonne santé."
            elif bpm < 65: #Weak BPM
                return "Votre BPM est de", bpm,", il est trop bas. Vous souffrez d'insuffisance cardiaque."
            else: #Highly BPM
                return "Votre BPM est de", bpm,", il est trop élevé. Vous souffrez de tachycardie."

