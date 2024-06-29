Devto blog project  
API: https://developers.forem.com/api/v0  
entities:  
- article:
- - fields:
- - - id 
- - - title
- - - cover_image
- - - url
- - - text #maybe 2 types html+md
- - - user
- - - published_at
- - methods:
- - - get_article_by_id -> Article
- - - get_my_articles -> [Article]
- - - get_pictures_from_my_article -> [links to images]
- comment
- - fields:
- - - id_code
- - - text
- - - user
- - methods:
- - - get_comment_by_id -> Comment
- - - get_comments_by_article_id -> [Comment]
- user
- - fields:
- - - id
- - - username
- - - name
- - - summary
- - - location
- - - profile_image (url)
- - methods:
- - - get_myself -> User
- - - get_user (by id and name) -> User

get entity -> save to db -> retrieve from db -> present retrieved info

get entity:  
1. send request
2. get response
3. prep object
4. return object