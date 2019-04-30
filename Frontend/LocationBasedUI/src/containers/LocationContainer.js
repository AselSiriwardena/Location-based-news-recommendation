import React, { Component } from 'react';
import { StyleSheet, Text, View,TouchableOpacity} from 'react-native';
import Icon from 'react-native-vector-icons/Ionicons';
import Geocoder from 'react-native-geocoding';

export default class InboxContainer extends Component {

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
		// Geocoder.init('AIzaSyDtWe3TP1KeWdRoxg9W22aTNzM8HIk6zzg');
    Geocoder.setApiKey("AIzaSyDtWe3TP1KeWdRoxg9W22aTNzM8HIk6zzg");
    Geocoder.getFromLatLng(5.9549,80.5550).then(
      json => {
        var address_component = json.results[0].address_components[0];
        var stateName = json.results[0].address_components.filter(x => x.types.filter(t => t == 'administrative_area_level_2').length > 0)[0].short_name;
        alert(stateName);
      },
      error => {
        alert(error);
      }
    );
  
  
	}
  static navigationOptions = {
    tabBarLabel: 'Location',
    tabBarIcon: ({ tintColor }) => (
      <Icon
        name="ios-ionic"
        size={21}
        color={tintColor}
      />
    ),
  };

  render() {
    return (
      <View style={styles.wrapper}>
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
};

const styles = StyleSheet.create({
  wrapper: {
    display: 'flex',
    padding: 50,
  }
});
