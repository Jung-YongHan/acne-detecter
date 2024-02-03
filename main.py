from sqlalchemy import create_engine, Column, Integer, String, Text, TIMESTAMP, DateTime, ForeignKey, VARCHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Member(Base):
    __tablename__ = 'member'

    userid = Column(String(16), primary_key=True)
    password = Column(String(255), nullable=False)
    contact = Column(String(20), nullable=False, unique=True)
    name = Column(String(50), nullable=False)


class Photo(Base):
    __tablename__ = 'photo'

    idphoto = Column(Integer, primary_key=True)
    uploadDate = Column(TIMESTAMP)
    userid = Column(String(16), ForeignKey('member.userid'), nullable=True)
    SkinDiseases_disease_id = Column(Integer, nullable=False)

    member = relationship("Member", backref="photos")


class SkinDiseases(Base):
    __tablename__ = 'SkinDiseases'

    disease_id = Column(Integer, primary_key=True, autoincrement=True)
    disease_name = Column(String(100), nullable=False)
    details = Column(Text, nullable=False)
    treatment = Column(Text, nullable=False)
    location = Column(VARCHAR(255))
    photo_idphoto = Column(Integer, ForeignKey('photo.idphoto'), nullable=False)

    photo = relationship("Photo", backref="SkinDiseases")


class Progress(Base):
    __tablename__ = 'Progress'

    progressid = Column(Integer, primary_key=True, autoincrement=True)
    photoid = Column(Integer, ForeignKey('photo.idphoto'), nullable=False)
    uploadDate = Column(DateTime, nullable=False)

    photo = relationship("Photo", backref="progress")


# 데이터베이스 엔진 생성
engine = create_engine('mysql+mysqlconnector://root:password@localhost/nacne_schema')

# 모델을 데이터베이스에 매핑
Base.metadata.create_all(engine)