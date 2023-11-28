const themeToggleDarkIcon = document.getElementById("theme-toggle-dark-icon");
const themeToggleLightIcon = document.getElementById("theme-toggle-light-icon");

// // Change the icons inside the button based on previous settings
// if (
//   localStorage.getItem("color-theme") === "dark" ||
//   (!("color-theme" in localStorage) &&
//     window.matchMedia("(prefers-color-scheme: dark)").matches)
// ) {
//   themeToggleLightIcon.classList.remove("hidden");
//   console.log("dark mode");
// } else {
//   themeToggleDarkIcon.classList.remove("hidden");
//   console.log("light mode");
// }

// const themeToggleBtn = document.getElementById("theme-toggle");

// let event = new Event("dark-mode");

// themeToggleBtn.addEventListener("click", function () {
//   // toggle icons
//   themeToggleDarkIcon.classList.toggle("hidden");
//   themeToggleLightIcon.classList.toggle("hidden");

//   // if set via local storage previously
//   if (localStorage.getItem("color-theme")) {
//     if (localStorage.getItem("color-theme") === "light") {
//       document.documentElement.classList.add("dark");
//       localStorage.setItem("color-theme", "dark");
//     } else {
//       document.documentElement.classList.remove("dark");
//       localStorage.setItem("color-theme", "light");
//     }

//     // if NOT set via local storage previously
//   } else {
//     if (document.documentElement.classList.contains("dark")) {
//       document.documentElement.classList.remove("dark");
//       localStorage.setItem("color-theme", "light");
//     } else {
//       document.documentElement.classList.add("dark");
//       localStorage.setItem("color-theme", "dark");
//     }
//   }

//   document.dispatchEvent(event);
// });


{
    let event = new Event("dark-mode");

  window.addEventListener("load", function (e) {
    function setTheme(mode) {
      if (mode !== "light" && mode !== "dark" && mode !== "auto") {
        console.error(`Got invalid theme mode: ${mode}. Resetting to auto.`);
        mode = "auto";
      }

      if (mode === "dark") {
        themeToggleLightIcon.classList.remove("hidden");
        document.documentElement.classList.remove("light");
        themeToggleDarkIcon.classList.add("hidden");
        document.documentElement.classList.add("dark");
      } else {
        themeToggleLightIcon.classList.add("hidden");
        document.documentElement.classList.add('light')
        themeToggleDarkIcon.classList.remove("hidden");
        document.documentElement.classList.remove('dark')
      }

      localStorage.setItem("color-theme", mode);
   

      console.log(`theme set: ${mode}`);
      // set theme code here
    }


    function cycleTheme() {
      const currentTheme = localStorage.getItem("color-theme") || "auto";
      const prefersDark = window.matchMedia(
        "(prefers-color-scheme: dark)"
      ).matches;

      if (prefersDark) {
        // Auto (dark) -> Light -> Dark
        if (currentTheme === "auto") {
          setTheme("light");
        } else if (currentTheme === "light") {
          setTheme("dark");
        } else {
          setTheme("light");
        }
      } else {
        // Auto (light) -> Dark -> Light
        if (currentTheme === "auto") {
          setTheme("dark");
        } else if (currentTheme === "dark") {
          setTheme("light");
        } else {
          setTheme("dark");
        }
      }

      document.dispatchEvent(event);

    }

    function initTheme() {
      // set theme defined in localStorage if there is one, or fallback to auto mode
      const currentTheme = localStorage.getItem("color-theme");
      currentTheme ? setTheme(currentTheme) : setTheme("auto");

    }

    function setupTheme() {
      // Attach event handlers for toggling themes
      const button = document.getElementById("theme-toggle");
      button.addEventListener("click", cycleTheme);
      initTheme();
    }

    setupTheme();
  });
}
