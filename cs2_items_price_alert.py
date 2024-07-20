import json
import requests

def load_items(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def get_price(item):
    app_id = 730
    url = f"https://steamcommunity.com/market/priceoverview/?currency=1&appid={app_id}&market_hash_name={item['item_name']}"
    response = requests.get(url)
    data = response.json()
    if 'lowest_price' in data:
        price_str = data['lowest_price'].replace('$', '').replace(',', '')
        return float(price_str)
    return None

def check_prices(items):
    alerts = []
    for item in items:
        current_price = get_price(item)
        if current_price is not None:
            if current_price < item['alert_below']:
                alerts.append(
                    f"The price of {item['item_name']} is below ${item['alert_below']}. Current price: ${current_price}")
            elif current_price > item['alert_above']:
                alerts.append(
                    f"The price of {item['item_name']} is above ${item['alert_above']}. Current price: ${current_price}")
    return alerts

def send_alerts(alerts, webhook_url):
    headers = {
        "Content-Type": "application/json"
    }
    for alert in alerts:
        payload = {
            "content": alert
        }
        response = requests.post(webhook_url, data=json.dumps(payload), headers=headers)
        if response.status_code != 204:
            print(f"Failed to send alert to Discord: {response.status_code}, {response.text}")

def main():
    items = load_items('items.json')
    alerts = check_prices(items)
    send_alerts(alerts, 'DISCORD_WEBHOOK_URL')

if __name__ == "__main__":
    main()
