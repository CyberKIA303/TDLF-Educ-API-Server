CREATE DATABASE educ_db;

-- For Download Books Feature --

CREATE TABLE author(
    author_id UUID PRIMARY KEY,
    author_name TEXT,
    osn TEXT
);

CREATE TABLE book(
    book_id UUID PRIMARY KEY,
    book_name TEXT,
    link TEXT,
    book_picture TEXT,
    osn TEXT
);

CREATE TABLE book_authors(
    book_authors_id UUID PRIMARY KEY,
    book_id TEXT,
    author_id TEXT,
    FOREIGN KEY (book_id) REFERENCES book(book_id),
    FOREIGN KEY (author_id) REFERENCES author(author_id)
);

CREATE TABLE school(
    school_id UUID PRIMARY KEY,
    school_name TEXT,
    school_address TEXT,
    school_level TEXT,
    school_picture TEXT
);

CREATE TABLE book_availability(
    book_availability_id UUID PRIMARY KEY,
    school_id TEXT,
    book_id TEXT,
    FOREIGN KEY (school_id) REFERENCES school(school_id),
    FOREIGN KEY (book_id) REFERENCES book(book_id)
);

-- For Taking Quiz Feature --

CREATE TABLE course(
    course_id UUID PRIMARY KEY,
    course_name TEXT,
    course_details TEXT,
    passing_score INT,
    kinder BOOLEAN,
    grade_1 BOOLEAN,
    grade_2 BOOLEAN,
    grade_3 BOOLEAN,
    grade_4 BOOLEAN,
    grade_5 BOOLEAN,
    grade_6 BOOLEAN,
    grade_7 BOOLEAN,
    grade_8 BOOLEAN,
    grade_9 BOOLEAN,
    grade_10 BOOLEAN,
    grade_11 BOOLEAN,
    grade_12 BOOLEAN,
    college BOOLEAN,
    osn TEXT
);

CREATE TABLE quiz(
    quiz_id UUID PRIMARY KEY,
    question TEXT,
    quiz_type INT,
    correct_answer TEXT,
    reason TEXT,
    course_id TEXT,
    FOREIGN KEY (course_id) REFERENCES course(course_id)
);

CREATE TABLE quiz_content(
    quiz_content_id UUID PRIMARY KEY,
    initial TEXT,
    content TEXT,
    quiz_id TEXT,
    FOREIGN KEY (quiz_id) REFERENCES quiz(quiz_id)
);

-- User Login & Belongging Feature --

CREATE TABLE user_info(
    user_info_id UUID PRIMARY KEY,
    username TEXT,
    user_email TEXT UNIQUE,
    user_password TEXT,
    user_status TEXT,
    ons TEXT
);

CREATE TABLE my_course(
    my_course_id UUID PRIMARY KEY,
    user_info_id TEXT,
    course_id TEXT,
    FOREIGN KEY (user_info_id) REFERENCES user_info(user_info_id),
    FOREIGN KEY (course_id) REFERENCES course(course_id)
);