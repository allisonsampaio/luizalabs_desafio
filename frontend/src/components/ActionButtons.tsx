import React from 'react';
import { Button, Box } from '@mui/material';

interface ActionButtonsProps {
  onProcess: () => void;
  onDownload: () => void;
  onReset: () => void;
  isFileSelected: boolean;
  isJsonGenerated: boolean;
}

const ActionButtons: React.FC<ActionButtonsProps> = ({
  onProcess,
  onDownload,
  onReset,
  isFileSelected,
  isJsonGenerated,
}) => {
  return (
    <Box display="flex" gap={2}>
      <Button
        variant="contained"
        color="primary"
        onClick={onProcess}
        disabled={!isFileSelected}
      >
        Processar Arquivo
      </Button>
      {isJsonGenerated && (
        <>
          <Button
            variant="contained"
            color="secondary"
            onClick={onDownload}
          >
            Baixar JSON
          </Button>
          <Button
            variant="outlined"
            color="error"
            onClick={onReset}
          >
            Resetar
          </Button>
        </>
      )}
    </Box>
  );
};

export default ActionButtons;