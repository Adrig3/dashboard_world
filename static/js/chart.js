// Usamos la variable global definida en HTML
const cities = window.citiesData;

// Generamos labels y datos
const labels = cities.map(city => city.Name);
const populations = cities.map(city => city.Population);

// Generamos colores dinámicamente
const backgroundColors = labels.map((_, i) => {
    const hue = Math.floor((i / labels.length) * 360);
    return `hsl(${hue}, 70%, 60%)`;
});

const data = {
    labels: labels,
    datasets: [{
        label: 'Población',
        data: populations,
        backgroundColor: backgroundColors,
        borderColor: '#ffffff',
        borderWidth: 1
    }]
};

const config = {
    type: 'doughnut',
    data: data,
    options: {
        responsive: true,
        plugins: {
            legend: { display: true, position: 'right' },
            title: { display: true, text: 'Población de las ciudades' }
        }
    }
};

// Creamos el gráfico
new Chart(document.getElementById('populationChart'), config);
