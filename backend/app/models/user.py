from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from app.core.database import Base

class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

class Shot(Base):
    __tablename__ = "shots"

    user_id = int

    shot_type = String          # cut / bank / safety / combo
    difficulty_score = 0   # 0–1

    success = bool            # made or missed
    pocketed_ball = int     # which ball

    error_typ = String         # IMPORTANT (explained below)

    cue_ball_path     # trajectory data (optional later)

    outcome_position_quality = float  # how good position after shot was (0–1)

class PlayerProfile(Base):
    overall_success_rate = float
    shot_type_stats = []
    error_distr = []
    dist_performance = []
    cue_control_score = []