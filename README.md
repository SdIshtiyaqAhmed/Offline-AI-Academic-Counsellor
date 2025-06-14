# Offline AI Academic Counsellor

## AI Suggestions to Support Students in Academics

---

## Table of Contents
* [Introduction](#introduction)
* [Features](#features)
* [Key Advantages: Privacy & Accessibility](#key-advantages-privacy--accessibility)
* [Technology Stack](#technology-stack)
* [Getting Started](#getting-started)
    * [Prerequisites](#prerequisites)
    * [Installation](#installation)
    * [Preparing Data Files](#preparing-data-files)
* [Usage](#usage)
* [Screenshots](#screenshots)
* [Future Enhancements](#future-enhancements)
* [Contributing](#contributing)

---

# Introduction

The **Offline AI Academic Counsellor** project directly addresses a critical deficiency in contemporary education: the widespread lack of personalized guidance tailored to individual student interests, skills, and challenges. Traditional, standardized teaching models often fall short in providing the unique support each student needs to truly thrive. This system offers an innovative solution by leveraging Artificial Intelligence to deliver highly personalized academic support right on the student's device.

Unlike generalized AI tools or conventional methods, this system is engineered to develop a comprehensive understanding of each student as a learner. It analyzes individual data, including academic performance (derived from quizzes), demonstrated skills, and stated interests, to provide relevant, contextualized, and actionable suggestions. By moving beyond a one-size-fits-all approach, the project aims to make learning more engaging, effective, and deeply aligned with what genuinely motivates each student.

## Features

The **Offline AI Academic Counsellor** offers a robust set of features designed to empower students on their academic journey:

* **Personalized Academic Suggestions:** Provides tailored guidance and recommendations based on the student's unique profile, including interests, skills, and academic performance.
* **Interactive AI Chatbot:** Serves as a non-judgmental academic counselor capable of:
    * Assisting with understanding complex concepts.
    * Solving problems across various subjects.
    * Offering effective study strategies.
    * Providing programming assistance (e.g., code explanations, examples).
    * Delivering motivational support.
* **Quiz-Based Assessment:** Includes a structured quiz functionality to gather valuable data on a student's skills, interests, and academic understanding, which directly informs personalization.
* **Career Guidance:** Offers personalized career suggestions aligned with the student's academic profile and identified interests.
* **Local Data Storage:** Ensures all student data is stored locally on the user's machine, enhancing privacy and security.
* **Intuitive Web-Based User Interface:** Provides a familiar and easy-to-use platform for interaction via a local web browser.

## Key Advantages: Privacy & Accessibility

The **Offline AI Academic Counsellor** project stands out due to its core commitments to user privacy and accessibility:

* **Uncompromised Privacy & Data Security:** Recognizing the sensitive nature of student data, the system operates entirely locally. Both the student's personal information and the AI model reside exclusively on the user's device. This decentralized design eliminates the risks associated with cloud-based data storage and external data transmission, ensuring student academic information remains under their direct control and mitigating concerns about unauthorized access or misuse.
* **Enhanced Accessibility & Cost-Effectiveness:** Unlike many large-scale AI models that demand significant computational resources and often incur high subscription costs, this project utilizes a pre-trained, relatively smaller Language Model (specifically **SmolLM2-360M-Instruct**). This model is capable of running efficiently on standard modern hardware, drastically lowering the barrier to entry. This strategic choice makes personalized AI academic support accessible and cost-effective for a broad range of students, eliminating the need for high-end computers or recurring payments.
* **Offline Capability:** A significant benefit of its local operation, the core AI functionality remains accessible even without a persistent internet connection after the initial setup, ensuring continuous support.

## Technology Stack

The project is built upon a robust and efficient technology stack:

* **Python:** The core programming language for the application logic.
* **Flask:** A lightweight Python web framework used to serve the web-based user interface locally.
* **Hugging Face Transformers:** Utilized for integrating and running the pre-trained Language Model (SmolLM2-360M-Instruct) for AI capabilities.
* **Pandas:** Likely used for efficient handling and processing of structured data, such as quiz questions from `questions.xlsx`.
* **Local File System:** Employed for secure, privacy-preserving storage of student records (e.g., `student_records.jsonl`) and quiz data.

## Getting Started

Follow these steps to get the **Offline AI Academic Counsellor** up and running on your local machine.

### Prerequisites

* **Python 3.x:** Ensure you have Python 3.8 or higher installed. You can download it from [python.org](https://www.python.org/).
* **pip:** Python's package installer, usually comes with Python.

### Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/offline-ai-academic-counsellor.git](https://github.com/your-username/offline-ai-academic-counsellor.git) # Replace with your actual repo URL
    cd offline-ai-academic-counsellor # Navigate into the project directory
    ```
2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    ```
3.  **Activate the virtual environment:**
    * **On Windows:**
        ```bash
        .\venv\Scripts\activate
        ```
    * **On macOS/Linux:**
        ```bash
        source venv/bin/activate
        ```
4.  **Install dependencies:**
    Create a `requirements.txt` file in your project root with the following contents:
    ```
    Flask
    transformers
    torch # or tensorflow, depending on your preferred backend for transformers
    pandas
    openpyxl # Required for reading/writing .xlsx files
    ```
    Then install them:
    ```bash
    pip install -r requirements.txt
    ```
    *(Note: The `transformers` library will automatically download the `SmolLM2-360M-Instruct` model the first time it is loaded, requiring an internet connection during the initial run.)*

### Preparing Data Files

* **`questions.xlsx`:** Ensure you have a file named `questions.xlsx` in the root directory of your project. This file should contain the quiz questions in a structured format that `chatModel.py` expects.

## Usage

1.  **Run the Flask application:**
    Open your terminal or command prompt in the project's root directory (where `chatModel.py` is located) and run:
    ```bash
    python chatModel.py
    ```
    The console will display a message indicating the server is running, usually at `http://127.0.0.1:5000/`.

2.  **Access the web interface:**
    Open your web browser and navigate to the address provided in the console (e.g., `http://127.0.0.1:5000/`).

3.  **Interact with the system:**
    * The home page will offer options to "Start Quiz" or "Try Our AI Counselor."
    * It's recommended to start with the quiz to provide data for a more personalized experience.
    * After the quiz, or directly, you can interact with the AI counselor via the chat interface for personalized academic guidance.

## Screenshots

Below are visual representations of the **Offline AI Academic Counsellor**'s user interface, showcasing key interaction points and design.

### Home / Dashboard Interface

![image](https://github.com/user-attachments/assets/3d643c35-509d-45eb-bf9d-8ca339017550)

This screenshot displays the main entry point of the application, featuring a clean, card-based layout that guides users to the core functionalities: taking a quiz for personalization and engaging with the AI counselor.

### Academic Counselor Chatbot Interface

![image](https://github.com/user-attachments/assets/e6d4d09c-678b-474f-8b93-9fd58ae8a190)

This image illustrates the primary chat window where users interact with the AI. It shows typical conversation flow, diverse query handling, and the AI's detailed, structured responses.

### Quiz Question Interface

![image](https://github.com/user-attachments/assets/5ed9ac3a-f571-46a5-a519-32b88fbad018)

This screenshot demonstrates the interactive quiz component, showing a question presented with multiple-choice options and a visible timer, indicating the system's method for assessing student knowledge and interests.

## Future Enhancements

The **Offline AI Academic Counsellor** has significant potential for future development to expand its capabilities and impact:

* **Expanded Data Integration:** Incorporate more diverse student data sources (e.g., manual grade input, other educational activity data).
* **Advanced AI Capabilities:** Implement sophisticated AI for deeper interest/skill analysis, content generation (practice problems, study plans), and sentiment analysis during interactions.
* **Enhanced User Interface & Experience:** Develop more comprehensive dashboards for progress visualization, interactive elements within suggestions, and improved quiz interfaces.
* **Robust Data Management:** Transition to a more robust local database (e.g., SQLite) for better management of historical student records and data integrity.
* **Extended Content & Resource Integration:** Integrate with Open Educational Resources (OERs) or allow user-provided learning materials.
* **Offline Capabilities Enhancement:** Explore ways to make more functionalities fully available offline.

## Contributing

Contributions are highly welcome! If you'd like to contribute, please follow these steps:

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix (`git checkout -b feature/your-feature-name`).
3.  Make your changes and ensure your code adheres to the project's style guidelines.
4.  Write clear, concise commit messages.
5.  Push your changes to your forked repository.
6.  Open a Pull Request to the `main` branch of the original repository, describing your changes
