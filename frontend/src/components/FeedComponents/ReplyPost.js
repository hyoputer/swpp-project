import React from 'react';
import {connect} from 'react-redux';
import {postReply} from '../../actions';

class ReplyPost extends React.Component {
  constructor(props) {
    super(props);

    this.handlePostReply = this.handlePostReply.bind(this);
  }
  
  handlePostReply() {
    let contents = this.refs.text;
    this.props.postReply(this.props.feedID, contents.value);
    contents.value = '';
  }

  render() {
    return (
      <div id="newReply">
        <div id="newReply-title">
          reply
        </div>
        <div id="newReply-text-wrapper">
          <textarea id="newReply-text" ref="text"/>
        </div>
        <button className="newReply-post"
          id={this.props.feedID + '-newReply-post'}
          onClick={this.handlePostReply}
        >
          POST
        </button>
      </div>
    );
  }
}

let mapDispatchToProps = (dispatch) => {
  return {
    postReply: (feedId, contents) => dispatch(postReply(feedId, contents))
  };
};

export default connect(null, mapDispatchToProps)(ReplyPost);
