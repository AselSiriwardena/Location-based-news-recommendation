import React, {Component} from 'react';
import { StyleSheet, Text, View,Dimensions,AppRegistry,TouchableOpacity} from 'react-native';
// import {Header,Right,Left,Icon,Container} from 'native-base'
import RNAndroidLocationEnabler from 'react-native-android-location-enabler';
import Geocoder from 'react-native-geocoding';



RNAndroidLocationEnabler.promptForEnableLocationIfNeeded({interval: 10000, fastInterval: 5000})
  .then(data => {
    // The user has accepted to enable the location services
    // data can be :
    //  - "already-enabled" if the location services has been already enabled
    //  - "enabled" if user has clicked on OK button in the popup
  }).catch(err => {
    // The user has not accepted to enable the location services or something went wrong during the process
    // "err" : { "code" : "ERR00|ERR01|ERR02", "message" : "message"}
    // codes : 
    //  - ERR00 : The user has clicked on Cancel button in the popup
    //  - ERR01 : If the Settings change are unavailable
    //  - ERR02 : If the popup has failed to open
  });
  export default class HomeScreen extends Component {

	constructor(props) {
	  super(props);
  
	  this.state = {
		latitude: null,
		longitude: null,
		error:null,
	  };
	}
   
	componentDidMount() {
	  navigator.geolocation.getCurrentPosition(
		 (position) => {
		   console.log("wokeeey");
		   console.log(position);
		   this.setState({
			 latitude: position.coords.latitude,
			 longitude: position.coords.longitude,
			 error: null,
		   });
		 },
		 (error) => this.setState({ error: error.message }),
		 { enableHighAccuracy: false, timeout: 200000, maximumAge: 1000 },
	   );
	 }
  
	getData(){
		
		Geocoder.init("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx");
  
	  Geocoder.from(this.state.latitude,this.state.longitude)
		  .then(json => {
			  var addressComponent = json.results[0].address_components[0];
       var stateName = json.results[0].address_components.filter(x => x.types.filter(t => t == 'administrative_area_level_2').length > 0)[0].short_name;
      //  var stateName = json.results[0].address_components.filter(x => x.types.filter(t => t == 'colloquial_area').length > 0)[0].short_name;
		   // alert(JSON.stringify(json.results[0].address_components));
	  alert(stateName);
		  })
		  .catch(error => console.warn(error));
  
	}
	
	// static navigationOptions={
	//   drawerIcon:({tintColor})=>(
	// 	<Icon name="md-wifi" style={{fontSize:24,color:tintColor}}/>
	//   )
	// }
	render() {
	 
	  return (
		 <View style={styles.container}>
  
		
  
		   <View>
			 
		  <Text> Longitude:- {this.state.latitude} </Text>
		  <Text> Latitude:- {this.state.longitude} </Text>
		  <Text> {this.state.error} </Text>
		  
		</View>
		<View>
		  <TouchableOpacity onPress={()=>{this.getData()}}>
		  <Text style={{fontSize:20}} >Get Address</Text>
		</TouchableOpacity>
		</View>
		</View>
	  );
	}
  }
  
  const styles = StyleSheet.create({
	container: {
	  flex: 1,
	
	},
	
	
	big: {
	  fontSize: 20
  }
  });
