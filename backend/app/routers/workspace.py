from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.db import models
from app.utils.dependency import get_current_user

router = APIRouter()

@router.post("/create")
def create_workspace(name: str, db: Session = Depends(get_db), user=Depends(get_current_user)):
    ws = models.Workspace(name=name, owner_id=user.id)
    db.add(ws)
    db.commit()
    return {"message": "Workspace created"}

@router.get("/")
def list_workspaces(db: Session = Depends(get_db), user=Depends(get_current_user)):
    return db.query(models.Workspace).filter(models.Workspace.owner_id == user.id).all()