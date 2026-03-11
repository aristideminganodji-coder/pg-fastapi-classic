from fastapi import APIRouter,HTTPException,Depends,status
from sqlalchemy.orm import Session
from app import models,schemas
from app.database import get_db
from app.routers.auth import get_password_hash

router=APIRouter(prefix="/users",tags=["Users"])

#GET/users/
@router.get("/",response_model=list[schemas.UserOut])
def get_users(skip:int=0,limit=100,db:Session=Depends(get_db)):
    users=db.query(models.User).offset(skip).limit(limit).all()
    return users

#GET/users/{id}
@router.get("/{user_id}",response_model=schemas.UserOut)
def get_user(user_id:int,db:Session=Depends(get_db)):
    user=db.query(models.User).filter(models.User.id==user_id).first()
    if not user:
        raise HTTPException(status_code=404,detail="User not found")
    return user

#PUT/user/{id}
@router.put("/{user_id}",response_model=schemas.UserOut)
def put_user(user_id:int,user_update:schemas.UserUpdate,db:Session=Depends(get_db)):
    user=db.query(models.User).filter(models.User.id==user_id).first()

    if not user:
        raise HTTPException(status_code=404,detail="User not found")
    
    #mettre a jour les champs
    if user_update.email is not None:
        user.email=user_update.email
    if user_update.password is not None:
        user.hashed_password=get_password_hash(user_update.password)
    if user_update.is_active is not None:
        user.is_active=user_update.is_active

    db.commit()
    db.refresh(user)
    return user

#DELETE/users/{id}
@router.delete("/{user_id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id:int,db:Session=Depends(get_db)):
    user=db.query(models.User).filter(models.User.id==user_id).first()
    if not user:
        raise HTTPException(status_code=404,detail="User not found")

    tasks_count=db.query(models.Task).filter(models.Task.user_id==user_id).count()
    if tasks_count>0:
        raise HTTPException(status_code=400,detail="Impossible de supprimer l'utilisateur car ce dernier a encore des tache")
    
    db.delete(user)
    db.commit()
    return None #204 no content