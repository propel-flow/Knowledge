# React Frontend Project

<!-- 
  Global settings and standards are defined in ~/.clinerules/CLAUDE.global.md
  
  These include:
  - Global Code Style Preferences
  - Global Architecture Guidelines
  - Dynamic Protection Registry
  
  Please refer to the global file for these standards.
-->

<!-- 
  Global settings and standards are defined in ~/.clinerules/CLAUDE.global.md
  
  These include:
  - Global Code Style Preferences
  - Global Architecture Guidelines
  - AI Agent Architecture Guidelines
  - Dynamic Protection Registry Classifications
  - Common Development Commands
  
  Please refer to the global file for these standards.
-->

## Project Overview
This is a React-based frontend application using modern JavaScript/TypeScript patterns. It follows component-based architecture with state management and routing.

## Protection Suggestions (AI Managed)
<!-- AI tools can add suggestions here for human review -->
<!-- Format: - `path` - SUGGESTED: reason (stage: classification) (added: timestamp) -->
<!-- Example: - `src/components/DataVisualizer.tsx` - SUGGESTED: Robust error handling (stage: PERFORMANCE_VERIFIED) (added: 2025-06-20) -->

## Critical Rules - READ FIRST

**WORKING COMPONENTS - VERIFY BEFORE MODIFYING:**
<!-- Components in development that are working but still evolving -->
<!-- Format: `path` - CLASSIFICATION: Details about current state -->
- `src/features/ai-assistant/` - PROTOTYPE_WORKING: Basic chat functionality operational
- `src/api/third-party/` - INTEGRATION_TESTED: External API integrations established
- `src/components/data-visualization/` - AGENT_VALIDATED: Charts rendering correctly with test data
- `src/hooks/usePerformanceMonitor.ts` - PERFORMANCE_VERIFIED: Optimized for production use

**DO NOT MODIFY THESE COMPLETED COMPONENTS:**
<!-- Stable components that should not be modified -->
- `src/components/ui/` - PRODUCTION_STABLE: SHARED UI COMPONENTS, MODIFY WITH CAUTION
- `src/auth/` - SECURITY_AUDITED: AUTHENTICATION SYSTEM, DO NOT MODIFY
- `.github/workflows/` - PRODUCTION_STABLE: CI PIPELINE, COORDINATED WITH DEVOPS TEAM
- `src/api/client.ts` - PRODUCTION_STABLE: API CLIENT, SHARED INTEGRATION POINT

## Build & Test Commands
```bash
# Environment setup
npm install
# or
yarn install

# Development server
npm start
# or
yarn start

# Testing
npm test
# or
yarn test

# Linting and formatting
npm run lint
npm run format
# or
yarn lint
yarn format

# Build for production
npm run build
# or
yarn build

# Type checking
npm run typecheck
# or
yarn typecheck
```

## Code Style Preferences
- ESLint with project-specific config
- Prettier for code formatting
- 2-space indentation
- TypeScript preferred over JavaScript
- Functional components with hooks
- Avoid class components unless necessary
- CSS-in-JS or styled-components for styling
- Clear component organization and naming

## Architecture Guidelines
- Component-based architecture
- Container/presenter pattern for complex components
- Context API or Redux for state management
- React Router for navigation
- Axios or fetch for API calls
- React Query for data fetching and caching
- Proper error handling and loading states
- Use environment variables for configuration

## Project Structure
```
src/
├── components/           # Shared components
│   ├── ui/               # Core UI components
│   │   ├── Button/
│   │   ├── Input/
│   │   └── Modal/
│   └── layout/           # Layout components
│       ├── Header/
│       ├── Footer/
│       └── Sidebar/
├── pages/                # Page components
│   ├── Home/
│   ├── Dashboard/
│   └── Settings/
├── features/             # Feature-specific components
│   ├── auth/             # Authentication
│   └── users/            # User management
├── hooks/                # Custom hooks
├── api/                  # API integration
│   ├── client.ts         # Base API client
│   └── endpoints/        # API endpoint definitions
├── utils/                # Utility functions
├── context/              # React Context providers
├── store/                # State management (Redux)
├── types/                # TypeScript type definitions
├── styles/               # Global styles
└── App.tsx               # Main application component
```

## Performance Optimization
- Lazy loading and code splitting
- Memoization with useMemo and useCallback
- Virtualization for long lists
- Image optimization
- Bundle size analysis and optimization
- Efficient re-rendering with proper key usage
- Proper use of useEffect dependencies

## Testing Strategy
- Jest for unit and integration tests
- React Testing Library for component testing
- Mock Service Worker for API mocking
- Component stories with Storybook
- End-to-end testing with Cypress
- Snapshot testing for UI components

## Deployment Notes
- Containerized deployment with Docker
- CI/CD pipeline with GitHub Actions
- Static hosting on AWS S3, Vercel, or Netlify
- Environment-specific configuration
- Feature flags for staged rollouts
- Monitoring and error tracking with Sentry

## Current Sprint Focus
- [Current development priorities]
- [Features being actively developed]
- [Components being refactored]
- [Performance optimizations in progress]

## Known Issues
- [Known bugs and limitations]
- [Technical debt items]
- [Browser compatibility issues]
- [Feature gaps]
