# Architecture

## High-Level Architecture
The project follows a decoupled Client-Server architecture:
- **Client (Frontend):** A Single Page Application (SPA) built with React, served via Vite, and deployed on Vercel.
- **Server (Backend):** A RESTful API built with Django REST Framework, deployed on environments like Railway/Render.

## Communication
- The frontend communicates with the backend via HTTPS REST API calls.
- `Axios` is used for API requests, configured to include credentials (cookies) for session-based authentication.
- `React Query` handles data fetching, caching, synchronization, and optimistic UI updates on the frontend.

## Data Flow
1. User interacts with the UI.
2. React components dispatch queries/mutations via React Query.
3. Axios sends HTTP requests to Django API endpoints.
4. Django authenticates the request via Session cookies.
5. Django ViewSets interact with Models to query/update PostgreSQL/SQLite database.
6. JSON response is returned and React UI updates reactively.

## Folder Structure

### Backend (`/hotel_backend`)
- `hotel_backend/` - Core Django settings, URLs, and WSGI/ASGI configurations.
- `bookings/` - Django app for booking models, views, and authentication endpoints.
- `rooms/` - Django app for room models, features, and corresponding API endpoints.
- `db.sqlite3` - Local development database.

### Frontend (`/lovable-hotel-frontend/aurora-grand-frontend-main`)
- `src/api/` - Axios configurations and API service functions.
- `src/components/` - Reusable UI components (Home, Layout, UI primitives).
- `src/pages/` - Top-level route components representing full pages.
- `src/hooks/` - Custom React hooks.
- `src/lib/` - Utility functions and helpers.
