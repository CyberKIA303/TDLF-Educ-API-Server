import sys
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import *
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from db_connection.connection import (nodes, resnode)

Base = declarative_base()
ResBase = declarative_base()

class Admin(Base):
    __tablename__ = "admin_table"
    admin_id = Column(Integer, primary_key=True, autoincrement=True)
    user_name = Column(String(100))
    password = Column(String(100))
    active_status = Column(Boolean)
    prime_class = relationship("Admin_Info", back_populates="foreign_class")
    prime_class1 = relationship("Cliant_Response_Confirmation", back_populates="foreign_class")
    prime_class2 = relationship("Cliant_Response_Confirmation", back_populates="foreign_class")
    
class Admin_Info(Base):
    __tablename__ = "admin_info_table"
    admin_info_id = Column(Integer, primary_key=True, autoincrement=True)
    admin_status = Column(String(100))
    contact_number = Column(String(100))
    email_adress = Column(String(100))
    active_status = Column(Boolean)
    admin_id = Column(Integer, ForeignKey("admin_table.admin_id"))
    foreign_class = relationship("Admin", back_populates="prime_class")
    
class Student(Base):
    __tablename__ = "student_table"
    student_id = Column(Integer, primary_key=True, autoincrement=True)
    student_school_id = Column(String(100))
    active_status = Column(Boolean)
    prime_class = relationship("Student_Record", back_populates="foreign_class")
    prime_class1 = relationship("Student_Enrollment_Form", back_populates="foreign_class")

class Student_Record(Base):
    __tablename__ = "student_record_table"
    student_record_id = Column(Integer, primary_key=True, autoincrement=True)
    year_level = Column(String(100))
    active_status = Column(Boolean)
    student_id = Column(Integer, ForeignKey("student_table.student_id"))
    foreign_class = relationship("Student", back_populates="prime_class")
    prime_class = relationship("Attendance", back_populates="foreign_class")
    prime_class1 = relationship("Grade", back_populates="foreign_class")
    
class Attendance(Base):
    __tablename__ = "attendance_table"
    attendance_id = Column(Integer, primary_key=True, autoincrement=True)
    date_in = Column(DateTime)
    status = Column(String(100))
    active_status = Column(Boolean)
    student_record_id = Column(Integer, ForeignKey("student_record_table.student_record_id"))
    foreign_class = relationship("Student_Record", back_populates="prime_class")
    
class Grade(Base):
    __tablename__ = "grade_table"
    grade_id = Column(Integer, primary_key=True, autoincrement=True)
    subject_or_course = Column(String(100))
    prelim_grade = Column(Float)
    midterm_grade = Column(Float)
    final_grade = Column(Float)
    status = Column(String(100))
    active_status = Column(Boolean)
    student_record_id = Column(Integer, ForeignKey("student_record_table.student_record_id"))
    foreign_class = relationship("Student_Record", back_populates="prime_class1")
    
class Teacher(Base):
    __tablename__ = "teacher_table"
    teacher_id = Column(Integer, primary_key=True, autoincrement=True)
    last_name = Column(String(100))
    first_name = Column(String(100))
    middle_name = Column(String(100))
    contact_number = Column(String(100))
    active_status = Column(Boolean)
    prime_class = relationship("Class_Room", back_populates="foreign_class")
    
class Class_Room(Base):
    __tablename__ = "class_room_table"
    class_room_id = Column(Integer, primary_key=True, autoincrement=True)
    section = Column(String(100))
    active_status = Column(Boolean)
    adviser = Column(Integer, ForeignKey("teacher_table.teacher_id"))
    sub_teacher = Column(Integer, ForeignKey("teacher_table.teacher_id"))
    foreign_class = relationship("Teacher", back_populates="prime_class")
    prime_class = relationship("Enrollment_Info", back_populates="foreign_class")
    
