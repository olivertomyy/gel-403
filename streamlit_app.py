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
          "programming_languages_exam_questions": [
            {
              "id": 1,
              "topic": "Your Topic",
              "question": "Your question?",
              "options": {
                "A": "Option A",
                "B": "Option B",
                "C": "Option C",
                "D": "Option D"
              },
              "correct_answer": "A",
              "explanation": "Your explanation here"
            }
          ]
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
            st.success("### 🏆 Outstanding! Programming Languages Expert!")
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
