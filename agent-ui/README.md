# Agent UI Frontend

This directory contains the Next.js frontend application for the Program Management Agent.

## Purpose

This UI provides a chat interface to interact with the backend agents and teams served by the Agno Playground.

## Setup

1.  **Ensure Node.js and pnpm are installed.**
2.  Navigate to this directory (`agent-ui`):
    ```bash
    cd agent-ui
    ```
3.  Install dependencies:
    ```bash
    pnpm install
    ```

## Running

1.  Make sure the backend server (`playground-app/playground.py`) is running (usually on `http://localhost:7777`).
2.  Start the frontend development server:
    ```bash
    pnpm dev
    ```
3.  Open your browser to `http://localhost:3000` (or the port indicated in the terminal).

## Configuration

*   The frontend expects the backend Playground API to be available at `http://localhost:7777` by default.
*   If your backend runs on a different URL, create a `.env.local` file in this directory (`agent-ui/`) and add:
    ```
    NEXT_PUBLIC_PLAYGROUND_ENDPOINT=http://your-backend-url:port
    ```
