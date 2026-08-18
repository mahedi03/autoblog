from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from app.db.session import get_session
from app.db.models import Project, User, GenerationSettings
from app.core.config import settings
from app.core.security import encrypt_data
from app.schemas.project import ProjectCreate, ProjectRead
from typing import List

router = APIRouter()

@router.post("/", response_model=ProjectRead)
def create_project(project: ProjectCreate, session: Session = Depends(get_session)):
    # For now, we assume a single user with ID 1
    db_project = Project(
        name=project.name,
        cms_type=project.cms_type,
        cms_credentials=project.cms_credentials,
        cta_template=project.cta_template,
        user_id=1,
    )
    session.add(db_project)
    session.commit()
    session.refresh(db_project)
    # Keep AI settings separate from the project record and encrypt the key at rest.
    api_key = settings.GEMINI_API_KEY if project.ai_provider == "gemini" else settings.OPENAI_API_KEY
    if api_key and not api_key.startswith("your_"):
        generation_settings = GenerationSettings(
            project_id=db_project.id,
            primary_keywords=project.primary_keywords,
            niche=project.niche,
            tone=project.tone,
            ai_provider=project.ai_provider,
            encrypted_ai_api_key=encrypt_data(api_key),
        )
        session.add(generation_settings)
        session.commit()
    return db_project

@router.get("/", response_model=List[ProjectRead])
def get_projects(session: Session = Depends(get_session)):
    projects = session.exec(select(Project)).all()
    return projects

@router.post("/test-connection")
def test_connection(data: dict):
    from app.services.cms import CMSService
    cms_type = data.get("cms_type")
    credentials = data.get("credentials")
    if not cms_type or not credentials:
        raise HTTPException(status_code=400, detail="Missing cms_type or credentials")

    return CMSService.test_connection(cms_type, credentials)

@router.get("/{project_id}", response_model=ProjectRead)
def get_project(project_id: int, session: Session = Depends(get_session)):
    project = session.get(Project, project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    return project
