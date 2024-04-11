import redis
import subprocess

def avvia_redis():
    try:
        # Esegui il comando sulla shell
        subprocess.run(['sudo', 'service', 'redis-server', 'start'], check=True)
        print("Redis server avviato con successo.")
    except subprocess.CalledProcessError as e:
        print("Si è verificato un errore durante l'avvio di Redis:", e)

def ferma():
    try:
        subprocess.run(['sudo', 'service', 'redis-server', 'stop'], check=True)
        print("Redis server fermato con successo.")
    except subprocess.CalledProcessError as e:
        print("Si è verificato un errore durante l'arresto di Redis:", e)

if __name__ == "__main__":
    avvia_redis()
    redis_client = redis.Redis()

    while True:

        #crea uno switch case per i comandi: "i" per inserire, "d" per fermare ed eliminare, "s" per fermare, "g" per ottenere, "f" per ottenere tutti, "m" per inserire più valori, "e" per eliminare, "h" per ottenere aiuto
        i = input("Inserisci un comando: ")

        if i == "i":
            print("Inserisci la chiave e il valore separati da una virgola:")
            key, value = input().split(",")
            redis_client.set(key, value)
            print("Comando salvato: {", key, ',', redis_client.get(key), '}')

        elif i == "d":
            redis_client.flushall()
            ferma()
            break

        elif i == "s":
            ferma()
            break

        elif i == "g":
            print("Inserisci la chiave:")
            key = input()
            value = redis_client.get(key)
            print("Valore ottenuto:", value)

        elif i == "f":
            keys = redis_client.keys()
            values = redis_client.mget(keys)
            print("Tutti i valori:")
            for key, value in zip(keys, values):
                print('{', key, ',', value, '}')

        elif i == "m":
            print("Inserisci i valori nel formato chiave1=valore1,chiave2=valore2,...:")
            data = input()
            pairs = data.split(",")
            for pair in pairs:
                key, value = pair.split("=")
                redis_client.set(key, value)
            print("Comandi salvati.")

        elif i == "e":
            print("Inserisci la chiave da eliminare:")
            key = input()
            redis_client.delete(key)
            print("Chiave eliminata.")

        elif i == "h":
            print("Comandi disponibili:")
            print("i - Inserire un valore")
            print("d - Fermare ed eliminare")
            print("s - Fermare")
            print("g - Ottenere un valore")
            print("f - Ottenere tutti i valori")
            print("m - Inserire più valori")
            print("e - Eliminare una chiave")
            print("h - Ottenere aiuto")

        else:
            print("Comando non valido. Inserisci 'h' per ottenere aiuto.")

    