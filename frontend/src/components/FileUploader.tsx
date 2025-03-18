import React from 'react';
import { TextField } from '@mui/material';

interface FileUploaderProps {
  onFileChange: (file: File) => void;
}

const FileUploader: React.FC<FileUploaderProps> = ({ onFileChange }) => {
  const handleChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    if (event.target.files && event.target.files[0]) {
      onFileChange(event.target.files[0]);
    }
  };

  return (
    <TextField
      type="file"
      inputProps={{ accept: '.txt' }}
      onChange={handleChange}
      fullWidth
    />
  );
};

export default FileUploader;