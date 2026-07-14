# AI Bootstrap

## Introduction
Welcome to the Lovable Hotel Platform (Aurora Grand Hotel). This document provides essential context for AI assistants to understand the project structure, coding conventions, and workflows before making any modifications.

## Understanding the Repository
This is a monorepo containing:
1. **Frontend:** React + Vite + TypeScript application in `lovable-hotel-frontend/aurora-grand-frontend-main`.
2. **Backend:** Django + DRF application in `hotel_backend`.

**Read the Documentation:** 
Before proposing architectural changes, please review:
- `ARCHITECTURE.md`
- `PROJECT_CONTEXT.md`
- `TECH_STACK.md`
- `COMPONENT_MAP.md`

## Coding Conventions

### Frontend (React/TypeScript)
- **Functional & Typed:** Use functional components and strictly type props/state with TypeScript interfaces.
- **Styling:** Use Tailwind CSS utility classes. DO NOT write raw CSS unless absolutely necessary.
- **Components:** Place reusable UI elements in `src/components/ui/` (Shadcn style). Create feature-specific folders within `src/components/` (e.g., `layout/`, `home/`).
- **State:** Use `React Query` (`@tanstack/react-query`) for all server state (API fetching). Avoid Redux/Context for server state.
- **Imports:** Use absolute path aliases (`@/components/...`) where configured.

### Backend (Django/Python)
- **RESTful Design:** Use Django REST Framework `ViewSets` and `ModelSerializers`.
- **Naming:** `snake_case` for variables, functions, and database columns. `PascalCase` for classes (Models, Views, Serializers).
- **Authentication:** The project uses Session Authentication. Ensure `CORS_ALLOW_CREDENTIALS = True` is respected.
- **Environment Variables:** Do not hardcode secrets. Use `python-decouple` (`config()`) to fetch environment variables.

## Workflow for AI Assistants
1. **Analyze First:** Use `list_dir` and `view_file` to inspect the target files before modifying.
2. **Check Dependencies:** Verify if a requested library already exists in `package.json` or `requirements.txt` before adding it.
3. **Use Specific Tools:** Prioritize `replace_file_content` or `multi_replace_file_content` for edits. Avoid running raw `sed` or `echo` via terminal commands for file modification.
4. **Preserve Integrity:** Maintain existing comments, docstrings, and overall code structure.
5. **Aesthetics:** For frontend changes, adhere to the `UI_GUIDELINES.md` to ensure a premium, modern design.

## Final Note
Your primary goal is to write clean, maintainable, and bug-free code that aligns with the established architecture and design system. Always double-check your syntax and logic before committing changes.
