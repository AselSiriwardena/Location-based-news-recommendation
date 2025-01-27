import React, { Component } from 'react';
import colors from '../styles/colors';
import Icon from 'react-native-vector-icons/Ionicons';
import {
    View,
    Text,
    StyleSheet,
} from 'react-native';

export default class SearchBar extends Component {
    render() {
        return (
            <View style={styles.wrapper}>
                <View style={styles.searchContainer}>
                    <Icon
                        name="ios-search"
                        size={20}
                        color={colors.gray02}
                        style={styles.searchIcon}
                    />
                    <Text style={styles.textInput}>Try "Matara"</Text>
                </View>
            </View>
        );
    }
};

const styles = StyleSheet.create({
    wrapper: {
        position: 'absolute',
        top: -20,
        left: 0,
        backgroundColor: 'rgba(255,255,255,0.9)',   //Making this semi transparent we can see scrolling to top
        width: '100%',
        height: 80,
        zIndex: 99,
    },
    searchContainer: {
        display: 'flex',
        borderWidth: 1,
        borderColor: colors.gray03,
        backgroundColor: colors.white,
        shadowColor: 'rgba(0,0,0,0.1)',
        shadowOffset: { width: 0, height: 5 },
        shadowOpacity: 0.7,
        shadowRadius: 10,
        borderRadius: 3,
        height: 40,
        marginTop: 28,
        marginLeft: 21,
        marginRight: 21,
    },
    searchIcon: {
        position: 'absolute',
        left: 18,
        top: 9,
    },
    textInput: {
        display: 'flex',
        marginTop: 11,
        marginLeft: 44,
        color: colors.gray02,
    },
});
