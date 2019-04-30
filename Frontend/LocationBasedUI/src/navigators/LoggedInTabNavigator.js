import {
    StackNavigator,
    TabBarBottom,
    TabNavigator,
} from 'react-navigation';
import ExploreContainer from '../containers/ExploreContainer';
import InboxContainer from '../containers/InboxContainer';
import ProfileContainer from '../containers/ProfileContainer';
import SavedContainer from '../containers/SavedContainer';
import LocationContainer from '../containers/LocationContainer';
import CreateList from '../screens/CreateList';     //added my own containers
import colors from '../styles/colors';

export const ExploreTab = StackNavigator({
    ExploreContainer: { screen: ExploreContainer},
    CreateList: { screen: CreateList},
},
    {
        mode: 'modal',
    });

const LoggedInTabNavigator = TabNavigator({
  Explore: { screen: ExploreContainer },
  Saved: { screen: SavedContainer },
  Location: { screen: LocationContainer },
  Inbox: { screen:  InboxContainer },
  Profile: { screen: ProfileContainer },
}, {
    tabBarComponent: TabBarBottom,
    tabBarPosition: 'bottom',
  tabBarOptions: {
  	labelStyle: {
  	  fontWeight: '600',
  	  marginBottom: 5,
  	},
    activeTintColor: colors.pink,
      inactiveTintColor: 'gray'
  },
});

export default LoggedInTabNavigator;
