console.log("loaded")

module.exports = {
  devServer: {
    proxy: {
        '/api': {
          target: 'http://api:5000',
          pathRewrite: {
            '^/api': ''
          }
        }
    }
  }
}