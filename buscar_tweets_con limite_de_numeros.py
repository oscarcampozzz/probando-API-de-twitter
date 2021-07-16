import tweepy

consumerkey = "dtqGEdINLiLdFGb3FC6nIPUKF"
consumersecret = "dtnFo3MMohrO2kA6p458J6fVSfhnDj6yxDeuZPtqfvPV7rxyTr"
accesstoken =  "1135795643715338240-YwUwGLQToKwsChsvS45jEMPkfzAzWt"
accesstokensecret = "TylCO3XxGubMRJm8VtItlFhRN2104sdSxqTq6d30vJZ3n"


auth = tweepy.OAuthHandler(consumerkey, consumersecret)
auth.set_access_token(accesstoken, accesstokensecret)

api = tweepy.API(auth)

keyword = input ("Escriba la palabra clave para buscar: ")
cantidad = int(input("Escriba cuantas tweets buscar: ")) 

for tweet in tweepy.Cursor(api.search, q=keyword).items(cantidad):
    print("El texto es " + tweet.text)
    print("La fecha de creación " + str(tweet.created_at))
    print("Número de favoritos "+ str(tweet.favorite_count))
    print("El número de retweets " + str(tweet.retweet_count))
    print("Las cordenadas del tweet " + str(tweet.coordinates))
