import React, { Component } from 'react';
import logo from "../res/login/logo.svg";
import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form';
import LoginBox from '../components/LoginBox';

export class Login extends Component {
  render() {
    return (
      <div className=' bg-gray-100 dark:bg-black  
      min-h-screen min-w-max flex justify-center
      align-middle'>
        <LoginBox />
     </div>
    )
  }
}

export default Login