from mongoengine import Document, StringField, ListField, ReferenceField

class User(Document):
    name = StringField(required=True)
    roles = ListField(StringField(required=True))
    email = StringField(required=True)
    password = StringField(required=True)

class Course(Document):
    code = StringField(required=True)
    title = StringField(required=True)
    lecturer = ReferenceField(User, required=True)
    status = StringField(required=True)

class CourseReg(Document):
    student = ReferenceField(User)
    course = ReferenceField(Course, required=True)
    status = StringField(required=True)
    message = StringField(required=True)

class Result(Document):
    student = ReferenceField(User, required=True)
    course = ReferenceField(Course, required=True)