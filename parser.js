const { parse } = require('path');

class Parser {
  static parsePath(filePath) {
    const parsedPath = parse(filePath);
    return {
      name: parsedPath.name,
      dir: parsedPath.dir,
      ext: parsedPath.ext,
      root: parsedPath.root,
      base: parsedPath.base,
    };
  }

  static parseQueryString(queryString) {
    const params = {};
    if (queryString) {
      const pairs = queryString.split('&');
      pairs.forEach((pair) => {
        const [key, value] = pair.split('=');
        if (key && value) {
          params[key] = decodeURIComponent(value);
        }
      });
    }
    return params;
  }
}

module.exports = Parser;