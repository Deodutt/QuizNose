<!-- TABLE OF CONTENTS -->
<h1 align="center">QuizNose</h1>

 <details style="display: inline-block" pen="open">
  <summary> Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">Project Description</a>
      <ul>
        <li><a href="#about-this-project">About this Project</a></li>
        <li><a href="#problems-this-application-solve">Problems this Application Solve</a></li>
        <li><a href="#current-version">Current Version</a></li>
        <li><a href="#high-level-system-design">High Level System Design</a></li>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li><a href="#getting-started">Getting Started</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#version-history">Version History</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>
<br/>

## About this Project

With QuizNose, you can smell the A+ from a mile away! QuizNose is an open source educational platform that allows for student teacher interaction with the goal to subject aptitude assessment for the modern classroom. Created with a microservice architecture, QuizNose can be scaled to meet consumer design. This will allow for higher volumes of traffic without worry of performance slow down as a monolithic application.

<br/>

## Problems this Application Solve

The application provides teachers insight on the performance of their students and has a granular view of the student’s understanding of a subject. By decoupling, we are able to ensure that the application is able to run smoothly and integrate any additional changes without drastically affecting other parts downstream.

<br/>

## High Level System Design

Image

<br/>

## Current Version

Stable version of QuizNose application that has unique user login, unique quiz sessions, and much more!

<br/>

## Built With

- [Python](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/en/2.0.x/)
- [HTML](https://www.w3schools.com/html/default.asp)
- [CSS](https://www.w3schools.com/css/default.asp)
- [JavaScript](https://www.javascript.com/)
- [Terraform](https://www.terraform.io/)
- [Docker](https://www.docker.com/)
- [GitHub Actions](https://github.com/features/actions)
  <br/><br/>

## Getting Started

To get a local copy up and running follow these simple steps.
<br/><br/>

1. Clone the repository and change directories into it

   ```sh
   git clone https://github.com/Deodutt/QuizNose
   cd QuizNose/application/
   ```

2. Create a virtual environment and activate it. (Windows command)

   ```sh
    (Windows command)
    py -m venv venv
    .\venv\Scripts\activate

    (Deactivate using the following)
    deactivate
   ```

   ```sh
    (Linux command)
    pip3 install virtualenv
    virtualenv quiznose
    source ./quiznose/bin/activate

    (Deactivate using the following)
    deactivate
   ```

3. Install the required application dependencies

   ```sh
   cd application
   pip install -r requirements.txt
   ```

4. Run the flask application

   ```sh
    (Windows command)
    $env:FLASK_APP = "app.py"
    flask run

    (Linux command)
    export FLASK_APP=app.py
    flask run
   ```

5. Go to the local callback IP on your browser
   ```sh
   http://127.0.0.1:5000/
   ```

<br/>

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork this Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request
   <br/><br/>

## Version History

- 1.0
  - Initial Release
    <br/><br/>

## Acknowledgements

- [Vivekkairi - Application Template to Startup](https://github.com/vivekkairi/quiz-app-flask)
- [Will Campbell - Advice / Troubleshooting](https://www.linkedin.com/in/will-campbell/)
- [Tyrone Sanderson - Advice / Troubleshooting](https://www.linkedin.com/in/tyronesanderson/)
- [Sai Ho Yip - Troubleshooting](https://www.linkedin.com/in/saihoyip/)
  <br/><br/>

## Contact

Ricardo Deodutt

[![Linkedin Badge](https://img.shields.io/badge/-Ricardo%20Deodutt-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/rixardo/)](https://www.linkedin.com/in/rixardo/) [![GitHub Badge](https://img.shields.io/badge/-Deodutt-black?style=flat-square&logo=GitHub&logoColor=white&link=https://www.github.com/Deodutt)](https://www.github.com/Deodutt) [![Twitter Badge](https://img.shields.io/badge/-@RixardoDe-1ca0f1?style=flat-square&labelColor=1ca0f1&logo=twitter&logoColor=white&link=https://www.twitter.com/RixardoDe)](https://www.twitter.com/RixardoDe)
<br/>

Kenneth Tan

[![Linkedin Badge](https://img.shields.io/badge/-Kenneth%20Tan-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/kenneth-tan-824407125/)](https://www.linkedin.com/in/kenneth-tan-824407125/) [![GitHub Badge](https://img.shields.io/badge/-KennethT404-black?style=flat-square&logo=GitHub&logoColor=white&link=https://github.com/KennethT404)](https://github.com/KennethT404)
<br/>

Kawang Wong

[![Linkedin Badge](https://img.shields.io/badge/-Kawang%20Wong-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/kawang-wong/)](https://www.linkedin.com/in/kawang-wong/) [![GitHub Badge](https://img.shields.io/badge/-kawangwong-black?style=flat-square&logo=GitHub&logoColor=white&link=https://github.com/kawangwong)](https://github.com/kawangwong)
<br/>

Dilobar Irisova

[![Linkedin Badge](https://img.shields.io/badge/-Dilobar%20Irisova-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/dilobar-irisova-547033216/)](https://www.linkedin.com/in/dilobar-irisova-547033216/) [![GitHub Badge](https://img.shields.io/badge/-DIrisova-black?style=flat-square&logo=GitHub&logoColor=white&link=https://github.com/DIrisova)](https://github.com/DIrisova)
