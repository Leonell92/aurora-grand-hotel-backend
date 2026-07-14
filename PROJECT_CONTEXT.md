# Project Context

## Purpose
The Lovable Hotel Platform (Aurora Grand Hotel) aims to provide a seamless, premium digital experience for guests booking luxury hotel accommodations. It aims to bridge the gap between high-end hospitality and modern digital convenience.

## Domain Model
The core domain revolves around the following entities:
1. **User (Guest & Admin):** Represents individuals interacting with the platform. Guests can book rooms, while Admins manage the platform.
2. **Room:** Represents a physical hotel room. Properties include type, price, description, images, capacity, and current availability status.
3. **Room Feature (Amenities):** Specific features attached to a room (e.g., "Ocean View", "King Size Bed", "Wi-Fi").
4. **Booking:** A reservation made by a User for a specific Room over a specified date range.

## Business Logic Highlights
- **Dynamic Availability:** Rooms must not be double-booked for intersecting date ranges.
- **Pricing:** Room prices may be dynamically managed, with potential seasonal adjustments.
- **Authentication:** Sessions are managed via Django cookies. Cross-Origin Resource Sharing (CORS) is configured strictly to allow communication only from recognized frontend origins.

## Target Audience
- Guests seeking luxury accommodations who expect a smooth, fast, and responsive digital booking process.
- Hotel management personnel who need a reliable and intuitive dashboard to oversee operations.
