const months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];

function ageCalculate() {
    let today = new Date();
    let inputDate = new Date(document.getElementById("date-input").value);
    
    let birthDate = inputDate.getDate();
    let birthMonth = inputDate.getMonth();
    let birthYear = inputDate.getFullYear();
    
    let currentYear = today.getFullYear();
    let currentMonth = today.getMonth();
    let currentDate = today.getDate();
    
    if (
        birthYear > currentYear || (birthYear === currentYear && birthMonth > currentMonth) || (birthYear === currentYear && birthMonth === currentMonth && birthDate > currentDate)
    ) {
        alert("Not Born Yet");
        displayResult("-", "-", "-");
        return;
    }
    
    months[1] = (currentYear % 4 === 0 && (currentYear % 100 !== 0 || currentYear % 400 === 0)) ? 29 : 28;
    
    let ageYear = currentYear - birthYear;
    let ageMonth = currentMonth - birthMonth;
    let ageDate = currentDate - birthDate;
    
    if (ageDate < 0) {
        ageMonth--;
        ageDate += months[(currentMonth - 1 + 12) % 12];
    }
    
    if (ageMonth < 0) {
        ageYear--;
        ageMonth += 12;
    }
    
    displayResult(ageDate, ageMonth, ageYear);
}

function displayResult(days, months, years) {
    document.getElementById("years").textContent = years;
    document.getElementById("months").textContent = months;
    document.getElementById("days").textContent = days;
}

