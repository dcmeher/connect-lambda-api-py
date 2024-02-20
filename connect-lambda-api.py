import json
import http.client
def lambda_handler(event, context):
    conn = http.client.HTTPSConnection("www.mohfw.gov.in")
    payload = ''
    headers = {
      'Cookie': 'BIGipServer10.247.252.72:80=1159460362.20480.0000'
    }
    conn.request("GET", "/data/datanew.json", payload, headers)
    res = conn.getresponse()
    data = res.read()
    try:
        # Parse JSON
        data = json.loads(data)
    
        # Extract "active" data
        active_data = [entry["active"] for entry in data]
    
        # Print extracted "active" data
        print("Active data:", active_data)
        #print(data.decode("utf-8"))
        resultMap = {
  		"active": active_data[1]
  		#"Balance": '$%s' % customerBalance
  		}
        
        return resultMap


    except Exception as e: