import React, { Component } from 'react';
import {
  View,
  Text,
  FlatList ,
  StyleSheet,
} from 'react-native';
// Import getNews function from news.js
import { getNews } from '../news';
import Article from '../components/Article';
import Icon from 'react-native-vector-icons/Ionicons';

export default class InboxContainer extends Component {
  constructor(props) {
    super(props);
    // when we start the app, we want the animation to start while we load the articles
    this.state = { articles: [], refreshing: true };
    this.fetchNews = this.fetchNews.bind(this);
  }
  // Called after a component is mounted
  componentDidMount() {
    // firebase.auth().signInWithEmailAndPassword
    // ("web@imandy.ie", "123456")
    this.fetchNews();
   }
   fetchNews() {
    getNews()
    // we set refreshing to false to stop the spinner animation.
      .then(articles => this.setState({ articles, refreshing: false }))
      .catch(() => this.setState({ refreshing: false }));
  }

  handleRefresh() {
    this.setState(
      {
        refreshing: true
    },
      () => this.fetchNews()
    );
  }

  static navigationOptions = {
    tabBarLabel: 'NEWS',
    tabBarIcon: ({ tintColor }) => (
      <Icon
        name="ios-archive-outline"
        size={25}
        color={tintColor}
      />
    ),
  };

  render() {
    return (
      // <View style={styles.wrapper}>
      //   <Text>Inbox Container</Text>
      // </View>
      <FlatList
        data={this.state.articles}
        renderItem={({ item }) => <Article article={item} />}
        keyExtractor={item => item.url}
        refreshing={this.state.refreshing}
        onRefresh={this.handleRefresh.bind(this)}
      />
    );
  }
};

const styles = StyleSheet.create({
  wrapper: {
    display: 'flex',
    padding: 50,
  }
});
