import React, { Component } from 'react';
import { StyleSheet, Text, View,TouchableOpacity} from 'react-native';
import Icon from 'react-native-vector-icons/Ionicons';
import Geocoder from 'react-native-geocoding';
import SearchBar from '../components/SearchBar';

export default class InboxContainer extends Component {
//   constructor(){
//     super();
//     this.state = {
//         ready: false,
//         where: {lat:null, lng:null},
//         error: null
//     }
// }
// componentDidMount(){
//     let geoOptions = {
//         enableHighAccuracy: true,
//         timeOut: 20000,
//         maximumAge: 60 * 60 * 24
//     };
//     this.setState({ready:false, error: null });
//     navigator.geolocation.getCurrentPosition( this.geoSuccess, 
//                                             this.geoFailure,
//                                             geoOptions);
// }
// geoSuccess = (position) => {
//     console.log(position.coords.latitude);
    
//     this.setState({
//         ready:true,
//         where: {lat: position.coords.latitude,lng:position.coords.longitude }
//     })
// }
// geoFailure = (err) => {
//     this.setState({error: err.message});
// }
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
    Geocoder.setApiKey("AIzaSyDg08XwkH-af7hrCC1q91Iu3TOkrCpNOik");
    // Geocoder.setApiKey("AIzaSyDtWe3TP1KeWdRoxg9W22aTNzM8HIk6zzg");
    Geocoder.getFromLatLng(this.state.latitude,this.state.longitude).then(
      json => {
        var address_component = json.results[0].address_components[0];
        var stateName = json.results[0].address_components.filter(x => x.types.filter(t => t == 'locality').length > 0)[0].short_name;
        alert(stateName);
      },
      error => {
        alert(error);
      }
    );
  
  
	}
  static navigationOptions = {
    tabBarLabel: 'LOCATION',
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
        <View style={styles.search}>
          <SearchBar />
        </View>
        <View>
			 
       <Text> Longitude:- {this.state.latitude} </Text>
       <Text> Latitude:- {this.state.longitude} </Text>
       {/* <Text>Longitude:-{this.state.where.lng}</Text>
       <Text>Latitude:-{this.state.where.lat}</Text> */}
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
  },
  search: {
    marginRight: 10,
  }
});
