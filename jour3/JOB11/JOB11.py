def time_to_text(minutes):
    if not isinstance(minutes, int) or minutes < 0:
        print("Veuillez entrer un nombre entier et positif.")
        return

    heures = minutes // 60
    minutes_restantes = minutes % 60

    print(f"{heures} heures et {minutes_restantes} minutes.")


time_to_text(60)
time_to_text(-120)
time_to_text(180)
time_to_text(240) 
time_to_text(75.5)  