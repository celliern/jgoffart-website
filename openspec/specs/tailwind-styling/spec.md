# tailwind-styling Specification

## Purpose
TBD - created by archiving change refactor-template-content-to-config. Update Purpose after archive.
## Requirements
### Requirement: All styles use Tailwind utility classes
The system SHALL use exact reference CSS from chloezapha.com, replacing Tailwind utility classes with inline CSS that matches the reference.

#### Scenario: Complete reference styling
- **WHEN** viewing any page
- **THEN** all styles SHALL match chloezapha.com exactly
- **AND** colors, fonts, spacing SHALL be identical
- **AND** CSS SHALL be inline in the template

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

### Requirement: Autocolor class uses Tailwind dark mode
The system SHALL implement autocolor styling using Tailwind utility classes with dark mode support.

#### Scenario: Autocolor with Tailwind
- **WHEN** rendering elements with autocolor class
- **THEN** it SHALL use Tailwind classes like `text-slate-800 dark:text-gray-300`
- **AND** the colors SHALL match the reference site's autocolor behavior

### Requirement: Publication grid uses Tailwind grid system
The system SHALL implement the 3/9 publication grid using Tailwind's grid utilities.

#### Scenario: Grid with Tailwind
- **WHEN** rendering publications with images or badges
- **THEN** it SHALL use `grid grid-cols-12` container
- **AND` image/badge column SHALL use `col-span-3` or `lg:col-span-3`
- **AND** content column SHALL use `col-span-9` or `lg:col-span-9`

#### Scenario: Full width without Tailwind grid
- **WHEN** rendering publications without images or badges
- **THEN** it SHALL not use the grid layout
- **AND** content SHALL span full width naturally

### Requirement: Template uses exact reference HTML
The system SHALL use the same HTML structure as chloezapha.com.

#### Scenario: Header structure
- **WHEN** rendering the header
- **THEN** it SHALL use semantic elements: `<position>`, `<email>`, `<autocolor>`
- **AND** it SHALL have the same class structure as reference

#### Scenario: Publication structure
- **WHEN** rendering publications
- **THEN** it SHALL use `<ol class="bibliography">` wrapper
- **AND** each item SHALL use `<li>` with `<div class="pub-row">`
- **AND** columns SHALL use `col-sm-3` and `col-sm-9` classes

### Requirement: CSS matches reference exactly
The system SHALL use identical CSS properties to chloezapha.com.

#### Scenario: Badge styling
- **WHEN** rendering a badge
- **THEN** it SHALL have background-color: #002D72
- **AND** it SHALL be positioned absolutely (top: 8px, left: 16px)
- **AND** it SHALL have box-shadow

#### Scenario: Link colors
- **WHEN** in light mode
- **THEN** links SHALL be color: #043361
- **WHEN** in dark mode
- **THEN** links SHALL be color: rgb(62, 183, 240)

