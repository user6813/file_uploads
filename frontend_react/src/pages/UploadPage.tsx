import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import UploadModal from '../components/UploadModal';
import UploadedFilesList from '../components/UploadedFilesList';

interface UploadedFile {
  id: string;
  file: File;
}

const UploadPage = () => {
  const [files, setFiles] = useState<UploadedFile[]>([]);
  const [modalOpen, setModalOpen] = useState(false);
  const navigate = useNavigate();

  if (localStorage.getItem('auth') !== 'true') {
    navigate('/auth');
    return null;
  }

  const handleAddFile = (file: File) => {
    const newFile = { id: Date.now().toString(), file };
    setFiles(prev => [...prev, newFile]);
  };

  return (
    <div className="w-screen h-screen min-h-screen min-w-full bg-gray-50 flex flex-col items-center justify-start p-8">
      <button
        className="mb-6 mt-4 bg-blue-500 text-white px-6 py-3 rounded hover:bg-blue-600 transition text-lg font-semibold"
        onClick={() => setModalOpen(true)}
      >
        Upload File
      </button>
      <UploadedFilesList files={files} onFileClick={file => navigate(`/view/${file.id}`, { state: { file: file.file } })} />
      <UploadModal open={modalOpen} onClose={() => setModalOpen(false)} onUpload={handleAddFile} />
    </div>
  );
};

export default UploadPage; 