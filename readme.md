# Use case
A batch application that scrapes auto ads pages and collect the data regarding sold cars.

[MVP]
- [x] Open up page for scraping. 
- [x] Collect ad urls regarding sold cars.
- [x] Place data into a txt file.

[MVP+]
- [ ] Collect url address, brand, model, price, year.
- [ ] Sort data by href.
- [ ] Place data as json into a file.
- [ ] Create a simple HTML page to show data as list.

# Development
### Startup
```
> . venv/bin/activate
> pip install requests
> pip freeze > requirements.txt
> deactivate
```

### Maintain
```
> . venv/bin/activate
> pip install -r requirements.txt
> deactivate
```