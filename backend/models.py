from datetime import datetime

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, UniqueConstraint
from sqlalchemy.orm import relationship

from backend.database import Base


class Room(Base):
    __tablename__ = "rooms"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(120), unique=True, nullable=False)
    location = Column(String(255), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    detections = relationship("Detection", back_populates="room")


class Detection(Base):
    __tablename__ = "detections"
    __table_args__ = (UniqueConstraint("filename"),)

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String(255), nullable=False)
    people_count = Column(Integer, nullable=False)
    room_id = Column(Integer, ForeignKey("rooms.id"), nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)

    room = relationship("Room", back_populates="detections")