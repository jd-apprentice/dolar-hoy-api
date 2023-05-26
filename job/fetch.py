import schedule

def run_cronjob(action):
    print("entro")
    schedule.every(1).minutes.do(action)

    while True:
        schedule.run_pending()
        time.sleep(1)