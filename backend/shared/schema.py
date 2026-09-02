from pydantic import BaseModel
from datetime import datetime
from typing import Optional, Any, List
from enum import Enum
from sqlalchemy import MetaData, Table, Column, String, DateTime, Float, Integer, JSON

class EventType(str, Enum):
    CALL = 'CALL'
    SMS = 'SMS'
    IPDR_SESSION = 'IPDR_SESSION'
    LOCATION_PING = 'LOCATION_PING'
    BANK_TRANSFER = 'BANK_TRANSFER'
    SOCIAL_POST = 'SOCIAL_POST'
    SOCIAL_INTERACTION = 'SOCIAL_INTERACTION'

class ConfidenceTier(str, Enum):
    CONFIRMED = 'CONFIRMED'
    PROBABLE = 'PROBABLE'
    CANDIDATE = 'CANDIDATE'

class CanonicalEvent(BaseModel):
    id: Optional[str] = None # uuid, set by ingest
    case_id: str
    event_type: EventType
    ts_start: datetime
    ts_end: Optional[datetime]
    actor_raw: str # raw MSISDN/account/IP before resolution
    peer_raw: Optional[str]
    device_id: Optional[str] # IMEI or device fingerprint
    location_raw: Optional[str] # tower_id or lat,lng string
    amount: Optional[float] # for BANK_TRANSFER
    payload: dict # source-specific extra fields
    source_file_id: str # FK to raw_files
    source_row: int # row number in original CSV
    confidence: float = 1.0

# SQLAlchemy Tables (Core)
metadata = MetaData()

cases = Table(
    'cases', metadata,
    Column('id', String, primary_key=True),
    Column('title', String)
)

raw_files = Table(
    'raw_files', metadata,
    Column('id', String, primary_key=True),
    Column('case_id', String),
    Column('filename', String),
    Column('file_type', String),
    Column('hash', String)
)

canonical_events = Table(
    'canonical_events', metadata,
    Column('id', String, primary_key=True),
    Column('case_id', String),
    Column('event_type', String),
    Column('ts_start', DateTime),
    Column('ts_end', DateTime, nullable=True),
    Column('actor_raw', String),
    Column('peer_raw', String, nullable=True),
    Column('device_id', String, nullable=True),
    Column('location_raw', String, nullable=True),
    Column('amount', Float, nullable=True),
    Column('payload', JSON),
    Column('source_file_id', String),
    Column('source_row', Integer),
    Column('confidence', Float)
)

entities = Table(
    'entities', metadata,
    Column('id', String, primary_key=True),
    Column('case_id', String),
    Column('type', String), # PHONE, ACCOUNT, etc.
    Column('canonical_value', String),
    Column('confidence_tier', String),
    Column('source_ids', JSON) # list of canonical_event ids
)

entity_links = Table(
    'entity_links', metadata,
    Column('id', String, primary_key=True),
    Column('entity_a', String),
    Column('entity_b', String),
    Column('link_type', String),
    Column('confidence', Float),
    Column('evidence_json', JSON) # list of canonical_event ids
)

episodes = Table(
    'episodes', metadata,
    Column('id', String, primary_key=True),
    Column('case_id', String),
    Column('ts_start', DateTime),
    Column('ts_end', DateTime),
    Column('summary', String),
    Column('entity_ids', JSON),
    Column('event_ids', JSON)
)

findings = Table(
    'findings', metadata,
    Column('id', String, primary_key=True),
    Column('case_id', String),
    Column('rule_id', String),
    Column('severity', String),
    Column('weight', Integer),
    Column('confidence', Float),
    Column('explanation', String),
    Column('entity_ids', JSON),
    Column('event_ids', JSON),
    Column('source_file_ids', JSON),
    Column('source_rows', JSON)
)

fraud_scores = Table(
    'fraud_scores', metadata,
    Column('case_id', String, primary_key=True),
    Column('score', Integer),
    Column('risk_level', String),
    Column('top_findings', JSON),
    Column('total_findings', Integer)
)
