import React, { Component } from 'react';
import { Provider } from 'react-redux';
import store from './src/redux/store';
import { createReduxBoundAddListener } from 'react-navigation-redux-helpers';
import AppWithNavigationState from './src/navigators/AppNavigator';
import * as firebase from 'firebase';

// Your web app's Firebase configuration
var firebaseConfig = {
  apiKey: "AIzaSyBJRzmRgaitddn12dRn4HwmhzBeiYizqOY",
    authDomain: "ratingfront.firebaseapp.com",
    databaseURL: "https://ratingfront.firebaseio.com",
    projectId: "ratingfront",
    storageBucket: "ratingfront.appspot.com",
    messagingSenderId: "569652245761"
};
// Initialize Firebase
firebase.initializeApp(firebaseConfig);

console.disableYellowBox = true;

export default class App extends Component {
  render() {
    return (
      <Provider store={store}>
        <AppWithNavigationState listener={createReduxBoundAddListener('root')} />
      </Provider>
    );
  }
}
