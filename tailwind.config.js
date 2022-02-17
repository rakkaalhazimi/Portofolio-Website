const colors = require("tailwindcss/colors")

module.exports = {
  mode: 'jit',
  purge: ['./app/templates/**/*.html'],
  darkMode: false, // or 'media' or 'class'
  theme: {
    container: {
      center: true,
    },
    extend: {
      colors: {
        primary: '#292828',
        secondary: '#cb6ce6',
        tertiary: '#5d17ad',
        tertiary_accent: '#42107A'

      }
    }
  },
  variants: {
    extend: {},
  },
  plugins: [],
}
