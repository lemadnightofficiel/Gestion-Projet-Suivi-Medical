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

def get_imc(weight, height):
    weight = float(weight) # kg
    height = float(height*0.1) # cm
    imc = (weight/(height*height))
    return imc
