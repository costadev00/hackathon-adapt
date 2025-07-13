import os
import modal
from pydantic import BaseModel
from typing import Dict, Any
# Create Modal image with all required dependencies and local files
image = modal.Image.debian_slim(python_version="3.13").pip_install(
    "fastapi[standard]",
    "langgraph",
    "langchain-openai",
    "langflow-base",
    "pydantic"
).add_local_dir(".", "/root")

app = modal.App(name="edu_one", image=image)

# Request/Response models
class CourseRequest(BaseModel):
    topic: str

class CourseResponse(BaseModel):
    modules: list

class FlashcardsRequest(BaseModel):
    course_content: Dict[str, Any]

class FlashcardsResponse(BaseModel):
    flashcards: list

class QuizRequest(BaseModel):
    content_json: str

class QuizResponse(BaseModel):
    questions: list

class CoursePackageRequest(BaseModel):
    topic: str

class CoursePackageResponse(BaseModel):
    course_content: Dict[str, Any]
    flashcards: Dict[str, Any]
    quiz: Dict[str, Any]

@app.function()
@modal.fastapi_endpoint(docs=True)
def hello():
    return {"message": "Hello from EduOne API!"}

@app.function()
@modal.fastapi_endpoint(method="POST", docs=True)
def generate_course_content(request: CourseRequest):
    """Generate course content for a given topic."""
    try:
        from course_content_agent import generate_course_content
        course_content = generate_course_content(request.topic)
        return {"course_content": course_content}
    except Exception as e:
        return {"error": str(e)}

@app.function()
@modal.fastapi_endpoint(method="POST", docs=True)
def generate_flashcards(request: FlashcardsRequest):
    """Generate flashcards based on course content."""
    try:
        from flashcards_agent import generate_flashcards
        flashcards = generate_flashcards(request.course_content)
        return {"flashcards": flashcards}
    except Exception as e:
        return {"error": str(e)}

@app.function()
@modal.fastapi_endpoint(method="POST", docs=True)
def generate_quiz(request: QuizRequest):
    """Generate a quiz based on course content JSON."""
    try:
        from quizzes_agent import generate_quiz
        quiz = generate_quiz(request.content_json)
        return {"quiz": quiz}
    except Exception as e:
        return {"error": str(e)}

@app.function()
@modal.fastapi_endpoint(method="POST", docs=True)
def generate_course_package(request: CoursePackageRequest):
    """Generate a complete course package with content, flashcards, and quiz."""
    try:
        from course_content_agent import generate_course_content
        from flashcards_agent import generate_flashcards
        from quizzes_agent import generate_quiz
        import json

        # Generate course content
        course_content = generate_course_content(request.topic)

        # Generate flashcards
        flashcards = generate_flashcards(course_content)

        # Generate quiz
        content_json = json.dumps(course_content, ensure_ascii=False, indent=2)
        quiz = generate_quiz(content_json)

        package = {
            "course_content": course_content,
            "flashcards": flashcards,
            "quiz": quiz
        }

        return package
    except Exception as e:
        return {"error": str(e)}

@app.function()
@modal.fastapi_endpoint(method="GET", docs=True)
def health():
    """Health check endpoint."""
    return {"status": "healthy", "service": "EduOne API"}

@app.function()
@modal.fastapi_endpoint(method="GET", docs=True)
def test_agents():
    """Test endpoint to verify all agents can be imported and work."""
    try:
        # Test course content agent
        from course_content_agent import generate_course_content

        # Test flashcards agent
        from flashcards_agent import generate_flashcards

        # Test quiz agent
        from quizzes_agent import generate_quiz

        return {
            "status": "success",
            "message": "All agents imported successfully",
            "agents": ["course_content_agent", "flashcards_agent", "quizzes_agent"]
        }
    except Exception as e:
        return {
            "status": "error",
            "message": f"Failed to import agents: {str(e)}"
        }
