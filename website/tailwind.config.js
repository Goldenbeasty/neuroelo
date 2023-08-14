module.exports = {
  content: [
    './src/*.{js,html}',
    './neuroelo_web/vedal-data/*.{js,html}',
  ],
  theme: {
    extend: {
      colors: {
        // Define your custom colors here
        pink: {
          main: "#f5a1ad",
          shadow: "#ed839b",
        },
        beige: {
          main: "#f8e6c7",
          darker: "#b19483",
        },
        green: {
          main: "#a0d99c",
          darker: "#35965a",
        },
      },
    },
  },
  variants: {
    extend: {},
  },
  plugins: [],
};
