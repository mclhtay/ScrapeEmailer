# Scrape Emailer

Scrape Emailer checks for keywords on websites you provide and sends you an email notification if a keyword is found

#### How it works
In essence it is a web scrapper that works dynamically with your inputs. With website data scraped, it runs regular expression on your keywords list. Once found, with the emailer client you provided, an email is sent to the receiver

#### Configuration files
configuration files should reside under ./configs/


> email_config.json

example format:
```json
{

  "smtp_server": "string" 
  
  "port": number,
  
  "sender_email" : "string",
  
  "password" : "string",
  
  "receiver_email" : "string"
  
}

```

> scrape_items.json

example format:

```json
{
  "items": [
    {
      "url": "string",      
      "key_words": [      
        "string"
      ],      
      "opp": boolean //whether or not should to send email if 0 item is found,      
      "message": "string to send in email"      
    }
  ]
}
```

### How to run
To run normally

```shell script
./run.sh
```

To run indefinitely
```shell script
./run.sh --no-stop
```
