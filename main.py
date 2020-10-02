from mongoengine import connect, Document, StringField, EmailField, NotUniqueError, ListField, EmbeddedDocumentField, \
    EmbeddedDocument


class User(Document):
    first_name = StringField(max_length=50)
    last_name = StringField(max_length=50)
    email = EmailField(required=True, unique=True)


POST_STATUS = ('pending', 'published', 'deleted', 'draft')

class Author(EmbeddedDocument):
    name = StringField(required=True)
    email = EmailField(required=True, unique=True)

class Posts(Document):
    title = StringField()
    url = StringField()
    content = StringField()
    status = StringField(choices=POST_STATUS)
    authors = ListField(EmbeddedDocumentField(Author))


def main():
    connect(db='theproject')
    post = Posts()
    post.title = "This is the first post"
    post.url = "https://blogs.com/first_post"
    post.content = "This is interesting stuff..."
    post.status = "pending"

    a1 = Author()
    a1.name = "Pelle"
    a1.email = "pelle@email.com"

    a2 = Author()
    a2.name = "Anna"
    a2.email = "anna@email.com"

    post.authors = [a1, a2]

    post.save()

if __name__ == '__main__':
    main()