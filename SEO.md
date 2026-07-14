# SEO Guidelines

## Current Implementation Status
- The application is a Single Page Application (SPA) built with React.
- Standard metadata (Title, Description) is currently static within the `index.html`.

## Best Practices & Future Improvements
To improve Search Engine Optimization for the Aurora Grand Hotel platform, the following practices should be implemented:

1. **Dynamic Meta Tags:**
   - Use libraries like `react-helmet-async` to dynamically update the `<title>` and `<meta name="description">` based on the current route.
   - For example, the Room Details page (`/rooms/:roomId`) should dynamically render the room name in the title (e.g., "Ocean View Suite | Aurora Grand").

2. **Semantic HTML:**
   - Ensure a clear hierarchy of headings (`<h1>` to `<h6>`). Each page should have exactly one `<h1>`.
   - Use semantic tags like `<article>`, `<section>`, `<nav>`, `<aside>`, and `<header>`.

3. **Open Graph & Twitter Cards:**
   - Add `<meta property="og:...">` tags to ensure beautiful link previews when sharing rooms on social media.

4. **Image Optimization:**
   - All images should have descriptive `alt` attributes.
   - Serve web-optimized image formats (WebP/AVIF) and implement lazy loading (which Vite/React can support).

5. **Server-Side Rendering (SSR) Consideration:**
   - Since standard React SPAs struggle slightly with deep SEO crawling, consider transitioning to a framework like Next.js in the future if organic search traffic for individual rooms becomes a top business priority. Currently, ensure Vite builds are performant and accessible.
