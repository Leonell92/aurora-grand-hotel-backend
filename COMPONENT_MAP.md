# Component Map

## Frontend Routes & Pages (`src/pages`)
- `/` -> `Index.tsx` (Home Page)
- `/rooms` -> `RoomsPage.tsx` (List of available rooms)
- `/rooms/:roomId` -> `RoomDetailsPage.tsx` (Detailed view of a specific room)
- `/booking` -> `BookingPage.tsx` (Booking workflow and form)
- `/bookings` -> `BookingsPage.tsx` (User's booking history)
- `/about` -> `AboutPage.tsx`
- `/contact` -> `ContactPage.tsx`
- `/login` -> `LoginPage.tsx`
- `/signup` -> `SignupPage.tsx`
- `/forgot-password` -> `ForgotPasswordPage.tsx`
- `/admin` -> `AdminDashboard.tsx`
- `/*` -> `NotFound.tsx`

## Frontend Reusable Components (`src/components`)
- **Layout:** `Header.tsx`, `Footer.tsx`, `Layout.tsx`
- **Home:** `HeroSection.tsx`, `FeaturedRooms.tsx`, `AmenitiesSection.tsx`, `AmenitiesSlideshow.tsx`, `TestimonialsSection.tsx`, `BookingWidget.tsx`
- **UI Primitives:** Contains standard Shadcn UI components (buttons, dialogs, inputs, toasts).

## Backend Endpoints (`hotel_backend`)
All API endpoints are prefixed with `/api/`.

### Auth Endpoints
- `POST /api/auth/register/` - Register a new user.
- `POST /api/auth/login/` - Authenticate and create a session.
- `POST /api/auth/logout/` - Destroy session.
- `GET /api/auth/status/` - Check current authentication status.

### Resources
- `GET /api/rooms/` - List rooms.
- `GET /api/rooms/{id}/` - Retrieve room details.
- `GET /api/room-features/` - List available room amenities.
- `GET /api/bookings/` - List user's bookings (admin sees all).
- `POST /api/bookings/` - Create a new booking.
