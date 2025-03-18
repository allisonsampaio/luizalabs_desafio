import axios from 'axios';

const API_BASE_URL = 'http://localhost:8000';

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

export const getOrderById = async (orderId: number) => {
  const response = await axios.get(`${API_BASE_URL}/orders/${orderId}`);
  return response.data;
};

export const getOrdersByDateRange = async (startDate: string, endDate: string) => {
  const response = await axios.get(`${API_BASE_URL}/orders/`, {
    params: {
      start_date: startDate,
      end_date: endDate,
    },
  });
  return response.data;
};