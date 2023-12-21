def coordonnees_relatives(coordonnees_origine, coordonnees_a_transformer):
    coord_relative = (
        coordonnees_a_transformer[0] - coordonnees_origine[0],
        coordonnees_a_transformer[1] - coordonnees_origine[1],
        coordonnees_a_transformer[2] - coordonnees_origine[2]
    )
    return coord_relative

coordonnees_reference = (0, 0, 0)

def coordonnees_relatives(reference, coordonnees):
    coord_relative = [coor - ref if coor != 0 else 0 for coor, ref in zip(coordonnees, reference)]
    return coord_relative

coordonnees_a_transformer = [
    (272.47, 182.00, -216.35),
    (272.48, 181.95, -216.23),
    (272.49, 181.60, -216.49)
]

plusX = int(input("Ajouter à x: "))
plusY = int(input("Ajouter à y: "))
plusZ = int(input("Ajouter à z: "))

coordonnees_tete = coordonnees_a_transformer[0]
coordonnees_poignee_bas = coordonnees_a_transformer[1]
coordonnees_poignee_haut = coordonnees_a_transformer[2]

coordonnees_reference = (coordonnees_a_transformer[1][0] + plusX, coordonnees_a_transformer[1][1] + plusY, coordonnees_a_transformer[1][2] + plusZ)

coordonnees_relatives_liste = [coordonnees_relatives(coordonnees_reference, coord) for coord in coordonnees_a_transformer]

for coord_relative in coordonnees_relatives_liste:
    print(f"~{coord_relative[0]:.2f} ~{coord_relative[1]:.2f} ~{coord_relative[2]:.2f}")


coordonnees_tete_relative = coordonnees_relatives(coordonnees_reference, coordonnees_tete)
coordonnees_poignee_bas_relative = coordonnees_relatives(coordonnees_reference, coordonnees_poignee_bas)
coordonnees_poignee_haut_relative = coordonnees_relatives(coordonnees_reference, coordonnees_poignee_haut)

