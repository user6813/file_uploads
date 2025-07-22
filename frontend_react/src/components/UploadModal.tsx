import { useRef } from 'react';

interface UploadModalProps {
  open: boolean;
  onClose: () => void;
  onUpload: (file: File) => void;
}

const UploadModal = ({ open, onClose, onUpload }: UploadModalProps) => {
  const fileInputRef = useRef<HTMLInputElement>(null);

  if (!open) return null;

  const handleUpload = () => {
    const file = fileInputRef.current?.files?.[0];
    if (file) {
      onUpload(file);
      onClose();
    }
  };

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center bg-black bg-opacity-40">
      <div className="bg-white rounded-lg shadow-lg p-8 w-full max-w-sm relative">
        <button className="absolute top-2 right-2 text-[#000] border-[1px] rouded-[4px] bg-[#fff]" onClick={onClose}>&times;</button>
        <h3 className="text-xl font-bold mb-4 text-center">Upload File</h3>
        <input type="file" ref={fileInputRef} className="mb-4 w-full" />
        <button
          className="w-full bg-blue-600 text-white py-2 rounded hover:bg-blue-700 transition font-semibold"
          onClick={handleUpload}
        >
          Upload
        </button>
      </div>
    </div>
  );
};

export default UploadModal; 