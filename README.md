# Lovable Hotel Platform

## Overview
Lovable Hotel Platform is a modern, responsive full-stack web application designed for a luxury hotel (Aurora Grand Hotel). It allows users to browse rooms, make bookings, manage their profiles, and provides an administrative interface for hotel staff.

## Project Structure
The repository is structured as a monorepo containing both the frontend and backend applications:
- `/hotel_backend` - Django REST Framework backend application
- `/lovable-hotel-frontend/aurora-grand-frontend-main` - Vite + React frontend application

## Features
- **User Authentication:** Secure signup, login, and session management.
- **Room Management:** Detailed room browsing with features, amenities, and dynamic pricing.
- **Booking System:** Seamless reservation workflow.
- **Admin Dashboard:** Centralized control for managing hotel operations.
- **Modern UI:** Built with Tailwind CSS and Shadcn UI components for a premium user experience.

## Getting Started

### Prerequisites
- Node.js (v18+)
- Python (3.10+)
- PostgreSQL (or SQLite for local development)

### Backend Setup
1. Navigate to `hotel_backend`.
2. Create a virtual environment: `python -m venv venv`
3. Activate the virtual environment.
4. Install dependencies: `pip install -r requirements.txt`
5. Apply migrations: `python manage.py migrate`
6. Run the server: `python manage.py runserver`

### Frontend Setup
1. Navigate to `lovable-hotel-frontend/aurora-grand-frontend-main`.
2. Install dependencies: `npm install`
3. Start the development server: `npm run dev`

## Documentation
Please refer to the following documentation files for more in-depth information:
- [PROJECT_CONTEXT.md](./PROJECT_CONTEXT.md)
- [ARCHITECTURE.md](./ARCHITECTURE.md)
- [TECH_STACK.md](./TECH_STACK.md)
- [COMPONENT_MAP.md](./COMPONENT_MAP.md)
- [UI_GUIDELINES.md](./UI_GUIDELINES.md)
- [AI_BOOTSTRAP.md](./AI_BOOTSTRAP.md)
