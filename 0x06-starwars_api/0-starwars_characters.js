#!/usr/bin/node

const myProcess = require('process');
const myRequest = require('request');
const argv = myProcess.argv;

if (argv.length === 3) {
  const url = 'https://swapi-api.alx-tools.com/api/films/' + argv[2];

  myRequest(url, async function (error, response, body) {
    if (error) {
      console.log(error);
    } else {
      const film = JSON.parse(body);

      for (const character of film.characters) {
        const promise = new Promise((resolve, reject) => {
          myRequest(character, function (error, response, body) {
            if (error) {
              reject(error);
            } else {
              resolve(JSON.parse(body).name);
            }
          });
        });
        console.log(await promise);
      }
    }
  });
}
