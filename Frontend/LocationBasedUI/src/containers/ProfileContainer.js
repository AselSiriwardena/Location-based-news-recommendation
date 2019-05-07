import React, { Component } from 'react';
import {
  StyleSheet,
  Text,
  View,
  Image,
  TouchableOpacity
} from 'react-native';
import Icon from 'react-native-vector-icons/Ionicons';

export default class InboxContainer extends Component {
  static navigationOptions = {
    tabBarLabel: 'PROFILE',
    tabBarIcon: ({ tintColor }) => (
      <Icon
        name="ios-contact-outline"
        size={22}
        color={tintColor}
      />
    ),
  };

  render() {
    // return (
    //   <View style={styles.wrapper}>
    //     <Text>Profile Container</Text>
    //   </View>
    // );
    return (
      <View style={styles.container}>
          <View style={styles.header}></View>
          <Image style={styles.avatar} source={{uri: 'https://bootdey.com/img/Content/avatar/avatar6.png'}}/>
          <View style={styles.body}>
            <View style={styles.bodyContent}>
              <Text style={styles.name}>John Doe</Text>
              {/* <Text style={styles.info}>UX Designer / Mobile developer</Text> */}
              {/* <Text style={styles.description}>Lorem ipsum dolor sit amet, saepe sapientem eu nam. Qui ne assum electram expetendis, omittam deseruisse consequuntur ius an,</Text> */}
              
              <TouchableOpacity style={styles.buttonContainer}>
                <Text>Edit User Preferences</Text>  
              </TouchableOpacity>              
              <TouchableOpacity style={styles.buttonContainer}>
                <Text>Edit Profile</Text> 
                </TouchableOpacity>
                   
            </View>
        </View>
      </View>
    );
  }
};

});