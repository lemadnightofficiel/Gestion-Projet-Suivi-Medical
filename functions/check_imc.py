def check_imc(weight, height):
    weight = float(weight) # kg
    height = float(height) # m
    imc = weight/height**2

    if imc < 16.5:
        print("Votre IMC est de", round(imc, 1), ". Vous êtes en insuffisance pondérale sévère.")
    elif 16.5 <= imc < 18.5:
        print("Votre IMC est de", round(imc, 1), ". Vous êtes en insuffisance pondérale modérée.")
    elif 18.5 <= imc < 25:
        print("Votre IMC est de", round(imc, 1), ". Vous avez un poids normal.")
    elif 25 <= imc < 30:
        print("Votre IMC est de", round(imc, 1), ". Vous êtes en obésité légère.")
    elif 30 <= imc < 35:
        print("Votre IMC est de", round(imc, 1), ". Vous êtes en obésité modérée.")
    elif 35 <= imc < 40:
        print("Votre IMC est de", round(imc, 1), ". Vous êtes en obésité sévère.")
    else:
        print("Votre IMC est de", round(imc, 1), ". Vous êtes en obésité morbide.")


check_imc(73, 1.80)