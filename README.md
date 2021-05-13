# Django-REST-with-JWT

Raw but simple Django REST API with JWT (Simple JWT)

If you want launch project, clone repository, create virtualenvironment, install requirements, create file .env, generate new secret key, and put secret key in .env file

like this

SECRET_KEY='dawhdjahwjkdhajklwhdjhadjahdjbawdjbawjdbawjkdbawkj'

# API endpoints
I used Postman, but you can use cURL or HTTPie

## Registration
your link should look like this

http://your_domain/api/accounts/register/

Put this link in form for links (left from SEND button), method should be POST, then, in Body choose x-www-form-urlencoded and fill KEYs with username, password, password2, email, first_name, last_name, and VALUEs with any values (first_name and last_name can be blank) and push Send.

## Login
Link

http://your_domain/api/accounts/login/

method POST, Body form-data, KEYS username, password (of registered user), VALUES your user name and user password, push Send

## Refresh token (if you need)
Link

http://your_domain/api/accounts/login/refresh/

method POST, Body x-www-form-urlencoded, KEY refresh VALUE your refresh token from Login, push Send and you will get new access token.

## Post create
Link

http://your_domain/api/posts/post_create/

method POST, Body, raw, JSON

put JSON in form (JSON example below)

{
	"title": "tes09",
    "body": "lalala lalal"
}

Authorization type Bearer Token, in Token form put your access token from Registration or Refresh.

## Post like
Link

http://your_domain/api/posts/post/<post_id>/like/

example http://supersite.com/api/posts/post/1/like/

method POST

Authorization type Bearer Token, in Token form put your access token from Registration or Refresh.
## Post unlike
Link

http://your_domain/api/posts/post/<post_id>/unlike/

example http://supersite.com/api/posts/post/1/unlike/

method POST

Authorization type Bearer Token, in Token form put your access token from Registration or Refresh.

## Analytics about how many likes was made.
return analytics aggregated by day.

Link

http://your_domain/api/posts/analitics/date_from=<date_from>date_to=<date_to>/

example

http://your_domain/api/posts/analitics/date_from=2021-05-10date_to=2021-05-12/

method GET

Authorization type Bearer Token, in Token form put your access token from Registration or Refresh.

## User activity endpoint

user activity an endpoint which will show when user was login last time and when he mades a last request to the service.

Link

http://your_domain/api/accounts/last_login_and_last_request/

method GET

Authorization type Bearer Token, in Token form put your access token from Registration or Refresh.

## Things to improve
change name of the app (app Post and model Post sound awful, better change app name to blog)

refactor code.

post like and unlike can be one function.

place inner function from serealizer in services for example. 

right way would be to add Many-To-Many relationship to Post model.
