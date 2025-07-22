import { useLocation, useNavigate } from 'react-router-dom';
import { Document, Page, pdfjs } from 'react-pdf';
import { useState } from 'react';

pdfjs.GlobalWorkerOptions.workerSrc = `//cdnjs.cloudflare.com/ajax/libs/pdf.js/${pdfjs.version}/pdf.worker.js`;

const FileViewerPage = () => {
  const location = useLocation();
  const navigate = useNavigate();
  const file = location.state?.file as File | undefined;
  const [numPages, setNumPages] = useState<number>();

  if (!file) {
    return (
      <div className="flex flex-col items-center justify-center min-h-screen bg-gray-50">
        <div className="bg-white p-8 rounded shadow-md w-full max-w-md text-center">
          <p>No file data found. Please go back and select a file.</p>
          <button className="mt-4 bg-blue-500 text-white px-4 py-2 rounded" onClick={() => navigate('/upload')}>Back to Uploads</button>
        </div>
      </div>
    );
  }

  const fileType = file.type;

  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-gray-50">
      <div className="bg-white p-8 rounded shadow-md w-full max-w-2xl">
        <h2 className="text-2xl font-bold mb-4 text-center">File Viewer</h2>
        {fileType === 'application/pdf' ? (
          <Document
            file={file}
            onLoadSuccess={({ numPages }) => setNumPages(numPages)}
            className="flex flex-col items-center"
          >
            {Array.from(new Array(numPages), (el, index) => (
              <Page key={`page_${index + 1}`} pageNumber={index + 1} />
            ))}
          </Document>
        ) : fileType.startsWith('image/') ? (
          <img src={URL.createObjectURL(file)} alt={file.name} className="max-w-full max-h-96 mx-auto" />
        ) : (
          <div className="text-center">
            <p>File name: <span className="font-semibold">{file.name}</span></p>
            <p>Preview not available for this file type.</p>
          </div>
        )}
        <button className="mt-6 bg-blue-500 text-white px-4 py-2 rounded" onClick={() => navigate('/upload')}>Back to Uploads</button>
      </div>
    </div>
  );
};

export default FileViewerPage; 