import React, { Component } from 'react';
import axios from 'axios'
//import Request from "./GetRequests"

//var request = require('request');


class Website extends Component {

  constructor () {
      super()
      this.state = {
        probs: ''
      }

      this.handleClick = this.handleClick.bind(this)
  }

  handleClick () {
    axios.get('http://localhost:5000/cloud/prob/98333')
        .then(response => this.setState({probs: response.data}))

  }

  render () {
    return (
      <div className='button__container'>
        <button className='button' onClick={this.handleClick}>Click Me</button>
        <p>{this.state.probs}</p>
      </div>
    )
  }
}

export default Website;
