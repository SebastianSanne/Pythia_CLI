# Setting Up
1. Get or register for Google API key
[https://console.developers.google.com](https://console.developers.google.com)
2. Create or source CSE id
[https://cse.google.com/cse/](https://cse.google.com/cse/)

3. Save environmental variables

```bash
export GOOGLE_CSE_API_KEY='KEY_GOES_HERE'
export GOOGLE_CSE_ID='ID_GOES_HERE'
```

Leave domain blank and under "advanced" use schema type "Thing"

4. Install Google API Client locally

```bash
pip install --upgrade google-api-python-client
```
