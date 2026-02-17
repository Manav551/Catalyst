module.exports = (function () {
  const cfg = require('./postcss.config.js');
  // if original exports default (ESM), cfg.default will exist; fall back to cfg itself
  return cfg && cfg.default ? cfg.default : cfg;
})();