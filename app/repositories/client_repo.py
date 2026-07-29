#app.repositories.client_repo.py
from sqlalchemy.orm import Session
from sqlalchemy import select

from app.models.client import Client

from datetime import datetime

def update_or_save_client_if_new(db: Session, id: str):
    client = db.scalars(select(Client).where(Client.client_id == id)).first()
    if client:
        client.last_seen_at = datetime.now()
        client.is_active = True
        db.commit()
        db.refresh(client)
        return False

    #TODO: configure topics and timestamp helper functions to display later
    new_client = Client(
        client_id = id,
        subscribed_topic = [],
        qos = 1,
        created_at = datetime.now(),
        last_seen_at = datetime.now(),
        is_active = True,
    )

    db.add(new_client)
    db.commit()
    return True

    