class Track(Base):
    __tablename__ = "track_table"
    track_id = Column(Integer, primary_key=True, autoincrement=True)
    track_name = Column(String(100))
    active_status = Column(Boolean)
    prime_class = relationship("Strand", back_populates="foreign_class")
    prime_class1 = relationship("Enrollment_Info", back_populates="foreign_class2")
    prime_class2 = relationship("Learner_In_Senior_High_School", back_populates="foreign_class")
    
class Strand(Base):
    __tablename__ = "strand_table"
    strand_id = Column(Integer, primary_key=True, autoincrement=True)
    strand_name = Column(String(100))
    active_status = Column(Boolean)
    track_id = Column(Integer, ForeignKey("track_table.track_id"))
    foreign_class = relationship("Track", back_populates="prime_class")
    prime_class = relationship("Subject", back_populates="foreign_class")
    prime_class1 = relationship("Enrollment_Info", back_populates="foreign_class1")
    prime_class2 = relationship("Learner_In_Senior_High_School", back_populates="foreign_class1")
    
class Subject(Base):
    __tablename__ = "subject_table"
    subject_id = Column(Integer, primary_key=True, autoincrement=True)
    subject_name = Column(String(100))
    active_status = Column(Boolean)
    strand_id = Column(Integer, ForeignKey("strand_table.strand_id"))
    foreign_class = relationship("Strand", back_populates="prime_class")
    prime_class = relationship("Course", back_populates="foreign_class")
    
class Course(Base):
    __tablename__ = "course_table"
    course_id = Column(Integer, primary_key=True, autoincrement=True)
    course_name = Column(String(100))
    active_status = Column(Boolean)
    subject_id = Column(Integer, ForeignKey("subject_table.subject_id"))
    foreign_class = relationship("Subject", back_populates="prime_class")
    
class Enrollment_Info(Base):
    __tablename__ = "enrollment_info_table"
    enrollment_info_id = Column(Integer, primary_key=True, autoincrement=True)
    grade_level = Column(String(100))
    active_status = Column(Boolean)
    class_room_id = Column(Integer, ForeignKey("class_room_table.class_room_id"))
    strand_id = Column(Integer, ForeignKey("strand_table.strand_id"))
    track_id = Column(Integer, ForeignKey("track_table.track_id"))
    foreign_class = relationship("Class_Room", back_populates="prime_class")
    foreign_class1 = relationship("Strand", back_populates="prime_class1")
    foreign_class2 = relationship("Track", back_populates="prime_class1")
    prime_class = relationship("Student_Enrollment_Form", back_populates="foreign_class1")
    
class Parents_Info(Base):
    __tablename__ = "parents_info_table"
    parents_info_id = Column(Integer, primary_key=True, autoincrement=True)
    last_name = Column(String(100))
    first_name = Column(String(100))
    middle_name = Column(String(100))
    contact_number = Column(String(100))
    active_status = Column(Boolean)
    prime_class = relationship("Validation", back_populates="foreign_class")
    prime_class1 = relationship("Enhanced_BEEF", back_populates="foreign_class2")
    
class Validation(Base):
    __tablename__ = "validation_table"
    validation_id = Column(Integer, primary_key=True, autoincrement=True)
    approval_content = Column(String(100))
    active_status = Column(Boolean)
    parents_info_id = Column(Integer, ForeignKey("parents_info_table.parents_info_id"))
    foreign_class = relationship("Parents_Info", back_populates="prime_class")
    prime_class = relationship("Preferred_Distance_Learning_Modality", back_populates="foreign_class")
    
class Learner_In_Senior_High_School(Base):
    __tablename__ = "learner_in_senior_high_school_table"
    learner_in_senior_high_school_id = Column(Integer, primary_key=True, autoincrement=True)
    semester = Column(String(100))
    active_status = Column(Boolean)
    track_id = Column(Integer, ForeignKey("track_table.track_id"))
    strand_id = Column(Integer, ForeignKey("strand_table.strand_id"))
    foreign_class = relationship("Track", back_populates="prime_class2")
    foreign_class1 = relationship("Strand", back_populates="prime_class2")
    prime_class = relationship("Enhanced_BEEF", back_populates="foreign_class5")
    
