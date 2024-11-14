def main():
    print("Welcome to the Cybersecurity Career Advisor Chatbot!")
    print("Please select a role you're interested in:")
    print("1. SOC Analyst")
    print("2. Penetration Tester")
    print("3. Cybersecurity Assessor (ISSO)")

    role = input("Enter the number corresponding to the role: ")
    
    if role == "1":
        soc_analyst_recommendations()
    elif role == "2":
        penetration_tester_recommendations()
    elif role == "3":
        cybersecurity_assessor_recommendations()
    else:
        print("Invalid input. Please select 1, 2, or 3.")

def soc_analyst_recommendations():
    print("\nFor SOC Analyst, here are some recommended certifications and skills:")
    print("Certifications:")
    print("- CompTIA Security+")
    print("- Certified SOC Analyst (CSA)")
    print("- CompTIA Cybersecurity Analyst (CySA+)")
    print("- GIAC Certified Intrusion Analyst (GCIA)")
    print("\nSkills:")
    print("- Threat analysis and monitoring")
    print("- Incident response and detection")
    print("- Log analysis and SIEM tools (e.g., Splunk, QRadar)")
    print("- Network protocols and firewall management\n")

def penetration_tester_recommendations():
    print("\nFor Penetration Tester, here are some recommended certifications and skills:")
    print("Certifications:")
    print("- Certified Ethical Hacker (CEH)")
    print("- Offensive Security Certified Professional (OSCP)")
    print("- GIAC Penetration Tester (GPEN)")
    print("- CompTIA PenTest+")
    print("\nSkills:")
    print("- Vulnerability assessment and exploitation")
    print("- Networking, scripting, and programming (Python, Bash)")
    print("- Familiarity with pentesting tools (e.g., Metasploit, Burp Suite)")
    print("- Knowledge of OS internals (Windows, Linux)\n")

def cybersecurity_assessor_recommendations():
    print("\nFor Cybersecurity Assessor (ISSO), here are some recommended certifications and skills:")
    print("Certifications:")
    print("- Certified Information Systems Security Professional (CISSP)")
    print("- Certified Information Security Manager (CISM)")
    print("- Certified Authorization Professional (CAP)")
    print("- Certified Information Systems Auditor (CISA)")
    print("\nSkills:")
    print("- Risk management and assessment")
    print("- Knowledge of security frameworks (NIST RMF, FISMA, ISO 27001)")
    print("- Policy and compliance analysis")
    print("- Audit and assessment techniques\n")

# Run the chatbot
if __name__ == "__main__":
    main()
