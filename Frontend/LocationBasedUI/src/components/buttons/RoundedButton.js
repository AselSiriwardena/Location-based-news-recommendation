import React, { Component } from 'react';
import PropTypes from 'prop-types';
import {
  Text,
  View,
    TouchableOpacity,
  TouchableHighlight,
  StyleSheet,
} from 'react-native';
import colors from '../../styles/colors';

export default class RoundedButton extends Component {
  render() {
  	const { text, textColor, background, icon, handleOnPress } = this.props;
  	const backgroundColor = background || 'transparent';
  	const color = textColor || colors.black;
    return (
      <TouchableOpacity
        style={[{backgroundColor},styles.wrapper]}
        onPress={handleOnPress}
        activeOpacity={0.7}
      >
        <View style={styles.buttonTextWrapper}>
          {icon}
          <Text style={[{color}, styles.buttonText]}>{text}</Text>
        </View>
      </TouchableOpacity>
    );
  }
}

RoundedButton.propTypes = {
  text: PropTypes.string.isRequired,
  textColor: PropTypes.string,
  background: PropTypes.string,
  icon: PropTypes.object,
  handleOnPress: PropTypes.func.isRequired,
};

const styles = StyleSheet.create({
  wrapper: {
    display: 'flex',
    padding: 15,
    borderRadius: 40,
    borderWidth: 1,
    borderColor: colors.white,
    marginBottom: 15,
    alignItems: 'center',
  },
  buttonTextWrapper: {
    flexDirection: 'row',
    justifyContent: 'flex-end',
  },
  buttonText: {
  	fontSize: 16,
  	width: '100%',
  	textAlign: 'center',
  }
});
