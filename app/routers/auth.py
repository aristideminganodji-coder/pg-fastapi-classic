from fastapi import APIRouter,Depends,HTTPException,status
from sqlalchemy.orm import Session
from app import models,schemas
from app.database import get_db
from passlib.context import CryptContext
import bcrypt

router=APIRouter(prefix="/auth",tags=["Authentication"])

#crypte le mot de passe lors du register
def get_password_hash(password:str)->str:
    #hash du mot de passe avec bcrypt
    #convertir en byters et hasher
    salt=bcrypt.gensalt()
    hashed=bcrypt.hashpw(password.encode('utf-8'),salt)
    return hashed.decode('utf-8')

#Permet de verifier le mot de passe entre par le user lors du login
def verify_password(plain_password:str,hashed_password:str)->bool:
    #verifie un mot de passe
    return bcrypt.checkpw(
        plain_password.encode('utf-8'),
        hashed_password.encode('utf-8')
    )

@router.post("/register",response_model=schemas.UserOut,status_code=status.HTTP_201_CREATED)
def register(user:schemas.UserCreate,db:Session=Depends(get_db)):
    #verifier si l'utilisateur existe deja
    existing_user=db.query(models.User).filter(models.User.email==user.email).first()
    if existing_user:
        raise HTTPException(status_code=400,detail="Email already registered")
    
    #hasher le mot de passw
    hashed_password=get_password_hash(user.password) 

    #creer l'utilisateur
    db_user=models.User(email=user.email,hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user

@router.post("/login-simple")
def login_simple(user:schemas.UserCreate,db:Session=Depends(get_db)):
    db_user=db.query(models.User).filter(models.User.email==user.email).first()

    #verifier le mot de passe
    if not db_user or not verify_password(user.password,db_user.hashed_password):
        raise HTTPException(status_code=401,detail="Email ou mot de passe incorrect")
    return {"message":"connexion reussie","user_id":db_user.id}