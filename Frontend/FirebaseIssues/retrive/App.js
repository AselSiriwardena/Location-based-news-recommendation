import React from 'react';
import { FlatList, ActivityIndicator, Text, View  } from 'react-native';

export default class FetchExample extends React.Component {

  constructor(props){
    super(props);
    this.state ={ isLoading: true}
  }

  componentDidMount(){
    fetch('http://192.168.8.101:8000/category/', {
      method: 'POST',
      
      headerss: {
          'Accept': 'application/json',
          "Content-Type": "application/json",                
      },
      body: JSON.stringify({
          cname: 'fuck',
         
      })
  })
      .then((resp)=>{
          return resp.json();
      })
      .then((jsonData) => {
          console.log(JSON.stringify(jsonData));
          // if(jsonData['result'] == true){
          //     AsyncStorage.setItem('USER', jsonData.user);
          //     AsyncStorage.setItem('TOKEN', jsonData.token);
          //     alert("You are: "+jsonData['user']);
          //     this.props.navigation.navigate('Dashboard');
          // }
          // else{
          //   alert("Wrong uername/password. Try again");
          // }
      })
      .catch((e)=>{
          console.log(e);
      })
    // return fetch('http://192.168.8.100:8000/category/')
    //   .then((response) => response.json())
    //   .then((responseJson) => {

    //     this.setState({
    //       isLoading: false,
    //       dataSource: responseJson,
    //     }, function(){

    //     });

    //   })
    //   .catch((error) =>{
    //     console.error(error);
    //   });
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



  render(){

    if(this.state.isLoading){
      return(
        <View style={{flex: 1, padding: 20}}>
          <ActivityIndicator/>
        </View>
      )
    }

    return(
      <View style={{flex: 1, paddingTop:20}}>
        <FlatList
          data={this.state.dataSource}
          renderItem={({item}) => <Text>{item.title}, {item.releaseYear}</Text>}
          keyExtractor={({id}, index) => id}
        />
      </View>
    );
  }
}
