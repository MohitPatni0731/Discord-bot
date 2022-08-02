for i in range(1):
  from dhooks import Webhook
  import re
  import time
  import requests

  # This is the API url which is used to fetch the rate of the currency.
  url = "https://api.apilayer.com/fixer/convert?to=INR&from=GBP&amount=1"
  IFTTT_WEBHOOKS_URL = 'https://maker.ifttt.com/trigger/{}/with/key/ikjRKm44HQqrnvBh8j0irFxxihKPyRx6OK6LNTK_jBC'

  payload = {}
  headers= {
    "apikey": "qlaZvLUc7oREf6dPiJDu3ZsrlChj7pwP"
  }
  
 
  response = requests.request("GET", url, headers=headers, data = payload)
  status_code = response.status_code
  result = response.text
  lists = list(result.split())
  final_result = lists[-2]
  
  
  hook = Webhook("https://discord.com/api/webhooks/1003993992360366080/1cS8w3N2GHzW-2aAwLYZ9tpfcHHhRBiASgTIafnfJ1Q--NbC1Exat7lVVzr4mgvH3l5f")
  data = "Current pound rate in INR is -> "+final_result
  hook.send(data)
  time.sleep(1)
