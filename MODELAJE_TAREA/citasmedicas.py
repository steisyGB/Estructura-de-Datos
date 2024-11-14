from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()

class Cita(Base):
    __tablename__ = 'tbl_cita'

    id = Column(Integer, primary_key=True)
    fecha = Column(DateTime, nullable=False)
    motivo = Column(String, nullable=False)

    paciente_id = Column(Integer, ForeignKey('tbl_paciente.id'))
    doctor_id = Column(Integer, ForeignKey('tbl_doctor.id'))

    paciente = relationship("Paciente", back_populates="citas")
    doctor = relationship("Doctor", back_populates="citas")

class Paciente(Base):
    __tablename__ = 'tbl_paciente'

    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    edad = Column(Integer, nullable=False)
    historial_medico = Column(String)

    citas = relationship("Cita", back_populates="paciente")

class Doctor(Base):
    __tablename__ = 'tbl_doctor'

    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    especialidad = Column(String, nullable=False)
    telefono = Column(String)

    citas = relationship("Cita", back_populates="doctor")

engine = create_engine('sqlite:///citas_medicas.db', echo=True)
Base.metadata.create_all(engine)