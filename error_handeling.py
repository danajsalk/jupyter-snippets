def function():

    try : 
        r = requests.get(url)
        r.raise_for_status()
        
    except Exception as err:
        print ("UNSUCCESSFUL")
        print("ERROR:", err)

        data = None
    else:
        print('Success!')
        data = r.json()
    return data
