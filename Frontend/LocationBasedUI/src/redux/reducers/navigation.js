import createReducer from '../helpers/createReducer';
import { NavigationActions } from 'react-navigation';
import { AppNavigator } from '../../navigators/AppNavigator';
import { StatusBar } from 'react-native';

const firstAction = AppNavigator.router.getActionForPathAndParams('LoggedIn');
const initialNavState = AppNavigator.router.getStateForAction(firstAction);

export const nav = (state = initialNavState, action) => {
   let nextState = AppNavigator.router.getStateForAction(action, state);
   //Setting status bar style dark at tabs
   if (action.routeName === 'TurnOnNotifications' || action.routeName === 'LoggedOut') {
      StatusBar.setBarStyle('dark-content', true);
   }
   return nextState || state;
};
