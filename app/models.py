from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
import datetime

Base = declarative_base()

# Business model
class Business(Base):
    __tablename__ = "businesses"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, nullable=False)

    symptoms = relationship("BusinessSymptom", back_populates="business")

# Symptom model
class Symptom(Base):
    __tablename__ = "symptoms"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String(50), unique=True, nullable=False)
    name = Column(String(100), nullable=False)

    businesses = relationship("BusinessSymptom", back_populates="symptom")

# Relationship model
class BusinessSymptom(Base):
    __tablename__ = "business_symptoms"

    id = Column(Integer, primary_key=True, index=True)
    business_id = Column(Integer, ForeignKey("businesses.id"))
    symptom_id = Column(Integer, ForeignKey("symptoms.id"))
    diagnostic = Column(String(200), nullable=True)

    business = relationship("Business", back_populates="symptoms")
    symptom = relationship("Symptom", back_populates="businesses")

