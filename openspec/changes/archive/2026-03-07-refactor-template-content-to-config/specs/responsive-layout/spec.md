## ADDED Requirements

### Requirement: Layout uses Flexbox instead of floats
The system SHALL replace the float-based sidebar layout with a Flexbox-based layout.

#### Scenario: Desktop layout
- **WHEN** viewing on desktop (lg breakpoint and above)
- **THEN** the layout SHALL use flex container
- **AND** sidebar SHALL be fixed-width (w-60 or ~15rem)
- **AND** main content SHALL fill remaining space (flex-1)
- **AND** sidebar SHALL be positioned on the left

#### Scenario: Mobile layout
- **WHEN** viewing on mobile (below lg breakpoint)
- **THEN** the layout SHALL stack vertically using flex-col
- **AND** sidebar SHALL be full width
- **AND** content SHALL come after sidebar

### Requirement: Container has max-width and centering
The system SHALL constrain the overall width and center the content.

#### Scenario: Desktop container
- **WHEN** viewing on desktop
- **THEN** the wrapper SHALL have max-width (max-w-6xl or ~960px)
- **AND** be centered with mx-auto
- **AND** have appropriate padding

### Requirement: Header/sidebar styling uses Tailwind
The system SHALL style the sidebar using Tailwind utility classes.

#### Scenario: Header appearance
- **WHEN** rendering the header/sidebar
- **THEN** it SHALL have appropriate padding (`pt-16` or similar)
- **AND** be text-centered (`text-center`)
- **AND** have proper spacing between elements

### Requirement: Avatar image is styled with Tailwind
The system SHALL style the avatar using Tailwind classes.

#### Scenario: Avatar appearance
- **WHEN** rendering the avatar
- **THEN** it SHALL be circular (`rounded-full`)
- **AND** have consistent sizing (`w-32` or similar)
- **AND** have proper margin bottom (`mb-4`)

### Requirement: Section/content area uses Tailwind
The system SHALL style the main content area using Tailwind.

#### Scenario: Section appearance
- **WHEN** rendering the section/main content
- **THEN** it SHALL have appropriate padding (`pt-16`, `pb-12`)
- **AND** proper width (flex-1 on desktop)
- **AND** proper spacing between sections

### Requirement: Responsive behavior works correctly
The system SHALL maintain responsive behavior at all breakpoints.

#### Scenario: Large screens
- **WHEN** viewport is 1024px and above
- **THEN** sidebar and content SHALL be side by side
- **AND** both sections SHALL be fully visible

#### Scenario: Medium screens
- **WHEN** viewport is between 768px and 1023px
- **THEN** layout SHALL transition gracefully
- **AND** content SHALL remain readable

#### Scenario: Small screens
- **WHEN** viewport is below 768px
- **THEN** layout SHALL stack vertically
- **AND** all content SHALL be readable without horizontal scroll
