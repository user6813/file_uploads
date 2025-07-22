import { Routes, Route, Navigate } from 'react-router-dom';
import AuthPage from './pages/AuthPage';
import UploadPage from './pages/UploadPage';
import FileViewerPage from './pages/FileViewerPage';
// import './App.css';

function App() {
  return (
    <Routes>
      <Route path="/auth" element={<AuthPage />} />
      <Route path="/upload" element={<UploadPage />} />
      <Route path="/view/:fileId" element={<FileViewerPage />} />
      <Route path="*" element={<Navigate to="/auth" replace />} />
    </Routes>
  );
}

export default App;
