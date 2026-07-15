from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app.database.dependencies import get_db
from app.auth.dependencies import get_current_user

from app.models.user import User
from app.models.vault import Vault

from app.schemas.vault import VaultCreate, VaultUpdate

from app.utils.encryption import encrypt_password, decrypt_password
from app.utils.password_strength import check_password_strength
from app.utils.password_generator import generate_password

router = APIRouter(
    prefix="/vault",
    tags=["Vault"]
)


# -----------------------------
# Add Password
# -----------------------------
@router.post("/add")
def add_password(
    vault: VaultCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    # Check password strength
    strength = check_password_strength(vault.password)

    # Save encrypted password
    new_password = Vault(
    title=vault.title,
    website=vault.website,
    username=vault.username,
    password=encrypt_password(vault.password),
    category=vault.category,
    owner_id=current_user.id
)

    db.add(new_password)
    db.commit()
    db.refresh(new_password)

    return {
        "message": "Password Saved Successfully",
        "id": new_password.id,
        "strength": strength
    }


# -----------------------------
# Get All Passwords
# -----------------------------
@router.get("/all")
def get_all_passwords(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    passwords = (
        db.query(Vault)
        .filter(Vault.owner_id == current_user.id)
        .all()
    )

    result = []

    for password in passwords:
        result.append({
    "id": password.id,
    "title": password.title,
    "website": password.website,
    "username": password.username,
    "password": decrypt_password(password.password),
    "category": password.category,
    "is_favorite": password.is_favorite,
    "created_at": password.created_at,
    "updated_at": password.updated_at,
    "owner_id": password.owner_id
})
    return result


# -----------------------------
# Generate Secure Password
# -----------------------------
@router.get("/generate")
def generate_secure_password(
    length: int = Query(16, ge=8, le=64)
):

    password = generate_password(length)

    return {
        "generated_password": password
    }

@router.get("/search")
def search_passwords(
    query: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    passwords = (
        db.query(Vault)
        .filter(
            Vault.owner_id == current_user.id
        )
        .all()
    )

    result = []

    for password in passwords:

        if (
            query.lower() in password.title.lower()
            or query.lower() in password.website.lower()
            or query.lower() in password.username.lower()
        ):

            result.append({
    "id": password.id,
    "title": password.title,
    "website": password.website,
    "username": password.username,
    "password": decrypt_password(password.password),
    "category": password.category,
    "is_favorite": password.is_favorite,
    "owner_id": password.owner_id
})

    return result

@router.put("/favorite/{password_id}")
def toggle_favorite(
    password_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    password = (
        db.query(Vault)
        .filter(
            Vault.id == password_id,
            Vault.owner_id == current_user.id
        )
        .first()
    )

    if password is None:
        raise HTTPException(
            status_code=404,
            detail="Password not found"
        )

    password.is_favorite = not password.is_favorite

    db.commit()
    db.refresh(password)

    return {
        "message": "Favorite status updated",
        "is_favorite": password.is_favorite
    }

@router.get("/favorites")
def get_favorite_passwords(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    passwords = (
        db.query(Vault)
        .filter(
            Vault.owner_id == current_user.id,
            Vault.is_favorite == True
        )
        .all()
    )

    result = []

    for password in passwords:
        result.append({
    "id": password.id,
    "title": password.title,
    "website": password.website,
    "username": password.username,
    "password": decrypt_password(password.password),
    "category": password.category,
    "is_favorite": password.is_favorite,
    "created_at": password.created_at,
    "updated_at": password.updated_at
})

    return result
# -----------------------------
# Update Password
# -----------------------------
@router.put("/update/{password_id}")
def update_password(
    password_id: int,
    vault: VaultUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    password = (
        db.query(Vault)
        .filter(
            Vault.id == password_id,
            Vault.owner_id == current_user.id
        )
        .first()
    )

    if password is None:
        raise HTTPException(
            status_code=404,
            detail="Password not found"
        )

    password.title = vault.title
    password.website = vault.website
    password.username = vault.username
    password.password = encrypt_password(vault.password)
    password.category = vault.category
    db.commit()
    db.refresh(password)

    return {
        "message": "Password updated successfully"
    }


# -----------------------------
# Delete Password
# -----------------------------
@router.delete("/delete/{password_id}")
def delete_password(
    password_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    password = (
        db.query(Vault)
        .filter(
            Vault.id == password_id,
            Vault.owner_id == current_user.id
        )
        .first()
    )

    if password is None:
        raise HTTPException(
            status_code=404,
            detail="Password not found"
        )

    db.delete(password)
    db.commit()

    return {
        "message": "Password deleted successfully"
    }