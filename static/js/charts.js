document.addEventListener('DOMContentLoaded', () => {
    const ctx = document.getElementById('GChart').getContext('2d');

    // Sample data

    const gamesData = {{ GData | safe}};
    console.log(gamesData)

// Parse the dates to JS
gamesData.forEach((d) => {
    d.x = new Date(d.date);
});

// Render the chart
const chart = new Chart(ctx, {
    type: 'bar',
    data: {
        datasets: [
            {
                label: 'Partidas por día',
                data: gamesData,
                backgroundColor: 'rgba(220,20,20,0.5)',
            },
        ],
    },
    options: {
        responsive: true,
        scales: {
            xAxes: [
                {
                    type: 'time',
                    time: {
                        unit: 'day',
                        round: 'day',
                        displayFormats: {
                            day: 'MMM D',
                        },
                    },
                },
            ],
            yAxes: [
                {
                    ticks: {
                        beginAtZero: true,
                    },
                },
            ],
        },
    },
});
});