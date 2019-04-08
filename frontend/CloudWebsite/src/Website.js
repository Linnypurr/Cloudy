import React, { Component } from 'react';
import axios from 'axios'
import './style.css'

class Website extends Component {

  constructor (props) {
      super(props)

      this.state = {
        zipValue: ''
      }


      this.handleChange = this.handleChange.bind(this)
  }

  handleChange(event) {
    this.setState({zipValue: event.target.value})
  }


  render () {
      return(
        <div>
            <div className="Title">
                <h1>Cloud Probability</h1>
                <h4>Enter your zipcode:</h4>
            </div>
            <div className="textDiv">
                <input type="text" className="textInput" value={this.state.zipValue} onChange={this.handleChange} />
                <Submit zipValue={this.state.zipValue} />
            </div>
        </div>
        );


  }
}

class Submit extends Component {

    constructor(props) {
        super(props)

        this.state = {
            cloud1prob: '',
            cloud1name: '',
            cloud2prob: '',
            cloud2name: '',
            showResults: false,
        }

        this.handleClick = this.handleClick.bind(this)
        this.functionTest = this.functionTest.bind(this)
    }

    functionTest () {
        console.log("inside function test")
        this.setState({showResults: true})
    }

    handleClick () {
        const urlApi = 'http://localhost:5000/cloud/prob/';
        const zipcode = this.props.zipValue
        axios.get(urlApi + zipcode)
            .then(response => this.setState({cloud1prob: response.data[0][0], cloud1name: response.data[0][1]
            , cloud2prob: response.data[1][0], cloud2name: response.data[1][1], showResults: true}))
    }


    render() {
     const isReady = this.state.showResults;
     const cloud1name = this.state.cloud1name
     const cloud2name = this.state.cloud2name

        return(
        <div>
            <input type="submit" className="submitInput" value="submit" onClick={this.handleClick}></input>
            <div>
              <h3 className ="probText">{this.state.cloud1prob}</h3>
              <h3 className ="probText">{this.state.cloud1name}</h3>
            <Results isReady = {isReady} cloudName = {cloud1name} />
              <h3 className ="probText">{this.state.cloud2prob}</h3>
              <h3 className ="probText">{this.state.cloud2name}</h3>
            <Results isReady = {isReady} cloudName = {cloud2name} />
            </div>
        </div>
        );


    }

}


class Results extends Component {

    constructor(props) {
        super(props)

        this.state = {
            infoText: ''
        }

        this.handleImgClick = this.handleImgClick.bind(this)
    }

    handleImgClick () {
        const urlApi = 'http://localhost:5000/cloud/info/';
        const picInfo = this.props.cloudName
        axios.get(urlApi + picInfo)
            .then(response => this.setState({infoText: response.data}))

    }

    render() {
        const cloudName = this.props.cloudName
        if(!this.props.isReady) {
            return null;
        }
        return(
            <div>
            <img src={require("./CloudPictures/"+cloudName+'.jpg')} alt="" height="400" width="600" onClick={this.handleImgClick} />
            <h4 className="infoText">{this.state.infoText}</h4>
            </div>
        );
    }

}


export default Website;
