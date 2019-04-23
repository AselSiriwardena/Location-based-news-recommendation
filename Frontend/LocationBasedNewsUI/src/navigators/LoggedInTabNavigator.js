import {TabBarBottom, TabNavigator} from 'react-navigation';
import ExploreContainer from '../containers/ExploreContainer';
import InboxContainer from '../containers/InboxContainer';
import ProfileContainer from '../containers/ProfileContainer';
import SavedContainer from '../containers/SavedContainer';
import LocationContainer from '../containers/LocationContainer';
import colors from '../styles/colors';

const LoggedInTabNavigator = TabNavigator({
  ExploreContainer: { screen: ExploreContainer },
  SavedContainer: { screen: SavedContainer },
  LocationContainer: { screen: LocationContainer },
  InboxContainer: { screen:  InboxContainer },
  ProfileContainer: { screen: ProfileContainer },
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
