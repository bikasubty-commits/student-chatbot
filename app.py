from flask import Flask, render_template, request, jsonify
from difflib import get_close_matches

app = Flask(__name__)

# =========================
# CHATBOT RESPONSES
# =========================

responses = {

    
# =========================
# NIELIT INSTITUTIONAL INFO
# =========================

#"nielit": "NIELIT stands for National Institute of Electronics and Information Technology.",

"full form of nielit": "NIELIT stands for National Institute of Electronics and Information Technology.",

"what is nielit": "NIELIT is an autonomous organization under the Ministry of Electronics and Information Technology, Government of India.",

"about nielit": "NIELIT provides education and training in electronics, information technology, and digital skills.",

"is nielit government": "Yes, NIELIT works under the Ministry of Electronics and Information Technology, Government of India.",

"is nielit a government institute": "Yes, NIELIT is a government organization under MeitY, Government of India.",

"government institute": "NIELIT is an autonomous body under the Government of India.",

#"nielit kokrajhar": "NIELIT Kokrajhar provides technical and professional IT education and training programs.",

"about nielit kokrajhar": "NIELIT Kokrajhar offers skill development and technical education courses for students.",

"where is nielit kokrajhar": "NIELIT Kokrajhar is located in Kokrajhar district of Assam.",

"location of nielit": "NIELIT Kokrajhar is situated in Assam, India.",

"nielit location": "NIELIT Kokrajhar is located in Kokrajhar, Assam.",

"what courses are available": "NIELIT offers courses related to AI, programming, networking, cybersecurity, electronics, and digital skills.",

"available courses": "Students can study AI, computer programming, networking, cybersecurity, and other IT courses at NIELIT.",

"computer courses": "NIELIT offers various computer and IT-related training programs.",

"ai": "AI courses include Artificial Intelligence basics, Machine Learning concepts, and Python programming.",

"python course": "Python courses teach programming fundamentals and software development skills.",

"networking course": "Networking courses teach communication systems, routers, switches, and internet technologies.",

"cyber security course": "Cyber Security courses focus on protecting systems, networks, and digital data.",

"skill development": "NIELIT focuses on technical skill development and digital education.",

"technical education": "NIELIT provides practical technical and computer education for students.",

"certificate course": "NIELIT provides certification courses in various technical and computer fields.",

"job oriented courses": "Many NIELIT courses are designed to improve practical and job-ready technical skills.",

"future scope": "Technical and AI-related skills have strong future career opportunities.",

"career opportunities": "NIELIT courses can help students build careers in IT and technology fields.",

"placement support": "Placement opportunities may depend on course type, skills, and institute programs.",

"student support": "NIELIT helps students through technical education, training, and skill development programs.",

"practical training": "Many NIELIT courses include practical and hands-on computer training.",

"computer lab": "Computer labs are used for practical learning and technical training.",

"offline classes": "Many courses provide classroom-based offline learning.",

"online classes": "Some courses may also be available in online learning mode.",

"class timing": "Class timings depend on the selected course and batch schedule.",

"exam system": "Examinations are conducted according to course guidelines and schedules.",

"course duration": "Course duration depends on the selected program and training level.",

"who can apply": "Eligibility depends on the course, but many programs are available for students after 10th or 12th.",

"after 10th": "Some NIELIT courses are available for students after completing 10th standard.",

"after 12th": "Many technical and professional courses are available after 12th standard.",

"beginners course": "NIELIT also offers beginner-friendly computer and IT courses.",

"advanced courses": "Advanced technical courses are available for higher-level learning and specialization.",

"digital skills": "Digital skills include computer knowledge, internet usage, programming, and technical problem solving.",

"why choose nielit": "NIELIT provides technical education, practical learning, and industry-relevant digital skills.",

"benefits of nielit": "NIELIT courses help students improve technical knowledge and career opportunities.",

"education center": "NIELIT is a recognized technical education and training organization.",

"national institute": "NIELIT is a national-level institute for electronics and information technology education.",
# =========================
# ADMISSION & APPLICATION
# =========================

#"admission": "Admissions are conducted through the official NIELIT admission process.Please check the official NIELIT website for the latest admission deadlines and important dates.",

"admission process": "The admission process usually includes registration, form submission, document verification, and fee payment.",

"how to apply": "Students can apply online through the official NIELIT admission portal.",

"application form": "Application forms are generally released during the admission session on the official website.",

"online registration": "Students must complete online registration before admission confirmation.",

"registration process": "The registration process includes filling personal details, uploading documents, and submitting the application.",

"apply online": "Students can apply online by visiting the official NIELIT website.",

"admission procedure": "The admission procedure includes application submission, verification, and enrollment.",

"how can i get admission": "Eligible students can apply through the official admission process announced by NIELIT.",

"steps for admission": "Students should register online, submit documents, and complete fee payment for admission.",

"eligibility": "Eligibility depends on the selected course and required educational qualification.",

"course eligibility": "Different courses have different eligibility criteria based on qualification and skill level.",

"who is eligible": "Students meeting the required educational qualification can apply for eligible courses.",

"required qualification": "Most courses require students to have completed 10th or 12th depending on the program.",

"can i apply after 10th": "Yes, some courses are available for students after completing 10th standard.",

"can i apply after 12th": "Yes, many technical and professional courses are available after 12th standard.",

"documents required": "Students generally need passport photo, Aadhaar card, educational certificates, and mark sheets.",

"required documents": "Common admission documents include ID proof, mark sheets, photographs, and certificates.",

"what documents are needed": "Students usually need educational certificates, identity proof, and passport photographs.",

"document verification": "Documents are verified during the admission process for eligibility confirmation.",

"photo upload": "Students may need to upload passport-size photographs during online registration.",

"aadhaar card": "Aadhaar card is commonly used as identity proof during admission.",

"marksheet": "Educational mark sheets are required during admission and verification.",

"fees": "Course fees depend on the selected course and training program.",

"course fee": "Different courses have different fee structures.",

"admission fee": "Admission fees vary depending on the selected program.",

"payment process": "Fees are usually paid through online or institute-approved payment methods.",

"online payment": "Online payment options may be available during admission registration.",

"last date": "Students should check the official NIELIT notification for admission deadlines.",

"admission deadline": "Admission deadlines are announced officially during each session.",

"important dates": "Important admission dates are released through official notifications.",

"admission notification": "Admission notifications are published officially by NIELIT.",

"new admission": "New admission announcements are released during the admission session.",

"admission open": "Students should check official notifications to know whether admissions are currently open.",

"entrance exam": "Some advanced courses may require entrance tests depending on the program.",

"selection process": "Selection depends on eligibility, document verification, and course requirements.",

"seat availability": "Admission may depend on seat availability in the selected course.",

"limited seats": "Some courses may have limited seats for admission.",

"reservation": "Reservation policies may apply according to government rules and institute guidelines.",

"scholarship": "Scholarship availability depends on eligibility and government schemes.",

"financial support": "Some students may receive support through scholarship or government schemes.",

"hostel admission": "Hostel facilities may be available depending on seat availability.",

"hostel facility": "Hostel availability depends on institute rules and accommodation capacity.",

"class start date": "Class schedules and starting dates are announced officially after admission.",

"batch timing": "Batch timing depends on the selected course and institute schedule.",

"student registration": "Students must complete registration before joining the course.",

"admission help": "Students can contact the institute office for detailed admission assistance.",

"contact office": "The institute office can provide official information related to admission and courses.",

"official website": "Students should visit the official NIELIT website for authentic updates and notifications.",

"where to apply": "Applications are generally submitted through the official online admission portal.",

"admission status": "Students should check official admission portals for application status updates.",

"confirmation": "Admission confirmation is usually provided after successful verification and payment.",

"cancel admission": "Admission cancellation policies depend on institute rules and guidelines.",

"refund policy": "Fee refund policies depend on institute rules and admission regulations.",

"admission support": "The institute provides guidance and support during the admission process.",

"student query": "Students can contact the institute for queries related to admission and courses.",

"help desk": "The help desk assists students with admission and registration-related questions.",

"when does admission start": "Admission schedules are announced officially before each academic session.",

"how many courses are available": "NIELIT offers multiple technical and professional courses in IT and electronics.",

"can beginners apply": "Yes, beginner-friendly courses are available for new students.",

"is admission online": "Many admission processes are conducted online through the official portal.",

"offline admission": "Some admission-related verification may be conducted offline at the institute.",
"who made you": "I was created by Bikash Basumatary during his AI course requirement project.",
"who created you": "i was created by Bikash Basumatary.",
"principle of nielit korajhar": "The HOD of nielit kokrajhar is Dr. Bipul Roy.",
"HOD": "The HOD of nielit kokrajhar is Dr. Bipul Roy.",



# greattings
"hello": "Hello! Welcome to NIELIT Kokrajhar Admission Assistant.",
"hi": "Hi! How may I assist you today?",
"hey": "Hey! Welcome to NIELIT Kokrajhar.",
"good morning": "Good morning! How can I help you regarding admissions?",
"good afternoon": "Good afternoon! Feel free to ask your admission queries.",
"good evening": "Good evening! Welcome to NIELIT Kokrajhar Admission Assistant.",
"how are you": "I am functioning properly and ready to assist students.",
"thank you": "You are welcome!",
"thanks": "Glad to help you.",
"good job": "Thank you for your feedback.",
"nice": "I appreciate your response.",
"bye": "Goodbye! Best wishes for your admission journey.",
"see you": "See you again! Feel free to return anytime.",
"good night": "Good night! Wishing you success in your studies.",
"who are you": "I am the NIELIT Kokrajhar Admission Assistant Chatbot.",
"can you help me": "Yes! I can help you with admissions, courses, fees, and student queries.",
"what can you do": "I can provide information related to admissions, eligibility, courses, and NIELIT Kokrajhar.",
"help": "Please ask your questions related to NIELIT admissions and courses.",
"welcome": "Welcome! How may I assist you today?",
"yo": "Hello! Welcome to NIELIT Kokrajhar Admission Assistant.",
"sup": "Hi! How can I help you today?",
"good to see you": "Thank you! I am here to assist students.",
"are you there": "Yes! I am available to help you.",
"anyone there": "Yes! NIELIT Kokrajhar Assistant is online.",
"hola": "Hello! Welcome to NIELIT Kokrajhar.",
"namaste": "Namaste! How may I assist you today?",
"good day": "Good day! Feel free to ask your admission-related questions.",


}


def chatbot_response(user_message):

    user_message = user_message.lower().strip()

    if user_message == "bye":
        return responses["bye"]

    # Keyword match
    for keyword in responses:
        if keyword in user_message:
            return responses[keyword]

    # Close match logic
    words = user_message.split()

    for word in words:

        close_match = get_close_matches(
            word,
            responses.keys(),
            n=1,
            cutoff=0.7
        )

        if close_match:
            return responses[close_match[0]]

    return "Sorry, I don't understand your question."


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():

    user_message = request.json.get("message")

    bot_reply = chatbot_response(user_message)

    return jsonify({
        "response": bot_reply
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)