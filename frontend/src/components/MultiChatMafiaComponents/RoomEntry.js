import React from 'react';
import {connect} from 'react-redux';
import {startMultiChat} from '../../actions';

class MultiChatRoomEntry extends React.Component {
  constructor(props) {
    super(props);
    this.handleStartMultiChat = this.handleStartMultiChat.bind(this);
  }

  componentDidMount() {
    this.enterTag = null;
    if (this.props.multichatEnterList.indexOf(this.props.id) !== -1)
      this.enterTag = '참석중!';
  }

  handleStartMultiChat() {
    this.props.startMultiChat(this.props.id);
  }

  render() {
    return (
      <div className="multichat-room" id={'multichat-room-id-'+this.props.id} onClick={this.handleStartMultiChat}>
        <div className="multichat-room-id">
          { this.props.id }
        </div>
        <div className="multichat-room-count">
          { (this.props.multichatCountList[this.props.id-1]) +'명 참가' }
        </div>
        <div className="multichat-room-enter">
          { this.enterTag }
        </div>
      </div>
    );
  }
}

let mapStateToProps = (state) => {
  return {
    multichatRoomIDList: state.multichat.multichatRoomIDList,
    multichatRoomList: state.multichat.multichatRoomList,
    multichatEnterList: state.multichat.multichatEnterList,
    multichatCountList: state.multichat.multichatCountList
  };
};

let mapDispatchToProps = (dispatch) => {
  return {
    startMultiChat: (multichatRoomID) => dispatch(startMultiChat(multichatRoomID)),
  };
};

export default connect(mapStateToProps, mapDispatchToProps)(MultiChatRoomEntry);
