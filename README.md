# Fonction du mouvement optimal

(u1, u2) = motion_optimal(x, y, theta, K, ubar, R)

où K est le gain, ubar un paramètre, et R le rayon pour le cercle

# Creation d'un dataset d'entrainement

input, output = get_dataset(N, K, ubar, R)

où input est de dimension (N,4) où pour chaque ligne on a: x, y, cos(theta), sin(theta) 

# Entrainement d'un réseau de neurone avec Pytorch 

pytorch_model = train_network(input, output)

# Conversion du réseau de neurone Pytorch au format csv attendu par le challenge

registrer_to_csv(pytorch_model)

