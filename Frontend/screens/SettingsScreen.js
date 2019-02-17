import React, {Component} from 'react';
import {Platform, StyleSheet, Text, View} from 'react-native';
import {Header,Right,Left,Icon} from 'native-base'



const instructions = Platform.select({
  ios: 'Press Cmd+R to reload,\n' + 'Cmd+D or shake for dev menu',
  android:
    'Double tap on your keyboard to reload,\n' +
    'Shake or press menu button for dev menu',
});



export default class SettingsScreen extends Component {
 
  static navigationOptions={
    drawerIcon:({tintColor})=>(
      <Icon name="md-cog" style={{fontSize:24,color:tintColor}}/>
    )
  }
  render() {
    return (
      <View style={styles.container}>
       <Header>
        <Left>
          <Icon name="md-menu" onPress={()=>this.props.navigation.openDrawer()}/>
        </Left> 
        </Header>
        
        <Text style={styles.welcome}>Welcome to SettingsScreen!</Text>
        <Text style={styles.instructions}>To get started, edit App.js</Text>
        <Text style={styles.instructions}>{instructions}</Text>
      </View>
    );
  }
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    
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