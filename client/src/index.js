import React, { useState } from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import ProductsPage from './pages/ProductsPage';
import 'bootstrap/dist/css/bootstrap.css';
import {BrowserRouter, Route, Routes} from "react-router-dom";
import './App.css';
import NavBar from './components/NavBar';
import { createTheme, ThemeProvider } from '@mui/material';
import './components/stylesheets/index.css';


const root = ReactDOM.createRoot(document.getElementById('root'));

const darkTheme = createTheme({
  palette: {
    mode: 'dark',
    primary: {
      main: '#1976d2',
    },
  },
});


root.render(
  <BrowserRouter>

      <ThemeProvider theme={darkTheme}>
        <NavBar/>
      </ThemeProvider>

      <div className="h-screen bg-black">
        <Routes>
          <Route path='/products' element={<ProductsPage/>}/>
        </Routes>
      </div>
  </BrowserRouter>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals