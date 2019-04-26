/**
 * Sample React Native App
 * https://github.com/facebook/react-native
 *
 * @format
 * @flow
 */

import React, {Component} from 'react';
import {Platform, StyleSheet, Text, View,TextInput} from 'react-native';
import firebase from 'react-native-firebase';
import Button from 'react-native-button'  ;


export default class App extends Component{
  constructor(props){
    super(props);
this.state={
  typedEmail:'',
  typedPassword:'',
  user:null,
 };
}

onRegister = () => {
    firebase.auth().createUserWithEmailAndPassword(this.state.typedEmail,this.state.typedPassword)
    .then((loggedInUser)=>{
      this.setState({user:loggedInUser})
      console.log(`REgister with user: ${JSON.stringify(loggedInUser.toJSON())}`);
    }).catch((error)=>{
      console.log(`Register fail with error : ${error}`);
    });
}
onLogin = () => {
  firebase.auth().signInWithEmailAndPassword(this.state.typedEmail,this.state.typedPassword)
    .then((loggedInUser)=>{
      this.setState({user:loggedInUser})
      console.log(`Login with user: ${JSON.stringify(loggedInUser.toJSON())}`);
    }).catch((error)=>{
      console.log(`Login fail with error : ${error}`);
    });
}



  render() {
    return (
      <View 
          style={{
            flex:1,
            alignItems:'center',
            backgroundColor:'white',
            borderRadius:Platform.OS=='android'? 30:0 ,

          }}
      >
      <TextInput style={{
              height:40,
              width :200,
              margin:10,
              padding:10,
              borderColor:'gray',
              borderWidth:1,
              color:'black'
      }}

      keyboardType='email-address'
      placeholder='Enter Your Email'
      autoCapitalize='none'
      onChangeText={
          (text)=>{
            this.setState({typedEmail:text});
          }
      }
      />

<TextInput style={{
              height:40,
              width :200,
              margin:10,
              padding:10,
              borderColor:'gray',
              borderWidth:1,
              color:'black'
      }}

      keyboardType='default'
      placeholder='Enter Your Password'
     secureTextEntry={true}
      onChangeText={
          (text)=>{
            this.setState({typedPassword:text});
          }
      }
      />

      <view style={{flexDirection:'row'}}>
          <Button containerStyle={{
                        padding:10,
                        borderRadius:4,
                        margin:10,
                        backgroundColor:'green'


          }}

            style={{fontSize:17,color:'white'}}
            onPress={this.onRegister}
          >Register</Button>
      
      <Button containerStyle={{
                        padding:10,
                        borderRadius:4,
                        margin:10,
                        backgroundColor:'blue'


          }}

            style={{fontSize:17,color:'white'}}
            onPress={this.onLogin}
          >Login</Button>
      
      
      
      </view>


        
      </View>
    );
  }
}


