import React, { useState } from 'react';
import { Container, Typography, Paper, Box } from '@mui/material';
import FileUploader from '../components/FileUploader';
import JsonViewer from '../components/JsonViewer';
import ActionButtons from '../components/ActionButtons';
import { processFile } from '../services/api';

const Home: React.FC = () => {
  const [file, setFile] = useState<File | null>(null);
  const [jsonData, setJsonData] = useState<any>(null);
  const [error, setError] = useState<string | null>(null);

  const handleFileChange = (file: File) => {
    setFile(file);
  };

  const handleSubmit = async () => {
    if (!file) {
      setError('Por favor, selecione um arquivo.');
      return;
    }

    try {
      const data = await processFile(file);
      setJsonData(data);
      setError(null);
    } catch (err: any) {
      if (err.response) {
        const errorMessage = err.response.data.message || 'Erro ao processar o arquivo.';
        const errorDetails = err.response.data.errors
          ? `Detalhes: ${err.response.data.errors.join(', ')}`
          : '';
        setError(`${errorMessage} ${errorDetails}`);
      } else {
        setError('Erro ao se conectar com o servidor.');
      }
      setJsonData(null);
    }
  };

  const handleDownload = () => {
    if (jsonData) {
      const blob = new Blob([JSON.stringify(jsonData, null, 2)], { type: 'application/json' });
      const url = URL.createObjectURL(blob);
      const link = document.createElement('a');
      link.href = url;
      link.download = 'output.json';
      link.click();
      URL.revokeObjectURL(url);
    }
  };

  const handleReset = () => {
    setFile(null);
    setJsonData(null);
    setError(null);
  };

  return (
    <Container maxWidth="md">
      <Typography variant="h4" component="h1" gutterBottom align="center" sx={{ marginTop: 4 }}>
        Processador de Arquivos
      </Typography>

      <Paper elevation={3} sx={{ padding: 3, marginTop: 2 }}>
        <Box display="flex" flexDirection="column" gap={2}>
          <FileUploader onFileChange={handleFileChange} />
          <ActionButtons
            onProcess={handleSubmit}
            onDownload={handleDownload}
            onReset={handleReset}
            isFileSelected={!!file}
            isJsonGenerated={!!jsonData}
          />
        </Box>
      </Paper>

      {error && (
        <Typography color="error" variant="body1" gutterBottom sx={{ marginTop: 2 }}>
          {error}
        </Typography>
      )}

      {jsonData && <JsonViewer jsonData={jsonData} />}
    </Container>
  );
};

export default Home;