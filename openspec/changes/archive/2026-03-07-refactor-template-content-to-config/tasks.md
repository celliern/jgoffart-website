## 1. Config Setup

- [x] 1.1 Add profile data to config.toml extra section (name, position, university, university_url, email, avatar)
- [x] 1.2 Add social links array to config.toml extra section (Google Scholar, CV, LinkedIn)
- [x] 1.3 Verify config.toml structure is valid TOML

## 2. Content Migration

- [x] 2.1 Update content/_index.md with proper frontmatter and about me section
- [x] 2.2 Add research interests list to content/_index.md
- [x] 2.3 Verify content/working-papers.md has proper frontmatter and content
- [x] 2.4 Verify content/other.md has proper frontmatter and content

## 3. Base Template Update

- [x] 3.1 Update templates/base.html with dark mode class strategy in Tailwind config
- [x] 3.2 Add prefers-color-scheme detection script to base.html
- [x] 3.3 Remove style.css link from base.html head
- [x] 3.4 Update body wrapper to use Tailwind flex container classes

## 4. Index Template Refactoring - Profile Section

- [x] 4.1 Replace hardcoded name with config.extra.name in header
- [x] 4.2 Replace hardcoded position with config.extra.position
- [x] 4.3 Replace hardcoded university link with config.extra.university and config.extra.university_url
- [x] 4.4 Replace hardcoded email with config.extra.email
- [x] 4.5 Replace hardcoded avatar path with config.extra.avatar
- [x] 4.6 Replace hardcoded social icons with loop over config.extra.social array
- [x] 4.7 Convert position element from custom <position> to semantic <span>
- [x] 4.8 Convert email element from custom <email> to semantic <span> or <a>

## 5. Index Template Refactoring - Content Sections

- [x] 5.1 Replace hardcoded About me section with content from section.content
- [x] 5.2 Replace hardcoded Research Interests section with content from section.content
- [x] 5.3 Replace hardcoded Working Papers section with content from get_page(path="working-papers.md")
- [x] 5.4 Replace hardcoded Other section with content from get_page(path="other.md")

## 6. Tailwind Styling - Layout

- [x] 6.1 Apply Tailwind flex container classes to wrapper div (flex, flex-col, lg:flex-row, max-w-6xl, mx-auto)
- [x] 6.2 Apply Tailwind sidebar classes to header (w-full, lg:w-60, lg:fixed, text-center, pt-16)
- [x] 6.3 Apply Tailwind main content classes to section (flex-1, lg:ml-60, pt-16, pb-12)
- [x] 6.4 Apply Tailwind footer classes (w-full, lg:w-60, text-center)

## 7. Tailwind Styling - Typography and Colors

- [x] 7.1 Apply Tailwind typography classes to h1 name (text-3xl, font-medium, text-slate-800, dark:text-sky-400)
- [x] 7.2 Apply Tailwind typography classes to position (text-lg, text-gray-600, dark:text-gray-400)
- [x] 7.3 Apply Tailwind typography classes to email (text-sm, font-mono, text-gray-600)
- [x] 7.4 Apply Tailwind link color classes (text-sky-500, hover:text-sky-600)
- [x] 7.5 Apply Tailwind section heading classes (text-2xl, font-medium, text-slate-800, dark:text-sky-400)
- [x] 7.6 Apply Tailwind body text classes (text-base, leading-relaxed, text-gray-600, dark:text-gray-300)

## 8. Tailwind Styling - Components

- [x] 8.1 Apply Tailwind avatar classes (rounded-full, w-32, mb-4, mx-auto)
- [x] 8.2 Apply Tailwind social icons container classes (flex, justify-center, gap-4, mt-4)
- [x] 8.3 Apply Tailwind social icon link classes (inline-flex, items-center, justify-center, w-10, h-10, rounded-full, hover:bg-gray-200, dark:hover:bg-gray-800)
- [x] 8.4 Apply Tailwind social icon classes (text-slate-800, dark:text-sky-400, text-xl)
- [x] 8.5 Apply Tailwind publications list classes (space-y-6)
- [x] 8.6 Apply Tailwind publication item classes (flex, flex-col, sm:flex-row, gap-4, border-b, border-gray-200, dark:border-gray-700, pb-6)
- [x] 8.7 Apply Tailwind publication image classes (w-full, sm:w-32, flex-shrink-0)
- [x] 8.8 Apply Tailwind publication content classes (flex-1)
- [x] 8.9 Apply Tailwind publication title classes (font-semibold, text-slate-800, dark:text-gray-100)
- [x] 8.10 Apply Tailwind publication metadata classes (text-sm, text-gray-600, dark:text-gray-400)

## 9. Style Cleanup

- [x] 9.1 Delete static/style.css file
- [x] 9.2 Verify no 404 errors for removed style.css
- [x] 9.3 Check for any remaining references to style.css classes in templates

## 10. Verification

- [x] 10.1 Run zola serve and verify site loads without errors
- [x] 10.2 Verify profile information displays correctly from config
- [x] 10.3 Verify content sections render from markdown
- [x] 10.4 Verify social icons display and link correctly
- [x] 10.5 Verify publications list displays correctly
- [x] 10.6 Test responsive layout at desktop (1024px+)
- [x] 10.7 Test responsive layout at tablet (768px-1023px)
- [x] 10.8 Test responsive layout at mobile (<768px)
- [x] 10.9 Test dark mode appearance (using browser dev tools prefers-color-scheme)
- [x] 10.10 Test light mode appearance
- [x] 10.11 Verify all links work (university, social, publication links)
- [x] 10.12 Verify typography is readable and matches original aesthetic
