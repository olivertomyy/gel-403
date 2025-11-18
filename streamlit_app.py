import streamlit as st
import random
import json
import os
import tempfile

def load_questions_from_json():
    """Load questions from JSON file with the programming_languages_exam_questions structure"""
    try:
        # Try to load from local file first
        if os.path.exists("programming_questions.json"):
            with open("programming_questions.json", 'r', encoding='utf-8') as f:
                data = json.load(f)
                questions = data.get("programming_languages_exam_questions", [])
                if questions:
                    st.success(f"✅ Loaded {len(questions)} exam questions from local file")
                    return questions
        
        # If local file doesn't exist, use fallback questions
        st.info("📝 Using built-in exam questions")
        return get_fallback_exam_questions()
        
    except Exception as e:
        st.error(f"❌ Error loading questions: {e}")
        return get_fallback_exam_questions()

def get_fallback_exam_questions():
    """Provide comprehensive fallback exam questions"""
    return [
        
    {
      "id": 1,
      "topic": "Definition of Marriage",
      "question": "According to the general definition provided, which of the following is NOT a characteristic of marriage?",
      "options": {
        "A": "It is a socially recognized relationship.",
        "B": "It involves a commitment or devotion.",
        "C": "It must involve more than one person.",
        "D": "It is primarily a financial partnership."
      },
      "correct_answer": "D",
      "page": 1,
      "explanation": "The general definition lists marriage as a 'socially recognized relationship,' involving 'more than one,' and being a 'commitment / devotion.' It does not mention a financial partnership as a defining characteristic."
    },
    {
      "id": 2,
      "topic": "Systems of Marriage",
      "question": "How is 'Christian Marriage' distinguished from other marriage systems in the document?",
      "options": {
        "A": "It is the oldest form of marriage.",
        "B": "It is the most legally recognized form globally.",
        "C": "It is marriage as God intended and divinely approved.",
        "D": "It is the simplest form of marriage to enter into."
      },
      "correct_answer": "C",
      "page": 1,
      "explanation": "The text explicitly states: 'Apart from the Christian Marriage, which is marriage as God intended and divinely approved, we also have other manifestations...'"
    },
    {
      "id": 3,
      "topic": "Systems of Marriage",
      "question": "Which of the following is listed as an example of a 'Traditional' marriage system?",
      "options": {
        "A": "Islamic Marriages",
        "B": "The Gay / Lesbian Marriages",
        "C": "Polygyny / polyandry",
        "D": "The Levirate / Sororate Marriages"
      },
      "correct_answer": "C",
      "page": 1,
      "explanation": "Under the 'Traditional' category, the document lists 'Polygyny \\ polyandry'."
    },
    {
      "id": 4,
      "topic": "Definition of Christian Marriage",
      "question": "What three forms of recognition does a Christian Marriage possess according to the specific definition provided?",
      "options": {
        "A": "Social, Legal, and Spiritual",
        "B": "Political, Economic, and Religious",
        "C": "Familial, Cultural, and Traditional",
        "D": "Emotional, Physical, and Intellectual"
      },
      "correct_answer": "A",
      "page": 1,
      "explanation": "The definition states: 'Marriage is a socially recognized, legally approved and spiritually ratified... relationship.'"
    },
    {
      "id": 5,
      "topic": "Definition of Christian Marriage",
      "question": "The definition of Christian Marriage states it is an 'exclusive, lifelong covenant relationship.' What does 'exclusive' imply in this context?",
      "options": {
        "A": "Exclusive to a particular social class.",
        "B": "Exclusive in terms of sexual and romantic fidelity between one man and one woman.",
        "C": "Exclusive to couples who are financially independent.",
        "D": "Exclusive to those who have a university education."
      },
      "correct_answer": "B",
      "page": 1,
      "explanation": "In the context of a lifelong covenant between one man and one woman, 'exclusive' primarily refers to sexual and romantic fidelity, ruling out other partners."
    },
    {
      "id": 6,
      "topic": "Definition of Christian Marriage",
      "question": "What is the stated purpose of a Christian marriage?",
      "options": {
        "A": "To achieve personal happiness and self-fulfillment above all else.",
        "B": "For living a God-exalting life and the procreation and nurturing of godly children.",
        "C": "To consolidate wealth and secure social status.",
        "D": "To fulfill a legal requirement for adulthood."
      },
      "correct_answer": "B",
      "page": 1,
      "explanation": "The document clearly states the purpose is 'for the purpose of living a God exalting life and the procreation and nurturing of godly children.'"
    },
    {
      "id": 7,
      "topic": "Definition of Christian Marriage",
      "question": "The document describes Christian marriage as involving the sharing of the whole of a person's life and a mutual self-surrender that results in 'oneness.' What important qualifier is given about this oneness?",
      "options": {
        "A": "It requires the complete loss of personal individuality.",
        "B": "It happens without losing their individuality.",
        "C": "It only occurs in the spiritual realm, not the physical.",
        "D": "It is a feeling that comes and goes."
      },
      "correct_answer": "B",
      "page": 1,
      "explanation": "The text specifies that the two people become 'one,' not only in body, but in soul,' but crucially adds 'without losing their individuality.'"
    },
    {
      "id": 8,
      "topic": "Origin of Marriage",
      "question": "According to the document, what was God's stated reason for instituting marriage?",
      "options": {
        "A": "It is not good that man should be alone.",
        "B": "The earth needed to be filled with people.",
        "C": "Man needed a servant to help him.",
        "D": "Woman needed a protector from the animals."
      },
      "correct_answer": "A",
      "page": 1,
      "explanation": "The origin is traced to Genesis 2:18: 'It is not good that man should be alone; I will make him a helper comparable to him.'"
    },
    {
      "id": 9,
      "topic": "Origin of Marriage",
      "question": "What does Adam's exclamation in Genesis 2:23, as cited in the document, signify?",
      "options": {
        "A": "His disappointment with God's creation.",
        "B": "His recognition and joyful acceptance of the woman as part of himself.",
        "C": "His confusion about what the woman was.",
        "D": "His intention to dominate the woman."
      },
      "correct_answer": "B",
      "page": 1,
      "explanation": "Adam's words, 'This is now bone of my bones and flesh of my flesh,' express a profound recognition of their shared nature and unity."
    },
    {
      "id": 10,
      "topic": "Origin of Marriage",
      "question": "What 'ideal' does Genesis 2:24 point to, according to the document?",
      "options": {
        "A": "That a man should have multiple wives.",
        "B": "That marriage is a temporary arrangement.",
        "C": "That a man should be the husband of one wife and for the marriage to be permanent.",
        "D": "That children are the most important part of marriage."
      },
      "correct_answer": "C",
      "page": 1,
      "explanation": "The text states that the passage 'point(s) to the fact that God’s ideal is for a man to be the husband of one wife and for the marriage to be permanent.'"
    },
    {
      "id": 11,
      "topic": "Assignment - Characteristics",
      "question": "The assignment on page 2 asks to reflect on a Christian marriage being a union of 'two believers in Christ.' This aligns with the biblical principle of:",
      "options": {
        "A": "Being unequally yoked.",
        "B": "Not being unequally yoked.",
        "C": "Marrying within one's tribe.",
        "D": "Priestly marriage restrictions."
      },
      "correct_answer": "B",
      "page": 2,
      "explanation": "The principle of 'not being unequally yoked' from 2 Corinthians 6:14 directly supports the idea that both partners in a Christian marriage should be believers."
    },
    {
      "id": 12,
      "topic": "Assignment - Characteristics",
      "question": "One point of reflection is that a Christian marriage is 'built on moral, physical and spiritual purity.' What is the specific term used for this in the assignment?",
      "options": {
        "A": "Unity",
        "B": "Godliness",
        "C": "Fidelity",
        "D": "Indissoluble"
      },
      "correct_answer": "C",
      "page": 2,
      "explanation": "The assignment parenthetically links 'moral, physical and spiritual purity' with the term '(Fidelity)'."
    },
    {
      "id": 13,
      "topic": "Purpose of Marriage",
      "question": "Which of the following is listed as a purpose of marriage?",
      "options": {
        "A": "Financial Security",
        "B": "Service",
        "C": "Political Alliance",
        "D": "Academic Achievement"
      },
      "correct_answer": "B",
      "page": 2,
      "explanation": "The four purposes listed are: Companionship, Sexual fulfilment, Child-rearing, and Service."
    },
    {
      "id": 14,
      "topic": "Purpose of Marriage",
      "question": "The purpose of 'companionship' most directly fulfills the need identified at the origin of marriage in:",
      "options": {
        "A": "Genesis 1:28",
        "B": "Genesis 2:18",
        "C": "Genesis 3:16",
        "D": "Exodus 20:14"
      },
      "correct_answer": "B",
      "page": 2,
      "explanation": "The purpose of companionship directly addresses God's declaration in Genesis 2:18 that 'It is not good that man should be alone.'"
    },
    {
      "id": 15,
      "topic": "Those Unfit for Marriage",
      "question": "According to the document, which of the following would be considered unfit for a Christian marriage?",
      "options": {
        "A": "A mature, single believer.",
        "B": "A person with the bond of a prior marriage.",
        "C": "A person from a different cultural background.",
        "D": "A person with a low-income job."
      },
      "correct_answer": "B",
      "page": 2,
      "explanation": "The list of those unfit includes 'Persons with bond of a prior marriage,' implying that a prior, binding marriage covenant (that has not been biblically dissolved) would prevent a new one."
    },
    {
      "id": 16,
      "topic": "Choosing a Mate",
      "question": "What is the primary biblical principle given for choosing a mate?",
      "options": {
        "A": "Marry within the body of believers.",
        "B": "Marry someone from a wealthy family.",
        "C": "Marry someone of the same nationality.",
        "D": "Marry someone who is highly educated."
      },
      "correct_answer": "A",
      "page": 2,
      "explanation": "The section begins: 'God’s desire for His people was that they marry within the body of believers.'"
    },
    {
      "id": 17,
      "topic": "Choosing a Mate",
      "question": "What was the specific danger cited for an Israelite marrying a foreigner under the Mosaic Law?",
      "options": {
        "A": "Financial ruin.",
        "B": "Being tempted to embrace the spouse's god.",
        "C": "Losing their inheritance immediately.",
        "D": "Being ostracized by their family only."
      },
      "correct_answer": "B",
      "page": 2,
      "explanation": "The text states: 'The Israelite would be constantly tempted to embrace the spouse’s god as well.'"
    },
    {
      "id": 18,
      "topic": "Choosing a Mate - Questions",
      "question": "Which of the following is NOT one of the suggested questions to resolve before marriage?",
      "options": {
        "A": "Is this person matured physically, mentally, spiritually, financially and emotionally?",
        "B": "Is this person a Christian?",
        "C": "Does this person come from a politically influential family?",
        "D": "Does this person demonstrate good character?"
      },
      "correct_answer": "C",
      "page": 3,
      "explanation": "The questions cover maturity, faith, love, character, and potential. Political influence is not mentioned."
    },
    {
      "id": 19,
      "topic": "Covenant vs. Contract",
      "question": "What is the fundamental difference between a 'covenant' perspective and a 'contract' perspective of marriage, as described in the document?",
      "options": {
        "A": "A covenant is a legal document, while a contract is a religious vow.",
        "B": "A contract is based on giving, while a covenant is based on getting.",
        "C": "A covenant is based on a desire to give for the other's benefit, while a contract focuses on anticipated personal benefits.",
        "D": "There is no significant difference; the terms are interchangeable."
      },
      "correct_answer": "C",
      "page": 3,
      "explanation": "The text clearly contrasts the two: 'A covenant marriage is based on “an overwhelming desire to give... for their benefit...” While a contract relationship focuses on anticipated personal benefits...'"
    },
    {
      "id": 20,
      "topic": "Covenant vs. Contract",
      "question": "According to the document, what is the underlying motivation of people who view marriage as a contract?",
      "options": {
        "A": "They marry because of what they expect to get out of it.",
        "B": "They marry with a desire for mutual self-surrender.",
        "C": "They marry primarily to serve God together.",
        "D": "They marry with no expectations at all."
      },
      "correct_answer": "A",
      "page": 3,
      "explanation": "The document states: 'Most people I have interacted with said they married because of what they expect to get out of it.' This is identified as the 'contract' perspective."
    },
    {
      "id": 21,
      "topic": "Principle of Connection",
      "question": "What biblical scene is used to illustrate the 'Principle of Connection' or 'Covenant Intimacy'?",
      "options": {
        "A": "The wedding at Cana.",
        "B": "Adam and Eve being naked and not ashamed.",
        "C": "The Song of Solomon.",
        "D": "Christ presenting the church to himself."
      },
      "correct_answer": "B",
      "page": 3,
      "explanation": "The Principle of Connection is illustrated with Genesis 2:25: 'the man and his wife were both naked and were not ashamed,' symbolizing complete trust and vulnerability."
    },
    {
      "id": 22,
      "topic": "Principle of Permanence",
      "question": "What is the 'Principle of Permanence' in marriage based on?",
      "options": {
        "A": "The practical difficulty of getting a divorce.",
        "B": "The words of Christ in Matthew 19:6 that what God has joined, no one should split apart.",
        "C": "Social pressures to stay married.",
        "D": "The financial cost of divorce."
      },
      "correct_answer": "B",
      "page": 4,
      "explanation": "The document cites Matthew 19:6, where Jesus says, 'let no one split apart what God has joined,' as the foundation for the Principle of Permanence."
    },
    {
      "id": 23,
      "topic": "Principle of Permanence",
      "question": "What practical advice is given regarding the mindset towards marriage's permanence?",
      "options": {
        "A": "Plan for lifelong success and avoid considering divorce as an option.",
        "B": "Keep divorce as a backup plan in case things get difficult.",
        "C": "Test the marriage for a few years before fully committing.",
        "D": "Focus on your own happiness, and leave if it's not working."
      },
      "correct_answer": "A",
      "page": 4,
      "explanation": "The text advises: 'If you plan for lifelong success you’ll get it. But if you keep the idea of divorce as an option, that may undermine your efforts to succeed.'"
    },
    {
      "id": 24,
      "topic": "Synthesis - Core Concept",
      "question": "The document repeatedly emphasizes that Christian marriage is a 'covenant.' Which of the following best captures the essence of this covenant as described?",
      "options": {
        "A": "A conditional agreement that can be voided if terms are broken.",
        "B": "A lifelong, binding promise of mutual self-giving, rooted in God's design and witnessed by Him.",
        "C": "A private understanding between two people that requires no external recognition.",
        "D": "A legal contract focused on defining rights and responsibilities."
      },
      "correct_answer": "B",
      "page": 3,
      "explanation": "Throughout the document, the covenant is described as lifelong, involving mutual self-surrender, made before God, and distinct from a self-focused contract. This makes option B the most comprehensive and accurate."
    },
    {
      "id": 25,
      "topic": "Application - Mate Selection",
      "question": "Based on the criteria for choosing a mate, a prospective partner who is a believer but is dishonest, lazy, and shows no vision for the future would:",
      "options": {
        "A": "Be an excellent choice because they are a believer.",
        "B": "Be a questionable choice because they fail the tests of character and potential.",
        "C": "Be automatically disqualified because they are not from the same tribe.",
        "D": "Be a good candidate because love can overcome these issues."
      },
      "correct_answer": "B",
      "page": 3,
      "explanation": "The document lists questions about character ('Is he or she humble, honest and diligent?') and potential ('Is he or she visionary?'). A person lacking these attributes, even if a believer, would not meet the suggested biblical criteria for a mate."
    },
    {
      "id": 1,
      "topic": "Module Focus",
      "question": "What is the specific focus of this module, as indicated by its title?",
      "options": {
        "A": "Pitfalls and Dangers",
        "B": "Process & Essence",
        "C": "Types and Definitions",
        "D": "Marriage and Family"
      },
      "correct_answer": "B",
      "page": 1,
      "explanation": "The title of the document is 'Relationships PROCESS & ESSENCE', clearly defining the two central themes for this module."
    },
    {
      "id": 2,
      "topic": "Key Objective",
      "question": "The key objective for this module is identical to previous ones. What is the ultimate goal of demonstrating basic relational skills?",
      "options": {
        "A": "To control and manipulate others.",
        "B": "To win every argument.",
        "C": "To appreciate and value human connections.",
        "D": "To achieve financial success through networking."
      },
      "correct_answer": "C",
      "page": 2,
      "explanation": "The objective consistently states that skills should 'help them appreciate and value the human connections formed in their lives.'"
    },
    {
      "id": 3,
      "topic": "Course Structure",
      "question": "In the course outline on page 3, which two topics are the specific focus of this particular module?",
      "options": {
        "A": "Definitions and Types",
        "B": "Process and Essence/Importance",
        "C": "Pitfalls and Definitions",
        "D": "Types and Pitfalls"
      },
      "correct_answer": "B",
      "page": 3,
      "explanation": "While the full course outline is shown, the title of this document specifies it covers 'Process & Essence', which are the third and fourth items on the outline list."
    },
    {
      "id": 4,
      "topic": "Recap - Theological Foundation",
      "question": "According to the recap on page 5, what is the divine origin of our relational ability?",
      "options": {
        "A": "It is a learned behavior from society.",
        "B": "It reflects our divine component of relational ability.",
        "C": "It is a result of evolutionary psychology.",
        "D": "It is a human invention for survival."
      },
      "correct_answer": "B",
      "page": 5,
      "explanation": "The first recap point states: 'Relationships reflect our divine component of relational ability (Gen. 1: 26-28)'."
    },
    {
      "id": 5,
      "topic": "Recap - Human Nature",
      "question": "The recap states that relationships affect every part of our being. Which model of human nature does this statement align with?",
      "options": {
        "A": "The Bipartite (Body and Mind) model.",
        "B": "The Tripartite (Body, Soul, and Spirit) model.",
        "C": "The Monistic (Purely Physical) model.",
        "D": "The Quadripartite (Mental, Physical, Emotional, Social) model."
      },
      "correct_answer": "B",
      "page": 5,
      "explanation": "The point 'Relationships affect every part of our being – body, soul and spirit' directly references the Tripartite nature of man discussed in previous modules."
    },
    {
      "id": 6,
      "topic": "Recap - Nature of Relationships",
      "question": "How does the recap describe the original design and intended effect of relationships?",
      "options": {
        "A": "As a necessary trial to build character.",
        "B": "As wonderfully complex, beautiful, and contributing to our overall well-being.",
        "C": "As simple, straightforward transactions.",
        "D": "As primarily for economic and social advancement."
      },
      "correct_answer": "B",
      "page": 5,
      "explanation": "The recap includes the points: 'Relationships can be wonderfully complex' and 'Relationships are originally designed by God to be beautiful and contribute our overall well-being.'"
    },
    {
      "id": 7,
      "topic": "Process - Foundation",
      "question": "According to page 7, where does the process of developing a proper understanding of relationships begin?",
      "options": {
        "A": "By finding the perfect partner.",
        "B": "By discovering YOURSELF.",
        "C": "By studying psychology textbooks.",
        "D": "By attending social events."
      },
      "correct_answer": "B",
      "page": 7,
      "explanation": "The document states unequivocally: 'The process... starts by discovering YOURSELF (Romans 12:3; 1 Cor. 4:3-4)'."
    },
    {
      "id": 8,
      "topic": "Process - Foundation",
      "question": "The biblical references (Romans 12:3; 1 Cor. 4:3-4) alongside 'discovering YOURSELF' suggest this self-discovery is about:",
      "options": {
        "A": "Developing arrogant self-confidence.",
        "B": "Gaining a sober, biblical judgment of oneself, free from both inferiority and pride.",
        "C": "Focusing exclusively on one's own needs and desires.",
        "D": "Judging the shortcomings of others."
      },
      "correct_answer": "B",
      "page": 7,
      "explanation": "Romans 12:3 warns against thinking too highly of oneself, and 1 Corinthians 4:3-4 discusses being judged by the Lord, not by one's own judgment. This points to a humble, God-centered self-assessment."
    },
    {
      "id": 9,
      "topic": "The Johari Window",
      "question": "What is the name of the model introduced on page 8 to illustrate self-awareness in relationships?",
      "options": {
        "A": "The Maslow Hierarchy of Needs",
        "B": "The SWOT Analysis",
        "C": "The JOHARI Window Model",
        "D": "The Myers-Briggs Type Indicator"
      },
      "correct_answer": "C",
      "page": 8,
      "explanation": "The diagram is clearly labeled 'The JOHARI Window Model'."
    },
    {
      "id": 10,
      "topic": "The Johari Window",
      "question": "In the Johari Window, the 'Blind Spot' quadrant represents what?",
      "options": {
        "A": "What is known by self and known by others.",
        "B": "What is not known by self but is known by others.",
        "C": "What is known by self but not known by others.",
        "D": "What is not known by self and not known by others."
      },
      "correct_answer": "B",
      "page": 8,
      "explanation": "According to the diagram, the 'Blind Spot' is defined as 'Not known by self' but 'Known by others'."
    },
    {
      "id": 11,
      "topic": "The Johari Window",
      "question": "The 'Façade' quadrant in the Johari Window represents aspects of ourselves that we:",
      "options": {
        "A": "Hide from others but are aware of ourselves.",
        "B": "Are unaware of, but others can see.",
        "C": "Share openly with everyone.",
        "D": "Are completely unaware of, along with everyone else."
      },
      "correct_answer": "A",
      "page": 8,
      "explanation": "The 'Façade' quadrant is defined as 'Known by self' but 'Not known by others', representing information we consciously choose to hide."
    },
    {
      "id": 12,
      "topic": "Self-Disclosure",
      "question": "According to page 9, what is a primary benefit of self-disclosure?",
      "options": {
        "A": "It allows us to manipulate how others perceive us.",
        "B": "It is one sure way to help our relationships grow in depth and meaning.",
        "C": "It guarantees that others will agree with us.",
        "D": "It helps us avoid all future conflict."
      },
      "correct_answer": "B",
      "page": 9,
      "explanation": "The text lists several benefits, concluding with: 'It is one sure way to help our relationships grow in depth and meaning.'"
    },
    {
      "id": 13,
      "topic": "Self-Disclosure",
      "question": "How does self-disclosure relate to the Johari Window model?",
      "options": {
        "A": "It shrinks the 'Open Arena' quadrant by hiding more information.",
        "B": "It expands the 'Open Arena' quadrant by sharing information from the 'Façade'.",
        "C": "It primarily enlarges the 'Unknown' quadrant.",
        "D": "It has no direct correlation to the model."
      },
      "correct_answer": "B",
      "page": 9,
      "explanation": "The purpose of self-disclosure is to share information that is known to you but not to others (your Façade), thereby increasing the shared 'Open Arena' and building intimacy and trust."
    },
    {
      "id": 14,
      "topic": "Stages - Acquaintance",
      "question": "How is communication described in the 'Acquaintance' stage?",
      "options": {
        "A": "Deep and vulnerable sharing of secrets.",
        "B": "Polite and careful disclosure of common/shared interests.",
        "C": "Aggressive and confrontational to test boundaries.",
        "D": "Non-verbal and indirect."
      },
      "correct_answer": "B",
      "page": 11,
      "explanation": "The document states that the Acquaintance stage involves 'communicating common/shared interests – often in polite and careful disclosure'."
    },
    {
      "id": 15,
      "topic": "Stages - Acquaintance",
      "question": "What is the level of commitment typically like in the Acquaintance stage?",
      "options": {
        "A": "A deep, lifelong commitment is made.",
        "B": "It is a non-committal stage where the relationship may thrive or break off.",
        "C": "Legal contracts are often signed.",
        "D": "Commitment is expected to be absolute and unwavering."
      },
      "correct_answer": "B",
      "page": 11,
      "explanation": "The text explicitly describes it as an 'often a non-committal stage where the relationship may either thrive or break off'."
    },
    {
      "id": 16,
      "topic": "Stages - Development",
      "question": "What becomes a key 'currency' in the relationship during the Development stage?",
      "options": {
        "A": "Money and gifts.",
        "B": "Trust.",
        "C": "Social status.",
        "D": "Power and influence."
      },
      "correct_answer": "B",
      "page": 12,
      "explanation": "The document states: 'Stage where friendship builds up. Trust becomes a currency in the relationship'."
    },
    {
      "id": 17,
      "topic": "Stages - Development",
      "question": "What emotional and behavioral changes are noted in the Development stage?",
      "options": {
        "A": "People draw nearer and the tendency to concentrate on the relationship increases.",
        "B": "People become more distant and independent.",
        "C": "Communication becomes more formal and infrequent.",
        "D": "The relationship becomes entirely goal-oriented, losing personal sentiment."
      },
      "correct_answer": "A",
      "page": 12,
      "explanation": "The text describes that 'People draw nearer in energetic fashion and feeling of sentiment develops' and the 'Tendency to concentrate more on the relationship increases'."
    },
    {
      "id": 18,
      "topic": "Stages - Continuation",
      "question": "How is the 'Continuation' stage characterized?",
      "options": {
        "A": "As a period of stagnation and boredom.",
        "B": "As a time when the connection flourishes into long-term commitments and becomes stabilized.",
        "C": "As the point where the relationship is most fragile and likely to end.",
        "D": "As a stage of constant conflict and negotiation."
      },
      "correct_answer": "B",
      "page": 13,
      "explanation": "The Continuation stage is defined by 'long-term commitments', 'greater comprehension', 'expressions of intimacy', and is termed a 'stabilized relationship'."
    },
    {
      "id": 19,
      "topic": "Stages - Waning/Deterioration",
      "question": "What is the primary cause of the 'Waning/Deterioration' stage?",
      "options": {
        "A": "External pressures from society.",
        "B": "Shortfalls in trust, uniformity, care, and affections.",
        "C": "A natural and inevitable conclusion to all relationships.",
        "D": "The achievement of all relationship goals."
      },
      "correct_answer": "B",
      "page": 14,
      "explanation": "The text states: 'This is mostly caused by shortfalls in issues of trust, uniformity, care and affections...'"
    },
    {
      "id": 20,
      "topic": "Stages - Waning/Deterioration",
      "question": "What important qualifier is given about this stage?",
      "options": {
        "A": "All relationships must go through it.",
        "B": "It is always reversible with enough effort.",
        "C": "Not all relationships go through this stage.",
        "D": "It is the most important stage for personal growth."
      },
      "correct_answer": "C",
      "page": 14,
      "explanation": "The document clearly notes: 'Not all relationships go through this stage', indicating that decline is not inevitable for every relationship."
    },
    {
      "id": 21,
      "topic": "Essence of Relationships",
      "question": "How is the 'essence' of relationships defined on page 15?",
      "options": {
        "A": "As a modern social experiment.",
        "B": "As a personal choice for happiness.",
        "C": "As ordained by God as the standard, consistent pattern for building all human society.",
        "D": "As a biological imperative for reproduction only."
      },
      "correct_answer": "C",
      "page": 15,
      "explanation": "The statement on the essence of relationships is: 'Ordained by God as the standard, consistent pattern for building all human society (Malachi 2:15 - 16; Matthew 19:4 - 8)'."
    },
    {
      "id": 22,
      "topic": "Tools for Building",
      "question": "Which of the following is listed as a 'Tool of Relationship Building'?",
      "options": {
        "A": "Ignoring problems.",
        "B": "Face-to-face communication.",
        "C": "Financial manipulation.",
        "D": "Social isolation."
      },
      "correct_answer": "B",
      "page": 16,
      "explanation": "'Face-to-face communication' is the first item listed in the tools for relationship building."
    },
    {
      "id": 23,
      "topic": "Tools for Building",
      "question": "The list of tools includes both traditional methods like 'Correspondence (Letter-writing)' and modern methods like 'Social media platforms.' What does this suggest?",
      "options": {
        "A": "That only traditional methods are valid.",
        "B": "That the principles of connection can be applied through various mediums, both old and new.",
        "C": "That social media is the most important tool.",
        "D": "That letter-writing is obsolete."
      },
      "correct_answer": "B",
      "page": 16,
      "explanation": "The inclusive list implies that the core activity of building connections is what matters, and it can be facilitated by a range of tools across different eras and technologies."
    },
    {
      "id": 24,
      "topic": "Social Media Role",
      "question": "Page 17 poses a question about the role of social media. Based on the context of the entire module, what is the MOST LIKELY intended critique or consideration?",
      "options": {
        "A": "Social media has no role and should be avoided entirely.",
        "B": "While it can be a tool for connection, it may struggle to facilitate the deep, gradual, self-disclosing process required for 'lasting relationships'.",
        "C": "Social media is the only tool needed for modern relationship building.",
        "D": "Its role is identical to face-to-face communication in every way."
      },
      "correct_answer": "B",
      "page": 17,
      "explanation": "Given the module's emphasis on a slow process involving self-discovery, careful disclosure, and building trust over time, the question likely prompts students to critically evaluate if social media's often quick and superficial interactions can truly fulfill this deep process."
    },
    {
      "id": 25,
      "topic": "Conclusion",
      "question": "What is the culminating point of 'well managed relationships' according to the conclusion on page 18?",
      "options": {
        "A": "They lead to successful business partnerships.",
        "B": "They grow in a steady manner until the institution of marriage.",
        "C": "They always remain in the 'Continuation' stage indefinitely.",
        "D": "They eventually dissolve to make room for new ones."
      },
      "correct_answer": "B",
      "page": 18,
      "explanation": "The conclusion states that well-managed relationships 'grows in a steady, culminating manner until the holy and sweet institution of marriage', presenting marriage as a God-ordained culmination for a romantic relationship."
    },
    {
      "id": 26,
      "topic": "Synthesis - Process & Essence",
      "question": "How does the 'Process' of relationships (stages, self-discovery) connect to the 'Essence' of relationships (God's design for society)?",
      "options": {
        "A": "There is no connection; they are separate topics.",
        "B": "The process is how individuals personally experience and build what God has ordained as the essential fabric of human society.",
        "C": "The essence is about avoiding relationships, while the process is about starting them.",
        "D": "The process is purely psychological, while the essence is purely theological."
      },
      "correct_answer": "B",
      "page": 15,
      "explanation": "The 'Essence' provides the 'why'—relationships are God's foundational pattern for society. The 'Process' provides the 'how'—the practical steps and stages through which individuals build these God-ordained connections. They are intrinsically linked."
    },
    {
      "id": 27,
      "topic": "Application - Johari Window",
      "question": "If a person receives feedback from friends that they are a good listener, something they had never consciously considered, this information would move from which quadrant to which quadrant in their Johari Window?",
      "options": {
        "A": "From Façade to Open Arena",
        "B": "From Blind Spot to Open Arena",
        "C": "From Unknown to Blind Spot",
        "D": "From Open Arena to Blind Spot"
      },
      "correct_answer": "B",
      "page": 8,
      "explanation": "This was something 'Not known by self' (Blind Spot) but 'Known by others'. Upon receiving and accepting the feedback, it becomes known to both self and others, thus moving into the 'Open Arena'."
    },
    {
      "id": 28,
      "topic": "Analysis - Theological Integration",
      "question": "This module integrates psychology (Johari Window, relationship stages) with theology. What is the overall effect of this integration?",
      "options": {
        "A": "It creates confusion between secular and sacred knowledge.",
        "B": "It demonstrates that biblical principles are often aligned with observable human relational dynamics, providing a holistic view.",
        "C": "It suggests that psychological models are superior to biblical ones.",
        "D": "It argues that all psychology is incompatible with faith."
      },
      "correct_answer": "B",
      "page": 8,
      "explanation": "The module seamlessly uses a psychological tool (Johari Window) and stage theory alongside biblical references on self-assessment and God's design. This presents a worldview where God's truth is seen in both general revelation (observable human nature) and special revelation (the Bible)."
    },


     {
      "id": 1,
      "topic": "Biblical Foundation",
      "question": "Which two books of the Bible are referenced on the title page to establish a scriptural basis for the study of relationships?",
      "options": {
        "A": "Matthew and John",
        "B": "Genesis and Proverbs",
        "C": "Psalms and Ephesians",
        "D": "Romans and Corinthians"
      },
      "correct_answer": "B",
      "page": 1,
      "explanation": "The title page explicitly cites 'Genesis 1:24-30; Proverbs 30:19' as the foundational biblical texts for this module."
    },
    {
      "id": 2,
      "topic": "Course Identity",
      "question": "What is the full course code and title as presented on the cover page?",
      "options": {
        "A": "GEL 403: Pitfalls in Relationships",
        "B": "GEL 403: Relationships and Family",
        "C": "GEL 403: Introduction to Marriage",
        "D": "GEL 403: The Equipping Christian Ministry"
      },
      "correct_answer": "B",
      "page": 1,
      "explanation": "The cover page clearly states 'GEL403:RELATIONSHIPSANDFAMILY', establishing the broader course context for this introductory module."
    },
    {
      "id": 3,
      "topic": "Key Objectives",
      "question": "According to the key objective on page 2, what is the ultimate purpose of demonstrating basic relational skills?",
      "options": {
        "A": "To win arguments and influence people.",
        "B": "To appreciate and value the human connections formed in their lives.",
        "C": "To become a professional counselor.",
        "D": "To isolate oneself from negative influences."
      },
      "correct_answer": "B",
      "page": 2,
      "explanation": "The learning outcome states the skills are a means to the end goal: to 'help them appreciate and value the human connections formed in their lives.'"
    },
    {
      "id": 4,
      "topic": "Course Structure",
      "question": "Which of the following is the correct order of topics as listed in the course outline on page 3?",
      "options": {
        "A": "Types, Definitions, Pitfalls, Process, Essence",
        "B": "Definitions, Types, Essence/Importance, Process, Pitfalls",
        "C": "Pitfalls, Process, Types, Definitions, Essence",
        "D": "Definitions, Pitfalls, Types, Process, Essence"
      },
      "correct_answer": "B",
      "page": 3,
      "explanation": "The outline on page 3 lists the topics in this exact order: Definitions, Types, Essence/Importance, Process, Pitfalls."
    },
    {
      "id": 5,
      "topic": "Philosophical Foundation",
      "question": "According to the 'Opening thoughts' on page 5, what is the described origin of the human desire to relate?",
      "options": {
        "A": "It is a learned behavior from our parents.",
        "B": "It is a social construct developed over centuries.",
        "C": "It is an in-built (default) constitution designed by God.",
        "D": "It is a psychological response to trauma."
      },
      "correct_answer": "C",
      "page": 5,
      "explanation": "The text states: 'Everyone is born with a desire to relate to something. This is an in-built (default) constitution designed by God in the basic human setup (Gen. 1: 26-28).'"
    },
    {
      "id": 6,
      "topic": "Philosophical Foundation",
      "question": "The reference to Genesis 1:26-28 in the opening thoughts likely connects the desire to relate to:",
      "options": {
        "A": "The Fall of Man and the introduction of sin.",
        "B": "Humanity's creation in the image of a relational God.",
        "C": "The specific command to build the ark.",
        "D": "The story of Joseph and his brothers."
      },
      "correct_answer": "B",
      "page": 5,
      "explanation": "Genesis 1:26-28 deals with the creation of humanity in God's image. A key aspect of the Christian God is relationality (as a Trinity), and this passage includes the command to be fruitful and fill the earth, implying relationship. This grounds the human desire for connection in the Imago Dei."
    },
    {
      "id": 7,
      "topic": "Human Nature",
      "question": "What model of human nature is presented on page 6?",
      "options": {
        "A": "The Bipartite (Body and Soul) nature.",
        "B": "The Monistic (Purely Physical) nature.",
        "C": "The Tripartite (Spirit, Soul, Body) nature.",
        "D": "The Quadripartite (Mental, Physical, Emotional, Social) nature."
      },
      "correct_answer": "C",
      "page": 6,
      "explanation": "The diagram and heading on page 6 clearly present the 'The Tripartite Nature of Man,' consisting of SPIRIT, SOUL, and BODY."
    },
    {
      "id": 8,
      "topic": "Human Nature",
      "question": "The presentation of the Tripartite Nature of Man implies that relationships:",
      "options": {
        "A": "Are solely a physical and biological process.",
        "B": "Can engage humans on multiple levels: spiritual, soulish (mind, will, emotions), and physical.",
        "C": "Are only important for the soul, not the spirit or body.",
        "D": "Are a function of the body alone, designed for procreation."
      },
      "correct_answer": "B",
      "page": 6,
      "explanation": "By defining humans as three-part beings, the module suggests that relationships are complex and can involve spiritual connection, emotional and intellectual bonding (soul), and physical interaction (body)."
    },
    {
      "id": 9,
      "topic": "Core Definition",
      "question": "What is the simplest, most basic definition of a relationship provided on page 8?",
      "options": {
        "A": "A legally binding contract between two parties.",
        "B": "A deep emotional and spiritual union.",
        "C": "Associations or connections.",
        "D": "A long-term commitment between family members."
      },
      "correct_answer": "C",
      "page": 8,
      "explanation": "Page 8 provides the foundational definition: 'On the simplest level, relationships are associations or connections.'"
    },
    {
      "id": 10,
      "topic": "Interpersonal Relationships Definition",
      "question": "According to page 9, what are the three required criteria for an association to be considered an 'Interpersonal Relationship'?",
      "options": {
        "A": "Shared bloodline, shared property, shared goals.",
        "B": "Legal documentation, public ceremony, financial merger.",
        "C": "Interdependence, consistent patterns of interaction, interaction over an extended period.",
        "D": "Physical attraction, intellectual compatibility, spiritual alignment."
      },
      "correct_answer": "C",
      "page": 9,
      "explanation": "The definition on page 9 specifies that interpersonal relationships are between people who are 'interdependent,' who use some 'consistent patterns of interaction,' and who have interacted for an 'extended period of time.'"
    },
    {
      "id": 11,
      "topic": "Scope of Relationships",
      "question": "The examples on page 10 ('A dating couple,' 'A single parent and child,' etc.) demonstrate that interpersonal relationships:",
      "options": {
        "A": "Are limited to romantic partnerships.",
        "B": "Can vary in the number of people involved and the nature of their connection.",
        "C": "Must always involve at least three people to be stable.",
        "D": "Are only valid if they are between family members."
      },
      "correct_answer": "B",
      "page": 10,
      "explanation": "The page provides examples of relationships involving 'Two people' (e.g., couple, friends) and 'More than two people' (e.g., family, team), showing the diversity in the scope and type of interpersonal connections."
    },
    {
      "id": 12,
      "topic": "Interdependence",
      "question": "What is the meaning of 'interdependence' in the context of interpersonal relationships, as explained on page 11?",
      "options": {
        "A": "Total independence from one another.",
        "B": "One person being completely dependent on the other.",
        "C": "Mutual dependence and having an impact on each other.",
        "D": "A competitive dynamic where each person tries to outperform the other."
      },
      "correct_answer": "C",
      "page": 11,
      "explanation": "Page 11 explicitly defines interdependence: 'Interdependence implies mutual dependence and having impact on each other.'"
    },
    {
      "id": 13,
      "topic": "Patterns of Interaction",
      "question": "Which of the following is given as an example of a 'consistent pattern of interaction' on page 12?",
      "options": {
        "A": "Shared financial investments.",
        "B": "Hugs, kisses, and handshakes.",
        "C": "Having the same political views.",
        "D": "Living in the same neighborhood."
      },
      "correct_answer": "B",
      "page": 12,
      "explanation": "The examples provided for consistent patterns of interaction are 'Hugs,' 'Kisses,' 'Handshakes,' and 'Unique code names.'"
    },
    {
      "id": 14,
      "topic": "Patterns of Interaction",
      "question": "The mention of 'Unique code names' as a pattern of interaction suggests that these patterns:",
      "options": {
        "A": "Are always universal and understood by everyone.",
        "B": "Can be highly personalized and specific to the relationship.",
        "C": "Must be verbally communicated to be valid.",
        "D": "Are primarily for the purpose of secrecy."
      },
      "correct_answer": "B",
      "page": 12,
      "explanation": "The term 'unique' implies that these patterns of interaction are insider language or rituals developed within the specific relationship, highlighting their personalized nature."
    },
    {
      "id": 15,
      "topic": "Duration of Interaction",
      "question": "How does the document distinguish a 'One-Time' interaction from an 'Interpersonal Relationship' on page 13?",
      "options": {
        "A": "One-Time interactions are more emotionally intense.",
        "B": "Interpersonal Relationships involve lasting connections and commitments, unlike brief one-time encounters.",
        "C": "One-Time interactions require more planning and effort.",
        "D": "There is no significant difference between the two."
      },
      "correct_answer": "B",
      "page": 13,
      "explanation": "The document contrasts 'One-Time' interactions (characterized by 'Brief/Passing interest' and 'No commitment') with 'Interpersonal Relationships' (characterized as 'Lasting' and involving 'Commitments')."
    },
    {
      "id": 16,
      "topic": "Types of Relationships - Complementary",
      "question": "What is the core dynamic of a 'Complementary relationship' as described on page 15?",
      "options": {
        "A": "Each person is in competition with the other.",
        "B": "Each person supplies what the other lacks.",
        "C": "Both individuals are identical in personality and gifts.",
        "D": "The relationship is based solely on physical attraction."
      },
      "correct_answer": "B",
      "page": 15,
      "explanation": "The definition states: 'Each person supplies what the other person or persons lack, often in a mutualistic nature.'"
    },
    {
      "id": 17,
      "topic": "Types of Relationships - Complementary",
      "question": "Why do participants in a complementary relationship 'tend to thrive,' according to the text?",
      "options": {
        "A": "Because they never experience conflict.",
        "B": "Because their needs are often met.",
        "C": "Because they are constantly challenged to change.",
        "D": "Because they are more goal-oriented."
      },
      "correct_answer": "B",
      "page": 15,
      "explanation": "The document explains that relationships are 'more personal as participants tend to thrive in such relationships as their needs are often met.'"
    },
    {
      "id": 18,
      "topic": "Types of Relationships - Complementary",
      "question": "What is the provided example of a complementary relationship?",
      "options": {
        "A": "Two intelligent co-workers on a project.",
        "B": "A friendship between an introverted person and an extroverted one.",
        "C": "A married couple who are both outgoing.",
        "D": "A parent and a newborn child."
      },
      "correct_answer": "B",
      "page": 15,
      "explanation": "The text gives the example: 'a friendship between an introverted person and an extroverted one,' where their differing social energies complement each other."
    },
    {
      "id": 19,
      "topic": "Types of Relationships - Symmetrical",
      "question": "What is the defining feature of a 'Symmetrical relationship'?",
      "options": {
        "A": "Individuals mirror each other or are highly similar.",
        "B": "One person is the leader and the other the follower.",
        "C": "The relationship is based on fulfilling each other's weaknesses.",
        "D": "It involves a strict hierarchy and chain of command."
      },
      "correct_answer": "A",
      "page": 16,
      "explanation": "The document defines symmetrical relationships by stating: 'Individuals mirror each other or are highly similar.'"
    },
    {
      "id": 20,
      "topic": "Types of Relationships - Symmetrical",
      "question": "How is the general focus of symmetrical relationships described?",
      "options": {
        "A": "They are more personal and need-oriented.",
        "B": "They tend to be more goal-oriented.",
        "C": "They are primarily for emotional support.",
        "D": "They are focused on romantic intimacy."
      },
      "correct_answer": "B",
      "page": 16,
      "explanation": "In contrast to the personal nature of complementary relationships, the text states that symmetrical relationships 'tend to be more goal-oriented.'"
    },
    {
      "id": 21,
      "topic": "Types of Relationships - Symmetrical",
      "question": "What example is given for a symmetrical relationship?",
      "options": {
        "A": "A friendship between an introvert and an extrovert.",
        "B": "A relationship between two intelligent co-workers on a project team.",
        "C": "A single parent and their child.",
        "D": "A dating couple from different cultural backgrounds."
      },
      "correct_answer": "B",
      "page": 16,
      "explanation": "The example provided is 'a relationship between two intelligent individuals or co-workers on a project team who seek to stimulate each other for better performance.' Their similar drive and intelligence create a symmetrical, goal-focused dynamic."
    },
    {
      "id": 22,
      "topic": "Conclusion",
      "question": "How does the conclusion on page 17 frame the importance of relationships for human society?",
      "options": {
        "A": "They are a pleasant but unnecessary luxury.",
        "B": "They are the key for every meaningful success, progress and development.",
        "C": "They are the primary source of conflict and should be minimized.",
        "D": "They are important only for individual emotional well-being."
      },
      "correct_answer": "B",
      "page": 17,
      "explanation": "The concluding statement is a strong, overarching claim: 'Relationships are the key for every meaningful success, progress and development of human society.'"
    },
    {
      "id": 23,
      "topic": "Synthesis - Definitions",
      "question": "Based on the definitions provided, which of the following scenarios best qualifies as an 'Interpersonal Relationship'?",
      "options": {
        "A": "Two strangers who make brief eye contact on a bus.",
        "B": "A customer and a cashier who have a quick, polite transaction.",
        "C": "Two siblings who rely on each other for advice, have inside jokes, and have been close their entire lives.",
        "D": "A person reading a biography about a historical figure."
      },
      "correct_answer": "C",
      "page": 9,
      "explanation": "This scenario meets all three criteria: Interdependence (relying on each other), Consistent patterns of interaction (inside jokes), and Interaction over an extended period (their entire lives). The other options lack one or more of these elements."
    },
    {
      "id": 24,
      "topic": "Synthesis - Human Nature & Relating",
      "question": "The module's progression from the 'Tripartite Nature of Man' to the 'Definition of Relationships' suggests that:",
      "options": {
        "A": "Human biology is the only important factor in relationships.",
        "B": "Our design as multi-faceted beings (spirit, soul, body) is the foundation for the complex nature of our connections.",
        "C": "The spirit is the only part of a human that can truly connect with others.",
        "D": "Relationships are purely a function of the soul (mind and emotions)."
      },
      "correct_answer": "B",
      "page": 6,
      "explanation": "By establishing the tripartite nature first, the module provides a theological anthropology that explains why relationships can be so multifaceted—involving spiritual fellowship, emotional and intellectual bonding, and physical presence."
    },
    {
      "id": 25,
      "topic": "Application - Relationship Types",
      "question": "A business partnership where two accountants with similar expertise and work ethic come together to start a firm is most likely an example of a:",
      "options": {
        "A": "Complementary Relationship",
        "B": "Symmetrical Relationship",
        "C": "One-Time Interaction",
        "D": "Familial Relationship"
      },
      "correct_answer": "B",
      "page": 16,
      "explanation": "This is a goal-oriented partnership between two highly similar individuals (both are accountants with similar expertise), which aligns perfectly with the definition and example of a symmetrical relationship."
    },
    {
      "id": 26,
      "topic": "Analysis - Foundational View",
      "question": "What is the overarching perspective on relationships presented in this introductory module?",
      "options": {
        "A": "They are random, meaningless encounters.",
        "B": "They are a biological imperative for survival only.",
        "C": "They are a fundamental, God-designed aspect of human existence that is crucial for personal and societal thriving.",
        "D": "They are primarily a source of pain and should be approached with caution."
      },
      "correct_answer": "C",
      "page": 17,
      "explanation": "The module grounds relationships in God's design (Gen 1, Tripartite nature), defines them as essential connections, and concludes they are the 'key' to societal success. This presents a positive, purposeful, and foundational view."
    },
    {
      "id": 1,
      "topic": "Course Title & Introduction",
      "question": "How is marriage metaphorically described on the title page of the document?",
      "options": {
        "A": "A Social Contract",
        "B": "A Legal Agreement",
        "C": "God's Relationship Masterpiece",
        "D": "A Human Tradition"
      },
      "correct_answer": "C",
      "page": 1,
      "explanation": "The main title of the document is 'Marriage: God’s Relationship Masterpiece,' indicating a view of marriage as a divine and expertly crafted work of art."
    },
    {
      "id": 2,
      "topic": "Course Title & Introduction",
      "question": "What is the specific focus of this section of the GEL 403 course?",
      "options": {
        "A": "Pitfalls in Relationships",
        "B": "Introduction and Basic Concepts of Marriage",
        "C": "Advanced Family Counseling",
        "D": "The History of Wedding Ceremonies"
      },
      "correct_answer": "B",
      "page": 1,
      "explanation": "The subtitle beneath the main title clearly states 'Introduction and Basic Concepts,' setting the scope for this part of the course material."
    },
    {
      "id": 3,
      "topic": "Key Objectives",
      "question": "According to the key objective on page 2, what two things should students be able to do regarding marriage?",
      "options": {
        "A": "Plan a wedding and manage a family budget.",
        "B": "Describe marriage as God intends it and distinguish human value sets from God's standards.",
        "C": "Counsel couples in crisis and perform marriage ceremonies.",
        "D": "Analyze the sociology of the family and write a research paper."
      },
      "correct_answer": "B",
      "page": 2,
      "explanation": "The learning outcome explicitly states: 'The students should be able to describe marriage as God intends it and distinguish the value sets of various human patterns vis-à-vis God’s required standards for the marriage institution.'"
    },
    {
      "id": 4,
      "topic": "Course Structure",
      "question": "Which of the following is NOT listed as part of the course outline on page 3?",
      "options": {
        "A": "Definitions",
        "B": "Therapy Techniques",
        "C": "Characteristics (General vs Christian)",
        "D": "Entry Points"
      },
      "correct_answer": "B",
      "page": 3,
      "explanation": "The outline includes Definitions, Characteristics, Types, Functions, and Entry Points. 'Therapy Techniques' is not mentioned, consistent with an introductory, conceptual module."
    },
    {
      "id": 5,
      "topic": "Introduction",
      "question": "How does the document describe marriage and family in relation to human society?",
      "options": {
        "A": "They are optional social clubs.",
        "B": "They are the key fundamental units.",
        "C": "They are outdated institutions.",
        "D": "They are primarily economic partnerships."
      },
      "correct_answer": "B",
      "page": 4,
      "explanation": "The introduction begins with the definitive statement: 'Marriage and family are the key fundamental units of human society.'"
    },
    {
      "id": 6,
      "topic": "Introduction",
      "question": "What is identified as the reason for the increasing complexity and confusion around marriage and family in modern times?",
      "options": {
        "A": "A lack of interest in relationships.",
        "B": "Modernistic views and variations, legal basis, constituents, and expectations.",
        "C": "Decreased life expectancy.",
        "D": "The influence of ancient traditions."
      },
      "correct_answer": "B",
      "page": 4,
      "explanation": "The text states: 'In modern times, the connections of these two social constructs are becoming increasingly complex (confused) due to modernistic views and variations, legal basis, constituents, and its expectations.'"
    },
    {
      "id": 7,
      "topic": "Definitions - Sociology",
      "question": "From a sociological perspective, how is marriage primarily defined on page 5?",
      "options": {
        "A": "A spiritual covenant before God.",
        "B": "A socially approved way of establishing a family of procreation and a legally recognized contract.",
        "C": "A temporary arrangement for emotional support.",
        "D": "An economic agreement between families."
      },
      "correct_answer": "B",
      "page": 5,
      "explanation": "The sociological definition provided includes two key parts: 'A socially approved way of establishing a family of procreation' and 'A legally recognized contract... with an expectation of permanence.'"
    },
    {
      "id": 8,
      "topic": "Definitions - Sociology",
      "question": "The sociological definition emphasizes the concept of a 'contract.' What is the implied nature of this contract?",
      "options": {
        "A": "It is a private, unspoken understanding.",
        "B": "It is a legal and socially recognized agreement.",
        "C": "It is a covenant that cannot be broken.",
        "D": "It is a financial merger."
      },
      "correct_answer": "B",
      "page": 5,
      "explanation": "By specifying it as a 'legally recognized contract,' the sociological perspective grounds marriage in the realm of civil law and public sanction, distinct from purely religious or personal definitions."
    },
    {
      "id": 9,
      "topic": "Definitions - Bibliocentric",
      "question": "How does the 'Bibliocentric Perspective' on page 6 fundamentally differ from the sociological one in its view of marriage's origin?",
      "options": {
        "A": "It views marriage as a recent human invention.",
        "B": "It sees marriage as a God-inspired and designed institution.",
        "C": "It considers marriage a legal contract for tax benefits.",
        "D": "It defines marriage as a political tool for social stability."
      },
      "correct_answer": "B",
      "page": 6,
      "explanation": "The Bibliocentric definition begins by stating marriage is 'A God-inspired and designed institution,' establishing a divine, rather than purely social, origin."
    },
    {
      "id": 10,
      "topic": "Definitions - Bibliocentric",
      "question": "What is the core relational dynamic in the Bibliocentric definition of marriage?",
      "options": {
        "A": "A business partnership.",
        "B": "A mutual covenant of love and trust.",
        "C": "A temporary romantic arrangement.",
        "D": "A friendship with legal benefits."
      },
      "correct_answer": "B",
      "page": 6,
      "explanation": "The text describes the union as 'a mutual covenant of love and trust,' highlighting the personal, relational, and binding nature of the partnership from a biblical viewpoint."
    },
    {
      "id": 11,
      "topic": "Definitions - Bibliocentric",
      "question": "According to the Bibliocentric definition, what is the stated duration of the marital commitment?",
      "options": {
        "A": "For as long as love lasts.",
        "B": "Until the children are grown.",
        "C": "Till death do them part.",
        "D": "For a renewable term of seven years."
      },
      "correct_answer": "C",
      "page": 6,
      "explanation": "The definition explicitly includes the phrase 'till death do them part,' emphasizing the intended permanence of the covenant."
    },
    {
      "id": 12,
      "topic": "General Characteristics",
      "question": "Which of the following is listed as a general characteristic of marriage on page 8?",
      "options": {
        "A": "It is a practice found only in Western cultures.",
        "B": "It is a universally recognized institution.",
        "C": "It is an institution that is declining in importance globally.",
        "D": "It is primarily an economic transaction."
      },
      "correct_answer": "B",
      "page": 8,
      "explanation": "The first feature listed under general characteristics is 'Marriage is a universally recognized institution.'"
    },
    {
      "id": 13,
      "topic": "General Characteristics",
      "question": "The document states that marriage 'establishes family.' This implies that the family unit is:",
      "options": {
        "A": "An entity that exists independently of marriage.",
        "B": "Fundamentally initiated and formed through the marital union.",
        "C": "A less important social construct than marriage.",
        "D": "Only relevant when children are present."
      },
      "correct_answer": "B",
      "page": 8,
      "explanation": "The statement 'Marriage establishes family' positions marriage as the foundational act that creates the core family unit."
    },
    {
      "id": 14,
      "topic": "General Characteristics",
      "question": "What is required for a marriage to be 'legally contracted,' according to page 9?",
      "options": {
        "A": "Social and legal approval, often associated with a ceremony.",
        "B": "Only the mutual agreement of the two individuals.",
        "C": "The approval of religious authorities only.",
        "D": "A written contract drafted by a lawyer."
      },
      "correct_answer": "A",
      "page": 9,
      "explanation": "The text states: 'Marriage requires social and legal approval, without which it is not legally contracted. Thus, it is usually associated with some kind of civil or religious ceremony.'"
    },
    {
      "id": 15,
      "topic": "General Characteristics",
      "question": "What are 'definite symbols' of marriage mentioned in the document?",
      "options": {
        "A": "Shared bank accounts and a house.",
        "B": "Rings, bridal gowns, and wedding tuxedos.",
        "C": "Tattoos of each other's names.",
        "D": "A joint social media profile."
      },
      "correct_answer": "B",
      "page": 9,
      "explanation": "The document lists 'rings, special clothes (bridal gowns and wedding tuxedos, wedding bands, etc.)' as definite symbols of marriage."
    },
    {
      "id": 16,
      "topic": "Spiritual Characteristics",
      "question": "The first spiritual characteristic on page 11 states marriage is 'the one recognized institution in heaven and on earth.' This is supported by which biblical reference?",
      "options": {
        "A": "Ephesians 5:31-32",
        "B": "Matthew 19:4-6",
        "C": "Genesis 2:23-24",
        "D": "Romans 7:2-3"
      },
      "correct_answer": "B",
      "page": 11,
      "explanation": "The citation next to this point is '(Matthew 19:4-6, Malachi 2:14)', indicating these verses are used to support the claim of its divine recognition."
    },
    {
      "id": 17,
      "topic": "Spiritual Characteristics",
      "question": "What unique 'certificate' does marriage confer, according to page 11?",
      "options": {
        "A": "A government-issued marriage license.",
        "B": "A certificate of ownership.",
        "C": "A spiritual status where exit is permitted only by death.",
        "D": "A certificate of financial union."
      },
      "correct_answer": "C",
      "page": 11,
      "explanation": "The text states marriage 'confers on its participants a certificate before entry and exit is permitted only by death,' using Romans 7:2-3 to underscore the permanence of the bond."
    },
    {
      "id": 18,
      "topic": "Spiritual Characteristics",
      "question": "What dictates the 'operational currency' of marriage from a spiritual perspective?",
      "options": {
        "A": "Government laws.",
        "B": "Covenants in the form of vows.",
        "C": "The opinions of family members.",
        "D": "Fluctuating emotional feelings."
      },
      "correct_answer": "B",
      "page": 12,
      "explanation": "The document explains that 'covenants – in form of vows – dictate the operational currency of the institution,' meaning the promises made form the basis for how the marriage functions."
    },
    {
      "id": 19,
      "topic": "Spiritual Characteristics",
      "question": "What profound relationship does marriage reflect, according to Ephesians 5:31-32 as cited on page 12?",
      "options": {
        "A": "The relationship between a king and his subjects.",
        "B": "The relationship between Christ and His Church.",
        "C": "The relationship between business partners.",
        "D": "The relationship between close friends."
      },
      "correct_answer": "B",
      "page": 12,
      "explanation": "The text states: 'Marriage is the one institution that perfectly reflects the type of relationship that exists between Christ and His Church (Ephesians 5:31-32).'"
    },
    {
      "id": 20,
      "topic": "Spiritual Characteristics",
      "question": "How is 'growth in intimacy' achieved in marriage, according to the spiritual characteristic on page 13?",
      "options": {
        "A": "By fiercely maintaining self-determination and independence.",
        "B": "By losing self-determination and yielding into oneness with the spouse.",
        "C": "By spending large amounts of money on romantic gestures.",
        "D": "By avoiding conflict at all costs."
      },
      "correct_answer": "B",
      "page": 13,
      "explanation": "The document presents a paradox: 'growth in intimacy comes by losing self-determination and yielding or releasing oneself into oneness with the spouse,' referencing Genesis 2:23-24."
    },
    {
      "id": 21,
      "topic": "Functions of Marriage",
      "question": "Which of the following is listed as a function of marriage on page 14?",
      "options": {
        "A": "Financial Investment",
        "B": "Socialization",
        "C": "Political Advocacy",
        "D": "Career Advancement"
      },
      "correct_answer": "B",
      "page": 14,
      "explanation": "The functions listed are: Sexual, Reproductive, Socialization, Educational, and Security. 'Socialization' is explicitly stated."
    },
    {
      "id": 22,
      "topic": "Functions of Marriage",
      "question": "The 'Educational' function of marriage likely refers to:",
      "options": {
        "A": "Formal university education for both partners.",
        "B": "The role of the family in teaching values, skills, and cultural norms to children and each other.",
        "C": "Homeschooling children as the only valid educational method.",
        "D": "Preparing for a career in teaching."
      },
      "correct_answer": "B",
      "page": 14,
      "explanation": "In a sociological and familial context, the 'educational' function broadly encompasses the transmission of knowledge, values, and social norms within the family unit."
    },
    {
      "id": 23,
      "topic": "Types of Marriage",
      "question": "What is identified as the 'ideal and Biblical standard' for marriage on page 16?",
      "options": {
        "A": "Polygyny",
        "B": "Monogamy",
        "C": "Endogamy",
        "D": "Polyandry"
      },
      "correct_answer": "B",
      "page": 16,
      "explanation": "Under the heading 'Monogamy,' the document explicitly states it is the '(ideal and Biblical standard).'"
    },
    {
      "id": 24,
      "topic": "Types of Marriage",
      "question": "What is the key distinction between Polygyny and Polyandry?",
      "options": {
        "A": "Polygyny involves one woman with multiple husbands; Polyandry involves one man with multiple wives.",
        "B": "Polygyny is legal; Polyandry is illegal.",
        "C": "Polygyny involves one man with multiple wives; Polyandry involves one woman with multiple husbands.",
        "D": "Polygyny is a modern practice; Polyandry is an ancient one."
      },
      "correct_answer": "C",
      "page": 16,
      "explanation": "The document defines Polygyny as 'one man... marry[ing] more than one wife' and Polyandry as 'a woman... free to marry more than one man.'"
    },
    {
      "id": 25,
      "topic": "Types of Marriage",
      "question": "Where is Polygyny noted as a most common pattern?",
      "options": {
        "A": "In most traditional African societies.",
        "B": "In Western European nations.",
        "C": "In North American urban centers.",
        "D": "In isolated island communities."
      },
      "correct_answer": "A",
      "page": 16,
      "explanation": "The text states: 'This is a most common pattern practised in most traditional African societies.'"
    },
    {
      "id": 26,
      "topic": "Types of Marriage",
      "question": "A marriage between two people of the same Christian denomination is an example of:",
      "options": {
        "A": "Exogamy",
        "B": "Polygamy",
        "C": "Endogamy",
        "D": "Levirate"
      },
      "correct_answer": "C",
      "page": 17,
      "explanation": "Endogamy is defined as 'Marriage between people of the same social category e.g.... same-faith...' A marriage within the same Christian denomination fits this definition."
    },
    {
      "id": 27,
      "topic": "Types of Marriage",
      "question": "An 'inter-tribal' marriage is classified as what type of marriage pattern?",
      "options": {
        "A": "Endogamy",
        "B": "Monogamy",
        "C": "Exogamy",
        "D": "Sororate"
      },
      "correct_answer": "C",
      "page": 17,
      "explanation": "Exogamy is defined as 'Marriage between people of different social groups e.g. inter-tribal...'"
    },
    {
      "id": 28,
      "topic": "Other Patterns",
      "question": "Which of the following is listed in the table of 'Other Marriage/Family Patterns'?",
      "options": {
        "A": "Monogamy",
        "B": "Endogamy",
        "C": "Single parenting",
        "D": "Polygyny"
      },
      "correct_answer": "C",
      "page": 18,
      "explanation": "The table on page 18 includes: Levirate, Sororate, Group, Same-sex, Single parenting, Cohabitation, and Open marriage. 'Single parenting' is listed."
    },
    {
      "id": 29,
      "topic": "Family Entry Points",
      "question": "According to page 19, what are the three entry points into a family?",
      "options": {
        "A": "Marriage, Adoption, and Inheritance",
        "B": "Procreation, Marriage, and Adoption",
        "C": "Friendship, Marriage, and Purchase",
        "D": "Birth, Marriage, and Employment"
      },
      "correct_answer": "B",
      "page": 19,
      "explanation": "The page clearly lists three entry points: 'Procreation', 'Marriage', and 'Adoption'."
    },
    {
      "id": 30,
      "topic": "Conclusion",
      "question": "How does the conclusion on page 20 describe God's original design and intention for marriage?",
      "options": {
        "A": "As a necessary evil for procreation.",
        "B": "As a holy, beautiful, and fulfilling expression that completes the human experience in a perfect union of oneness.",
        "C": "As a temporary arrangement for personal growth.",
        "D": "As a primarily legal and financial partnership."
      },
      "correct_answer": "B",
      "page": 20,
      "explanation": "The concluding statement is: 'Marriage was designed and intended by God to be a holy, beautiful, and fulfilling expression that completes the human experience of relationships in a perfect union of oneness.'"
    },
    {
      "id": 31,
      "topic": "Synthesis - Definitions",
      "question": "The key difference between the Sociological and Bibliocentric definitions of marriage is that the Sociological focuses on it as a ______, while the Bibliocentric focuses on it as a ______.",
      "options": {
        "A": "covenant; contract",
        "B": "contract; covenant",
        "C": "friendship; business",
        "D": "tradition; innovation"
      },
      "correct_answer": "B",
      "page": 5,
      "explanation": "The Sociological definition explicitly calls it a 'contract.' The Bibliocentric definition explicitly calls it a 'mutual covenant.' This is the fundamental distinction presented."
    },
    {
      "id": 32,
      "topic": "Synthesis - Characteristics",
      "question": "Which spiritual characteristic of marriage directly challenges modern 'self-determination' culture?",
      "options": {
        "A": "It requires social and legal approval.",
        "B": "It is a universally recognized institution.",
        "C": "Growth in intimacy comes by losing self-determination and yielding to oneness.",
        "D": "It has definite symbols like rings and gowns."
      },
      "correct_answer": "C",
      "page": 13,
      "explanation": "The concept that intimacy is achieved through self-surrender and yielding ('losing self-determination') stands in direct contrast to a culture that often prioritizes individual autonomy and self-determination above all else."
    },
    {
      "id": 33,
      "topic": "Application - Types",
      "question": "If a man from the Yoruba tribe in Nigeria marries a woman from the Igbo tribe in Nigeria, this union would be classified as:",
      "options": {
        "A": "Endogamy, because it is within the same country.",
        "B": "Exogamy, because it is inter-tribal.",
        "C": "Polygyny, because it involves multiple cultural influences.",
        "D": "Monogamy, but only if it's his first marriage."
      },
      "correct_answer": "B",
      "page": 17,
      "explanation": "Since tribes are considered distinct social groups, a marriage between them is 'inter-tribal,' which is the example given for Exogamy."
    },
    {
      "id": 34,
      "topic": "Analysis - Overall Purpose",
      "question": "Based on the content of the entire document, what is its primary aim?",
      "options": {
        "A": "To provide a neutral, unbiased overview of all global marriage practices.",
        "B": "To argue for the superiority of the Christian, bibliocentric view of marriage as a divine covenant.",
        "C": "To promote polygamous marriage patterns as equally valid.",
        "D": "To detail the legal process of obtaining a marriage license."
      },
      "correct_answer": "B",
      "page": 20,
      "explanation": "The document begins by calling marriage 'God's Relationship Masterpiece,' contrasts human patterns with 'God's required standards,' details spiritual characteristics, and concludes with God's design. Its aim is to present and advocate for the Christian perspective."
    },
    {
      "id": 35,
      "topic": "Analysis - Theological Implication",
      "question": "The characterization of marriage as reflecting 'Christ and His Church' (Ephesians 5) implies that the relationship should be:",
      "options": {
        "A": "Characterized by mutual service, sacrifice, and loving leadership.",
        "B": "Focused solely on personal happiness and fulfillment.",
        "C": "A democratic partnership where all decisions are put to a vote.",
        "D": "Primarily concerned with social status and external perception."
      },
      "correct_answer": "A",
      "page": 12,
      "explanation": "The relationship between Christ and the Church is biblically defined by Christ's sacrificial love and leadership and the Church's faithful submission and respect. This analogy sets a high spiritual standard for the marital relationship, centered on selfless love and service."
    },
    {
      "id": 1,
      "topic": "Course Identity",
      "question": "What is the specific course code for 'Relationships and Family'?",
      "options": {
        "A": "REL 101",
        "B": "GEL 403",
        "C": "FAM 200",
        "D": "MIN 505"
      },
      "correct_answer": "B",
      "page": 1,
      "explanation": "The cover page clearly displays the course code as 'GEL 403'."
    },
    {
      "id": 2,
      "topic": "Course Identity",
      "question": "The subtitle 'Pitfalls' on the cover page suggests the course will primarily focus on:",
      "options": {
        "A": "Celebrating only the successes in relationships.",
        "B": "Common mistakes and challenges in relationships.",
        "C": "Legal aspects of family relationships.",
        "D": "Historical views on relationships."
      },
      "correct_answer": "B",
      "page": 1,
      "explanation": "A 'pitfall' is a hidden or unexpected danger or difficulty. The title indicates a focus on identifying and understanding common relational mistakes."
    },
    {
      "id": 3,
      "topic": "Course Objectives",
      "question": "The key objective states students should demonstrate relational skills to appreciate 'human connections.' This implies the course scope is:",
      "options": {
        "A": "Limited to marital relationships only.",
        "B": "Broad, encompassing various types of interpersonal bonds.",
        "C": "Focused solely on parent-child relationships.",
        "D": "Concerned only with relationships within the church."
      },
      "correct_answer": "B",
      "page": 2,
      "explanation": "The phrase 'human connections' is inclusive and broad, suggesting the principles apply to family, friends, romantic partners, and other interpersonal bonds."
    },
    {
      "id": 4,
      "topic": "Course Structure",
      "question": "Based on the outline, which topic would logically be covered BEFORE 'Pitfalls'?",
      "options": {
        "A": "Therapy Techniques",
        "C": "Essence/Importance",
        "B": "Advanced Counseling",
        "D": "Legal Frameworks"
      },
      "correct_answer": "C",
      "page": 3,
      "explanation": "The outline lists 'Essence/Importance' before 'Pitfalls'. Understanding what a relationship *should be* is foundational to understanding where it can go wrong."
    },
    {
      "id": 5,
      "topic": "Course Structure",
      "question": "The outline item 'Process' likely refers to:",
      "options": {
        "A": "The legal process of marriage.",
        "B": "The natural development and stages of a relationship.",
        "C": "The process of ending a relationship.",
        "D": "A specific communication technique."
      },
      "correct_answer": "B",
      "page": 3,
      "explanation": "In a relational context, 'Process' typically refers to the dynamic stages a relationship goes through, such as building trust, deepening intimacy, and navigating conflict."
    },
    {
      "id": 6,
      "topic": "Biblical Foundation",
      "question": "The reference to Matthew 19:6 ('what God has joined together...') is used to support the idea that relationships are designed to be:",
      "options": {
        "A": "Temporary and conditional.",
        "B": "Inseparable and lifelong.",
        "C": "Easily dissolved.",
        "D": "Primarily for procreation."
      },
      "correct_answer": "B",
      "page": 4,
      "explanation": "The document directly quotes this verse to establish the divine intent for permanence in relationships."
    },
    {
      "id": 7,
      "topic": "Biblical Foundation",
      "question": "Proverbs 27:6 and 17 are cited to illustrate that relationships are meant to:",
      "options": {
        "A": "Be completely free of conflict.",
        "B": "Add value through honest and sharpening interaction.",
        "C": "Provide financial security.",
        "D": "Isolate individuals from the world."
      },
      "correct_answer": "B",
      "page": 4,
      "explanation": "These Proverbs speak of the value of 'faithful wounds' and how 'iron sharpens iron,' highlighting that godly relationships improve and refine individuals."
    },
    {
      "id": 8,
      "topic": "Biblical Foundation",
      "question": "According to page 4, the love that underscores a Godly relationship is best defined by:",
      "options": {
        "A": "Emotional feelings alone.",
        "B": "The characteristics described in 1 Corinthians 13.",
        "C": "Societal definitions of romance.",
        "D": "Unconditional agreement."
      },
      "correct_answer": "B",
      "page": 4,
      "explanation": "The reference '1 Corinthians 13:4-7' points to the biblical definition of love as patient, kind, not envious, etc., which is the model for Godly relationships."
    },
    {
      "id": 9,
      "topic": "Pitfalls - Boundaries",
      "question": "The definition of boundaries as a 'framework' implies they are:",
      "options": {
        "A": "A rigid set of unchangeable rules.",
        "B": "A proactive and structured approach to interaction.",
        "C": "Designed to control other people's behavior entirely.",
        "D": "Only necessary in toxic relationships."
      },
      "correct_answer": "B",
      "page": 7,
      "explanation": "A framework provides structure and guidance. Healthy boundaries are not about controlling others but about defining one's own limits and how one will engage."
    },
    {
      "id": 10,
      "topic": "Pitfalls - Boundaries",
      "question": "Why is it important that people can express feelings 'without fear of being misunderstood,' according to the text?",
      "options": {
        "A": "It is a legal right in any relationship.",
        "B": "It fosters an environment of safety and trust, which is essential for respect.",
        "C": "It means all feelings must be agreed with.",
        "D": "It prevents any form of conflict from occurring."
      },
      "correct_answer": "B",
      "page": 7,
      "explanation": "The freedom to be honest without fear is a cornerstone of psychological safety and deep respect, allowing for genuine connection and conflict resolution."
    },
    {
      "id": 11,
      "topic": "Pitfalls - Boundaries",
      "question": "How do healthy boundaries help 'retain our unique identity'?",
      "options": {
        "A": "By forcing others to change their identity to match ours.",
        "B": "By preventing enmeshment and ensuring personal values, beliefs, and needs are not swallowed by the relationship.",
        "C": "By making the relationship entirely about one's own needs.",
        "D": "By creating a separate legal identity."
      },
      "correct_answer": "B",
      "page": 8,
      "explanation": "Boundaries define where one person ends and another begins. They prevent enmeshment, allowing individuals to maintain their distinct personalities and convictions within a relationship."
    },
    {
      "id": 12,
      "topic": "Pitfalls - Boundaries",
      "question": "The ability to be 'appropriately assertive' as a benefit of boundaries means:",
      "options": {
        "A": "Being aggressive to get what you want.",
        "B": "Clearly and respectfully communicating your needs, thoughts, and feelings.",
        "C": "Always giving in to keep the peace.",
        "D": "Using passive-aggressive communication."
      },
      "correct_answer": "B",
      "page": 8,
      "explanation": "Appropriate assertiveness is the balanced middle ground between aggression and passivity. It involves standing up for oneself respectfully and honestly."
    },
    {
      "id": 13,
      "topic": "Pitfalls - Gender Differences",
      "question": "The pitfall is not the existence of differences, but the:",
      "options": {
        "A": "Inability to recognize them.",
        "B": "Discussion of them.",
        "C": "Similarities between genders.",
        "D": "Biological facts themselves."
      },
      "correct_answer": "A",
      "page": 9,
      "explanation": "The pitfall is explicitly named as the 'Inability to recognize the fundamental differences.' The course teaches to recognize and respect them, not ignore or fight them."
    },
    {
      "id": 14,
      "topic": "Pitfalls - Gender Differences",
      "question": "Stating that men and women are 'DIFFERENT' (in all caps) emphasizes that these differences are:",
      "options": {
        "A": "Minor and insignificant.",
        "B": "A social construct with no basis in reality.",
        "C": "Fundamental and important to acknowledge.",
        "D": "Only relevant in a marital context."
      },
      "correct_answer": "C",
      "page": 9,
      "explanation": "The use of all capital letters is a typographical way to place strong emphasis, indicating that these differences are significant and foundational."
    },
    {
      "id": 15,
      "topic": "Pitfalls - Gender Differences",
      "question": "The reference to Matthew 19:6 in the context of gender differences likely reinforces the idea that:",
      "options": {
        "A": "Differences are a flaw in God's design.",
        "B": "The union of two different beings (male and female) is part of God's original plan.",
        "C": "Men and women are spiritually incompatible.",
        "D": "The verse has no relevance to gender differences."
      },
      "correct_answer": "B",
      "page": 9,
      "explanation": "Matthew 19:6 discusses the union of a man and a woman becoming 'one flesh.' Citing it here grounds the discussion of gender differences in the context of God's design for complementary union."
    },
    {
      "id": 16,
      "topic": "Pitfalls - Unavailability",
      "question": "The phrase 'Actions speak louder than words' in this context directly challenges:",
      "options": {
        "A": "The importance of verbal communication.",
        "B": "The value of written promises.",
        "C": "A person who claims a relationship is important but whose behavior (like being absent) proves otherwise.",
        "D": "The need for personal quiet time."
      },
      "correct_answer": "C",
      "page": 10,
      "explanation": "This proverb highlights the discrepancy between what someone says (e.g., 'You are important to me') and what they do (e.g., consistently being unavailable). Behavior is a truer measure of priority."
    },
    {
      "id": 17,
      "topic": "Pitfalls - Unavailability",
      "question": "How does the principle 'You CANNOT serve two masters' relate to unavailability?",
      "options": {
        "A": "It forbids having a job while in a relationship.",
        "B": "It suggests that divided loyalty (e.g., to work, hobbies, or other people over the relationship) will result in neglect and unavailability.",
        "C": "It means you can only have one friend at a time.",
        "D": "It is a warning against polygamy only."
      },
      "correct_answer": "B",
      "page": 10,
      "explanation": "The verse is applied metaphorically. If a person's ultimate priority ('master') is their career, a hobby, or another relationship, it will inevitably lead to them being 'unavailable' to their primary relationship."
    },
    {
      "id": 18,
      "topic": "Pitfalls - Communication",
      "question": "The play on words 'relation - ship' visually separates the word to emphasize that a relationship is:",
      "options": {
        "A": "A vessel that requires joint effort to navigate.",
        "B": "About to sink.",
        "C": "Similar to a business transaction.",
        "D": "Focused on travel and adventure."
      },
      "correct_answer": "A",
      "page": 11,
      "explanation": "This is a common metaphor. A 'ship' requires a crew (the people in the relationship), a destination (shared goals), and a means of navigation (communication) to sail successfully."
    },
    {
      "id": 19,
      "topic": "Pitfalls - Communication",
      "question": "If communication is the 'life blood,' then ineffective communication is akin to:",
      "options": {
        "A": "A minor cosmetic issue.",
        "B": "A clogged artery or sickness that weakens or kills the relationship.",
        "C": "An optional organ.",
        "D": "An external factor like weather."
      },
      "correct_answer": "B",
      "page": 11,
      "explanation": "Just as blood carries essential oxygen and nutrients, communication carries understanding, empathy, and connection. If it is ineffective, the relationship is starved of what it needs to live."
    },
    {
      "id": 20,
      "topic": "Pitfalls - Unrealistic Expectations",
      "question": "The myth that 'true love is expected to hurt' can lead to:",
      "options": {
        "A": "A healthier perspective on conflict.",
        "B": "Tolerating abusive or damaging behavior under the false pretense that it is normal.",
        "C": "Stronger emotional resilience.",
        "D": "A more realistic view of love."
      },
      "correct_answer": "B",
      "page": 12,
      "explanation": "This dangerous myth can cause individuals to stay in harmful situations, mistaking pain and suffering for the passion or sacrifice of 'true love.'"
    },
    {
      "id": 21,
      "topic": "Pitfalls - Unrealistic Expectations",
      "question": "Saying 'welcome to real living' after 'goodbye to fairytales' means embracing relationships that are:",
      "options": {
        "A": "Boring and mundane.",
        "B": "Imperfect, requiring work, grace, and commitment.",
        "C": "Exactly like the movies.",
        "D": "Devoid of any romance or excitement."
      },
      "correct_answer": "B",
      "page": 12,
      "explanation": "Real living' contrasts with the fantasy of fairytales. It acknowledges the beauty and depth found in real, imperfect relationships that grow through effort and forgiveness."
    },
    {
      "id": 22,
      "topic": "Pitfalls - Unrealistic Expectations",
      "question": "Applying the Golden Rule (Luke 6:31) to expectations means:",
      "options": {
        "A": "Expecting your partner to read your mind.",
        "B": "Balancing your expectations of others with your willingness to meet those same standards yourself.",
        "C": "Lowering all your standards to zero.",
        "D": "Always putting your own needs first."
      },
      "correct_answer": "B",
      "page": 12,
      "explanation": "The Golden Rule creates a standard of reciprocity. Before expecting perfection from your partner, you must be willing to offer the same level of understanding, effort, and grace that you desire."
    },
    {
      "id": 23,
      "topic": "Pitfalls - Connection to God",
      "question": "According to 1 John 4:19, the logical order for love is:",
      "options": {
        "A": "We love others first, which teaches us to love God.",
        "B": "We love ourselves first, and then we can love others.",
        "C": "We love because God first loved us.",
        "D": "Love for God and others develops simultaneously and independently."
      },
      "correct_answer": "C",
      "page": 13,
      "explanation": "The verse 'We love because he first loved us' (1 John 4:19) establishes God's love as the source and model for all human love. We can only give what we have first received."
    },
    {
      "id": 24,
      "topic": "Pitfalls - Connection to God",
      "question": "How does knowing God's 'perfect love' specifically 'cast out fear' in relationships?",
      "options": {
        "A": "It guarantees we will never be hurt by others.",
        "B": "It provides a security and identity that is not dependent on human performance, reducing fear of rejection, failure, or abandonment.",
        "C": "It makes us fearless to the point of being reckless.",
        "D": "It removes all consequences for our relational mistakes."
      },
      "correct_answer": "B",
      "page": 13,
      "explanation": "When one's core sense of love and acceptance is anchored in God's unchanging character, the inevitable ups and downs of human relationships are less threatening. This security allows one to love more freely and without manipulation."
    },
    {
      "id": 25,
      "topic": "Conclusion",
      "question": "The phrase 'how life will handle you' can be interpreted as:",
      "options": {
        "A": "A deterministic view where individuals have no control.",
        "B": "The quality of your life experiences, opportunities, and support systems, which are deeply influenced by the health of your relationships.",
        "C": "A financial outcome.",
        "D": "A reference to physical health only."
      },
      "correct_answer": "B",
      "page": 14,
      "explanation": "This speaks to the principle of sowing and reaping. If you handle relationships with care, respect, and love ('sow' well), you are more likely to experience a life ('reap') filled with support, joy, and resilience."
    },
    {
      "id": 26,
      "topic": "Course Identity",
      "question": "The provider of this course material is:",
      "options": {
        "A": "A Secular University",
        "B": "The Equipping Christian Ministry",
        "C": "A Governmental Body",
        "D": "An Unnamed Individual"
      },
      "correct_answer": "B",
      "page": 1,
      "explanation": "Every page of the document includes the footer 'The Equipping Christian Ministry', identifying it as the source."
    },
    {
      "id": 27,
      "topic": "Course Objectives",
      "question": "The ultimate goal of learning 'basic relational skills' is to:",
      "options": {
        "A": "Become a licensed therapist.",
        "B": "Appreciate and value human connections.",
        "C": "Win every argument.",
        "D": "Change other people's behavior."
      },
      "correct_answer": "B",
      "page": 2,
      "explanation": "The objective clearly states the skills are a means to the end of helping students 'appreciate and value the human connections formed in their lives'."
    },
    {
      "id": 28,
      "topic": "Biblical Foundation",
      "question": "The reference to John 3:16 alongside 1 Corinthians 13 connects God's love for humanity with:",
      "options": {
        "A": "The legal requirements of marriage.",
        "B": "The practical characteristics of love in daily relationships.",
        "C": "The importance of financial giving.",
        "D": "The history of the church."
      },
      "correct_answer": "B",
      "page": 4,
      "explanation": "John 3:16 demonstrates the ultimate sacrificial action of God's love, while 1 Corinthians 13 defines the day-to-day attributes of that love (patience, kindness, etc.). Together, they show the source and the expression of Godly love."
    },
    {
      "id": 29,
      "topic": "Pitfalls - Boundaries",
      "question": "A key aspect of the boundary definition is that it is a framework for how we treat others and:",
      "options": {
        "A": "How we allow ourselves to be treated.",
        "B": "How we control others.",
        "C": "How we avoid all responsibility.",
        "D": "How we win arguments."
      },
      "correct_answer": "A",
      "page": 7,
      "explanation": "The definition is two-sided: 'how we want to be treated and we treat other people'. It's about self-respect and respect for others."
    },
    {
      "id": 30,
      "topic": "Pitfalls - Boundaries",
      "question": "Healthy boundaries 'respects your needs and the needs of others.' This indicates boundaries are:",
      "options": {
        "A": "Selfish.",
        "B": "Balanced and considerate.",
        "C": "Focused only on the other person.",
        "D": "A tool for manipulation."
      },
      "correct_answer": "B",
      "page": 8,
      "explanation": "This phrase underscores that biblical, healthy boundaries are not about selfishness but about stewardship—caring for oneself in order to be able to love others well."
    },
    {
      "id": 31,
      "topic": "Pitfalls - Gender Differences",
      "question": "The differences mentioned (chemistry, physiology, morphology) are primarily:",
      "options": {
        "A": "Psychological constructs.",
        "B": "Biological and physical in nature.",
        "C": "Learned behaviors.",
        "D": "Identical in all cultures."
      },
      "correct_answer": "B",
      "page": 9,
      "explanation": "Chemistry (hormones), physiology (bodily functions), and morphology (physical form/structure) are all terms referring to the biological and physical distinctions between males and females."
    },
    {
      "id": 32,
      "topic": "Pitfalls - Unavailability",
      "question": "Unavailability as a pitfall can manifest as physical absence but also as:",
      "options": {
        "A": "Financial generosity.",
        "B": "Emotional or attentional absence even when physically present.",
        "C": "Perfect communication.",
        "D": "Overly high expectations."
      },
      "correct_answer": "B",
      "page": 10,
      "explanation": "A person can be in the same room but be emotionally distant, distracted by their phone, or mentally preoccupied. This form of unavailability is just as damaging as physical absence."
    },
    {
      "id": 33,
      "topic": "Pitfalls - Communication",
      "question": "Ineffective communication would directly undermine which other core element mentioned on page 4?",
      "options": {
        "A": "The physical differences between genders.",
        "B": "The mutual, self-giving manner in which relationships thrive.",
        "C": "The legal definition of marriage.",
        "D": "The need for financial planning."
      },
      "correct_answer": "B",
      "page": 11,
      "explanation": "A 'mutual, self-giving manner' requires understanding the other person's needs and perspectives, which is impossible without effective communication."
    },
    {
      "id": 34,
      "topic": "Pitfalls - Unrealistic Expectations",
      "question": "A fairytale expectation directly contradicted by the 'mutual, self-giving' essence of relationships is:",
      "options": {
        "A": "The expectation of shared values.",
        "B": "The expectation that a partner exists solely to meet one's own needs and 'complete' them.",
        "C": "The expectation of honesty.",
        "D": "The expectation of commitment."
      },
      "correct_answer": "B",
      "page": 12,
      "explanation": "Fairytales often promote the idea of a 'perfect partner' who fulfills every desire. The biblical model is two whole people giving themselves to each other, not one incomplete person looking for another to fix them."
    },
    {
      "id": 35,
      "topic": "Pitfalls - Connection to God",
      "question": "According to 1 John 4:8, a person who does not know God lacks a fundamental understanding of love because:",
      "options": {
        "A": "God is love.",
        "B": "God is justice.",
        "C": "God is omnipotent.",
        "D": "God is invisible."
      },
      "correct_answer": "A",
      "page": 13,
      "explanation": "The verse 'Whoever does not love does not know God, because God is love' (1 John 4:8) establishes that God is not just a source of love, but is the very definition and embodiment of it."
    },
    {
      "id": 36,
      "topic": "Course Structure",
      "question": "The placement of 'Video Insert' on page 5 suggests the course uses:",
      "options": {
        "A": "Only text-based materials.",
        "B": "A multi-media approach to teaching.",
        "C": "Outdated technology.",
        "D": "Audio recordings only."
      },
      "correct_answer": "B",
      "page": 5,
      "explanation": "The 'Video Insert' page indicates that visual and auditory media are integrated into the curriculum to enhance learning."
    },
    {
      "id": 37,
      "topic": "Pitfalls - Boundaries",
      "question": "The statement that people must be free to express feelings 'without fear' implies that a lack of boundaries creates an environment of:",
      "options": {
        "A": "Openness and trust.",
        "B": "Apprehension and control.",
        "C": "Boredom.",
        "D": "Financial instability."
      },
      "correct_answer": "B",
      "page": 7,
      "explanation": "If boundaries are not respected, people learn that expressing themselves leads to negative consequences like anger, manipulation, or dismissal. This creates fear and apprehension, stifling honest communication."
    },
    {
      "id": 38,
      "topic": "Pitfalls - Gender Differences",
      "question": "Respecting gender differences, as taught here, requires:",
      "options": {
        "A": "Stereotyping all men and all women.",
        "B": "Appreciating the general, God-designed distinctions while valuing individual uniqueness.",
        "C": "Ignoring the differences to ensure absolute equality.",
        "D": "Assuming one gender is superior."
      },
      "correct_answer": "B",
      "page": 9,
      "explanation": "The course teaches recognition of fundamental differences, not rigid stereotypes. It's about understanding general design principles while still relating to the unique individual."
    },
    {
      "id": 39,
      "topic": "Pitfalls - Unavailability",
      "question": "From a biblical perspective, unavailability could be seen as a failure to:",
      "options": {
        "A": "Love your neighbor as yourself.",
        "B": "Amass personal wealth.",
        "C": "Travel the world.",
        "D": "Maintain a strict schedule."
      },
      "correct_answer": "A",
      "page": 10,
      "explanation": "Loving your neighbor (which includes your spouse, family, and friends) requires being 'available' to them in time, attention, and care. Chronic unavailability is a practical failure to live out this commandment."
    },
    {
      "id": 40,
      "topic": "Pitfalls - Communication",
      "question": "The word 'effective' in 'effective communication' implies that mere talking is insufficient; it must also be:",
      "options": {
        "A": "Loud and frequent.",
        "B": "Understood and constructive.",
        "C": "Always agreeable.",
        "D": "Written down."
      },
      "correct_answer": "B",
      "page": 11,
      "explanation": "Communication is 'effective' only when the message is accurately understood by the receiver and serves to build up the relationship, even during difficult conversations."
    },
    {
      "id": 41,
      "topic": "Pitfalls - Unrealistic Expectations",
      "question": "Applying the Golden Rule to expectations helps to cultivate:",
      "options": {
        "A": "A sense of entitlement.",
        "B": "Humility and empathy.",
        "C": "Competitiveness.",
        "D": "Financial dependence."
      },
      "correct_answer": "B",
      "page": 12,
      "explanation": "Before demanding something from another, considering if you could consistently meet that standard yourself fosters humility and empathy, making expectations more realistic and gracious."
    },
    {
      "id": 42,
      "topic": "Pitfalls - Connection to God",
      "question": "A 'solid connection to God' is presented as the antidote to the pitfall of:",
      "options": {
        "A": "Having healthy boundaries.",
        "B": "Lacking a true understanding and source of love, which underpins all other pitfalls.",
        "C": "Recognizing gender differences.",
        "D": "Being overly available."
      },
      "correct_answer": "B",
      "page": 13,
      "explanation": "Many pitfalls (unrealistic expectations, fear, lack of self-giving love) stem from a deficient understanding of love. The course posits that knowing God's love is the foundational cure."
    },
    {
      "id": 43,
      "topic": "Conclusion",
      "question": "The command to 'Cherish your relationships!' is an appeal to:",
      "options": {
        "A": "See them as burdens.",
        "B": "Value them highly and treat them with tender care.",
        "C": "Ignore their problems.",
        "D": "Only cherish them when they are easy."
      },
      "correct_answer": "B",
      "page": 14,
      "explanation": "To 'cherish' something is to protect and care for it lovingly, to hold it dear. This is the active, positive response to the teachings on pitfalls."
    },
    {
      "id": 44,
      "topic": "Synthesis",
      "question": "Which pitfall is most directly linked to a failure to live out the 'self-giving' love described in the essence of relationships?",
      "options": {
        "A": "Unavailability",
        "B": "Defining boundaries",
        "C": "Recognizing gender differences",
        "D": "Having a connection to God"
      },
      "correct_answer": "A",
      "page": 10,
      "explanation": "Unavailability is a practical failure of self-giving. Giving oneself to a relationship requires the gift of one's time and attention, which unavailability withholds."
    },
    {
      "id": 45,
      "topic": "Synthesis",
      "question": "How does establishing healthy boundaries actually support the 'mutual' aspect of a relationship?",
      "options": {
        "A": "By creating a one-sided power dynamic.",
        "B": "By ensuring both individuals' needs and identities are respected, creating a partnership of two whole people.",
        "C": "By reducing the amount of communication needed.",
        "D": "By making the relationship more business-like."
      },
      "correct_answer": "B",
      "page": 8,
      "explanation": "Mutuality requires two distinct individuals to come together. Boundaries help maintain the health and identity of each individual, preventing codependency and allowing for a true partnership."
    },
    {
      "id": 46,
      "topic": "Application",
      "question": "If a couple is struggling with the myth that 'true love should hurt,' the most direct corrective teaching from this document would be:",
      "options": {
        "A": "The definition of boundaries.",
        "B": "The characteristics of love from 1 Corinthians 13 (patient, kind, etc.).",
        "C": "The differences between the sexes.",
        "D": "The importance of communication."
      },
      "correct_answer": "B",
      "page": 4,
      "explanation": "1 Corinthians 13 describes what true, Godly love looks like in action. It is a direct contrast to a love that is characterized by pain, control, or abuse."
    },
    {
      "id": 47,
      "topic": "Application",
      "question": "A person who fears setting boundaries because they might seem 'unloving' has misunderstood the teaching that boundaries are a sign of:",
      "options": {
        "A": "Control",
        "B": "Respect",
        "C": "Weakness",
        "D": "Selfishness"
      },
      "correct_answer": "B",
      "page": 7,
      "explanation": "The document explicitly teaches that 'Setting boundaries is a sign of respect in a relationship.' It is a loving act towards oneself and the other person, as it fosters health and clarity."
    },
    {
      "id": 48,
      "topic": "Application",
      "question": "According to the course material, the most foundational solution to overcoming relational pitfalls is:",
      "options": {
        "A": "Reading more relationship books.",
        "B": "Finding a perfect partner.",
        "C": "Cultivating a solid connection to God, the source of love.",
        "D": "Learning to manipulate conversations."
      },
      "correct_answer": "C",
      "page": 13,
      "explanation": "The final pitfall discussed, 'Lack of a solid connection to God,' is presented as the root issue, as it is the source of the love needed to solve all other problems."
    },
    {
      "id": 49,
      "topic": "Synthesis",
      "question": "The course progresses logically from the ___ of relationships to the ___ that hinder them.",
      "options": {
        "A": "Pitfalls, Definitions",
        "B": "Problems, Solutions",
        "C": "Essence, Pitfalls",
        "D": "Types, Process"
      },
      "correct_answer": "C",
      "page": 3,
      "explanation": "The outline shows a structure that first establishes what relationships are meant to be (Essence/Importance) and then examines where they go wrong (Pitfalls)."
    },
    {
      "id": 50,
      "topic": "Conclusion",
      "question": "The ultimate motivation for applying these teachings, as implied by the conclusion, is:",
      "options": {
        "A": "To achieve personal happiness alone.",
        "B": "To control the outcomes of your life experiences by investing wisely in your relationships.",
        "C": "To impress others.",
        "D": "To fulfill a mere academic requirement."
      },
      "correct_answer": "B",
      "page": 14,
      "explanation": "The concluding line 'How you handle your relationships determine how life will handle you' provides a powerful, practical motivation for applying the course material to one's life."
    },
    {
      "id": 1,
      "topic": "Module Introduction",
      "question": "According to the introduction of Module 2, what are the three key areas that relationships influence in our lives?",
      "options": {
        "A": "Financial stability, social status, and career progression",
        "B": "Emotional well-being, personal growth, and overall quality of life",
        "C": "Physical health, academic achievement, and spiritual depth",
        "D": "Communication skills, bargaining power, and behavioral flexibility"
      },
      "correct_answer": "B",
      "page": 1,
      "explanation": "The introduction explicitly states: 'Relationships are an integral part of our human lives that influence our emotional well-being, personal growth, and overall quality of life.'"
    },
    {
      "id": 2,
      "topic": "Module Introduction",
      "question": "What will serve as a 'baseline for defining' healthy and unhealthy relationships in this module?",
      "options": {
        "A": "Ancient philosophical texts",
        "B": "Psychological theories from the 20th century",
        "C": "Contemporary examples",
        "D": "Strict biblical interpretations only"
      },
      "correct_answer": "C",
      "page": 1,
      "explanation": "The introduction concludes by stating the module will focus on 'contemporary examples as a baseline for defining such relationships.'"
    },
    {
      "id": 3,
      "topic": "Healthy Characteristics - Communication",
      "question": "How is 'Effective Communication' characterized in a healthy relationship?",
      "options": {
        "A": "Partners communicate only through written messages to avoid conflict.",
        "B": "Partners express thoughts and feelings without fear of judgment or retribution.",
        "C": "Communication is limited to positive and affirming topics only.",
        "D": "One partner takes the lead in all discussions to ensure efficiency."
      },
      "correct_answer": "B",
      "page": 1,
      "explanation": "The text defines effective communication as being 'open and honest' where partners 'express their thoughts and feelings without fear of judgment or retribution.'"
    },
    {
      "id": 4,
      "topic": "Healthy Characteristics - Sacrifice",
      "question": "The module describes 'Sacrifice' in healthy relationships as a readiness to give up personal interests for what purpose?",
      "options": {
        "A": "To completely lose one's individuality.",
        "B": "For the overall good of the relationship.",
        "C": "To prove one's love beyond doubt.",
        "D": "To avoid any form of conflict at all costs."
      },
      "correct_answer": "B",
      "page": 1,
      "explanation": "The characteristic of sacrifice is defined as a 'readiness to give up personal interests, satisfaction, desires and wants as a working ingredient for the overall good of the relationship.'"
    },
    {
      "id": 5,
      "topic": "Healthy Characteristics - Respect",
      "question": "How does 'Mutual Respect' manifest in a healthy relationship, according to the text?",
      "options": {
        "A": "By always agreeing with the other person's opinions.",
        "B": "By valuing each other's thoughts, feelings, and boundaries, and affirming the right to individuality.",
        "C": "By respecting only the feelings that are deemed logical.",
        "D": "By setting identical goals and interests for both partners."
      },
      "correct_answer": "B",
      "page": 1,
      "explanation": "The document states that respect involves 'valuing each other's thoughts, feelings, and boundaries' and that it 'best shows up in appreciating and affirming the right to individuality of the other.'"
    },
    {
      "id": 6,
      "topic": "Healthy Characteristics - Trust",
      "question": "What specific action is mentioned as part of 'Trust and Transparency'?",
      "options": {
        "A": "Sharing all passwords and social media accounts.",
        "B": "Keeping each other’s secrets and other vital personal information safe.",
        "C": "Providing a full account of one's daily activities.",
        "D": "Trusting that the other person will never change."
      },
      "correct_answer": "B",
      "page": 1,
      "explanation": "The text explicitly mentions that trust involves partners being 'confident that they can rely on each other and keep each other’s secrets and other vital personal information safe.'"
    },
    {
      "id": 7,
      "topic": "Healthy Characteristics - Support & Independence",
      "question": "The characteristic of 'Independence' in a healthy relationship allows individuals to:",
      "options": {
        "A": "Spend most of their time apart from their partner.",
        "B": "Maintain their individuality and pursue their own goals and interests.",
        "C": "Make major financial decisions without consultation.",
        "D": "Have separate circles of friends that never interact."
      },
      "correct_answer": "B",
      "page": 1,
      "explanation": "The document clearly states that 'Healthy relationships allow each person to maintain their individuality and pursue their own goals and interests.'"
    },
    {
      "id": 8,
      "topic": "Impact of Healthy Relationships",
      "question": "Which of the following is NOT listed as an impact of healthy relationships?",
      "options": {
        "A": "A sense of security and reduced stress.",
        "B": "Guaranteed financial prosperity.",
        "C": "Strengthened resilience in adversity.",
        "D": "Encouragement of personal growth and self-discovery."
      },
      "correct_answer": "B",
      "page": 2,
      "explanation": "The text mentions mental/emotional well-being (security, happiness, reduced stress), personal growth, strengthened resilience, and longevity. It does not mention financial prosperity."
    },
    {
      "id": 9,
      "topic": "Impact of Healthy Relationships",
      "question": "According to the module, how are healthy relationships associated with 'Longevity'?",
      "options": {
        "A": "They guarantee a person will live to be over 100 years old.",
        "B": "They are linked to longer, happier lives and better physical health.",
        "C": "They make time feel like it passes more slowly.",
        "D": "They refer to the length of the relationship itself, not the individuals' lives."
      },
      "correct_answer": "B",
      "page": 2,
      "explanation": "The text states: 'Healthy relationships are associated with longer and happier lives. People in such relationships tend to have better physical health and a lower risk of chronic illnesses.'"
    },
    {
      "id": 10,
      "topic": "Unhealthy Characteristics - Obsession",
      "question": "The characteristic of 'Obsession' in an unhealthy relationship is marked by a desire to:",
      "options": {
        "A": "Spend every waking moment together.",
        "B": "Drive and control the relationship using manipulative strategies.",
        "C": "Learn everything about the partner's past.",
        "D": "Protect the partner from any external harm."
      },
      "correct_answer": "B",
      "page": 2,
      "explanation": "The document defines obsession as the 'continuous desire to drive and control the relationship... by playing mind games, the victim card and other manipulative strategies.'"
    },
    {
      "id": 11,
      "topic": "Unhealthy Characteristics - Jealousy",
      "question": "What is the fundamental cause of envy/jealousy in an unhealthy relationship, as described in the module?",
      "options": {
        "A": "A lack of financial resources.",
        "B": "Emotional insecurity.",
        "C": "Cultural and societal pressures.",
        "D": "Having too many friends."
      },
      "correct_answer": "B",
      "page": 2,
      "explanation": "The text explicitly states: 'This emotion is a strong sign of emotional insecurity and often a prominent feature of unhealthy relationships.'"
    },
    {
      "id": 12,
      "topic": "Unhealthy Characteristics - Mental Abuse",
      "question": "What is the stated purpose of mental abuse in an unhealthy relationship?",
      "options": {
        "A": "To help the partner become emotionally stronger.",
        "B": "To keep the other partner enslaved in the relationship.",
        "C": "To vent personal frustrations in a 'safe' environment.",
        "D": "To prepare the partner for the harshness of the outside world."
      },
      "correct_answer": "B",
      "page": 2,
      "explanation": "The module describes mental abuse as 'emotional violence designed to keep the other partner enslaved in the relationship.'"
    },
    {
      "id": 13,
      "topic": "Unhealthy Characteristics - Gossip",
      "question": "What is a potential consequence of 'Gossip' as defined in the module?",
      "options": {
        "A": "Strengthening the bond with mutual friends.",
        "B": "Leading to untold emotional, career or even physical harm to the partner.",
        "C": "Increasing the social popularity of the relationship.",
        "D": "Serving as a harmless outlet for stress."
      },
      "correct_answer": "B",
      "page": 2,
      "explanation": "The text warns that gossip 'could lead to untold emotional, career or even physical harm to the partner.'"
    },
    {
      "id": 14,
      "topic": "Unhealthy Characteristics - Communication",
      "question": "How is communication described in an unhealthy relationship?",
      "options": {
        "A": "As overly polite and avoidant.",
        "B": "As marked by brash, insulting, denigrating, and deceptive interactions.",
        "C": "As infrequent and brief.",
        "D": "As solely focused on problem-solving."
      },
      "correct_answer": "B",
      "page": 2,
      "explanation": "The document states that in unhealthy relationships, 'communication is often marked by brash, insulting, denigrating and deceptive interactions.'"
    },
    {
      "id": 15,
      "topic": "Impact of Unhealthy Relationships",
      "question": "Which of the following is listed as an impact of unhealthy relationships?",
      "options": {
        "A": "Enhanced social circles",
        "B": "Emotional distress, including anxiety and depression",
        "C": "Rapid personal and professional advancement",
        "D": "Increased independence and self-reliance"
      },
      "correct_answer": "B",
      "page": 2,
      "explanation": "The first point under the impact of unhealthy relationships is 'Emotional Distress: Unhealthy relationships can lead to emotional distress, including anxiety, depression, and low self-esteem.'"
    },
    {
      "id": 16,
      "topic": "Impact of Unhealthy Relationships",
      "question": "The impact labeled 'Stagnation' refers to individuals feeling:",
      "options": {
        "A": "Overwhelmed by too many opportunities.",
        "B": "Stuck or unable to grow due to a lack of support or constant negativity.",
        "C": "Bored because the relationship is too peaceful.",
        "D": "Pressured to grow in a direction they do not want to."
      },
      "correct_answer": "B",
      "page": 3,
      "explanation": "The text defines stagnation as when 'individuals in unhealthy relationships may feel stuck or unable to grow due to a lack of support or constant negativity.'"
    },
    {
      "id": 17,
      "topic": "Impact of Unhealthy Relationships",
      "question": "How can unhealthy relationships lead to 'Physical Health Issues'?",
      "options": {
        "A": "Through direct physical abuse only.",
        "B": "Through prolonged exposure to chronic stress.",
        "C": "By encouraging unhealthy eating habits together.",
        "D": "By reducing the time available for exercise."
      },
      "correct_answer": "B",
      "page": 3,
      "explanation": "The document states: 'Prolonged exposure to unhealthy relationships can lead to chronic stress, which can have detrimental effects on physical health.'"
    },
    {
      "id": 18,
      "topic": "Management - Bargaining",
      "question": "What is the core purpose of 'Bargaining' in relationship management?",
      "options": {
        "A": "To determine a winner and a loser in a conflict.",
        "B": "To reach an agreement on what each party should give and receive.",
        "C": "To avoid discussing difficult topics altogether.",
        "D": "To convince the other party to completely adopt one's own viewpoint."
      },
      "correct_answer": "B",
      "page": 3,
      "explanation": "Bargaining is defined as when 'two or more parties in the relationship attempt to reach an agreement on what each should give and receive in a transaction between them.'"
    },
    {
      "id": 19,
      "topic": "Management - Bargaining",
      "question": "Which of the following is a necessary feature for a bargaining situation to exist?",
      "options": {
        "A": "One party must have significantly more power than the other.",
        "B": "All parties must be related by blood or marriage.",
        "C": "Each party perceives the other(s) as having conflicting preferences or opposed interests.",
        "D": "A neutral third-party mediator must be present."
      },
      "correct_answer": "C",
      "page": 3,
      "explanation": "The first of the three listed features of a bargaining situation is 'Each party perceives the other(s) as having conflicting preferences or opposed interests.'"
    },
    {
      "id": 20,
      "topic": "Management - Behavioural Flexibility",
      "question": "A person with 'Behavioural Flexibility' is characterized by:",
      "options": {
        "A": "Being dogmatic and sticking rigidly to principles.",
        "B": "The ability to alter behavior to adapt to new situations.",
        "C": "Always changing their opinion to please others.",
        "D": "Refusing to adjust their communication style for anyone."
      },
      "correct_answer": "B",
      "page": 3,
      "explanation": "The text defines Behavioral Flexibility as 'the ability to alter behaviour to adapt to new situations and relate in new ways when necessary.'"
    },
    {
      "id": 21,
      "topic": "Management - Behavioural Flexibility",
      "question": "According to the module, a flexible person demonstrates good listening skills and is:",
      "options": {
        "A": "Confident about sharing messages with others and self-disclosing as appropriate.",
        "B": "Secretive and rarely shares personal information.",
        "C": "Quick to interrupt and correct others.",
        "D": "Focused solely on getting their own point across."
      },
      "correct_answer": "A",
      "page": 3,
      "explanation": "The document states that a flexible person 'is confident about sharing messages with others, self-disclosing as appropriate and understands the messages others provide by demonstrating good listening skills.'"
    },
    {
      "id": 22,
      "topic": "Case Study - Healthy",
      "question": "Mike and Gloria Bamiloye's relationship is presented as a case study for what?",
      "options": {
        "A": "The challenges of inter-cultural marriage.",
        "B": "A healthy relationship that serves as a positive influence and role model.",
        "C": "A relationship that survived infidelity.",
        "D": "The dangers of being in the public eye."
      },
      "correct_answer": "B",
      "page": 3,
      "explanation": "The case study introduces them as a 'supportive and respectful relationship that aligns with healthy relationship characteristics' and states their 'model serve as a positive influence and role model for others.'"
    },
    {
      "id": 23,
      "topic": "Case Study - Healthy",
      "question": "What is cited as evidence of the health of the Bamiloyes' relationship beyond their own marriage?",
      "options": {
        "A": "Their vast financial wealth.",
        "B": "Their children's thriving, supportive homes.",
        "C": "Their extensive international travels.",
        "D": "Their critically acclaimed artistic works."
      },
      "correct_answer": "B",
      "page": 3,
      "explanation": "The text mentions that their partnership has become a 'fruitful template' for 'all three of his children, all settled in Christian ministry with thriving, supportive homes.'"
    },
    {
      "id": 24,
      "topic": "Case Study - Unhealthy",
      "question": "Will and Jada Pinkett Smith's relationship is used as a case study for what?",
      "options": {
        "A": "How to maintain a perfect public image.",
        "B": "The manifestation of unhealthy relationships within a seemingly strong union.",
        "C": "A successful example of an open marriage.",
        "D": "The benefits of public confession for relationship healing."
      },
      "correct_answer": "B",
      "page": 4,
      "explanation": "The case study begins by stating: 'Unhealthy relationships can manifest in various forms even within seemingly strong unions. A classic example of that of Will and Jada Smith...'"
    },
    {
      "id": 25,
      "topic": "Case Study - Unhealthy",
      "question": "What specific event in 2020 marked a turning point in the public's perception of the Smiths' marriage?",
      "options": {
        "A": "They renewed their wedding vows in a grand ceremony.",
        "B": "They publicly discussed their relationship struggles.",
        "C": "Will Smith won an Academy Award.",
        "D": "They announced a joint business venture."
      },
      "correct_answer": "B",
      "page": 4,
      "explanation": "The case study notes that 'in the year 2020, the cracks in their relationship began to visibly show, when Will Smith and Jada Pinkett Smith made world headlines when they publicly discussed their relationship struggles.'"
    },
    {
      "id": 26,
      "topic": "Case Study - Unhealthy",
      "question": "Jada Pinkett Smith revealed that their relationship had undergone what significant, hidden event since 2016?",
      "options": {
        "A": "A secret adoption.",
        "B": "A secret divorce.",
        "C": "A secret business failure.",
        "D": "A secret religious conversion."
      },
      "correct_answer": "B",
      "page": 4,
      "explanation": "The text states: 'Jada even admitted to the fact that the relationship had undergone a secret divorce since 2016, but they were still posing like a happy couple...'"
    },
    {
      "id": 27,
      "topic": "Case Study - Unhealthy",
      "question": "Which of the following negative values was NOT listed as a marker of the Smiths' 'roller coaster relationship'?",
      "options": {
        "A": "Loose boundaries and disrespect.",
        "B": "Deceit and 'gaslighting'.",
        "C": "Shared financial goals and frugality.",
        "D": "Involvement in other intimate relationships while still married."
      },
      "correct_answer": "C",
      "page": 4,
      "explanation": "The listed negative values are: 'claims of deep emotional connection, loose boundaries, involvement in other intimate relationships while still married, disrespect, deceit, ‘gaslighting’, fear of the unknown and mind control games.' Shared financial goals are not mentioned."
    },
    {
      "id": 28,
      "topic": "Conclusion",
      "question": "What does the conclusion identify as the key factor that will lead to 'lasting and thriving relationships'?",
      "options": {
        "A": "Wealth and social status.",
        "B": "Willingness to boldly address challenges of communication and growth.",
        "C": "Finding a perfectly compatible partner from the start.",
        "D": "Avoiding all forms of conflict and disagreement."
      },
      "correct_answer": "B",
      "page": 4,
      "explanation": "The concluding sentence of the module is: 'Willingness to boldly address challenges of communication and growth in relationships will lead to lasting and thriving relationships.'"
    },
    {
      "id": 29,
      "topic": "Synthesis - Healthy vs. Unhealthy",
      "question": "Which characteristic of a healthy relationship is the direct opposite of 'Aggressive and hurtful communication'?",
      "options": {
        "A": "Sacrifice",
        "B": "Independence",
        "C": "Effective Communication",
        "D": "Longevity"
      },
      "correct_answer": "C",
      "page": 1,
      "explanation": "Effective Communication is defined by open, honest, and respectful dialogue, which is the direct antithesis of communication that is 'brash, insulting, denigrating and deceptive.'"
    },
    {
      "id": 30,
      "topic": "Synthesis - Concepts",
      "question": "The management technique of 'Behavioural Flexibility' is most aligned with which characteristic of a healthy relationship?",
      "options": {
        "A": "Trust and Transparency",
        "B": "Sacrifice",
        "C": "Mutual Respect",
        "D": "Independence"
      },
      "correct_answer": "B",
      "page": 3,
      "explanation": "Sacrifice involves a 'readiness to give up personal interests... for the overall good of the relationship.' Behavioural Flexibility is the practical skill of 'alter[ing] behaviour to adapt,' which is often a form of sacrifice for the relationship's benefit."
    },
    {
      "id": 31,
      "topic": "Application - Characteristics",
      "question": "If a person feels their partner tries to isolate them from their friends, which characteristic of an unhealthy relationship are they likely experiencing?",
      "options": {
        "A": "Obsession",
        "B": "Envy/Jealousy",
        "C": "Gossip",
        "D": "Mental Abuse"
      },
      "correct_answer": "B",
      "page": 2,
      "explanation": "The description of Envy/Jealousy states that one partner 'tries by every means to reduce or eliminate contact between the partner and other individuals outside the relationship,' which is a form of isolation."
    },
    {
      "id": 32,
      "topic": "Application - Impact",
      "question": "A person in a relationship who constantly feels anxious, doubts their self-worth, and is unable to pursue their career goals is likely experiencing the impacts of:",
      "options": {
        "A": "A healthy relationship that is pushing them to grow.",
        "B": "An unhealthy relationship, leading to emotional distress and stagnation.",
        "C": "The normal challenges of any long-term relationship.",
        "D": "A relationship that is too independent."
      },
      "correct_answer": "B",
      "page": 2,
      "explanation": "Anxiety and low self-esteem are listed under 'Emotional Distress,' and feeling 'unable to grow' is the definition of 'Stagnation,' both of which are impacts of unhealthy relationships."
    },
    {
      "id": 33,
      "topic": "Application - Management",
      "question": "A couple is deciding how to split household chores. They discuss their preferences, acknowledge their different opinions, and work towards a solution that seems fair to both. This is an example of:",
      "options": {
        "A": "Gossip",
        "B": "Bargaining",
        "C": "Obsession",
        "D": "Stagnation"
      },
      "correct_answer": "B",
      "page": 3,
      "explanation": "This scenario fits the definition of bargaining: attempting to reach an agreement on what each should give and receive, with perceived conflicting preferences but a potential for a mutually acceptable outcome."
    },
    {
      "id": 34,
      "topic": "Analysis - Case Studies",
      "question": "The case studies of the Bamiloyes and the Smiths are primarily used in this module to:",
      "options": {
        "A": "Provide celebrity gossip and entertainment.",
        "B": "Illustrate the theoretical concepts with concrete, contemporary examples.",
        "C": "Promote specific religious beliefs about marriage.",
        "D": "Demonstrate that all long-term relationships are fundamentally the same."
      },
      "correct_answer": "B",
      "page": 3,
      "explanation": "The introduction stated the module would use 'contemporary examples as a baseline.' The case studies serve to ground the abstract characteristics, impacts, and management techniques in real-world scenarios."
    },
    {
      "id": 35,
      "topic": "Analysis - Overall Message",
      "question": "What is the overarching message of Module 2?",
      "options": {
        "A": "Relationships are easy to maintain if you find the right person.",
        "B": "Understanding the distinct characteristics, impacts, and management strategies of healthy and unhealthy relationships is crucial for personal well-being.",
        "C": "Unhealthy relationships are always obvious and should be immediately terminated.",
        "D": "The health of a relationship is determined solely by its longevity."
      },
      "correct_answer": "B",
      "page": 4,
      "explanation": "The module is structured to first define the characteristics of both types, then explore their impacts, and finally offer management strategies. The conclusion emphasizes proactive management for a thriving relationship, encapsulating this overarching message."
    }
  ]

    
