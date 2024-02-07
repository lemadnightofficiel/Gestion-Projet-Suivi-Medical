def check_pressure(pas, pad):

    if pas < 50 and pad < 50:
        print("Vous êtes en hypotension sévère.")
    elif 50 <= pas < 90 and 50 <= pad < 60:
        print("Vous êtes en hypotension.")
    elif 90 <= pas < 120 and 60 <= pad < 80:
        print("Votre tension est optimale.")
    elif 120 <= pas < 130  and 80 <= pad < 85:
        print("Votre tension est légèrement élevée.")
    elif 130 <= pas < 140  and 85 <= pad < 90:
        print("Vous êtes en pré-hypertension.")
    elif 140 <= pas < 160  and 90 <= pad < 100:
        print("Vous êtes en hypertension légère.")
    elif 160 <= pas < 180  and 100 <= pad < 105:
        print("Vous êtes en hypertension modérée.")
    elif pas >= 180 or pad >= 110:
        print("Vous êtes en Hypertension avancée.")
    elif pas >= 160:
        print("Vous êtes en hypertension systolique.")
    else:
        print("Votre tension est à surveiller car elle peut présenter des fluctuations.")

check_pressure(117,84)
