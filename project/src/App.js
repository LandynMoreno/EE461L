import React, {useState, useEffect} from 'react'
import { BrowserRouter as Router, Route, Routes} from "react-router-dom";
import './App.css';
import { ThemeProvider } from '@mui/material/styles';
import { theme } from './components/theme';
import Signin from './components/Signin';
import Newuser from './components/Newuser';
import Projects from './components/Projects'
import DataAccess from './components/DataAccess';
import ResourceManagement from './components/ResourceMagement';

function App() {


  return (
    <div className = "App">
      <ThemeProvider theme = {theme}>

        <Router>
          <Routes>
            <Route path ='/' element={<Signin/>}/>
            <Route path ='/newuser' element={<Newuser/>}/>
            <Route path ='/projects' element={<Projects/>}/>
            <Route path = '/dataaccess' element={<DataAccess/>}/>
            <Route path ='/resourceManagement' element={<ResourceManagement/>}/>
          </Routes>
        </Router>
      </ThemeProvider>
      



    </div>
    
  )
}

export default App
