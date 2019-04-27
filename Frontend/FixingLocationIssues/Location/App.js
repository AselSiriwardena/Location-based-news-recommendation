import React, { Component } from 'react';
import { StyleSheet,
  Text,
  View,
TouchableOpacity } from 'react-native';
import Geocoder from 'react-native-geocoding';
import RNAndroidLocationEnabler from 'react-native-android-location-enabler';
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

class Home extends Component {
	constructor(props) {
		super(props);
	
		this.state = {
			latitude : 28.6139,
	longitude : 77.2090,
		  error: null,
		};
	  }
	//   componentDidMount() {
	// 	navigator.geolocation.getCurrentPosition(
	// 	  (position) => {
	// 		this.setState({
	// 		  latitude: position.coords.latitude,
	// 		  longitude: position.coords.longitude,
	// 		  error: null,
	// 		});
	// 	  },
	// 	  (error) => this.setState({ error: error.message }),
	// 	  { enableHighAccuracy: true, timeout: 10000, maximumAge: 1000 },
	// 	);
	//   }

  getData(){
    // Geocoder.setApiKey("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx");
	Geocoder.init("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx");
	// Geocoder.init('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx');

    Geocoder.from(this.state.latitude, this.state.longitude)
		.then(json => {
//         		var addressComponent = json.results[0].formatted_address;
//       console.log(addressComponent);
//       console.log(addressComponent)
// 	  alert(addressComponent);
// })
// .catch(error => console.warn(error));
	var addressComponent = json.results[0].address_components[0];
           var stateName = json.results[0].address_components.filter(x => x.types.filter(t => t == 'administrative_area_level_2').length > 0)[0].short_name;
         // alert(JSON.stringify(json.results[0].address_components));
    alert(stateName);
		})
  	.catch(error => console.warn(error));
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

export default Home


// Works as well :
// ------------

// location object
// Geocoder.from({
// 	latitude : 41.89,
// 	longitude : 12.49
// });

// latlng object
// Geocoder.from({
// 	lat : 41.89,
// 	lng : 12.49
// });

// array
// Geocoder.from([41.89, 12.49]);