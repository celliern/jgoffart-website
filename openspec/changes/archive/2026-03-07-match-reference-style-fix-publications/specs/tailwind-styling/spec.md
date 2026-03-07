## ADDED Requirements

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

## MODIFIED Requirements

### Requirement: All styles use Tailwind utility classes
The system SHALL replace all custom CSS with Tailwind utility classes, including new autocolor and grid layouts.

#### Scenario: Complete Tailwind styling
- **WHEN** viewing any page
- **THEN** body styles SHALL use Tailwind classes
- **AND** autocolor SHALL use Tailwind dark mode classes
- **AND** publication grids SHALL use Tailwind grid classes
- **AND** no custom CSS file SHALL be needed
