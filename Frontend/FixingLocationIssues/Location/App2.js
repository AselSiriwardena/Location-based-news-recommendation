//<uses-permission android:name="android.permission.ACCESS_FINE_LOCATION" />
//C:\Users\Luciferishie\Desktop\aSAASA\findCoordsApp\android\app\src\main\AndroidManifest.xml


import React, { Component } from 'react';
import {
	Platform,
	StyleSheet,
	Text,
	View,
	Alert,
	TouchableOpacity
} from 'react-native';

export default class App2 extends Component {
	state = {
		location: null
	};

	findCoordinates = () => {
		navigator.geolocation.getCurrentPosition(
			position => {
				const location = JSON.stringify(position);

				this.setState({ location });
			},
			error => Alert.alert(error.message),
			{ enableHighAccuracy: true, timeout: 20000, maximumAge: 1000 }
		);
	};

	render() {
		return (
			<View style={styles.container}>
				<TouchableOpacity onPress={this.findCoordinates}>
					<Text style={styles.welcome}>Find My Coords?</Text>
          <Text>Location: {this.state.location}</Text>
				</TouchableOpacity>
			</View>
		);
	}
}

const styles = StyleSheet.create({
	container: {
		flex: 1,
		justifyContent: 'center',
		alignItems: 'center',
		backgroundColor: '#F5FCFF'
	},
	welcome: {
		fontSize: 20,
		textAlign: 'center',
		margin: 10
	},
	instructions: {
		textAlign: 'center',
		color: '#333333',
		marginBottom: 5
	}
});