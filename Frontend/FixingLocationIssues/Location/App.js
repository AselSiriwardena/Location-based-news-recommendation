import React, { Component } from 'react';
import { StyleSheet,
  Text,
  Image,
  View,
TouchableOpacity } from 'react-native';
import Geocoder from 'react-native-geocoding';

class App extends Component {

  getData(){
    // Geocoder.setApiKey("AIzaSyC7U5cHz_cW6Z4bVCmnKUimvMmmkKc4Qj4");
    Geocoder.init("AIzaSyC7U5cHz_cW6Z4bVCmnKUimvMmmkKc4Qj4");

    //Geocoder.from(41.89, 12.49)
	//	.then(json => {
     //   		var addressComponent = json.results[0].formatted_address;
      // console.log(addressComponent);
      console.log(addressComponent)
     // alert(addressComponent);
	//	})
  	//.catch(error => console.warn(error));
	////////////////////////////////////////////////////////////////////
  // Geocoder.from("Colosseum")
	// 	.then(json => {
	// 		var location = json.results[0].geometry.location;
  //     // console.log(location);
  //     alert(location);
	// 	})
	// 	.catch(error => console.warn(error));
  }
  
  render() {
    return (
      <View style={styles.container}>
      <TouchableOpacity onPress={()=>{this.getData()}}>
        <Text>Get Address</Text>
        </TouchableOpacity>
      </View>
    );
  }
}
const styles = StyleSheet.create({
  container: {
    backgroundColor: '#F5FCFF',
    flex: 10,
    justifyContent: 'center'
  },
});

export default App
