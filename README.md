# Spreact

Easy to use scipt-utility for creating a Spring Boot Backend + ReactJS Frontend Application

## Prerequisites

The folling programs need to be available on the ENV PATH.

- yarn
- npm >= 5.2.0
- Gradle or Maven (depending on your build automation tool)

## Steps to Generate Project

1. Clone repo
2. Run `pip install -r requirements.txt`
3. Run `python spreact.py`
4. Fill out Project Details
5. Done!

**Note: When installing the ReactJS app, we add a `proxy: {"http://localhost:8080"}` property to the project's `package.json` file so that any requests not mapped to `/` are redirected to the Spring Boot API. This avoids CORS related issues amongst other things.**
