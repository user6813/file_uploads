interface UploadedFile {
  id: string;
  file: File;
}

interface UploadedFilesListProps {
  files: UploadedFile[];
  onFileClick: (file: UploadedFile) => void;
}

const UploadedFilesList = ({ files, onFileClick }: UploadedFilesListProps) => (
  <div className="w-full max-w-2xl mx-auto bg-white rounded-lg shadow p-6">
    <h3 className="text-lg font-semibold mb-4 text-[#000]">Uploaded Files</h3>
    {files.length === 0 ? (
      <div className="text-gray-500 text-center text-[#000]">No files uploaded yet.</div>
    ) : (
      <ul className="divide-y divide-gray-200">
        {files.map(f => (
          <li key={f.id} className="py-2 flex items-center justify-between text-[#000]">
            <span className="truncate max-w-xs">{f.file.name}</span>
            <button
              className="bg-blue-600 text-[#fff] text-sm font-medium"
              onClick={() => onFileClick(f)}
            >
              View
            </button>
          </li>
        ))}
      </ul>
    )}
  </div>
);

export default UploadedFilesList; 