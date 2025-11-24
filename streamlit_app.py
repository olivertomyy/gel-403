import streamlit as st
import random
import json
import os
import tempfile
import io
import pickle
import time

# Constants for session persistence
SESSION_FILE = "exam_session.pkl"

def save_session_state():
    """Save critical session state to file for persistence"""
    try:
        session_data = {
            'questions': st.session_state.get('questions', []),
            'current_question': st.session_state.get('current_question', 0),
            'score': st.session_state.get('score', 0),
            'answered': st.session_state.get('answered', False),
            'user_answers': st.session_state.get('user_answers', []),
            'exam_completed': st.session_state.get('exam_completed', False),
            'topics': st.session_state.get('topics', {}),
            'questions_loaded': st.session_state.get('questions_loaded', False),
            'last_uploaded_file_name': st.session_state.get('last_uploaded_file_name', None),
            'session_timestamp': time.time()
        }
        
        with open(SESSION_FILE, 'wb') as f:
            pickle.dump(session_data, f)
    except Exception as e:
        print(f"Warning: Could not save session: {e}")

def load_session_state():
    """Load session state from file if it exists and is recent"""
    try:
        if os.path.exists(SESSION_FILE):
            # Check if session file is recent (less than 24 hours old)
            file_age = time.time() - os.path.getmtime(SESSION_FILE)
            if file_age < 24 * 3600:  # 24 hours
                with open(SESSION_FILE, 'rb') as f:
                    session_data = pickle.load(f)
                return session_data
    except Exception as e:
        print(f"Warning: Could not load session: {e}")
    return None

def load_questions_from_json():
    """Load questions from JSON file with the programming_languages_exam_questions structure"""
    try:
        # Try to load from local file first
        if os.path.exists("programming_questions.json"):
            with open("programming_questions.json", 'r', encoding='utf-8') as f:
                data = json.load(f)
                questions = extract_questions_from_data(data)
                if questions:
                    st.success(f"✅ Loaded {len(questions)} exam questions from local file")
                    return questions
        
        # If local file doesn't exist, use fallback questions
        st.info("📝 Using built-in exam questions")
        return get_fallback_exam_questions()
        
    except Exception as e:
        st.error(f"❌ Error loading questions: {e}")
        return get_fallback_exam_questions()

def extract_questions_from_data(data):
    """Extract questions from JSON data structure"""
    # If data is already a list of questions
    if isinstance(data, list) and len(data) > 0:
        if validate_question_structure(data[0]):
            return data
    
    # Look for questions in common keys
    possible_keys = [
        "programming_languages_exam_questions",
        "chemistry_questions",
        "questions",
        "quiz_questions",
        "exam_questions",
        "question_bank",
        "items"
    ]
    
    for key in possible_keys:
        if key in data and isinstance(data[key], list) and len(data[key]) > 0:
            questions = data[key]
            if validate_question_structure(questions[0]):
                return questions
    
    # If no standard key found, look for any list with question structure
    for key, value in data.items():
        if isinstance(value, list) and len(value) > 0:
            if validate_question_structure(value[0]):
                return value
    
    return None

def validate_question_structure(question):
    """Validate that the question has the required structure"""
    if not isinstance(question, dict):
        return False
    
    required_fields = ['question', 'options', 'correct_answer']
    return all(field in question for field in required_fields)

def get_fallback_exam_questions():
    """Provide comprehensive fallback exam questions"""
    return [
        {
            "id": 1,
            "topic": "Language Categories",
            "question": "Which category of programming languages achieves its effect by changing the value of variables through assignment statements?",
            "options": {
                "A": "Functional Languages",
                "B": "Logic Programming Languages", 
                "C": "Imperative Languages",
                "D": "Object-Oriented Languages"
            },
            "correct_answer": "C",
            "page": 1,
            "explanation": "Imperative languages work by changing program state through assignment statements and commands."
        },
        {
            "id": 2,
            "topic": "Functional Programming",
            "question": "Which of the following is a key characteristic of functional programming?",
            "options": {
                "A": "Mutable state",
                "B": "Side effects",
                "C": "Immutable data",
                "D": "Class inheritance"
            },
            "correct_answer": "C",
            "page": 2,
            "explanation": "Functional programming emphasizes immutable data and avoiding side effects."
        },
        {
            "id": 3,
            "topic": "Object-Oriented Programming",
            "question": "What is encapsulation in OOP?",
            "options": {
                "A": "Hiding implementation details",
                "B": "Creating multiple instances",
                "C": "Inheriting properties",
                "D": "Polymorphic behavior"
            },
            "correct_answer": "A",
            "page": 3,
            "explanation": "Encapsulation bundles data and methods while hiding internal implementation details."
        }
    ]

