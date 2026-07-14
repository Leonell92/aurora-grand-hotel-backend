# UI Guidelines

## Design System
The frontend design system is powered by **Tailwind CSS** and **Shadcn UI**. 
- **Tailwind CSS:** Provides utility-first classes for rapid UI development without writing custom CSS.
- **Shadcn UI:** A collection of re-usable components built with Radix UI and Tailwind CSS. It is NOT a component library, but rather a set of beautifully designed, accessible components that are copied directly into the project (`src/components/ui`).

## Core Principles
1. **Premium Aesthetic:** Use ample whitespace, elegant typography, and subtle animations (via `tailwindcss-animate` and `framer-motion` if added, or pure CSS).
2. **Accessibility (a11y):** Radix UI primitives ensure components are accessible by default (ARIA attributes, keyboard navigation).
3. **Responsive Design:** Mobile-first approach. All components must look great on mobile and scale gracefully to desktop.

## Styling Rules
- **Avoid Custom CSS:** Rely on Tailwind utility classes. Use `src/index.css` only for global resets or `@apply` directives for highly repeated complex patterns.
- **Component States:** Always style `hover:`, `focus:`, `active:`, and `disabled:` states to provide immediate visual feedback.
- **Dark Mode:** Support light and dark modes utilizing the `next-themes` integration. Tailwind classes should utilize the `dark:` variant appropriately.

## Icons
Use **Lucide React** (`lucide-react`) for all iconography to maintain consistency.

## Interaction
- Implement smooth transitions using Tailwind's `transition` utilities.
- Use `sonner` and `@radix-ui/react-toast` for user notifications and feedback.
