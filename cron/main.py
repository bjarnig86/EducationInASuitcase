from deta import app
from program import cron

@app.lib.cron()
def cron_job(event):
    cron()
    return "Cron job executed"