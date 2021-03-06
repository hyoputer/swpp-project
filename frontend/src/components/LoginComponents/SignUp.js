import React from 'react';
import {connect} from 'react-redux';
import {newID, newNick, newPW, retypePW,toMain} from '../../actions';

class SignUp extends React.Component {
  constructor(props) {
    super(props);

    this.handleUpdateID = this.handleUpdateID.bind(this);
    this.handleUpdateNick = this.handleUpdateNick.bind(this);
    this.handleUpdatePW = this.handleUpdatePW.bind(this);
    this.handleUpdateRetypePW = this.handleUpdateRetypePW.bind(this);
    this.handleToMain = this.handleToMain.bind(this);
    this.passwordCheck = this.passwordCheck.bind(this);
    this.handleKeyPress = this.handleKeyPress.bind(this);
  }

  handleUpdateID(e) {
    this.props.onUpdateID(e.target.value);
  }

  handleUpdateNick(e) {
    this.props.onUpdateNick(e.target.value);
  }

  handleUpdatePW(e) {
    this.props.onUpdatePW(e.target.value);
  }
	
  handleUpdateRetypePW(e) {
    this.props.onUpdateRetypePW(e.target.value);
  }

  handleToMain() {
    this.props.toMain();
  }

  passwordCheck() {
    if (this.props.newPW === '' || this.props.retypePW === '')
      return '-';
    return ((this.props.newPW === this.props.retypePW)? 'O':'X');
  }

  handleKeyPress(e) {
    if(e.key === 'Enter')
      this.handleToMain();
  }

  render() {
    return (<div id="login">
      <div className="line-thick">Sign Up</div>
      <div className="line">
        <div id="username">ID</div>
        <input type="text" id="input-username" onChange={this.handleUpdateID}/>
      </div>
      <div className="line">
        <div id="nickname">Nickname</div>
        <input type="text" id="input-nickname" onChange={this.handleUpdateNick}/>
      </div>
      <div className="line">
        <div id="password">Password</div>
        <input type="password" id="input-password" onChange={this.handleUpdatePW}/>
      </div>
      <div className="line-thick">
        <div id="retypepassword">retype PW</div>
        <input type="password" id="input-retypepassword"
          onChange={this.handleUpdateRetypePW}
          onKeyPress={this.handleKeyPress}
        />
				<div id="password-check">{this.passwordCheck()}</div>
      </div>
      <div>
        <button id="SignUp" className="loginButtons" onClick={this.handleToMain}>Sign Up</button>
      </div>
    </div>);
  }
}

let mapStateToProps = (state) => {
  return {
    newPW : state.server.newPW,
    retypePW : state.server.retypePW
  };
};

let mapDispatchToProps = (dispatch) => {
  return {
    onUpdateID: (value) => dispatch(newID(value)),
    onUpdateNick: (value) => dispatch(newNick(value)),
    onUpdatePW: (value) => dispatch(newPW(value)),
    onUpdateRetypePW: (value) => dispatch(retypePW(value)),
    toMain: () => dispatch(toMain())
  };
};

export default connect(mapStateToProps, mapDispatchToProps)(SignUp);
