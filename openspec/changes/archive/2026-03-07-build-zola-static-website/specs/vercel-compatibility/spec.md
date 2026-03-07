## ADDED Requirements

### Requirement: Vercel configuration file
The project SHALL include a `vercel.json` file for deployment configuration.

#### Scenario: Vercel config exists
- **WHEN** project is created
- **THEN** `vercel.json` file exists in project root

#### Scenario: Framework specified
- **WHEN** vercel.json is read
- **THEN** `framework` is set to "zola"

#### Scenario: Build command specified
- **WHEN** vercel.json is read
- **THEN** `buildCommand` is set to "zola build"

#### Scenario: Output directory specified
- **WHEN** vercel.json is read
- **THEN** `outputDirectory` is set to "public"

### Requirement: Build succeeds locally
The project SHALL build successfully with `zola build`.

#### Scenario: Local build works
- **WHEN** `zola build` is run
- **THEN** `public/` directory is generated with static files
