
let wrapper = document.getElementById("wrapper");

let predictGender = () => {
  let name = document.getElementById("name").value.trim();
  let error = document.getElementById("error");
  

  error.innerHTML = "";

  if (name.length > 0 && /^[A-Za-z]+$/.test(name)) {
    
    let prevInfo = document.getElementById("info");
    if (prevInfo) {
      prevInfo.remove();
    }

    fetch(`https://api.genderize.io?name=${name}`)
      .then((resp) => resp.json())
      .then((data) => {
        let div = document.createElement("div");
        div.setAttribute("id", "info");
        div.innerHTML = `
          <h2 id="result-name">${data.name}</h2>
          <img src="" id="gender-icon"/>
          <h1 id="gender">${data.gender || "Not Found"}</h1>
          <h4 id="prob">Probability: ${Math.ceil(data.probability * 100)}%</h4>
        `;
        wrapper.append(div);

        if (data.gender === "female") {
          div.classList.add("female");
          document.getElementById("gender-icon").setAttribute("src", "https://st3.depositphotos.com/27803420/33210/v/380/depositphotos_332109276-stock-illustration-female-sign-simply-vector-illustration.jpg");
        } else if (data.gender === "male") {
          div.classList.add("male");
          document.getElementById("gender-icon").setAttribute("src", "https://as2.ftcdn.net/v2/jpg/02/73/47/17/1000_F_273471769_djMJxYbSPmIBuxVlqJs5tkyljjyKvxxP.jpg");
        } else {
          document.getElementById("gender-icon").remove();
        }
      })
      .catch((err) => {
        error.innerHTML = "EROR, please try again ";
      });

    document.getElementById("name").value = "";
    document.getElementById("name").focus();
  } else {
    error.innerHTML = "Enter a valid name with no spaces or special characters.";
  }
};

document.getElementById("submit").addEventListener("click", predictGender);