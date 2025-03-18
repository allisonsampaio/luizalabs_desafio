import React from 'react';
import { Paper, Typography } from '@mui/material';
import { styled } from '@mui/system';

const JsonPaper = styled(Paper)(({ theme }) => ({
  padding: theme.spacing(2),
  marginTop: theme.spacing(2),
  maxHeight: '400px',
  overflowY: 'auto',
  backgroundColor: '#f5f5f5',
  fontFamily: 'monospace',
  whiteSpace: 'pre-wrap',
}));

interface JsonViewerProps {
  jsonData: any;
}

const JsonViewer: React.FC<JsonViewerProps> = ({ jsonData }) => {
  return (
    <JsonPaper elevation={3}>
      <Typography variant="h6" component="h2" gutterBottom>
        Resultado JSON:
      </Typography>
      <pre>
        <code>{JSON.stringify(jsonData, null, 2)}</code>
      </pre>
    </JsonPaper>
  );
};

export default JsonViewer;