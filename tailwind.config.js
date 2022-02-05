const colors = require("tailwindcss/colors")

module.exports = {
  mode: 'jit',
  purge: ['./app/templates/**/*.html'],
  darkMode: false, // or 'media' or 'class'
  theme: {
    extend: {
      colors: {
        primary: "#292828",
        secondary: "#cb6ce6",
      }
    }
  },
  variants: {
    extend: {},
  },
  plugins: [],
}
