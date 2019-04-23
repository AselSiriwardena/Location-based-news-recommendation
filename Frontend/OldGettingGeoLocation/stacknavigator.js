import React from "react";
import { View } from "react-native";
import Home from "./screens/Home";
import OTP from "./screens/OTP";
import { createStackNavigator } from "react-navigation";

const Routes = createStackNavigator(
  {
    Home: {
      screen: Home
    },
    OTP: {
      screen: OTP
    }
  },
  {
    initialRouteName: "Home",
    navigationOptions: {
      headerTitleStyle: {
        fontWeight: "bold",
        color: "#fff",
      },
      headerTintColor: "#fff"
    }
  }
);