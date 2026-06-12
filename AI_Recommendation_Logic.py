print("==================================")
print("AI Recommendation Logic")
print("==================================")
print("Type 'exit','quit', or' bye' to end the program.")
recommendations = {
    "ai": [
        "Machine Learning",
        "Deep Learning",
        "Computer Vision",
        "Natural Language Processing",
    ],

    "data_science": [
        "Data Analysis",
        "Data Visualization",
        "Statistics",
        "Python for Data Science",
    ],

    "web development":[
        "CSS",
        "HTML",
        "React",
        "JavaScript",
    ],

    "cyber security":[
        "Network Secuurity",
        "Ethical Hacking",
        "Penetration Testing",
        "Digital Forensics",
    ],

    "cloud computing":[
        "AWS",
        "Microsoft Azure",
        "Google Cloud",
        "ChildProcessError",
    ]
}
while True:
    user_interest = input("Enter your interest (AI, Data Science, Web Development, Cyber Security, Cloud Computing):").lower().strip()
    if user_interest in ["exit", "quit", "bye"]:
        print("\nThank you for using the AI Recommendation System.")
        print("Goodbye!")
        break

    elif user_interest in recommendations:
        print("\nRecommended Courses:")
        for course in recommendations[user_interest]:
            print("-",course)
    else:
        print("\nSorry, No recommendations found for that interest.")
        print("Please Choose from: AI, Data Science, Web Development, Cyber Security, Cloud Computing.")
