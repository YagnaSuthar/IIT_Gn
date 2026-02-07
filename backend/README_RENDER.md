# FarmXpert Backend - Render Deployment

This folder contains the backend FastAPI application configured for Render deployment.

## Quick Start for Render

1. **Repository Setup**
   ```bash
   git init
   git add .
   git commit -m "Initial backend setup for Render"
   git remote add origin https://github.com/yourusername/farmxpert-backend.git
   git push -u origin main
   ```

2. **Render Configuration**
   - Connect this repository to Render Web Service
   - Environment: Python 3
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app.main:app --workers 1 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:$PORT`

3. **Required Environment Variables**
   ```
   GEMINI_API_KEY=your-gemini-api-key
   JWT_SECRET_KEY=your-jwt-secret
   DATABASE_URL=auto-set-by-render
   REDIS_URL=auto-set-by-render
   ```

4. **Database Setup**
   - Add PostgreSQL service on Render
   - Run `python scripts/init_db.py` in Render Shell

## Key Files

- `render.yaml` - Render service configuration
- `requirements.txt` - Python dependencies
- `app/main.py` - FastAPI application entry point
- `scripts/init_db.py` - Database initialization script

## API Endpoints

Once deployed, your API will be available at:
`https://your-service-name.onrender.com`

Documentation available at:
`https://your-service-name.onrender.com/docs`
