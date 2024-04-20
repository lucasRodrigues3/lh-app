import React, { useState } from 'react';
import { Button, TextField, Container } from '@mui/material';
import { gerarItem } from './main.js';


const Formulario = () => {
  const handleSubmit = (e) => {
    e.preventDefault();
    gerarItem()
  };

  return (
    <Container maxWidth="sm">
      <form onSubmit={handleSubmit}>
        <Button type="submit" variant="contained" color="primary">
          Enviar
        </Button>
      </form>
    </Container>
  );
};

export default Formulario;
