import React, { useState } from 'react';
import { TextField, Button, Box } from '@mui/material';
import { getOrderById } from '../services/api';

interface OrderSearchByIdProps {
  onSearch: (data: any) => void;
}

const OrderSearchById: React.FC<OrderSearchByIdProps> = ({ onSearch }) => {
  const [orderId, setOrderId] = useState<string>('');
  const [error, setError] = useState<string | null>(null);

  const handleSearch = async () => {
    if (!orderId) {
      setError('Por favor, insira um ID válido.');
      return;
    }

    try {
      const data = await getOrderById(Number(orderId));
      onSearch(data);
      setError(null);
    } catch (err: any) {
      setError('Erro ao buscar o pedido. Verifique o ID e tente novamente.');
      onSearch(null);
    }
  };

  return (
    <Box display="flex" gap={2} alignItems="center">
      <TextField
        label="ID do Pedido"
        variant="outlined"
        value={orderId}
        onChange={(e) => setOrderId(e.target.value)}
        error={!!error}
        helperText={error}
      />
      <Button variant="contained" color="primary" onClick={handleSearch}>
        Buscar
      </Button>
    </Box>
  );
};

export default OrderSearchById;