class Preferred_Distance_Learning_Modality(Base):
    __tablename__ = "preferred_distance_learning_modality_table"
    preferred_distance_learning_modality_id = Column(Integer, primary_key=True, autoincrement=True)
    modular_print = Column(Boolean)
    modular_digital = Column(Boolean)
    online = Column(Boolean)
    educational_televetion = Column(Boolean)
    radio_base_instruction = Column(Boolean)
    homeschooling = Column(Boolean)
    blended = Column(Boolean)
    face_to_face = Column(Boolean)
    date_in = Column(DateTime)
    active_status = Column(Boolean)
    validation_id = Column(Integer, ForeignKey("validation_table.validation_id"))
    foreign_class = relationship("Validation", back_populates="prime_class")
    prime_class = relationship("Enhanced_BEEF", back_populates="foreign_class4")
    
class Mother_Tongue(Base):
    __tablename__ = "mother_tongue_table"
    mother_tongue_id = Column(Integer, primary_key=True, autoincrement=True)
    person_dialect = Column(String(100))
    active_status = Column(Boolean)
    prime_class = relationship("Learners_Information", back_populates="foreign_class")
    
class Country(Base):
    __tablename__ = "country_table"
    country_id = Column(Integer, primary_key=True, autoincrement=True)
    country_name = Column(String(100))
    active_status = Column(Boolean)
    prime_class = relationship("Province", back_populates="foreign_class")
    prime_class1 = relationship("Address", back_populates="foreign_class")
    
class Province(Base):
    __tablename__ = "province_table"
    province_id = Column(Integer, primary_key=True, autoincrement=True)
    province_name = Column(String(100))
    active_status = Column(Boolean)
    country_id = Column(Integer, ForeignKey("country_table.country_id"))
    foreign_class = relationship("Country", back_populates="prime_class")
    prime_class = relationship("Municipal_Or_City", back_populates="foreign_class")
    prime_class1 = relationship("Address", back_populates="foreign_class1")
    
class Municipal_Or_City(Base):
    __tablename__ = "municipal_or_city_table"
    municipal_or_city_id = Column(Integer, primary_key=True, autoincrement=True)
    municipal_or_city_name = Column(String(100))
    active_status = Column(Boolean)
    province_id = Column(Integer, ForeignKey("province_table.province_id"))
    foreign_class = relationship("Province", back_populates="prime_class")
    prime_class = relationship("Barangay", back_populates="foreign_class")
    prime_class1 = relationship("Address", back_populates="foreign_class2")
    
class Barangay(Base):
    __tablename__ = "barangay_table"
    barangay_id = Column(Integer, primary_key=True, autoincrement=True)
    barangay_name = Column(String(100))
    active_status = Column(Boolean)
    municipal_or_city_id = Column(Integer, ForeignKey("municipal_or_city_table.municipal_or_city_id"))
    foreign_class = relationship("Municipal_Or_City", back_populates="prime_class")
    prime_class = relationship("Street", back_populates="foreign_class")
    prime_class1 = relationship("Zip_Code_Coverage", back_populates="foreign_class1")
    prime_class2 = relationship("Address", back_populates="foreign_class3")
    
class Street(Base):
    __tablename__ = "street_table"
    street_id = Column(Integer, primary_key=True, autoincrement=True)
    street_name = Column(String(100))
    active_status = Column(Boolean)
    barangay_id = Column(Integer, ForeignKey("barangay_table.barangay_id"))
    foreign_class = relationship("Barangay", back_populates="prime_class")
    prime_class = relationship("Address", back_populates="foreign_class4")
    
class Zip_Code(Base):
    __tablename__ = "zip_code_table"
    zip_code_id = Column(Integer, primary_key=True, autoincrement=True)
    code = Column(Integer)
    active_status = Column(Boolean)
    prime_class = relationship("Zip_Code_Coverage", back_populates="foreign_class")
    prime_class1 = relationship("Address", back_populates="foreign_class5")
    
