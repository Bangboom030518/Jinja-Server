const colors = require('tailwindcss/colors')

/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["templates/**/*.jinja"],
  theme: {
    extend: {
      colors: {
        base: colors.white,
        secondary: colors.black,
      }
    },
  },
  plugins: [],
}
