import React, { useState } from 'react';
import { TextField, Button, Box } from '@mui/material';
import { getOrdersByDateRange } from '../services/api';

interface OrderSearchByDateRangeProps {
  onSearch: (data: any) => void;
}

const OrderSearchByDateRange: React.FC<OrderSearchByDateRangeProps> = ({ onSearch }) => {
  const [startDate, setStartDate] = useState<string>('');
  const [endDate, setEndDate] = useState<string>('');
  const [error, setError] = useState<string | null>(null);

  const handleSearch = async () => {
    if (!startDate || !endDate) {
      setError('Por favor, insira ambas as datas.');
      return;
    }

    try {
      const data = await getOrdersByDateRange(startDate, endDate);
      onSearch(data);
      setError(null);
    } catch (err: any) {
      setError('Erro ao buscar pedidos. Verifique as datas e tente novamente.');
      onSearch(null);
    }
  };

  return (
    <Box display="flex" gap={2} alignItems="center">
      <TextField
        label="Data Início (YYYYMMDD)"
        variant="outlined"
        value={startDate}
        onChange={(e) => setStartDate(e.target.value)}
        error={!!error}
      />
      <TextField
        label="Data Fim (YYYYMMDD)"
        variant="outlined"
        value={endDate}
        onChange={(e) => setEndDate(e.target.value)}
        error={!!error}
        helperText={error}
      />
      <Button variant="contained" color="primary" onClick={handleSearch}>
        Buscar
      </Button>
    </Box>
  );
};

export default OrderSearchByDateRange;