# How to authenticate using JWT

1. POST your login and password to `/login` URL:

```
curl -X POST http://your.url/login -d 'user=yourname&password=yourword'
```

The answer should look like:
```
{"token":"SomeVeryLongText.separatedBy.3dots"}
```

2. Send this token in the `Authorization` header to the protected URL:

```
curl http://your.url/protected/ -H "Authorization: Bearer YourToken.FromThe.PreviousStep"
```