def analyze_exam_topics(questions):
    """Analyze and categorize exam questions by topic"""
    topics = {}
    for q in questions:
        topic = q.get('topic', 'General')
        topics[topic] = topics.get(topic, 0) + 1
    return topics

def initialize_exam_state():
    """Initialize or reset the exam state"""
    questions = load_questions_from_json()
    
    st.session_state.questions = questions
    st.session_state.current_question = 0
    st.session_state.score = 0
    st.session_state.answered = False
    st.session_state.user_answers = [None] * len(questions)
    st.session_state.exam_completed = False
    st.session_state.topics = analyze_exam_topics(questions)
    random.shuffle(st.session_state.questions)

def parse_uploaded_json(uploaded_file):
    """Parse uploaded JSON file and extract questions"""
    try:
        data = json.load(uploaded_file)
        
        # Try different possible question keys
        possible_keys = [
            "programming_languages_exam_questions",
            "chemistry_questions",
            "questions",
            "quiz_questions",
            "exam_questions"
        ]
        
        for key in possible_keys:
            if key in data and isinstance(data[key], list) and len(data[key]) > 0:
                questions = data[key]
                # Validate question structure
                if all('question' in q and 'options' in q and 'correct_answer' in q for q in questions):
                    st.success(f"✅ Found {len(questions)} questions with key: '{key}'")
                    return questions
        
        # If no standard key found, look for any list with question structure
        for key, value in data.items():
            if isinstance(value, list) and len(value) > 0:
                sample_item = value[0]
                if isinstance(sample_item, dict) and 'question' in sample_item and 'options' in sample_item and 'correct_answer' in sample_item:
                    st.success(f"✅ Found {len(value)} questions with key: '{key}'")
                    return value
        
        st.error("❌ No valid questions found in the uploaded file")
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

    # Initialize session state
    if 'questions' not in st.session_state or not st.session_state.questions:
        initialize_exam_state()
    
    # Header
    st.title("💻Exam")
    st.markdown("### Upload your own JSON question file or use the built-in questions")
    
    # File Upload Section - PROMINENTLY DISPLAYED
    with st.expander("📁 Upload Your JSON Question File", expanded=True):
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
        """)
        
        uploaded_file = st.file_uploader(
            "Choose a JSON file", 
            type="json",
            help="Upload your questions in JSON format"
        )
        
        if uploaded_file is not None:
            # Parse the uploaded file
            questions = parse_uploaded_json(uploaded_file)
            
            if questions:
                col1, col2 = st.columns(2)
                
                with col1:
                    if st.button("🔄 Load Uploaded Questions", type="primary"):
                        st.session_state.questions = questions
                        st.session_state.current_question = 0
                        st.session_state.score = 0
                        st.session_state.answered = False
                        st.session_state.user_answers = [None] * len(questions)
                        st.session_state.exam_completed = False
                        st.session_state.topics = analyze_exam_topics(questions)
                        random.shuffle(st.session_state.questions)
                        st.success(f"✅ Loaded {len(questions)} questions!")
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
            placeholder='Paste your JSON questions here...'
        )
        
        if st.button("📥 Load from Text", type="secondary"):
            if json_text.strip():
                try:
                    # Create a temporary file-like object
                    import io
                    fake_file = io.BytesIO(json_text.encode('utf-8'))
                    fake_file.name = "pasted_json.json"
                    
                    questions = parse_uploaded_json(fake_file)
                    if questions:
                        st.session_state.questions = questions
                        st.session_state.current_question = 0
                        st.session_state.score = 0
                        st.session_state.answered = False
                        st.session_state.user_answers = [None] * len(questions)
                        st.session_state.exam_completed = False
                        st.session_state.topics = analyze_exam_topics(questions)
                        random.shuffle(st.session_state.questions)
                        st.success(f"✅ Loaded {len(questions)} questions from pasted JSON!")
                        st.rerun()
                except Exception as e:
                    st.error(f"❌ Error parsing JSON text: {e}")
            else:
                st.warning("Please paste some JSON text first.")
    
    # Show warning if no questions
    if not st.session_state.questions:
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
            current_attempted = st.session_state.current_question + 1 if st.session_state.current_question > 0 else 0
            st.metric("Current Score", f"{st.session_state.score}/{current_attempted}")
        else:
            st.metric("Final Score", f"{st.session_state.score}/{len(st.session_state.questions)}")
    with col4:
        if st.button("🔄 Use Built-in Questions"):
            initialize_exam_state()
            st.rerun()
    
    # Sidebar for exam progress and info
    with st.sidebar:
        st.header("📊 Exam Progress")
        
        current_score = st.session_state.score
        total_questions = len(st.session_state.questions)
        
        if not st.session_state.exam_completed:
            questions_attempted = st.session_state.current_question + 1
            progress = questions_attempted / total_questions
            score_percentage = (current_score / questions_attempted) * 100 if questions_attempted > 0 else 0
        else:
            questions_attempted = total_questions
            progress = 1.0
            score_percentage = (current_score / total_questions) * 100
        
        st.write(f"**Score:** {current_score}/{questions_attempted}")
        st.write(f"**Accuracy:** {score_percentage:.1f}%")
        st.progress(progress)
        st.write(f"**Progress:** {questions_attempted}/{total_questions}")
        
        # Exam controls
        st.header("🎯 Exam Controls")
        if st.button("🔄 Restart Exam", use_container_width=True):
            initialize_exam_state()
            st.rerun()
        
        if st.button("🔀 Shuffle Questions", use_container_width=True):
            random.shuffle(st.session_state.questions)
            st.session_state.current_question = 0
            st.session_state.answered = False
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
            user_answer = st.radio(
                "Select your answer:",
                option_labels,
                format_func=lambda x: f"{x}. {current_q['options'][x]}",
                key=f"q{st.session_state.current_question}"
            )
            
            # Submit button
            if st.button("🚀 Submit Answer", type="primary"):
                st.session_state.answered = True
                st.session_state.user_answers[st.session_state.current_question] = user_answer
                
                # Check if answer is correct
                if user_answer == current_q['correct_answer']:
                    st.session_state.score += 1
                
                # Rerun to show results and explanation
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
                        st.rerun()
            
            with col2:
                if st.session_state.current_question < len(st.session_state.questions) - 1:
                    if st.button("⏭️ Next Question", type="primary", use_container_width=True):
                        st.session_state.current_question += 1
                        st.session_state.answered = False
                        st.rerun()
                else:
                    if st.button("🏁 Finish Exam", type="primary", use_container_width=True):
                        st.session_state.exam_completed = True
                        st.rerun()
            
            with col3:
                if st.button("🔄 Try Again", use_container_width=True):
                    st.session_state.answered = False
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
        
        # Detailed answer review with explanations
        st.subheader("🔍 Detailed Answer Review")
        for i, question in enumerate(st.session_state.questions):
            with st.expander(f"Question {i+1}: {question['question'][:80]}...", expanded=False):
                user_ans = st.session_state.user_answers[i]
                correct_ans = question['correct_answer']
                
                # Show question details
                st.write(f"**Topic:** {question.get('topic', 'General')}")
                if 'page' in question:
                    st.write(f"**Reference:** Page {question['page']}")
                
                # Show user's answer vs correct answer
                st.write(f"**Your answer:** {user_ans}. {question['options'][user_ans] if user_ans else 'Not answered'}")
                st.write(f"**Correct answer:** {correct_ans}. {question['options'][correct_ans]}")
                
                # Show explanation
                if 'explanation' in question and question['explanation']:
                    st.info(f"**Explanation:** {question['explanation']}")
                
                # Show result
                if user_ans == correct_ans:
                    st.success("✅ You answered this correctly!")
                else:
                    st.error("❌ You answered this incorrectly.")
        
        # Restart option
        st.write("---")
        if st.button("🔄 Take Exam Again", type="primary"):
            initialize_exam_state()
            st.rerun()

if __name__ == "__main__":
    main()