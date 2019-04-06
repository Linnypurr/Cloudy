import React, { Component } from 'react';
import axios from 'axios'


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
        <div >
            <input type="text" value={this.state.zipValue} onChange={this.handleChange} />
            <Submit zipValue={this.state.zipValue} />
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
                <input type="submit" value="submit" onClick={this.handleClick}></input>
                  <p>{this.state.cloud1prob}</p>
                  <p>{this.state.cloud1name}</p>
                <Results isReady = {isReady} cloudName = {cloud1name} />
                  <p>{this.state.cloud2prob}</p>
                  <p>{this.state.cloud2name}</p>
                <Results isReady = {isReady} cloudName = {cloud2name} />
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
            <p>{this.state.infoText}</p>
            </div>
        );
    }

}


export default Website;
