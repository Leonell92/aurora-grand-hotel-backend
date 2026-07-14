# Tech Stack

## Frontend
- **Framework:** React 18 (Functional components, hooks)
- **Build Tool:** Vite (Fast, optimized build process)
- **Language:** TypeScript (Type safety, interfaces for API models)
- **Routing:** React Router DOM v6
- **State Management & Data Fetching:** TanStack React Query v5 (Caching, synchronization), Axios
- **Styling:** Tailwind CSS (Utility classes)
- **Component Library:** Shadcn UI (Accessible Radix UI primitives + Tailwind styling)
- **Icons:** Lucide React
- **Forms:** React Hook Form + Zod (Validation)
- **Date Handling:** Date-fns, React Day Picker

## Backend
- **Framework:** Django 6.0
- **API Framework:** Django REST Framework (DRF) 3.15
- **Database:** PostgreSQL (Production), SQLite (Development)
- **Authentication:** Custom Session-based authentication via DRF (Cookies)
- **Environment Management:** python-decouple (for `.env` management)
- **Static Files:** WhiteNoise (Serving static files efficiently in production)
- **CORS:** django-cors-headers

## Deployment & Hosting
- **Frontend Hosting:** Vercel (Configured via `vercel.json` and CORS settings in backend)
- **Backend Hosting:** Railway / Render (Configured via `nixpacks.toml`, `railway.json`, `Procfile`)
