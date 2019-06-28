import React, { Component } from 'react';
import {
    View,
    Text,
    ScrollView,
    StyleSheet,
} from 'react-native';
import Icon from 'react-native-vector-icons/Ionicons';
import SearchBar from '../components/SearchBar';
import Categories from '../components/explore/Categories';
import Listings from '../components/explore/Listings';
import colors from '../styles/colors';
import categoriesList from '../data/categories';
import listings from '../data/listings';

export default class InboxContainer extends Component {
    static navigationOptions = {
        tabBarLabel: 'EXPLORE',
        tabBarIcon: ({ tintColor }) => (
            <Icon
                name="ios-search"
                size={22}
                color={tintColor}
            />
        ),
    };

    constructor(props) {
        super(props);
        this.handleAddToFav= this.handleAddToFav.bind(this);
    }

    handleAddToFav() {
        const {navigate } = this.props.navigation;
        navigate('CreateList');
    }

    renderListings() {
        return listings.map((listing, index) => {
            return (
                <View
                    key={`listing-${index}`}
                >
                    <Listings
                        key={`listing-item-${index}`}
                        title={listing.title}
                        boldTitle={listing.boldTitle}
                        listings={listing.listings}
                        showAddToFav={listing.showAddToFav}
                        handleAddToFav ={this.handleAddToFav}
                    />
                </View>
            );
        });
    }

    render() {
        return (
            <View style={styles.wrapper}>
                <SearchBar />
                <ScrollView
                    style={styles.scrollview}
                    contentContainerStyle={styles.scrollViewContent}
                >
                    <Text style={styles.heading}>Explore Noticias</Text>
                    <View style={styles.categories}>
                        <Categories categories={categoriesList} />
                    </View>
                    {this.renderListings()}
                </ScrollView>
            </View>
        );
    }
};

const styles = StyleSheet.create({
    wrapper: {
        flex: 1,
        backgroundColor: colors.white,
    },
    scrollview: {
        // paddingTop: 100,
        paddingTop: 80,
    },
    scrollViewContent: {
        paddingBottom: 80,
    },
    categories: {
        marginBottom: 40,
    },
    heading: {
        fontSize: 22,
        fontWeight: '600',
        paddingLeft: 20,
        paddingBottom: 20,
        color: colors.gray04,
    }
});
