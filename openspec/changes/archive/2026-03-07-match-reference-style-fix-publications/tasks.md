## 1. Content Structure Setup

- [x] 1.1 Create content/working-papers/ directory
- [x] 1.2 Create content/working-papers/_index.md with proper frontmatter
- [x] 1.3 Create content/work-in-progress/ directory
- [x] 1.4 Create content/work-in-progress/_index.md with proper frontmatter
- [x] 1.5 Verify content/publications/ section has proper structure

## 2. Content Migration

- [x] 2.1 Move working papers from content/working-papers.md to individual files in content/working-papers/
- [x] 2.2 Add badge field to working paper frontmatter (badge = "WP")
- [x] 2.3 Add images to working papers if available (no images available, skipped)
- [x] 2.4 Update content/_index.md to remove working papers content (now in separate section)

## 3. Template Updates - Publication Grid Layout

- [x] 3.1 Update templates/index.html publications loop to use grid layout
- [x] 3.2 Add conditional logic: if page.extra.image or page.extra.badge, use 3/9 grid
- [x] 3.3 Implement 3-column section for image/badge (col-span-3)
- [x] 3.4 Implement 9-column section for content (col-span-9)
- [x] 3.5 Handle full-width case when no image or badge (col-span-12 or no grid)
- [x] 3.6 Add responsive classes for mobile (stack on small screens)

## 4. Template Updates - Badge Support

- [x] 4.1 Add badge rendering logic in publication item template
- [x] 4.2 Create badge HTML structure (abbr or span with badge class)
- [x] 4.3 Apply Tailwind badge styling (background, text color, padding, border-radius)
- [x] 4.4 Position badge correctly (in image column, above or overlaying image)

## 5. Template Updates - Autocolor Support

- [x] 5.1 Add autocolor CSS class using Tailwind (text-slate-800 dark:text-gray-300)
- [x] 5.2 Apply autocolor class to university link
- [x] 5.3 Apply autocolor class to publication title links
- [x] 5.4 Apply autocolor class to other appropriate links in content

## 6. Template Updates - Section Separation

- [x] 6.1 Add Working Papers section rendering from content/working-papers/ section
- [x] 6.2 Add Work in Progress section rendering from content/work-in-progress/ section
- [x] 6.3 Keep existing Publications section rendering from content/publications/
- [x] 6.4 Ensure sections render in correct order (Working Papers, Work in Progress, Publications)

## 7. Styling and CSS

- [x] 7.1 Add badge styling classes to Tailwind (or inline styles)
- [x] 7.2 Verify autocolor class works in both light and dark modes
- [x] 7.3 Test publication grid spacing and alignment
- [x] 7.4 Add gap between grid columns (gap-4 or similar)

## 8. Responsive Design

- [x] 8.1 Test grid layout on desktop (1024px+)
- [x] 8.2 Test stacked layout on tablet (768px - 1023px)
- [x] 8.3 Test stacked layout on mobile (<768px)
- [x] 8.4 Verify images scale properly on all screen sizes

## 9. Dark Mode Testing

- [x] 9.1 Test autocolor classes in light mode
- [x] 9.2 Test autocolor classes in dark mode
- [x] 9.3 Test badge visibility in both modes
- [x] 9.4 Verify all text is readable in both modes

## 10. Verification and Testing

- [x] 10.1 Run zola serve and verify site builds without errors
- [x] 10.2 Verify publications with images show 3/9 grid layout
- [x] 10.3 Verify publications without images span full width
- [x] 10.4 Verify publications with badges show badge in image column
- [x] 10.5 Verify Working Papers section renders correctly
- [x] 10.6 Verify Work in Progress section renders correctly
- [x] 10.7 Verify Publications section still works correctly
- [x] 10.8 Test all links (university, social, publication links)
- [x] 10.9 Verify responsive behavior on all breakpoints
- [x] 10.10 Test dark mode appearance
- [x] 10.11 Compare layout with reference site (chloezapha.com)
- [x] 10.12 Verify no empty space remains for publications without images
