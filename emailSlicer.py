popular_domains= {
"gmail": "Google",
"hotmail":"Microsoft",
"yahoo":"Yahoo",
"outlook":"Microsoft"
}
correoUsuario = input("Cual es tu direccion de correo electronico?\n")

nombreUsuario = correoUsuario.split("@")[0]
dominioCorreo = correoUsuario.split("@")[-1]
dominioCorreo = dominioCorreo.split(".")[0]

if dominioCorreo in popular_domains.keys():
    print(f"Hola {nombreUsuario} parece que tu correo esta registrado con {popular_domains[dominioCorreo]}!")
else:
    print(f"Hey {nombreUsuario} parece que tu correo tiene su propio dominio {dominioCorreo}!")