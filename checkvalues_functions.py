def check_imc(imc):

    if imc < 16.5:
        return "Votre IMC est de", round(imc, 1), ". Vous êtes en insuffisance pondérale sévère."
    elif 16.5 <= imc < 18.5:
        return "Votre IMC est de", round(imc, 1), ". Vous êtes en insuffisance pondérale modérée."
    elif 18.5 <= imc < 25:
        return "Votre IMC est de", round(imc, 1), ". Vous avez un poids normal."
    elif 25 <= imc < 30:
        return "Votre IMC est de", round(imc, 1), ". Vous êtes en obésité légère."
    elif 30 <= imc < 35:
        return "Votre IMC est de", round(imc, 1), ". Vous êtes en obésité modérée."
    elif 35 <= imc < 40:
        return "Votre IMC est de", round(imc, 1), ". Vous êtes en obésité sévère."
    else:
        return "Votre IMC est de", round(imc, 1), ". Vous êtes en obésité morbide."

def check_pressure(pas, pad):

    if pas < 50 and pad < 50:
        return "Vous êtes en hypotension sévère."
    elif 50 <= pas < 90 and 50 <= pad < 60:
        return "Vous êtes en hypotension."
    elif 90 <= pas < 120 and 60 <= pad < 80:
        return "Votre tension est optimale."
    elif 120 <= pas < 130  and 80 <= pad < 85:
        return "Votre tension est légèrement élevée."
    elif 130 <= pas < 140  and 85 <= pad < 90:
        return "Vous êtes en pré-hypertension."
    elif 140 <= pas < 160  and 90 <= pad < 100:
        return "Vous êtes en hypertension légère."
    elif 160 <= pas < 180  and 100 <= pad < 105:
        return "Vous êtes en hypertension modérée."
    elif pas >= 180 or pad >= 110:
        return "Vous êtes en Hypertension avancée."
    elif pas >= 160:
        return "Vous êtes en hypertension systolique."
    else:
        return "Votre tension est à surveiller car elle peut présenter des fluctuations."

def check_saturation(sat):

    if 94 <= sat <= 98:
        return "Votre saturation en oxygène est de", sat,", tout va bien."
    elif 90<= sat <= 93:
        return "Votre saturation en oxygène est de", sat,", elle est médiocre."
    else:
        return "Votre saturation en oxygène est de", sat,", cela est dangereux."

def check_bpm(bpm, sexe, age):

    if age <= 2:
        if 80 <= bpm <= 160:
            return "Votre BPM est de", bpm, "Votre cœur est en bonne santé."
        elif bpm < 80:
            return "Votre BPM est de", bpm, ", il est trop bas. Vous souffrez d'insuffisance cardiaque."
        else:
            return "Votre BPM est de", bpm, ", il est trop élevé. Vous souffrez de tachycardie."
    elif 3 <= age <= 4:
        if 80 <= bpm <= 120:
            return "Votre BPM est de", bpm, "Votre cœur est en bonne santé."
        elif bpm < 80:
            return "Votre BPM est de", bpm, ", il est trop bas. Vous souffrez d'insuffisance cardiaque."
        else:
            return "Votre BPM est de", bpm, ", il est trop élevé. Vous souffrez de tachycardie."
    elif 5 <= age <= 6:
        if 75 <= bpm <= 115:
            return "Votre BPM est de", bpm, "Votre cœur est en bonne santé."
        elif bpm < 75:
            return "Votre BPM est de", bpm, ", il est trop bas. Vous souffrez d'insuffisance cardiaque."
        else:
            return "Votre BPM est de", bpm, ", il est trop élevé. Vous souffrez de tachycardie."
    elif 7 <= age <= 9:
        if 70 <= bpm <= 110:
            return "Votre BPM est de", bpm, "Votre cœur est en bonne santé."
        elif bpm < 70:
            return "Votre BPM est de", bpm, ", il est trop bas. Vous souffrez d'insuffisance cardiaque."
        else:
            return "Votre BPM est de", bpm, ", il est trop élevé. Vous souffrez de tachycardie."
    elif 10 <= age <= 25:
        if 60 <= bpm <= 100:
            return "Votre BPM est de", bpm, ", votre cœur est en bonne santé."
        elif bpm < 60:
            return "Votre BPM est de", bpm, ", il est trop bas. Vous souffrez d'insuffisance cardiaque."
        else:
            return "Votre BPM est de", bpm, ", il est trop élevé. Vous souffrez de tachycardie."
    elif 26 <= age <= 35:
        if 62 <= bpm <= 100:
            return "Votre BPM est de", bpm, "Votre cœur est en bonne santé."
        elif bpm < 62:
            return "Votre BPM est de", bpm, ", il est trop bas. Vous souffrez d'insuffisance cardiaque."
        else:
            return "Votre BPM est de", bpm, ", il est trop élevé. Vous souffrez de tachycardie."

    elif 36 <= age <= 45:
        if sexe:
            if 63 <= bpm <= 100:
                return "Votre BPM est de", bpm, "Votre cœur est en bonne santé."
            elif bpm < 63:
                return "Votre BPM est de", bpm, ", il est trop bas. Vous souffrez d'insuffisance cardiaque."
            else:
                return "Votre BPM est de", bpm, ", il est trop élevé. Vous souffrez de tachycardie."
        else:
            if 65 <= bpm <= 100:
                return "Votre BPM est de", bpm, "Votre cœur est en bonne santé."
            elif bpm < 65:
                return "Votre BPM est de", bpm, ", il est trop bas. Vous souffrez d'insuffisance cardiaque."
            else:
                return "Votre BPM est de", bpm, ", il est trop élevé. Vous souffrez de tachycardie."
    
    if 46 <= age <= 55:
        if sexe:
            if 64 <= bpm <= 100:
                return "Votre BPM est de", bpm, ". Votre cœur est en bonne santé."
            elif bpm < 64:
                return "Votre BPM est de", bpm, ", il est trop bas. Vous souffrez d'insuffisance cardiaque."
            else:
                return "Votre BPM est de", bpm, ", il est trop élevé. Vous souffrez de tachycardie."
        else:
            if 66 <= bpm <= 100:
                return "Votre BPM est de", bpm,". Votre cœur est en bonne santé."
            elif bpm < 66:
                return "Votre BPM est de", bpm,", il est trop bas. Vous souffrez d'insuffisance cardiaque."
            else:
                return "Votre BPM est de", bpm,", il est trop élevé. Vous souffrez de tachycardie."

    if age >= 56:
        if sexe:
            if 62 <= bpm <= 100:
                return "Votre BPM est de", bpm,". Votre cœur est en bonne santé."
            elif bpm < 62:
                return "Votre BPM est de", bpm,", il est trop bas. Vous souffrez d'insuffisance cardiaque."
            else:
                return "Votre BPM est de", bpm,", il est trop élevé. Vous souffrez de tachycardie."
        else:
            if 65 <= bpm <= 100:
                return "Votre BPM est de", bpm,". Votre cœur est en bonne santé."
            elif bpm < 65:
                return "Votre BPM est de", bpm,", il est trop bas. Vous souffrez d'insuffisance cardiaque."
            else:
                return "Votre BPM est de", bpm,", il est trop élevé. Vous souffrez de tachycardie."