def analyze_exam_topics(questions):
    """Analyze and categorize exam questions by topic"""
    topics = {}
    for q in questions:
        topic = q.get('topic', 'General')
        topics[topic] = topics.get(topic, 0) + 1
    return topics

def initialize_exam_state(questions=None, restore_progress=False):
    """Initialize or reset the exam state"""
    if questions is None:
        questions = load_questions_from_json()
    
    if restore_progress and st.session_state.get('questions_loaded', False):
        # Keep existing progress
        st.info("🔄 Restored your exam progress")
    else:
        # Reset progress
        st.session_state.questions = questions
        st.session_state.current_question = 0
        st.session_state.score = 0
        st.session_state.answered = False
        st.session_state.user_answers = [None] * len(questions)
        st.session_state.exam_completed = False
        st.session_state.topics = analyze_exam_topics(questions)
        st.session_state.questions_loaded = True
    
    # Save session after initialization
    save_session_state()

def parse_uploaded_json(uploaded_file):
    """Parse uploaded JSON file and extract questions"""
    try:
        # Read the file content
        content = uploaded_file.read()
        
        # Try to decode as JSON
        try:
            data = json.loads(content.decode('utf-8'))
        except UnicodeDecodeError:
            # If UTF-8 fails, try other encodings
            try:
                data = json.loads(content.decode('latin-1'))
            except:
                st.error("❌ Could not decode the file. Please use UTF-8 encoding.")
                return None
        
        # Extract questions from the data
        questions = extract_questions_from_data(data)
        
        if questions:
            st.success(f"✅ Successfully loaded {len(questions)} questions!")
            return questions
        else:
            st.error("❌ No valid questions found in the uploaded file. Please check the format.")
            return None
        
    except json.JSONDecodeError as e:
        st.error(f"❌ Invalid JSON format: {e}")
        return None
    except Exception as e:
        st.error(f"❌ Error parsing JSON file: {e}")
        return None

def save_uploaded_file(uploaded_file):
    """Save uploaded file locally"""
    try:
        with open("programming_questions.json", "wb") as f:
            f.write(uploaded_file.getbuffer())
        st.success("✅ File saved successfully!")
        return True
    except Exception as e:
        st.error(f"❌ Error saving file: {e}")
        return False

