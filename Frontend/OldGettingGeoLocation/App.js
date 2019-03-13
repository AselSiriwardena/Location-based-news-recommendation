/**
 * Sample React Native App
 * https://github.com/facebook/react-native
 *
 * @format
 * @flow
 */

import React, {Component} from 'react';
import {Platform, StyleSheet, Text, View,SafeAreaView,ScrollView,Dimensions,Image,Button,TouchableOpacity} from 'react-native';
import {createDrawerNavigator,DrawerItems} from 'react-navigation';

import HomeScreen from './screens/HomeScreen'
import SettingsScreen from './screens/SettingsScreen'

const {width}= Dimensions.get('window')
const instructions = Platform.select({
  ios: 'Press Cmd+R to reload,\n' + 'Cmd+D or shake for dev menu',
  android:
    'Double tap R on your keyboard to reload,\n' +
    'Shake or press menu button for dev menu',
});

export default class App extends React.Component {

  render() {
   
    return (
      
      <AppDrawerNavigator />
   
    );
  }
}
const CustomerDrawerComponent=(props)=>(
  <SafeAreaView style={{flex:1}}>
  <View style={{height:150,backgroundColor:'white',alignItems:'center',justifyContent:'center'}}>
  <Image source={require('./image/imgnews.png')} style={{height:150,width:150,borderRadius:60}} />
  </View>
  <ScrollView>
    <DrawerItems{...props}/>
  </ScrollView>
  </SafeAreaView>
)
const AppDrawerNavigator=createDrawerNavigator({
  Home:HomeScreen,
  Settings:SettingsScreen 
},{
  contentComponent:CustomerDrawerComponent,
  contentOptions:{
    activeTintColor:'orange'

  }
});

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: '#F5FCFF',
  },
  welcome: {
    fontSize: 20,
    textAlign: 'center',
    margin: 10,
  },
  instructions: {
    textAlign: 'center',
    color: '#333333',
    marginBottom: 5,
  },
});
