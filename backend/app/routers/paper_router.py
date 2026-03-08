from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import List

from app.db.database import get_db
from app.models.paper import Paper

router = APIRouter()


# ----------------------------
# Pydantic Schema
# ----------------------------

class PaperCreate(BaseModel):
    title: str
    abstract: str


class PaperResponse(BaseModel):
    id: int
    title: str
    abstract: str

    class Config:
        from_attributes = True  # Required for Pydantic v2


# ----------------------------
# Create Paper
# ----------------------------

@router.post("/papers", response_model=PaperResponse)
def create_paper(paper: PaperCreate, db: Session = Depends(get_db)):
    new_paper = Paper(
        title=paper.title,
        abstract=paper.abstract
    )

    db.add(new_paper)
    db.commit()
    db.refresh(new_paper)

    return new_paper


# ----------------------------
# Get All Papers
# ----------------------------

@router.get("/papers", response_model=List[PaperResponse])
def get_papers(db: Session = Depends(get_db)):
    papers = db.query(Paper).all()
    return papers


# ----------------------------
# Get Single Paper
# ----------------------------

@router.get("/papers/{paper_id}", response_model=PaperResponse)
def get_paper(paper_id: int, db: Session = Depends(get_db)):
    paper = db.query(Paper).filter(Paper.id == paper_id).first()

    if not paper:
        raise HTTPException(status_code=404, detail="Paper not found")

    return paper