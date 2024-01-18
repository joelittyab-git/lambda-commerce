import React, { Component } from 'react';
import logo from "../res/login/logo.svg";
export class Login extends Component {
  render() {
    return (
      <div className=' bg-gray-100 dark:bg-black  min-h-screen'>
          <img src={logo} alt={logo} />
     </div>
    )
  }
}

export default Login