"""
Generate synthetic resume data for demonstration purposes.
"""
import json
import random

# Sample job titles and skills
JOB_TITLES = [
    "Software Engineer", "Data Scientist", "Product Manager", "DevOps Engineer",
    "Frontend Developer", "Backend Developer", "Full Stack Developer", "UI/UX Designer",
    "Machine Learning Engineer", "Data Analyst", "Business Analyst", "Project Manager",
    "QA Engineer", "Security Engineer", "Cloud Architect", "Mobile Developer",
    "System Administrator", "Database Administrator", "Network Engineer", "AI Researcher"
]

SKILLS = {
    "programming": ["Python", "Java", "JavaScript", "C++", "Go", "Ruby", "PHP", "Swift", "Kotlin", "TypeScript"],
    "frameworks": ["React", "Angular", "Vue.js", "Django", "Flask", "Spring Boot", "Express.js", "TensorFlow", "PyTorch", "Scikit-learn"],
    "databases": ["MySQL", "PostgreSQL", "MongoDB", "Redis", "Cassandra", "DynamoDB", "Oracle", "SQL Server"],
    "cloud": ["AWS", "Azure", "Google Cloud", "Docker", "Kubernetes", "Terraform", "Jenkins", "CircleCI"],
    "soft_skills": ["Leadership", "Communication", "Problem Solving", "Team Collaboration", "Agile", "Scrum", "Critical Thinking"]
}

EXPERIENCE_DESCRIPTIONS = [
    "Developed and maintained scalable web applications",
    "Led a team of developers in building microservices architecture",
    "Implemented machine learning models for predictive analytics",
    "Designed and optimized database schemas for high performance",
    "Collaborated with cross-functional teams to deliver products",
    "Automated deployment processes using CI/CD pipelines",
    "Conducted code reviews and mentored junior developers",
    "Improved system performance by optimizing algorithms",
    "Built RESTful APIs and integrated third-party services",
    "Created data visualizations and dashboards for stakeholders"
]

EDUCATION = [
    "Bachelor's in Computer Science",
    "Master's in Data Science",
    "Bachelor's in Information Technology",
    "Master's in Software Engineering",
    "PhD in Machine Learning",
    "Bachelor's in Mathematics",
    "Master's in Artificial Intelligence"
]

def generate_resume(resume_id):
    """Generate a single synthetic resume."""
    # Select job title
    job_title = random.choice(JOB_TITLES)
    
    # Generate relevant skills (5-10 skills)
    all_skills = []
    for skill_category in SKILLS.values():
        all_skills.extend(skill_category)
    
    num_skills = random.randint(5, 10)
    skills = random.sample(all_skills, num_skills)
    
    # Generate experience (2-4 bullet points)
    num_experiences = random.randint(2, 4)
    experience = random.sample(EXPERIENCE_DESCRIPTIONS, num_experiences)
    
    # Generate education
    education = random.choice(EDUCATION)
    
    # Generate years of experience
    years_experience = random.randint(1, 15)
    
    # Create resume text
    resume_text = f"""
Name: Candidate {resume_id}
Job Title: {job_title}
Years of Experience: {years_experience}

Skills: {', '.join(skills)}

Experience:
{chr(10).join('- ' + exp for exp in experience)}

Education: {education}
"""
    
    return {
        "id": resume_id,
        "name": f"Candidate {resume_id}",
        "job_title": job_title,
        "years_experience": years_experience,
        "skills": skills,
        "experience": experience,
        "education": education,
        "resume_text": resume_text.strip()
    }

def generate_dataset(num_resumes=100):
    """Generate a dataset of synthetic resumes."""
    resumes = []
    for i in range(1, num_resumes + 1):
        resumes.append(generate_resume(i))
    return resumes

def save_dataset(resumes, filename="resumes.json"):
    """Save the dataset to a JSON file."""
    with open(filename, 'w') as f:
        json.dump(resumes, f, indent=2)
    print(f"Generated {len(resumes)} resumes and saved to {filename}")

if __name__ == "__main__":
    # Generate 100 synthetic resumes
    resumes = generate_dataset(100)
    save_dataset(resumes)
