from pydantic import BaseModel, Field, EmailStr
from typing import Optional, Dict, Any, List
from datetime import datetime

# User Models
class UserCreate(BaseModel):
    name: str = Field(..., min_length=2, max_length=100)
    email: str
    password: str = Field(..., min_length=6)

class UserLogin(BaseModel):
    email: str
    password: str

class UserResponse(BaseModel):
    id: str
    email: str
    name: str

class TokenResponse(BaseModel):
    token: str
    user: UserResponse
    message: str

# Content Models
class ContentGenerate(BaseModel):
    prompt: Optional[str] = None
    templateType: Optional[str] = None
    inputs: Optional[Dict[str, Any]] = None
    options: Optional[Dict[str, Any]] = None

class ContentImprove(BaseModel):
    content: str
    instructions: str

class ContentVariations(BaseModel):
    content: str
    count: Optional[int] = 3

class ContentRequest(BaseModel):
    template: str  # blog, social, email, product, ad, video
    topic: str
    tone: Optional[str] = "professional"
    target_audience: Optional[str] = None
    industry: Optional[str] = None
    platform: Optional[str] = "general"  # For social/ads: facebook, instagram, linkedin, twitter
    count: Optional[int] = 1  # Number of variations for social/ads
    goal: Optional[str] = None  # For emails: "convert", "nurture", "inform"
    additional_context: Optional[str] = None

class ContentResponse(BaseModel):
    content: str
    template: str
    message: str

# Brand Voice Models
class BrandVoice(BaseModel):
    tone: str
    style: str
    messaging: Optional[str] = None
    audience: Optional[str] = None
    keywords: Optional[str] = None

class BrandVoiceResponse(BaseModel):
    success: bool
    message: str
    brandVoice: Optional[Dict[str, Any]] = None

# Template Models
class TemplateResponse(BaseModel):
    success: bool
    template: Optional[Dict[str, Any]] = None
    templates: Optional[list] = None
    categories: Optional[list] = None
