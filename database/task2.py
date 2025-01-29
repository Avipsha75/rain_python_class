from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

class Course(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)

class Enrollment(Base):
    __tablename__ = 'enrollments'
    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('students.id'))
    course_id = Column(Integer, ForeignKey('courses.id'))

engine = create_engine('sqlite:///enrollment_system.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

def add_student(name):
    session.add(Student(name=name))
    session.commit()
    print(f"Student added: {name}")

def add_course(title):
    session.add(Course(title=title))
    session.commit()
    print(f"Course added: {title}")

def enroll_student(student_id, course_id):
    session.add(Enrollment(student_id=student_id, course_id=course_id))
    session.commit()
    print(f"Student {student_id} enrolled in Course {course_id}")

def view_enrollments():
    for enrollment in session.query(Enrollment).all():
        print(f"Student ID: {enrollment.student_id}, Course ID: {enrollment.course_id}")

if __name__ == "__main__":
    add_student("Alice")
    add_student("Bob")
    add_course("Math")
    add_course("Science")
    enroll_student(1, 1)
    enroll_student(2, 2)
    view_enrollments()
