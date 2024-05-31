
const form = document.getElementById('conversion-form');
const exchangeRateDisplay = document.getElementById('exchange-rate');

form.addEventListener('submit', function(event) {
    event.preventDefault();

    const fromCurrency = document.getElementById('from-currency').value;
    const toCurrency = document.getElementById('to-currency').value;

    const exchangeRates = {
        usd: { usd: 1, gel: 3.5, euro: 0.85 },
        gel: { usd: 0.28, gel: 1, euro: 0.25 },
        euro: { usd: 1.18, gel: 4, euro: 1 }
    };

    if (fromCurrency in exchangeRates && toCurrency in exchangeRates[fromCurrency]) {
        const exchangeRate = exchangeRates[fromCurrency][toCurrency];
        exchangeRateDisplay.textContent = `1 ${fromCurrency} = ${exchangeRate} ${toCurrency}`;
    } else {
        exchangeRateDisplay.textContent = 'Exchange rate not available';
    }
});