def main():
    # Set page configuration
    st.set_page_config(
        page_title="EXAM QUESTIONS",
        page_icon="💻",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    # Try to load existing session first
    if 'questions_loaded' not in st.session_state:
        saved_session = load_session_state()
        if saved_session:
            # Restore from saved session
            for key, value in saved_session.items():
                st.session_state[key] = value
            st.success("🔁 Restored your previous exam session!")
        else:
            # Initialize fresh session
            initialize_exam_state()
    
    # Header
    st.title("💻 Exam - Persistent Session")
    st.markdown("### Your progress is automatically saved! Leave and return anytime.")
    
    # Auto-save notice
    st.info("💾 **Auto-save enabled**: Your progress is automatically saved and will be restored when you return.")
    
    # File Upload Section
    with st.expander("📁 Upload Your JSON Question File", expanded=False):
        st.markdown("""
        **Upload your JSON file with questions in this format:**
        ```json
        {
          {
"questions": [
{
"id": 1,
"topic": "Work Readiness",
"question": "According to the text, what is no longer sufficient to differentiate a candidate from other bright sparks in the job market?",
"options": {
"A": "Work experience",
"B": "A university degree",
"C": "Soft skills",
"D": "Networking connections"
},
"correct_answer": "B",
"explanation": "Page 1 states: 'Having a degree, while incredibly important and rewarding, is no longer sufficient to differentiate you from all the other bright sparks trying to enter the job market.'"
},
{
"id": 2,
"topic": "Work Readiness",
"question": "What types of jobs are now being filled by graduates, despite not requiring a university qualification?",
"options": {
"A": "Engineering and medical roles",
"B": "Bank clerks, police officers, and shop managers",
"C": "Senior executive positions",
"D": "IT specialists and developers"
},
"correct_answer": "B",
"explanation": "Page 1 mentions: 'jobs that don’t even require a university qualification (bank clerks, police officers, restaurant and shop managers) are now being filled by graduates.'"
},
{
"id": 3,
"topic": "Work Readiness",
"question": "Work readiness refers to which of the following expected by employers?",
"options": {
"A": "High GPA and academic awards",
"B": "Skills, aptitudes, and attitudes",
"C": "Financial stability and dress code",
"D": "Previous management experience"
},
"correct_answer": "B",
"explanation": "Page 1 defines Work Readiness as: 'Refers to the skills, aptitudes, and attitudes employers expect job seekers to have in preparation for the culture and demands of the workplace.'"
},
{
"id": 4,
"topic": "Self Awareness",
"question": "According to the text, what is the 'ticket to a shining career'?",
"options": {
"A": "Being flawless in an interview",
"B": "Having a First Class degree",
"C": "Being aware of both your strengths and weaknesses",
"D": "Hiding your faults from the employer"
},
"correct_answer": "C",
"explanation": "Page 1 states: 'The ticket to a shining career is being aware of both your strengths and weaknesses.'"
},
{
"id": 5,
"topic": "Personal Branding",
"question": "What does a strong personal brand help a hiring manager decide?",
"options": {
"A": "How much to pay you",
"B": "How suitable you will be for a role",
"C": "Where you live",
"D": "Your academic history"
},
"correct_answer": "B",
"explanation": "Page 2 states: 'The stronger your personal brand, the easier it is for someone hiring you to decide how suitable you’ll be for a role.'"
},
{
"id": 6,
"topic": "Soft Skills",
"question": "Why might an employer hire a graduate with a 2:1 over someone with a First?",
"options": {
"A": "They are cheaper to hire",
"B": "They have better technical knowledge",
"C": "They possess the right soft skills and attributes",
"D": "They have more academic references"
},
"correct_answer": "C",
"explanation": "Page 2 explains: 'In some jobs, an employer would rather hire a graduate with a 2:1 over someone with a First if they have the right skills and attributes... because it’s easier to train someone in the technical aspects... than train them to acquire communication... capabilities.'"
},
{
"id": 7,
"topic": "Problem Solving",
"question": "What does the 'I' in the IDEAL problem-solving framework stand for?",
"options": {
"A": "Initiate the plan",
"B": "Identify the problem",
"C": "Investigate the cause",
"D": "Imagine the solution"
},
"correct_answer": "B",
"explanation": "Page 2 lists the IDEAL framework where I stands for: 'Identify the problem'."
},
{
"id": 8,
"topic": "Job Search Strategies",
"question": "What percentage of job seekers rely on applying online, and what is the approximate yield rate?",
"options": {
"A": "50% rely on it; 10% yield",
"B": "90% rely on it; less than 3% yield",
"C": "75% rely on it; 20% yield",
"D": "30% rely on it; 50% yield"
},
"correct_answer": "B",
"explanation": "Page 3 states: 'Over 90% of the job seekers rely on this strategy only, yet it yields less than a 3% chance of getting an interview.'"
},
{
"id": 9,
"topic": "Job Search Strategies",
"question": "How much more likely are job seekers to get a job offer through a referral?",
"options": {
"A": "Two times more likely",
"B": "Three times more likely",
"C": "Five times more likely",
"D": "Ten times more likely"
},
"correct_answer": "C",
"explanation": "Page 3 states: 'Studies also show that job seekers are five times more likely to get a job offer through a job referral.'"
},
{
"id": 10,
"topic": "Networking",
"question": "When connecting with executive or agency recruiters, who do they work for?",
"options": {
"A": "They work for the job seeker",
"B": "They work for the government",
"C": "They work for themselves only",
"D": "They work for the employers"
},
"correct_answer": "D",
"explanation": "Page 3 states: 'Keep in mind that recruiters don't work for you, they work for the employers.'"
},
{
"id": 11,
"topic": "Networking",
"question": "Why are management level executives considered 'influencers' or 'decision-makers'?",
"options": {
"A": "They have large social media followings",
"B": "They are the ones who identify that they need to hire people",
"C": "They control the company budget",
"D": "They interview every candidate personally"
},
"correct_answer": "B",
"explanation": "Page 4 states: 'Management level executives are the people whom I consider as influencers or decision-makers because they are the ones who identify that they need to hire people.'"
},
{
"id": 12,
"topic": "Networking",
"question": "What type of conversation should you start with an executive to stand out?",
"options": {
"A": "A pitch about your resume",
"B": "A request for a job immediately",
"C": "A consultative conversation to understand business needs",
"D": "A conversation about salary expectations"
},
"correct_answer": "C",
"explanation": "Page 4 suggests: 'take a consultative approach where you start a conversation to understand business needs and challenges.'"
},
{
"id": 13,
"topic": "Job Search Strategies",
"question": "According to SHRM, by what percentage does a referral increase your chances of landing a job?",
"options": {
"A": "25%",
"B": "30%",
"C": "45%",
"D": "60%"
},
"correct_answer": "C",
"explanation": "Page 5 states: 'According to the Society of Human Resources Management, getting a referral increases your chances of landing the job by 45%.'"
},
{
"id": 14,
"topic": "LinkedIn Strategies",
"question": "How should you write the 'About' section on LinkedIn?",
"options": {
"A": "In the third person (e.g., 'He is...')",
"B": "In the first person (using 'I')",
"C": "As a bulleted list only",
"D": "Leaving it blank"
},
"correct_answer": "B",
"explanation": "Page 5 advises: 'write in first person, which means use “I” throughout this section.'"
},
{
"id": 15,
"topic": "Job Search Tactics",
"question": "Why is the 'shotgun approach' to applying for jobs described as never effective?",
"options": {
"A": "It focuses too much on one company",
"B": "It involves applying for anything and everything",
"C": "It requires too many cover letters",
"D": "It is too expensive"
},
"correct_answer": "B",
"explanation": "Page 5 states: 'The shotgun approach where you apply for anything and everything is never effective.'"
},
{
"id": 16,
"topic": "Networking Maintenance",
"question": "What is the recommended frequency for having a conversation with potential people from your network?",
"options": {
"A": "Once a month",
"B": "At least one conversation a week",
"C": "Every day",
"D": "Only when you need a job"
},
"correct_answer": "B",
"explanation": "Page 6 recommends: 'Make your list of potential people to call and have at least one conversation a week.'"
},
{
"id": 17,
"topic": "References",
"question": "How many references should you line up?",
"options": {
"A": "One or two",
"B": "Three to five",
"C": "Five to ten",
"D": "Just one family member"
},
"correct_answer": "B",
"explanation": "Page 6 states: 'You need three to five references.'"
},
{
"id": 18,
"topic": "Job Search Tactics",
"question": "When contacting a department head directly, what should you NOT include in your initial message?",
"options": {
"A": "Your phone number",
"B": "Your accomplishments",
"C": "A resume",
"D": "Interest in the company"
},
"correct_answer": "C",
"explanation": "Page 6 explicitly states: 'Do not include a resume. A personal conversation is what you are after.'"
},
{
"id": 19,
"topic": "CV Basics",
"question": "What does 'Curriculum Vitae' translate to from Latin?",
"options": {
"A": "Work History",
"B": "Course of Life",
"C": "Skills and Abilities",
"D": "Professional Summary"
},
"correct_answer": "B",
"explanation": "Page 7 states: 'CV stands for Curriculum Vitae (latin for: course of life).'"
},
{
"id": 20,
"topic": "CV Formatting",
"question": "What is the recommended font size for the body text of a CV?",
"options": {
"A": "9 to 10 pt",
"B": "11 to 12 pt",
"C": "14 to 16 pt",
"D": "18 pt"
},
"correct_answer": "B",
"explanation": "Page 7 advises: 'Use 11 to 12 pt font size and single spacing.'"
},
{
"id": 21,
"topic": "CV Content",
"question": "What is the difference between a CV Objective and a CV Summary?",
"options": {
"A": "Objectives are for executives; Summaries are for students",
"B": "Objectives are longer than Summaries",
"C": "Objectives show skills and fit (good for little experience); Summaries highlight career progress",
"D": "There is no difference"
},
"correct_answer": "C",
"explanation": "Page 8 explains: 'a CV objective shows what skills you’ve mastered and how you’d fit in... A CV summary, in turn, highlights your career progress and achievements.'"
},
{
"id": 22,
"topic": "CV Writing",
"question": "Which of the following is an example of an 'action verb' recommended for a CV?",
"options": {
"A": "Responsible for",
"B": "Implemented",
"C": "Hardworking",
"D": "Duties included"
},
"correct_answer": "B",
"explanation": "Page 8 lists action verbs: 'created,' 'analysed,' 'implemented,' not 'responsible for creating...'"
},
{
"id": 23,
"topic": "CV Ethics",
"question": "What is a potential consequence of altering your degree grade on a CV (e.g., from 2:2 to 2:1)?",
"options": {
"A": "A simple warning",
"B": "Degree fraud and a prison sentence",
"C": "Demotion",
"D": "A mandatory training course"
},
"correct_answer": "B",
"explanation": "Page 9 states: 'altering your degree grade from a 2:2 to 2:1 is classed as degree fraud and can result in a prison sentence.'"
},
{
"id": 24,
"topic": "Hard Skills",
"question": "Which of the following is considered a 'Hard Skill'?",
"options": {
"A": "Teamwork",
"B": "Empathy",
"C": "Data Analysis",
"D": "Conflict Management"
},
"correct_answer": "C",
"explanation": "Page 10 lists 'Data analysis' under Hard skills to include on a CV."
},
{
"id": 25,
"topic": "Soft Skills",
"question": "How are soft skills defined in the text?",
"options": {
"A": "Job-specific abilities learned through school",
"B": "Technical skills needed for a specific job",
"C": "Innate character traits that positively impact interaction with others",
"D": "Skills that are difficult to learn"
},
"correct_answer": "C",
"explanation": "Page 10 defines Soft skills as: 'innate character traits that positively impact how you work or interact with other people'."
},
{
"id": 26,
"topic": "Interview Goals",
"question": "According to research mentioned in the text, how quickly does an interviewer decide to hire on average?",
"options": {
"A": "In the first 30 seconds",
"B": "In just 5 minutes",
"C": "After the second interview",
"D": "After checking references"
},
"correct_answer": "B",
"explanation": "Page 12 states: 'Research indicates that, on average, an interviewer decides to hire in just 5 minutes.'"
},
{
"id": 27,
"topic": "Interview Preparation",
"question": "Which of the following is NOT one of the 7 key competencies employers look for?",
"options": {
"A": "Critical Thinking",
"B": "Physical Strength",
"C": "Teamwork/Collaboration",
"D": "Professionalism/Work Ethic"
},
"correct_answer": "B",
"explanation": "Page 12 lists the 7 key competencies, which include Critical Thinking, Teamwork, Leadership, etc., but not Physical Strength."
},
{
"id": 28,
"topic": "Interview Etiquette",
"question": "How early should you arrive for an interview?",
"options": {
"A": "30 minutes early",
"B": "Right on time",
"C": "10 minutes early",
"D": "1 hour early"
},
"correct_answer": "C",
"explanation": "Page 13 advises: 'Arrive 10 minutes early to allow yourself time to park and collect your thoughts.'"
},
{
"id": 29,
"topic": "Interview Types",
"question": "In a 'Traditional' interview, what is the typical speaking ratio?",
"options": {
"A": "Interviewer speaks 75%, Interviewee speaks 25%",
"B": "Interviewer speaks 50%, Interviewee speaks 50%",
"C": "Interviewer speaks 25%, Interviewee speaks 75%",
"D": "It is entirely a monologue by the candidate"
},
"correct_answer": "C",
"explanation": "Page 13 describes Traditional interviews: 'The interviewer typically asks questions and speaks about 25% of the time and the interviewee... speaks 75% of the time.'"
},
{
"id": 30,
"topic": "First Impressions",
"question": "How long does it take to form a first impression?",
"options": {
"A": "Thirty seconds",
"B": "Two minutes",
"C": "Ten minutes",
"D": "One hour"
},
"correct_answer": "A",
"explanation": "Page 14 states: 'First impressions take only thirty seconds.'"
},
{
"id": 31,
"topic": "Interview Tricks",
"question": "What is the '30 second – 2 minute rule' used for?",
"options": {
"A": "The time you have to read the job description",
"B": "The duration of your handshake",
"C": "Providing a concise but thorough answer",
"D": "The time you should wait before sitting down"
},
"correct_answer": "C",
"explanation": "Page 14 advises: 'Follow the 30 second – 2 minute rule so that you provide a concise but thorough answer.'"
},
{
"id": 32,
"topic": "Interview Questions",
"question": "When answering 'What are your weaknesses?', what should you include?",
"options": {
"A": "A list of all your faults",
"B": "A claim that you are a perfectionist",
"C": "An explanation of one area of improvement and how you are working on it",
"D": "A refusal to answer the question"
},
"correct_answer": "C",
"explanation": "Page 15 suggests: 'For your weakness, provide an explanation of one area of improvement... addressing how you are working to improve on this area.'"
},
{
"id": 33,
"topic": "Behavioral Interviews",
"question": "What technique should be used to answer behavioral interview questions?",
"options": {
"A": "STAR or CAR technique",
"B": "IDEAL framework",
"C": "SWOT analysis",
"D": "Yes/No answers"
},
"correct_answer": "A",
"explanation": "Page 16 states: 'Strong responses to behavioral interview questions use the STAR or “CAR” technique below.'"
},
{
"id": 34,
"topic": "Public Speaking",
"question": "Which of the following is NOT one of the five basic elements of a public speech mentioned in the figure?",
"options": {
"A": "Who?",
"B": "When?",
"C": "Whom?",
"D": "Medium?"
},
"correct_answer": "B",
"explanation": "Page 17 lists the elements in the figure: 'Who?', 'What?', 'Whom?', 'Medium?', 'Effect?'. 'When?' is not listed."
},
{
"id": 35,
"topic": "Public Speaking Strategies",
"question": "What is a suggested way to improve speaking skills dramatically after recording a presentation?",
"options": {
"A": "Deleting the video immediately",
"B": "Watching yourself later and working on areas that did not go well",
"C": "Sending it to a professional editor",
"D": "Only listening to the audio"
},
"correct_answer": "B",
"explanation": "Page 17 states: 'You can improve your speaking skills dramatically by watching yourself later, and then working on improving in areas that did not go well.'"
},
{
"id": 36,
"topic": "Speech Preparation",
"question": "Which step of eloquent speech preparation involves the creation of the structure of a coherent argument?",
"options": {
"A": "Invention",
"B": "Arrangement",
"C": "Style",
"D": "Memory"
},
"correct_answer": "B",
"explanation": "Page 18 defines Arrangement as: 'creation of the structure of a coherent argument'."
},
{
"id": 37,
"topic": "Conquering Nerves",
"question": "What is a 'great tip' mentioned to build rapport and reduce nerves before speaking?",
"options": {
"A": "Hide in the bathroom until the last minute",
"B": "Greet audience members at the door and do a quick survey",
"C": "Drink a lot of coffee",
"D": "Read your notes continuously"
},
"correct_answer": "B",
"explanation": "Page 18 advises: 'A great tip is to greet audience members at the door and do a quick survey of why they are there...'"
},
{
"id": 38,
"topic": "Presentation Delivery",
"question": "Why should you avoid memorizing your speech word-for-word?",
"options": {
"A": "It takes too long",
"B": "It makes your delivery sound like a robot and increases nervousness if you miss a word",
"C": "The audience prefers reading slides",
"D": "It is illegal"
},
"correct_answer": "B",
"explanation": "Page 19 states: 'all this does is make your delivery sound like it is coming from a robot. If you miss a word... your whole presentation is thrown off'."
},
{
"id": 39,
"topic": "Calming Nerves",
"question": "How does deep breathing help with public speaking nerves?",
"options": {
"A": "It makes you louder",
"B": "It tricks your body into believing you are calmer by slowing the pace",
"C": "It helps you memorize lines",
"D": "It stops you from sweating"
},
"correct_answer": "B",
"explanation": "Page 19 explains: 'the slower pace will trick your body into believing you are calmer.'"
},
{
"id": 40,
"topic": "Presentation Tips",
"question": "According to the 'Ten Tips' on the final page, what kind of slides should you use?",
"options": {
"A": "White slides",
"B": "Black slides",
"C": "Rainbow slides",
"D": "Text-heavy slides"
},
"correct_answer": "B",
"explanation": "Page 20 lists Tip 9 as: 'Use black slides'."
}
]
}
        }
        ```
        """)
        
        uploaded_file = st.file_uploader(
            "Choose a JSON file", 
            type="json",
            help="Upload your questions in JSON format",
            key="file_uploader"
        )
        
        # AUTO-LOAD when file is uploaded
        if uploaded_file is not None:
            # Parse the uploaded file
            questions = parse_uploaded_json(uploaded_file)
            
            if questions:
                # Store file info for persistence
                st.session_state.last_uploaded_file_name = uploaded_file.name
                
                # Initialize with new questions but preserve progress if compatible
                current_questions = st.session_state.get('questions', [])
                if len(current_questions) == len(questions):
                    st.info("📚 Questions updated while preserving your progress!")
                    st.session_state.questions = questions
                else:
                    st.warning("🔄 Question set changed - resetting progress")
                    initialize_exam_state(questions)
                
                save_session_state()
                st.rerun()
        
        # Manual controls for uploaded file
        if uploaded_file is not None:
            col1, col2 = st.columns(2)
            
            with col1:
                if st.button("🔄 Reload Uploaded Questions", type="primary"):
                    uploaded_file.seek(0)  # Reset file pointer
                    questions = parse_uploaded_json(uploaded_file)
                    if questions:
                        initialize_exam_state(questions)
                        st.success(f"✅ Reloaded {len(questions)} questions!")
                        st.rerun()
            
            with col2:
                if st.button("💾 Save File Locally"):
                    if save_uploaded_file(uploaded_file):
                        st.info("File saved as 'programming_questions.json'. It will be loaded automatically next time.")
    
    # Quick JSON Input Section
    with st.expander("📝 Or Paste JSON Directly", expanded=False):
        json_text = st.text_area(
            "Paste your JSON here:",
            height=200,
            placeholder='Paste your JSON questions here...',
            key="json_text_area"
        )
        
        if st.button("📥 Load from Text", type="secondary"):
            if json_text.strip():
                try:
                    # Create a temporary file-like object
                    fake_file = io.BytesIO(json_text.encode('utf-8'))
                    fake_file.name = "pasted_json.json"
                    
                    questions = parse_uploaded_json(fake_file)
                    if questions:
                        initialize_exam_state(questions)
                        st.success(f"✅ Loaded {len(questions)} questions from pasted JSON!")
                        st.rerun()
                except Exception as e:
                    st.error(f"❌ Error parsing JSON text: {e}")
            else:
                st.warning("Please paste some JSON text first.")
    
    # Show warning if no questions
    if not st.session_state.get('questions'):
        st.error("❌ No exam questions available.")
        return
    
    # Exam info header
    st.write("---")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Total Questions", len(st.session_state.questions))
    with col2:
        st.metric("Topics Covered", len(st.session_state.topics))
    with col3:
        if not st.session_state.exam_completed:
            current_attempted = sum(1 for ans in st.session_state.user_answers if ans is not None)
            st.metric("Current Score", f"{st.session_state.score}/{current_attempted}")
        else:
            st.metric("Final Score", f"{st.session_state.score}/{len(st.session_state.questions)}")
    with col4:
        if st.button("🔄 Reset Exam", help="Start over with current questions"):
            initialize_exam_state(st.session_state.questions)
            st.rerun()
    
    # Progress persistence info
    answered_count = sum(1 for ans in st.session_state.user_answers if ans is not None)
    st.write(f"**Progress:** {answered_count}/{len(st.session_state.questions)} questions answered • **Auto-saved**")
    
    # Source indicator
    if st.session_state.get('last_uploaded_file_name'):
        current_source = f"📁 {st.session_state.last_uploaded_file_name}"
    else:
        current_source = "📝 Built-in Questions"
    st.write(f"**Question source:** {current_source}")
    
    # Sidebar for exam progress and info
    with st.sidebar:
        st.header("📊 Exam Progress")
        
        current_score = st.session_state.score
        total_questions = len(st.session_state.questions)
        answered_count = sum(1 for ans in st.session_state.user_answers if ans is not None)
        
        if not st.session_state.exam_completed:
            progress = answered_count / total_questions
            score_percentage = (current_score / answered_count) * 100 if answered_count > 0 else 0
        else:
            progress = 1.0
            score_percentage = (current_score / total_questions) * 100
        
        st.write(f"**Score:** {current_score}/{answered_count}")
        st.write(f"**Accuracy:** {score_percentage:.1f}%")
        st.progress(progress)
        st.write(f"**Progress:** {answered_count}/{total_questions}")
        
        # Session management
        st.header("💾 Session")
        if st.button("💾 Save Progress Now", use_container_width=True):
            save_session_state()
            st.success("Progress saved!")
        
        if st.button("🗑️ Clear Saved Session", use_container_width=True):
            if os.path.exists(SESSION_FILE):
                os.remove(SESSION_FILE)
            st.success("Saved session cleared!")
            st.rerun()
        
        # Exam controls
        st.header("🎯 Exam Controls")
        if st.button("🔄 Restart Exam", use_container_width=True):
            initialize_exam_state(st.session_state.questions)
            st.rerun()
        
        if st.button("🔀 Shuffle Questions", use_container_width=True):
            random.shuffle(st.session_state.questions)
            st.session_state.current_question = 0
            st.session_state.answered = False
            save_session_state()
            st.success("Questions shuffled!")
            st.rerun()
        
        # Exam topics
        st.header("📚 Exam Topics")
        for topic, count in st.session_state.topics.items():
            st.write(f"• {topic}: {count} questions")
    
    # Main exam interface
    if not st.session_state.exam_completed:
        current_q = st.session_state.questions[st.session_state.current_question]
        
        # Question header with metadata
        st.subheader(f"📝 Question {st.session_state.current_question + 1}")
        st.markdown(f"**Topic:** {current_q.get('topic', 'General')}")
        if 'page' in current_q:
            st.markdown(f"**Reference:** Page {current_q['page']}")
        
        # Question text
        st.markdown(f"### {current_q['question']}")
        
        if not st.session_state.answered:
            # Display options for answering
            option_labels = list(current_q['options'].keys())
            
            # Pre-select if already answered
            previous_answer = st.session_state.user_answers[st.session_state.current_question]
            user_answer = st.radio(
                "Select your answer:",
                option_labels,
                index=option_labels.index(previous_answer) if previous_answer in option_labels else 0,
                format_func=lambda x: f"{x}. {current_q['options'][x]}",
                key=f"q{st.session_state.current_question}"
            )
            
            # Submit button
            col1, col2 = st.columns([1, 4])
            with col1:
                if st.button("🚀 Submit Answer", type="primary"):
                    st.session_state.answered = True
                    st.session_state.user_answers[st.session_state.current_question] = user_answer
                    
                    # Check if answer is correct
                    if user_answer == current_q['correct_answer']:
                        st.session_state.score += 1
                    
                    # Auto-save after answering
                    save_session_state()
                    st.rerun()
        
        else:
            # AFTER ANSWERING - SHOW RESULTS AND EXPLANATION
            st.write("---")
            
            # Show answer result
            user_answer = st.session_state.user_answers[st.session_state.current_question]
            if user_answer == current_q['correct_answer']:
                st.success("🎉 **Correct!** Well done!")
            else:
                st.error(f"😞 **Incorrect.** The correct answer is **{current_q['correct_answer']}**")
            
            # Show color-coded options review
            st.subheader("📋 Answer Review")
            option_labels = list(current_q['options'].keys())
            for option in option_labels:
                option_text = f"{option}. {current_q['options'][option]}"
                if option == current_q['correct_answer']:
                    st.success(f"✅ **{option_text}** - **Correct Answer**")
                elif option == user_answer:
                    st.error(f"❌ **{option_text}** - **Your Answer**")
                else:
                    st.write(f"📝 {option_text}")
            
            # SHOW EXPLANATION
            st.write("---")
            if 'explanation' in current_q and current_q['explanation']:
                st.subheader("💡 Explanation")
                st.info(current_q['explanation'])
            else:
                st.warning("No explanation available for this question.")
            
            # Navigation buttons
            st.write("---")
            col1, col2, col3 = st.columns([1, 1, 1])
            
            with col1:
                if st.session_state.current_question > 0:
                    if st.button("⏮️ Previous Question", use_container_width=True):
                        st.session_state.current_question -= 1
                        st.session_state.answered = False
                        save_session_state()
                        st.rerun()
            
            with col2:
                if st.session_state.current_question < len(st.session_state.questions) - 1:
                    if st.button("⏭️ Next Question", type="primary", use_container_width=True):
                        st.session_state.current_question += 1
                        st.session_state.answered = False
                        save_session_state()
                        st.rerun()
                else:
                    if st.button("🏁 Finish Exam", type="primary", use_container_width=True):
                        st.session_state.exam_completed = True
                        save_session_state()
                        st.rerun()
            
            with col3:
                if st.button("🔄 Try Again", use_container_width=True):
                    st.session_state.answered = False
                    save_session_state()
                    st.rerun()
    
    else:
        # Exam completed
        st.balloons()
        st.success("## 🎉 Exam Completed!")
        
        final_score = st.session_state.score
        total_questions = len(st.session_state.questions)
        score_percentage = (final_score / total_questions) * 100
        
        # Final results
        st.subheader("📈 Final Exam Results")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Total Questions", total_questions)
        with col2:
            st.metric("Correct Answers", final_score)
        with col3:
            st.metric("Final Score", f"{score_percentage:.1f}%")
        
        # Performance message
        st.write("---")
        if score_percentage >= 90:
            st.success("### 🏆 Outstanding! Exams Genius!")
        elif score_percentage >= 80:
            st.success("### 🌟 Excellent! Strong Understanding of Concepts!")
        elif score_percentage >= 70:
            st.info("### 👍 Very Good! Solid Knowledge Base!")
        elif score_percentage >= 60:
            st.warning("### 📚 Good! Review Challenging Topics!")
        else:
            st.error("### 💪 Keep Studying! Focus on Fundamental Concepts!")
        
        # Restart option
        st.write("---")
        if st.button("🔄 Take Exam Again", type="primary"):
            initialize_exam_state(st.session_state.questions)
            st.rerun()

if __name__ == "__main__":
    main()
