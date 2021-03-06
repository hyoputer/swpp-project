import React from 'react';
import {Redirect} from 'react-router';
import {connect} from 'react-redux';
import BeforeMultiChatMain from './MultiChatMafiaComponents/BeforeMultiChatMain';
import MultiChatMain from './MultiChatMafiaComponents/Main';

class MultiChat extends React.Component {
  render() {
    console.log('MultiChat What?');
    console.log('multichatOn: ',this.props.multichatOn);
    console.log('multichatRoomID: ',this.props.multichatRoomID);
    if(this.props.isLoggedIn){
      if(this.props.multichatOn){
        if(this.props.multichatRoomID === null)
          return <BeforeMultiChatMain/>;
        return <MultiChatMain/>;
      }
      return <Redirect to="/"/>;
    }
    return <Redirect to="/login/"/>;
  }
}

let mapStateToProps = (state) => {
  return {
    isLoggedIn : state.server.loggedIn,
    multichatOn : state.multichat.multichatOn,
    multichatRoomID : state.multichat.multichatRoomID,
  };
};

export default connect(mapStateToProps)(MultiChat);
