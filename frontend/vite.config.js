import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

const cacheDir =
  process.env.NODE_ENV === 'development-docker'
    ? '/app/node_modules/.vite'
    : 'node_modules/.vite';

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
  server: {
    host: true,
    port: 5173,
  },
  cacheDir,
});
