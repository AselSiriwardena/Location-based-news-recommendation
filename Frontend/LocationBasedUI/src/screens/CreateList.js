import React, { Component } from 'react';
import {
    View,
    Text,
    StyleSheet,
} from 'react-native';

export default class CreateList extends Component {

    render() {
        return (
            <View style={styles.wrapper}>
                <Text>Profile Container</Text>
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
