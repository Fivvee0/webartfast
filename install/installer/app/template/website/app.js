document.addEventListener("DOMContentLoaded", (event) => {
  const htmlContent = `<h1>Hello world!</h1>`;

  const appDiv = document.getElementById("App");
  if (appDiv) {
    appDiv.innerHTML = htmlContent;
  } else {
    console.error('Element with id "App" not found');
  }
});
