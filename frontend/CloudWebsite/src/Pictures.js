import React, { Component } from 'react';

  const Altostratus = require('./CloudPictures/altostratus.png');
      const Stratus = require('./CloudPictures/stratus.jpg');
        const Altostratus = require('./CloudPictures/altostratus.png');
        const Stratus = require('./CloudPictures/stratus.jpg');
        const Altocumulous = require('./CloudPictures/altocumulous.jpg');
        const Cirrocumulus = require('./CloudPictures/Cirrocumulus.jpeg');
        const Cirrostratus = require('./CloudPictures/cirrostratus.jpg');
        const Cirrus = require('./CloudPictures/cirrus.jpg');
        const Cumulonimbus= require('./CloudPictures/cumulonimbus.jpg');
        const Nimbostratus = require('./CloudPictures/nimbostratus.png');
        const Stratocumulus = require('./CloudPictures/stratocumulus.jpeg');
      picList: [Altostratus, Stratus],

            { this.state.showResults ? <Results.renderResults /> : null}
            <p>{this.state.cloud1prob}</p>
            <p>{this.state.cloud1name}</p>
            <p>{this.state.cloud2prob}</p>
            <p>{this.state.cloud2name}</p>

function Pictures(picList, cloudname) {
    var index = 0;
    for(let i = 0; i < 11; i++) {
        if (picList[i] === cloudname) {
            index = i;
        }
    }

    return index;
}

export default Pictures;