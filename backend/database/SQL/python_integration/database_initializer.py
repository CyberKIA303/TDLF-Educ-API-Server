import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import (relationship, sessionmaker)
from sqlalchemy import *
from . import nodes
import uuid
os.environ["PGSSLMODE"] = "require"
os.environ["PGSSLCERT"] = ""
os.environ["PGSSLKEY"] = ""

Base = declarative_base()

class Author(Base):
    __tablename__ = "author"
    author_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    author_name = Column(Text)
    osn = Column(Text)
    prime_class = relationship("Book_Authors", back_populates="foreign_class1")


class Book(Base):
    __tablename__ = "book"
    book_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    book_name = Column(Text)
    link = Column(Text)
    book_picture = Column(Text)
    osn = Column(Text)
    prime_class = relationship("Book_Authors", back_populates="foreign_class")
    prime_class1 = relationship("Book_Availability", back_populates="foreign_class1")


class Book_Authors(Base):
    __tablename__ = "book_authors"
    book_authors_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    book_id = Column(UUID(as_uuid=True), ForeignKey("book.book_id"))
    author_id = Column(UUID(as_uuid=True), ForeignKey("author.author_id"))
    foreign_class = relationship("Book", back_populates="prime_class")
    foreign_class1 = relationship("Author", back_populates="prime_class")

class School(Base):
    __tablename__ = "school"
    school_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    school_name = Column(Text)
    school_address = Column(Text)
    school_level = Column(Text)
    school_picture = Column(Text)
    prime_class = relationship("Book_Availability", back_populates="foreign_class")

class Book_Availability(Base):
    __tablename__ = "book_availability"
    book_availability_id = Column(UUID(as_uuid=True),primary_key=True, default=uuid.uuid4)
    school_id = Column(UUID(as_uuid=True),
    ForeignKey("school.school_id"))
    book_id = Column(UUID(as_uuid=True), ForeignKey("book.book_id"))
    foreign_class = relationship("School", back_populates="prime_class")
    foreign_class1 = relationship("Book", back_populates="prime_class1"
    )

class Course(Base):
    __tablename__ = "course"
    course_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    course_name = Column(Text)
    course_details = Column(Text)
    passing_score = Column(Integer)
    kinder = Column(Boolean)
    grade_1 = Column(Boolean)
    grade_2 = Column(Boolean)
    grade_3 = Column(Boolean)
    grade_4 = Column(Boolean)
    grade_5 = Column(Boolean)
    grade_6 = Column(Boolean)
    grade_7 = Column(Boolean)
    grade_8 = Column(Boolean)
    grade_9 = Column(Boolean)
    grade_10 = Column(Boolean)
    grade_11 = Column(Boolean)
    grade_12 = Column(Boolean)
    college = Column(Boolean)
    osn = Column(Text)
    prime_class = relationship("Quiz", back_populates="foreign_class")
    prime_class1 = relationship("My_Course", back_populates="foreign_class1")

class Quiz(Base):
    __tablename__ = "quiz"
    quiz_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    question = Column(Text)
    quiz_type = Column(Integer)
    correct_answer = Column(Text)
    reason = Column(Text)
    course_id = Column(UUID(as_uuid=True), ForeignKey("course.course_id"))
    foreign_class = relationship("Course", back_populates="prime_class")
    prime_class = relationship("Quiz_Content", back_populates="foreign_class")

class Quiz_Content(Base):
    __tablename__ = "quiz_content"
    quiz_content_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    initial = Column(Text)
    content = Column(Text)
    quiz_id = Column(UUID(as_uuid=True), ForeignKey("quiz.quiz_id"))
    foreign_class = relationship("Quiz", back_populates="prime_class")

class User_Info(Base):
    __tablename__ = "user_info"
    user_info_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    username = Column(Text)
    user_email = Column(Text, unique=True)
    user_password = Column(Text)
    user_status = Column(Text)
    ons = Column(Text)
    prime_class = relationship("My_Course", back_populates="foreign_class")

class My_Course(Base):
    __tablename__ = "my_course"
    my_course_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_info_id = Column(UUID(as_uuid=True), ForeignKey("user_info.user_info_id"))
    course_id = Column(UUID(as_uuid=True), ForeignKey("course.course_id"))
    foreign_class = relationship("User_Info", back_populates="prime_class")
    foreign_class1 = relationship("Course", back_populates="prime_class1")
    
def create_tables():
    for node in nodes:
        try:
            url = f"postgresql+psycopg2://{node['user']}:{node['password']}@{node['host']}:{node['port']}/{node['database']}"
            engine = create_engine(url, connect_args={"sslmode": node.get("sslmode", "prefer")})
            Base.metadata.create_all(engine)
            print(f"Connected to {node['type']}")
        except Exception as e:
            print(f"Failed to Connect to {node['type']}: {e}")