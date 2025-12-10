from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from backend.utils.security import hash_password, verify_password
from backend.database import get_db_connection

router = APIRouter(prefix="/auth")

class UserRegister(BaseModel):
    username: str
    password: str

class UserLogin(BaseModel):
    username: str
    password: str


@router.post("/register")
def register(user: UserRegister):
    print("📩 RAW USER INPUT:", user)
    print("📩 PASSWORD RECEIVED:", repr(user.password))
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM users WHERE username = ?", (user.username,))
    existing = cur.fetchone()

    if existing:
        raise HTTPException(status_code=400, detail="Username already exists")

    if len(user.password.encode("utf-8")) > 72:
        raise HTTPException(
            status_code=400,
            detail="Password too long (max 72 characters)"
        )

    hashed_pw = hash_password(user.password)

    cur.execute(
        "INSERT INTO users (username, password_hash) VALUES (?, ?)",
        (user.username, hashed_pw)
    )
    conn.commit()
    conn.close()

    return {"message": "User registered successfully"}


@router.post("/login")
def login(user: UserLogin):
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM users WHERE username = ?", (user.username,))
    db_user = cur.fetchone()

    if not db_user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    if not verify_password(user.password, db_user["password_hash"]):
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    return {"message": "Login successful", "user_id": db_user["id"]}
