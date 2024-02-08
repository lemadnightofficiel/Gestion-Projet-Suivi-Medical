def check_pulse(bpm, sexe, age):

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
        if sexe == "Homme":
            if 63 <= bpm <= 100:
                return "Votre BPM est de", bpm, "Votre cœur est en bonne santé."
            elif bpm < 63:
                return "Votre BPM est de", bpm, ", il est trop bas. Vous souffrez d'insuffisance cardiaque."
            else:
                return "Votre BPM est de", bpm, ", il est trop élevé. Vous souffrez de tachycardie."
    else:
        if 36 <= age <= 45:
            if 65 <= bpm <= 100:
                return "Votre BPM est de", bpm, "Votre cœur est en bonne santé."
            elif bpm < 65:
                return "Votre BPM est de", bpm, ", il est trop bas. Vous souffrez d'insuffisance cardiaque."
            else:
                return "Votre BPM est de", bpm, ", il est trop élevé. Vous souffrez de tachycardie."
    
    if 46 <= age <= 55:
        if sexe == "Homme":
            if 64 <= bpm <= 100:
                return "Votre BPM est de", bpm, ". Votre cœur est en bonne santé."
            elif bpm < 64:
                return "Votre BPM est de", bpm, ", il est trop bas. Vous souffrez d'insuffisance cardiaque."
            else:
                return "Votre BPM est de", bpm, ", il est trop élevé. Vous souffrez de tachycardie."
    else:
        if 46 <= age <= 55:
            if 66 <= bpm <= 100:
                return "Votre BPM est de", bpm,". Votre cœur est en bonne santé."
            elif bpm < 66:
                return "Votre BPM est de", bpm,", il est trop bas. Vous souffrez d'insuffisance cardiaque."
            else:
                return "Votre BPM est de", bpm,", il est trop élevé. Vous souffrez de tachycardie."

    if age <= 56:
            if sexe == "Homme":
                if 62 <= bpm <= 100:
                    return "Votre BPM est de", bpm,". Votre cœur est en bonne santé."
                elif bpm < 62:
                    return "Votre BPM est de", bpm,", il est trop bas. Vous souffrez d'insuffisance cardiaque."
                else:
                    return "Votre BPM est de", bpm,", il est trop élevé. Vous souffrez de tachycardie."
    else:
        if age <= 56:
            if 65 <= bpm <= 100:
                return "Votre BPM est de", bpm,". Votre cœur est en bonne santé."
            elif bpm < 65:
                return "Votre BPM est de", bpm,", il est trop bas. Vous souffrez d'insuffisance cardiaque."
            else:
                return "Votre BPM est de", bpm,", il est trop élevé. Vous souffrez de tachycardie."


def check_saturation(sat):

    if 94 <= sat <= 98:
        return "Votre saturation en oxygène est de", sat,", tout va bien."
    elif 90<= sat <= 93:
        return "Votre saturation en oxygène est de", sat,", elle est médiocre."
    else:
        return "Votre saturation en oxygène est de", sat,", cela est dangereux."

