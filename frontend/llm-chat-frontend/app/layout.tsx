import './globals.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import { ThemeProvider } from '../context/ThemeContext';

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en" className="h-full">
      <body>
        <ThemeProvider>{children}</ThemeProvider>
      </body>
    </html>
  );
}