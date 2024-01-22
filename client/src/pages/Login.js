import React, { Component } from 'react';
import logo from "../res/login/logo.svg";
import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form';

export class Login extends Component {
  render() {
    return (
      <div className=' bg-gray-100 dark:bg-black  min-h-screen min-w-max flex'>
        <div className=" h-screen bg-blue-700 w-1/4">

        </div>
        <div className=' h-screen w-3/4 bg-stone-950 border-slate-50 border-2 flex justify-center'>
          <div className=' bg-red-600 w-36 h-40 mt-48'>
        
          </div>
        </div>
     </div>
    )
  }
}

export default Login