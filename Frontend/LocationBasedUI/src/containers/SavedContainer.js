import React, { Component } from 'react';
import {
  FlatList,
   ActivityIndicator,
  View,
  Text,
  StyleSheet,
} from 'react-native';
import Icon from 'react-native-vector-icons/Ionicons';

export default class InboxContainer extends Component {

  constructor(props){
    super(props);
    this.state ={ isLoading: true}
  }
  static navigationOptions = {
    tabBarLabel: 'Catogory',
    tabBarIcon: ({ tintColor }) => (
      <Icon
        name="ios-contact-outline"
        size={22}
        color={tintColor}
      />
    ),
  };

  componentDidMount(){
    return fetch('http://192.168.8.102:8000/category/', {
          method: 'POST',
          
          headerss: {
              'Accept': 'application/json',
              "Content-Type": "application/json",                
          },
          body: JSON.stringify({
              cname: 'sports',
             
          })
      })
      .then((response) => response.json())
      .then((responseJson) => {

        this.setState({
          isLoading: false,
          dataSource: responseJson,
        }, function(){

        });

      })
      .catch((error) =>{
        console.error(error);
      });
//     fetch('http://192.168.8.100:8000/category/', {
//   method: 'POST',
//   headers: {
//     Accept: 'application/json',
//     'Content-Type': 'application/json',
//   },
//   body: JSON.stringify({
//     cname: 'sports',
   
//   }),
// });
  }


  render() {

    if(this.state.isLoading){
      return(
        <View style={{flex: 1, padding: 20}}>
          <ActivityIndicator/>
        </View>
      )
    }
    return (
      <View style={{flex: 1, paddingTop:20}}>
        <FlatList
          data={this.state.dataSource}
          renderItem={({item}) => <Text>{item.title}, {item.releaseYear}</Text>}
          keyExtractor={({id}, index) => id}
        />
      </View>
    );
  }
};

const styles = StyleSheet.create({
  wrapper: {
    display: 'flex',
    padding: 50,
  }
});