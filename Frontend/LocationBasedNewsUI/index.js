import {
    AppRegistry,
    StatusBar
} from 'react-native';
import App from './App';

StatusBar.setBarStyle('Light-content', true);
AppRegistry.registerComponent('AirbnbClone', () => App);