class Zip_Code_Coverage(Base):
    __tablename__ = "zip_code_coverage_table"
    zip_code_coverage_id = Column(Integer, primary_key=True, autoincrement=True)
    active_status = Column(Boolean)
    zip_code_id = Column(Integer, ForeignKey("zip_code_table.zip_code_id"))
    barangay_id = Column(Integer, ForeignKey("barangay_table.barangay_id"))
    foreign_class = relationship("Zip_Code", back_populates="prime_class")
    foreign_class1 = relationship("Barangay", back_populates="prime_class1")
    
class Address(Base):
    __tablename__ = "address_table"
    address_id = Column(Integer, primary_key=True, autoincrement=True)
    house_no = Column(String(100))
    active_status = Column(Boolean)
    country_id = Column(Integer, ForeignKey("country_table.country_id"))
    province_id = Column(Integer, ForeignKey("province_table.province_id"))
    municipal_or_city_id = Column(Integer, ForeignKey("municipal_or_city_table.municipal_or_city_id"))
    barangay_id = Column(Integer, ForeignKey("barangay_table.barangay_id"))
    street_id = Column(Integer, ForeignKey("street_table.street_id"))
    zip_code_id = Column(Integer, ForeignKey("zip_code_table.zip_code_id"))
    foreign_class = relationship("Country", back_populates="prime_class1")
    foreign_class1 = relationship("Province", back_populates="prime_class1")
    foreign_class2 = relationship("Municipal_Or_City", back_populates="prime_class1")
    foreign_class3 = relationship("Barangay", back_populates="prime_class2")
    foreign_class4 = relationship("Street", back_populates="prime_class")
    foreign_class5 = relationship("Zip_Code", back_populates="prime_class1")
    prime_class = relationship("Enhanced_BEEF", back_populates="foreign_class1")
    
class Learners_Information(Base):
    __tablename__ = "learners_information_table"
    learners_information_id = Column(Integer, primary_key=True, autoincrement=True)
    psa_birth_certificate_no = Column(String(100))
    last_name = Column(String(100))
    first_name = Column(String(100))
    middle_name = Column(String(100))
    extension_name = Column(String(100))
    learning_reference_no = Column(String(100))
    birthdate = Column(Date)
    sex = Column(String(25))
    age = Column(Integer)
    place_of_bith = Column(String(100))
    is_belong_as_ip = Column(Boolean)
    if_ip_then_specify = Column(String(100))
    is_beneficiary_of_4ps = Column(Boolean)
    if_4ps_then_hind = Column(String(100))
    active_status = Column(Boolean)
    mother_tongue_id = Column(Integer, ForeignKey("mother_tongue_table.mother_tongue_id"))
    foreign_class = relationship("Mother_Tongue", back_populates="prime_class")
    prime_class = relationship("Enhanced_BEEF", back_populates="foreign_class")
    
class Returning_Lerners_Or_Transfery(Base):
    __tablename__ = "returning_lerners_or_transfery_table"
    returning_lerners_or_transfery_id = Column(Integer, primary_key=True, autoincrement=True)
    last_grade_level_completed = Column(String(100))
    last_school_attended = Column(String(100))
    school_id = Column(String(100))
    active_status = Column(Boolean)
    prime_class = relationship("Enhanced_BEEF", back_populates="foreign_class3")
    
