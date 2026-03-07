## ADDED Requirements

### Requirement: All styles use Tailwind utility classes
The system SHALL replace all custom CSS in style.css with Tailwind utility classes in the HTML templates.

#### Scenario: Base styles replaced
- **WHEN** viewing any page
- **THEN** body styles SHALL use Tailwind classes (`bg-white dark:bg-[#20212b]`, `text-gray-600 dark:text-gray-300`, `font-serif`)
- **AND** no custom CSS from style.css SHALL be needed for basic styling

### Requirement: Color scheme uses Tailwind classes
The system SHALL implement light and dark mode using Tailwind's dark mode modifier.

#### Scenario: Light mode colors
- **WHEN** the system is in light mode
- **THEN** background SHALL be white
- **AND** text SHALL be gray-600
- **AND** headings SHALL be slate-800 or similar

#### Scenario: Dark mode colors
- **WHEN** the system is in dark mode (via prefers-color-scheme)
- **THEN** background SHALL be dark gray (#20212b or gray-900)
- **AND** text SHALL be light gray (#dadbdf or gray-300)
- **AND** headings SHALL be sky-400 or similar blue

### Requirement: Typography uses Tailwind scale
The system SHALL use Tailwind's typography utilities for text sizing.

#### Scenario: Heading hierarchy
- **WHEN** rendering h1 (name)
- **THEN** it SHALL use text size around text-2xl to text-3xl (approx 28px)
- **AND** font-weight SHALL be font-medium (500)

#### Scenario: Body text
- **WHEN** rendering body text
- **THEN** it SHALL use `text-base` (16px)
- **AND** line-height SHALL use `leading-normal` or `leading-relaxed`

### Requirement: Custom CSS file is removed or minimized
The system SHALL remove the static/style.css file or reduce it to minimal custom styles only.

#### Scenario: Complete Tailwind migration
- **WHEN** all styling is migrated
- **THEN** style.css SHALL be deleted
- **AND** base.html SHALL not include the style.css link

#### Scenario: Minimal custom CSS needed
- **WHEN** certain styles cannot be expressed with Tailwind
- **THEN** style.css SHALL contain only those specific styles
- **AND** the file SHALL be under 50 lines
