# README

## Description

This project is a tool for monitoring the prices of selected items. The script will notify the user of price changes via a Discord webhook. The values you need to edit and customize are located in the `cs2_items_price_alert.py` and `items.json` files.

## Configuration

### Editing `cs2_items_price_alert.py`

1. Open the `script.py` file in a text editor.
2. Find the line containing `DISCORD_WEBHOOK_URL`.
3. Edit the value of `DISCORD_WEBHOOK_URL` by pasting your Discord webhook URL. Example:
    ```python
    send_alerts(alerts, 'https://discord.com/api/webhooks/your_webhook_url')
    ```

### Editing `items.json`

1. Open the `items.json` file in a text editor.
2. Define the items you want to monitor using their market names.
3. Set price alerts for each item by specifying values for price below (`price_below`) and price above (`price_above`). Example:
    ```json
    [
        {
            "item_name": "example_item_1",
            "alert_below": 100.0,
            "alert_above": 200.0
        },
        {
            "item_name": "example_item_2",
            "alert_below": 50.0,
            "alert_above": 150.0
        }
    ]
    ```

## Usage

1. Ensure all required dependencies are installed.
2. Run the script:
    ```bash
    python3 cs2_items_price_alert.py
    ```
3. The script will check the prices for the specified items in the JSON file and send an alert to Discord if the conditions are met.
4. This process can be automated by adding the script to a cron job for periodic execution.