class Enhanced_BEEF(Base):
    __tablename__ = "enhanced_beef_table"
    enhanced_beef_id = Column(Integer, primary_key=True, autoincrement=True)
    school_year = Column(String(100))
    grade_level_to_enroll = Column(String(100))
    with_lrn = Column(String(100))
    returning_learner = Column(Boolean)
    active_status = Column(Boolean)
    learners_information_id = Column(Integer, ForeignKey("learners_information_table.learners_information_id"))
    current_address = Column(Integer, ForeignKey("address_table.address_id"))
    permanent_address = Column(Integer, ForeignKey("address_table.address_id"))
    father_name = Column(Integer, ForeignKey("parents_info_table.parents_info_id"))
    mother_name = Column(Integer, ForeignKey("parents_info_table.parents_info_id"))
    guardian_name = Column(Integer, ForeignKey("parents_info_table.parents_info_id"))
    returning_lerners_or_transfery_id = Column(Integer, ForeignKey("returning_lerners_or_transfery_table.returning_lerners_or_transfery_id"))
    preferred_distance_learning_modality_id = Column(Integer, ForeignKey("preferred_distance_learning_modality_table.preferred_distance_learning_modality_id"))
    learner_in_senior_high_school_id = Column(Integer, ForeignKey("learner_in_senior_high_school_table.learner_in_senior_high_school_id"))
    foreign_class = relationship("Learners_Information", back_populates="prime_class")
    foreign_class1 = relationship("Address", back_populates="prime_class")
    foreign_class2 = relationship("Parents_Info", back_populates="prime_class1")
    foreign_class3 = relationship("Returning_Lerners_Or_Transfery", back_populates="prime_class")
    foreign_class4 = relationship("Preferred_Distance_Learning_Modality", back_populates="prime_class")
    foreign_class5 = relationship("Learner_In_Senior_High_School", back_populates="prime_class")
    prime_class = relationship("Student_Enrollment_Form", back_populates="foreign_class2")
    
class Student_Enrollment_Form(Base):
    __tablename__ = "student_enrollment_form_table"
    student_enrollment_form_id = Column(Integer, primary_key=True, autoincrement=True)
    active_status = Column(Boolean)
    student_id = Column(Integer, ForeignKey("student_table.student_id"))
    enrollment_info_id = Column(Integer, ForeignKey("enrollment_info_table.enrollment_info_id"))
    enhanced_beef_id = Column(Integer, ForeignKey("enhanced_beef_table.enhanced_beef_id"))
    foreign_class = relationship("Student", back_populates="prime_class1")
    foreign_class1 = relationship("Enrollment_Info", back_populates="prime_class")
    foreign_class2 = relationship("Enhanced_BEEF", back_populates="prime_class")
    
class Cliant_Response_Confirmation(ResBase):
    __tablename__ = "cliant_response_confirmation_table"
    cliant_id = Column(Integer, ForeignKey("admin_table.admin_id"), primary_key=True)
    cliant_incripted_token = Column(Text)
    foreign_class = relationship("Admin", back_populates="prime_class1")
    
class Regestered_Project(ResBase):
    __tablename__ = "regestered_project_table"
    regestered_project_id = Column(Integer, primary_key=True, autoincrement=True)
    project_name = Column(String(100))
    project_version = Column(String(100))
    project_licence = Column(Text)
    granted_access = Column(Boolean)
    active_status = Column(Boolean)
    cliant_id = Column(Integer, ForeignKey("admin_table.admin_id"))
    foreign_class = relationship("Admin", back_populates="prime_class2")
    prime_class = relationship("Regestered_Device", back_populates="foreign_class")

class Regestered_Device(ResBase):
    __tablename__ = "regestered_revice_table"
    regestered_revice_id = Column(Integer, primary_key=True, autoincrement=True)
    device_ip = Column(String(25))
    active_status = Column(Boolean)
    regestered_project_id = Column(Integer, ForeignKey("regestered_project_table.regestered_project_id"))
    foreign_class = relationship("Regestered_Project", back_populates="prime_class")

def create_tables():
    for node in nodes:
        try:
            engine = create_engine(f"postgresql://{node['user']}:{node['password']}@{node['host']}:{node['port']}/{node['database']}")
            Base.metadata.create_all(engine)
            print(f"Connected to {node['type']}")
        except Exception as e:
            print(f"Failed to Connect to {node['type']}")
    for node in resnode:
        try:
            engine = create_engine(f"postgresql://{node['user']}:{node['password']}@{node['host']}:{node['port']}/{node['database']}")
            ResBase.metadata.create_all(engine)
            print(f"Connected to {node['type']}")
        except Exception as e:
            print(f"Failed to Connect to {node['type']}")