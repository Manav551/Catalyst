from motor.motor_asyncio import AsyncIOMotorClient
import os
import certifi

print("🔄 Initializing MongoDB client...")

# MongoDB connection with SSL configuration
try:
    mongodb_uri = os.getenv("MONGODB_URI")
    
    # Create client with SSL certificate and timeout settings
    client = AsyncIOMotorClient(
        mongodb_uri,
        tlsCAFile=certifi.where(),
        serverSelectionTimeoutMS=5000,
        connectTimeoutMS=10000,
        socketTimeoutMS=10000,
    )
    
    db = client.contentai
    
    # Test connection
    async def test_connection():
        try:
            await client.admin.command('ping')
            print("✅ MongoDB Atlas connected successfully")
            print(f"   Database: contentai")
            print(f"   Collections: content, brand_voice, templates")
            return True
        except Exception as e:
            print(f"❌ MongoDB connection failed: {e}")
            print(f"   URI: {mongodb_uri[:50]}...")  # Print partial URI for debugging
            return False
    
except Exception as e:
    print(f"❌ Failed to initialize MongoDB client: {e}")
    raise e

# Collections
content_collection = db.content
brand_voice_collection = db.brand_voice
templates_collection = db.templates

async def get_database():
    """Dependency for database access"""
    return db