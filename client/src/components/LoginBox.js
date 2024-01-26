import React, { Component } from 'react';
import { TextField } from '@mui/material';
import Button from '@mui/material/Button';
import axios from 'axios';


export class LoginBox extends Component {

     constructor(props){
          super(props);

          this.state = {
               username:"",
               password:""
          }
     }

     setUsername = (string) => {
          this.setState({
               username:string,
               password:this.state.password
          })
     }

     setPassword = (string) => {
          this.setState({
               username:this.state.username,
               password:string
          })
     }
     

     submit = async () => {
          const response = await axios.post(
               "http://127.0.0.1:8000/commerce/auth/p_auth/",
               {
                    "username":this.state.username,
                    "password":this.state.password
               }     
          );
          console.log(response);
     }

     onUsernameBoxChange = (e) => {
          this.setState({
               username:e.target.value
          })
     }
     onPasswordBoxChange = (e) => {
          this.setState({
               password:e.target.value
          })
     }

  render() {
    return (
      <div className="bg-white lg:w-[50vw] lg:h-[60vh] lg:mt-32 relative w-screen h-screen">
          <div className="title pl-8 pt-6">
               <div className=" text-[5vh] text-sky-600 font-bold">Login</div>
               <div className=" text-[1.9vh] text-gray-500 mt-3">You can login here...</div>
          </div>
          <div className="login-form mt-10 ml-8 mr-8">
               <form action="/" method='POST' className=''>
                    <div className="email-container ">
                         <TextField color='info' label='Email'
                              margin='dense' placeholder='Example: email@email.com'
                              required={true} className=' w-[100%]' 
                              onChange={this.onUsernameBoxChange}
                          />
                    </div>

                    <div className="email-container mt-10">
                         <TextField color='info' label='Password'
                              margin='dense' p
                              required={true} className=' w-[100%]'
                              type='password'
                              onChange={this.onPasswordBoxChange}
                          />
                    </div>

                    <div className="email-container mt-[16vh] w-full mb-[10vh]">
                         <Button variant='contained' color='info'
                          className=' bg-sky-600 w-full'
                          fullWidth="true" onClick={this.submit}>Submit</Button>
                    </div>
               </form>
          </div>
      </div>
    )
  }
}

export default LoginBox