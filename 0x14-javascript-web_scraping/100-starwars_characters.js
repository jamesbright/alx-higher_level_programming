#!/usr/bin/node

const request = require('request');
const starWarsUri = 'https://swapi-api.alx-tools.com/api/films/'.concat(process.argv[2]);

request(starWarsUri, function (err, res, body) {
  const characters = JSON.parse(body).characters;

  for (let i = 0; i < characters.length; ++i) {
    request(characters[i], function (cErr, cRes, cBody) {
      console.log(JSON.parse(cBody).name);
    });
  }
});
