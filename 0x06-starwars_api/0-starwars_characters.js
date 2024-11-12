#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.hbtn.io/api/films/${movieId}/`;

request(apiUrl, function (error, response, body) {
  if (error) {
    console.error('Error:', error);
    return;
  }

  const characters = JSON.parse(body).characters;
  const promises = characters.map((character) => {
    return new Promise((resolve, reject) => {
      request(character, function (error, response, body) {
        if (error) {
          reject(error);
        } else {
          resolve(JSON.parse(body).name);
        }
      });
    });
  });

  Promise.all(promises)
    .then((names) => {
      names.forEach((name) => {
        console.log(name);
      });
    })
    .catch((error) => {
      console.error('Error:', error);
    });
});
