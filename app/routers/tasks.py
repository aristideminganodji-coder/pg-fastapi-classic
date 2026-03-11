from fastapi import APIRouter,Depends,HTTPException,status
from sqlalchemy.orm import Session
from app import models,schemas
from app.database import get_db

router=APIRouter(prefix="/tasks",tags=["Tasks"])

#GET/tasks/
@router.get("/",response_model=list[schemas.Task])
def read_tasks(skip:int=0,limit:int=100,db:Session=Depends(get_db)):
    tasks=db.query(models.Task).offset(skip).limit(limit).all()
    return tasks

#GET/taks/{id}
@router.get("/{task_id}",response_model=schemas.Task)
def read_task(task_id:int,db:Session=Depends(get_db)):
    task=db.query(models.Task).filter(models.Task.id==task_id).first()
    if not task:
        raise HTTPException(status_code=404,detail="task not found")
    return task

#POST/tasks/
@router.post("/",response_model=schemas.Task,status_code=status.HTTP_201_CREATED)
def create_task(task:schemas.TaskCreate,db:Session=Depends(get_db)):
    user=db.query(models.User).filter(models.User.id==task.user_id).first()
    if not user:
        raise HTTPException(status_code=404,detail="User not found")

    #creer la tache 
    db_task=models.Task(**task.dict())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

#PUT/tasks/{id}
@router.put("/{task_id}",response_model=schemas.Task)
def update_task(task_id:int,task_update:schemas.TaskUpdate,db:Session=Depends(get_db)):
    task=db.query(models.Task).filter(models.Task.id==task_id).first()
    if not task:
        raise HTTPException(status_code=404,detail="task not found")
    
    #mettre a jour les champs
    if task_update.title is not None:
        task.title=task_update.title
    if task_update.description is not None:
        task.description=task_update.description
    if task_update.completed is not None:
        task.completed=task_update.completed

    db.commit()
    db.refresh(task)
    return task

#DELETLE/tasks/{id}
@router.delete("/{task_id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id:int,db:Session=Depends(get_db)):
    task=db.query(models.Task).filter(models.Task.id==task_id).first()
    if not task:
        raise HTTPException(status_code=404,detail="task not found")
    
    db.delete(task)
    db.commit()
    return None #204 no content