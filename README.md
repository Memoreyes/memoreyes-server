# memoreyes-server

### API Documentation
* All requests should be sent to port 5000.
* / returns a timestamp and welcome message
* /api returns generic json
* use /api/t2s for text to speech
* use /api/s2t for speech to text
* use /api/fr for facial recognition
* use /api/db for database calls

#### Text to Speech (t2s)
JSON Request Format:
{
  'user_id':'123456',
  'payload':'This is what would be said aloud to the user.'
}

JSON response Format:
{
  'success':'t/f',
  'user_id':'123456',
  'payload':'audio_url'
}

#### Speech to Text (s2t)
JSON Request Format:
{
  'user_id':'123456',
  'payload':'audio_url'
}

POST format?

JSON response Format:
{
  'success':'t/f',
  'user_id':'123456',
  'payload':'Your speech, now text.'
}

#### Facial Recognition (fr)
JSON Request Format:
{
  'user_id':'123456',
  'payload':'This is your image file.'
}

JSON response Format:
{
  'success':'t/f',
  'user_id':'123456',
  'payload':[
              'name':'...'
              'relationship':'...'
              'info':'...'
            ]
}

#### Database (db)
JSON Request Format:
{
  'user_id':'123456',
  'payload':'This is your SQL query.'
}

JSON response Format:
{
  'success':'t/f',
  'user_id':'123456',
  'payload':[
              'key':'value'
              ...
            ]
}
