# Todo

1. Allow user to supply aspec ratio and check for it with pip
2. ~~Check for content type with response.headers (and json)~~
3. ~~Restructure database, adding int time columns to both tables~~
5. ~~Generally make the database more sensible (maybe an ID column but keeping links unique)~~
4. ~~Improve database querying, no reason to pull links that are months old (allow user to specify this in settings)~~
5. Look into making the http requests concurrent to improve speed
6. Improve config handling, it's a mess atm, more specifically parse input properly, a user can easily fuck up their config