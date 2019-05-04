//This is an example code to make a Star Rating Bar // 
import React, { Component } from 'react';
//import react in our code. 
import {
  StyleSheet,
  View,
  Platform,
  Text,
  Image,
  TouchableOpacity,
} from 'react-native';
//import all the components we are going to use.
import * as firebase from 'firebase';

// var firebaseConfig = { // yours
//   apiKey: "AIzaSyBGkjZlPb6rikmmIaKUaVohWEru8JG3lLI",
//     authDomain: "test2-f9e73.firebaseapp.com",
//     databaseURL: "https://test2-f9e73.firebaseio.com",
//     projectId: "test2-f9e73",
//     storageBucket: "test2-f9e73.appspot.com",
//     messagingSenderId: "374924886708",
//     appId: "1:374924886708:web:2d9ae903e2607534"
// };
var firebaseConfig = { // mine
  apiKey: "AIzaSyBvLfWskE0cSngaLjy2WnaxSNtHdgw1zuE",
  authDomain: "messenger-test-40575.firebaseapp.com",
  databaseURL: "https://messenger-test-40575.firebaseio.com",
  projectId: "messenger-test-40575",
  storageBucket: "messenger-test-40575.appspot.com",
  messagingSenderId: "540508529569",
  // appId: "1:540508529569:web:d02598553991c53b"
};
firebase.initializeApp(firebaseConfig);

var currentUser


export default class Myapp extends Component {

  componentDidMount() {

    firebase.auth().signInWithEmailAndPassword("web@imandy.ie", "123456").catch(
      function (err) {
        alert(err.message);
        firebase = null;
        return;
      }
    )
  }

  addToFavourites = async () => {

    //get current user 
    if (firebase == null) {
      alert("Firebase authentication failed");
      return;
    }
    currentUser = await firebase.auth().currentUser
    if (currentUser == null) {
      alert("User is not logged in");
      return;
    }

    //get a unique key 
    var databaseRef = await firebase.database().ref(currentUser.uid).child('favourites')
      .push()
      .catch(
        function (err) {
          alert(err.message);
          return;
        }
      )

    //update the beername at the unique key
    databaseRef.set({
      'name': this.state.Default_Rating
    }).catch(
      function (err) {
        alert(err.message);
        return;
      }
    )

  }
  constructor() {
    super();
    this.state = {
      Default_Rating: 2,
      //To set the default Star Selected
      Max_Rating: 5,
      //To set the max number of Stars
    };
    //Filled Star. You can also give the path from local
    this.Star = 'http://aboutreact.com/wp-content/uploads/2018/08/star_filled.png';

    //Empty Star. You can also give the path from local
    this.Star_With_Border = 'http://aboutreact.com/wp-content/uploads/2018/08/star_corner.png';
  }
  UpdateRating(key) {
    this.setState({ Default_Rating: key });
    //Keeping the Rating Selected in state
  }
  render() {
    let React_Native_Rating_Bar = [];
    //Array to hold the filled or empty Stars
    for (var i = 1; i <= this.state.Max_Rating; i++) {
      React_Native_Rating_Bar.push(
        <TouchableOpacity
          activeOpacity={0.7}
          key={i}
          onPress={this.UpdateRating.bind(this, i)}>
          <Image
            style={styles.StarImage}
            source={
              i <= this.state.Default_Rating
                ? { uri: this.Star }
                : { uri: this.Star_With_Border }
            }
          />
        </TouchableOpacity>
      );
    }
    return (
      <View style={styles.MainContainer}>
        <Text style={styles.textStyle}>How was your experience with us</Text>
        <Text style={styles.textStyleSmall}>Please Rate Us</Text>
        {/*View to hold our Stars*/}
        <View style={styles.childView}>{React_Native_Rating_Bar}</View>

        <Text style={styles.textStyle}>
          {/*To show the rating selected*/}
          {this.state.Default_Rating} / {this.state.Max_Rating}
        </Text>

        <TouchableOpacity
          activeOpacity={0.7}
          style={styles.button}
          onPress={() => this.addToFavourites(this.state.Default_Rating)}>
          {/*Clicking on button will show the rating as an alert*/}
          <Text>Get Selected Value</Text>
        </TouchableOpacity>
      </View>
    );
  }
}

const styles = StyleSheet.create({
  MainContainer: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    paddingTop: Platform.OS === 'ios' ? 20 : 0,
  },
  childView: {
    justifyContent: 'center',
    flexDirection: 'row',
    marginTop: 30,
  },
  button: {
    justifyContent: 'center',
    flexDirection: 'row',
    marginTop: 30,
    padding: 15,
    backgroundColor: '#8ad24e',
  },
  StarImage: {
    width: 40,
    height: 40,
    resizeMode: 'cover',
  },
  textStyle: {
    textAlign: 'center',
    fontSize: 23,
    color: '#000',
    marginTop: 15,
  },
  textStyleSmall: {
    textAlign: 'center',
    fontSize: 16,

    color: '#000',
    marginTop: 15,
  },
});