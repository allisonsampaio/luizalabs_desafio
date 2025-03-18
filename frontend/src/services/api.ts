import axios from 'axios';

const API_BASE_URL = 'http://backend:8000';

export const processFile = async (file: File) => {
  const formData = new FormData();
  formData.append('file', file);

  const response = await axios.post(`${API_BASE_URL}/upload`, formData, {
    headers: {
      'Content-Type': 'multipart/form-data',
    },
  });

  return response.data;
};