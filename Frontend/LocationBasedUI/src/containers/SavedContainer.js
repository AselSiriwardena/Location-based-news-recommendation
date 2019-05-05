import React, { Component } from 'react';
import {
  View,
  FlatList,
  Image,
  Text,
  TouchableOpacity,
  StyleSheet,
} from 'react-native';
import { data } from '../data2';
import {
  RkText,
  RkCard, RkStyleSheet,
} from 'react-native-ui-kitten';
// import {SocialBar} from '../components/socialBar';
import Icon from 'react-native-vector-icons/Ionicons';
// import NoResults from '../components/saved/NoResults';
import colors from '../styles/colors';
import NavigationType from '../config/navigation/propTypes';

const moment = require('moment');


export default class InboxContainer extends Component {
  static propTypes = {
    navigation: NavigationType.isRequired,
  };
 
  static navigationOptions = {
    tabBarLabel: 'SAVED',
    tabBarIcon: ({ tintColor }) => (
        <Icon
            name="ios-heart-outline"
            size={22}
            color={tintColor}
        />
    ),
  };

  state = {
    data: data.getArticles(),
  };

  extractItemKey = (item) => `${item.id}`;

  onItemPressed = (item) => {
    this.props.navigation.navigate('Article', { id: item.id });
  };

  componentDidMount(){
    return fetch('http://192.168.8.100:8000/category/')
      .then((response) => response.json())
      .then((responseJson) => {

        this.setState({
          isLoading: false,
          dataSource: responseJson,
        }, function(){

        });

      })
      .catch((error) =>{
        console.error(error);
      });
  }

  //onItempress navigation missing
  renderItem = ({ item }) => (
    <TouchableOpacity
    delayPressIn={70}
    activeOpacity={0.8}
    onPress={() => this.onItemPressed(item)}>
    <RkCard rkType='blog' style={styles.card}>
        {/* <Image rkCardImg source={item.photo} /> */}
        <View rkCardHeader style={styles.content}>
          <RkText style={styles.section} rkType='header4'>{item.title}</RkText>
        </View>
        <View rkCardContent>
          <View>
            <RkText rkType='primary3 mediumLine' numberOfLines={2}>{item.summary}</RkText>
          </View>
        </View>
        <View rkCardFooter>
          <View style={styles.userInfo}>
            {/* <Avatar style={styles.avatar} rkType='circle small' img={item.user.photo} /> */}
            {/* <RkText rkType='header6'>{`${item.user.firstName} ${item.user.lastName}`}</RkText> */}
          </View>
          <RkText rkType='secondary2 hintColor'>{moment().add(item.date_time, 'seconds').fromNow()}</RkText>
        </View>
      </RkCard>
    </TouchableOpacity>
  );

  render() {
    return (
      <FlatList
      data={this.state.dataSource}
      renderItem={this.renderItem}
      keyExtractor={this.extractItemKey}
      style={styles.container}
    />
    );
  }
};



const styles = RkStyleSheet.create(theme => ({
  container: {
    backgroundColor: theme.colors.screen.scroll,
    paddingVertical: 8,
    paddingHorizontal: 14,
  },
  card: {
    marginVertical: 8,
  },
  userInfo: {
    flexDirection: 'row',
    alignItems: 'center',
  },
  
}));
