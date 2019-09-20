# Chewie Pie

## Cron job
Run the following command: `crontab -e`
Then, insert the following line: `* * * * * /home/pi/Repositories/chewie-pie/utils/cron.sh`

## Chewie Pie application

## Install dependencies
Run the following command: `cd python; pipenv install`
Run the following command: `go get github.com/pilu/fresh`

## Run the application
Run the following command: `python3 python/server.py`
Run the following command: `cd golang; fresh`
 