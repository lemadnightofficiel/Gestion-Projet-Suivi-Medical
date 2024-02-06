def check_pulse():
    bpm = 95
    sexe = "Homme"
    age = 18

    if age <= 2:
        if 80 <= bpm <= 160:
            print("Votre BPM est de", bpm, ". Votre cœur est en bonne santé.")
        elif bpm < 80:
            print("Votre BPM est de", bpm, ", il est trop bas. Vous souffrez d'insuffisance cardiaque.")
        else:
            print("Votre BPM est de", bpm, ", il est trop élevé. Vous souffrez de tachycardie.")
    if 3 <= age <= 4:
        if 80 <= bpm <= 120:
            print("Votre BPM est de", bpm, ". Votre cœur est en bonne santé.")
        elif bpm < 80:
            print("Votre BPM est de", bpm, ", il est trop bas. Vous souffrez d'insuffisance cardiaque.")
        else:
            print("Votre BPM est de", bpm, ", il est trop élevé. Vous souffrez de tachycardie.")
    if 5 <= age <= 6:
        if 75 <= bpm <= 115:
            print("Votre BPM est de", bpm, ". Votre cœur est en bonne santé.")
        elif bpm < 75:
            print("Votre BPM est de", bpm, ", il est trop bas. Vous souffrez d'insuffisance cardiaque.")
        else:
            print("Votre BPM est de", bpm, ", il est trop élevé. Vous souffrez de tachycardie.")
    if 7 <= age <= 9:
        if 70 <= bpm <= 110:
            print("Votre BPM est de", bpm, ". Votre cœur est en bonne santé.")
        elif bpm < 70:
            print("Votre BPM est de", bpm, ", il est trop bas. Vous souffrez d'insuffisance cardiaque.")
        else:
            print("Votre BPM est de", bpm, ", il est trop élevé. Vous souffrez de tachycardie.")
    if 10 <= age <= 25:
        if 60 <= bpm <= 100:
            print("Votre BPM est de", bpm, ". Votre cœur est en bonne santé.")
        elif bpm < 60:
            print("Votre BPM est de", bpm, ", il est trop bas. Vous souffrez d'insuffisance cardiaque.")
        else:
            print("Votre BPM est de", bpm, ", il est trop élevé. Vous souffrez de tachycardie.")
    if 26 <= age <= 35:
        if 62 <= bpm <= 100:
            print("Votre BPM est de", bpm, ". Votre cœur est en bonne santé.")
        elif bpm < 62:
            print("Votre BPM est de", bpm, ", il est trop bas. Vous souffrez d'insuffisance cardiaque.")
        else:
            print("Votre BPM est de", bpm, ", il est trop élevé. Vous souffrez de tachycardie.")

    if sexe == "Homme":
        if 36 <= age <= 45:
            if 63 <= bpm <= 100:
                print("Votre BPM est de", bpm, ". Votre cœur est en bonne santé.")
            elif bpm < 63:
                print("Votre BPM est de", bpm, ", il est trop bas. Vous souffrez d'insuffisance cardiaque.")
            else:
                print("Votre BPM est de", bpm, ", il est trop élevé. Vous souffrez de tachycardie.")
    else:
        if 36 <= age <= 45:
            if 65 <= bpm <= 100:
                print("Votre BPM est de", bpm, ". Votre cœur est en bonne santé.")
            elif bpm < 65:
                print("Votre BPM est de", bpm, ", il est trop bas. Vous souffrez d'insuffisance cardiaque.")
            else:
                print("Votre BPM est de", bpm, ", il est trop élevé. Vous souffrez de tachycardie.")
    
    if sexe == "Homme":
        if 46 <= age <= 55:
            if 64 <= bpm <= 100:
                print("Votre BPM est de", bpm, ". Votre cœur est en bonne santé.")
            elif bpm < 64:
                print("Votre BPM est de", bpm, ", il est trop bas. Vous souffrez d'insuffisance cardiaque.")
            else:
                print("Votre BPM est de", bpm, ", il est trop élevé. Vous souffrez de tachycardie.")
    else:
        if 46 <= age <= 55:
            if 66 <= bpm <= 100:
                print("Votre BPM est de", bpm, ". Votre cœur est en bonne santé.")
            elif bpm < 66:
                print("Votre BPM est de", bpm, ", il est trop bas. Vous souffrez d'insuffisance cardiaque.")
            else:
                print("Votre BPM est de", bpm, ", il est trop élevé. Vous souffrez de tachycardie.")

    if sexe == "Homme":
        if age <= 56:
            if 62 <= bpm <= 100:
                print("Votre BPM est de", bpm, ". Votre cœur est en bonne santé.")
            elif bpm < 62:
                print("Votre BPM est de", bpm, ", il est trop bas. Vous souffrez d'insuffisance cardiaque.")
            else:
                print("Votre BPM est de", bpm, ", il est trop élevé. Vous souffrez de tachycardie.")
    else:
        if age <= 56:
            if 65 <= bpm <= 100:
                print("Votre BPM est de", bpm, ". Votre cœur est en bonne santé.")
            elif bpm < 65:
                print("Votre BPM est de", bpm, ", il est trop bas. Vous souffrez d'insuffisance cardiaque.")
            else:
                print("Votre BPM est de", bpm, ", il est trop élevé. Vous souffrez de tachycardie.")


def check_saturation():
    sat = 98

    if 94 <= sat <= 98:
        print("Votre saturation en oxygène est de", sat,", tout va bien.")
    elif 90<= sat <= 93:
        print("Votre saturation en oxygène est de", sat,", elle est médiocre.")
    else:
        print("Votre saturation en oxygène est de", sat,", cela est dangereux.")

check_pulse()
check_saturation()