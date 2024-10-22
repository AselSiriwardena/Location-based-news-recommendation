import React from 'react';
import { View, Linking,StyleSheet,Image,TouchableOpacity,TouchableNativeFeedback } from 'react-native';
import { Text, Button, Card, Divider } from 'react-native-elements';
import moment from 'moment';

// import * as firebase from 'firebase'

// var currentUser



export default class Article extends React.Component {

  // addToFavourites = async(newsName) => {

  //   //getting current user
  //   currentUser = await firebase.auth().currentUser

  //   //get a unique key
  //   var databaseRef = await firebase.database().ref(currentUser.uid).child('favourites').push()

  //       //update the name at the unique key
  //       databaseRef.set({
  //           'name': newsName
  //       })
  // }

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
    const {
      title,
      description,
      publishedAt,
      source,
      urlToImage,
      url
    } = this.props.article;
    // In render we define time to store the time for when the article was published. We use the moment library to convert the date to the time passed since then, and we pass publishedAt or time from now if publishedAt is null.
    const { noteStyle, featuredTitleStyle } = styles;
    const time = moment(publishedAt || moment.now()).fromNow();
    //In case of image is null
    const defaultImg =
      'https://wallpaper.wiki/wp-content/uploads/2017/04/wallpaper.wiki-Images-HD-Diamond-Pattern-PIC-WPB009691.jpg';

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
      <TouchableNativeFeedback
        useForeground
        onPress={() => Linking.openURL(url)}
      >
        <Card
          featuredTitle={title}
          featuredTitleStyle={featuredTitleStyle}
          image={{
            uri: urlToImage || defaultImg
          }}
        >
          <Text style={{ marginBottom: 10 }}>
            {description || 'Read More..'}
          </Text>
          {/* <View>
            <Button onPress={() =>
              this.addToFavourites(source.name)}
              title="+ Favourites"></Button>
          </View> */}
          <View style={styles.childView}>
          {React_Native_Rating_Bar}
          {/* <Text>
          {this.state.Default_Rating} / {this.state.Max_Rating}
          </Text> */}

          </View>
          <Divider style={{ backgroundColor: '#dfe6e9' }} />
          <View
            style={{ flexDirection: 'row', justifyContent: 'space-between' }}
          >
            <Text style={noteStyle}>{source.name.toUpperCase()}</Text>
            <Text style={noteStyle}>{time}</Text>
          </View>
        </Card>

      </TouchableNativeFeedback>
    );
  }
}

const styles = {
  noteStyle: {
    margin: 5,
    fontStyle: 'italic',
    color: '#b2bec3',
    fontSize: 10
  },
  childView: {
    // justifyContent: 'center',
    flexDirection: 'row',
    marginTop: -2,
  },
  StarImage: {
    width: 20,
    height: 20,
    resizeMode: 'cover',
    marginLeft: 6,
  },
  featuredTitleStyle: {
    marginHorizontal: 5,
    textShadowColor: '#00000f',
    textShadowOffset: { width: 3, height: 3 },
    textShadowRadius: 3
  }
};

