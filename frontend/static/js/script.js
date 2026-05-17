// =====================================================
// CHART VARIABLES
// =====================================================

let cuisineChart;
let ratingChart;
let topRatedChart;
let cuisinePopularityChart;

// =====================================================
// LOAD DASHBOARD
// =====================================================

async function loadDashboard() {

    try {

        // =========================================
        // GET SELECTED CITY
        // =========================================

        const selectedCity =

            document.getElementById(
                'city-select'
            ).value;

        // =========================================
        // FETCH DATA
        // =========================================

        const response =

            await fetch(
                `/dashboard-data?city=${selectedCity}`
            );

        const data =
            await response.json();

        console.log(data);

        // =========================================
        // LOAD ALL INDIAN CITIES
        // =========================================

        const citySelect =

            document.getElementById(
                'city-select'
            );

        // LOAD ONLY ONCE

        if (citySelect.options.length <= 1) {

            data.cities.forEach(city => {

                const option =
                    document.createElement('option');

                option.value = city;

                option.textContent = city;

                citySelect.appendChild(option);
            });
        }

        // =========================================
        // KPI CARDS
        // =========================================

        document.getElementById(
            'restaurants-count'
        ).innerText =
            data.total_restaurants;

        document.getElementById(
            'avg-rating'
        ).innerText =
            data.avg_rating;

        document.getElementById(
            'avg-cost'
        ).innerText =
            '₹' + data.avg_cost;

        document.getElementById(
            'total-votes'
        ).innerText =
            data.total_votes;

        // =========================================
        // TABLE
        // =========================================

        const tableBody =

            document.getElementById(
                'restaurant-table-body'
            );

        tableBody.innerHTML = '';

        data.restaurants.forEach(
            restaurant => {

                const row = `

                    <tr>

                        <td>
                            ${restaurant['Restaurant Name']}
                        </td>

                        <td>
                            ${restaurant['City']}
                        </td>

                        <td>
                            ${restaurant['Cuisines']}
                        </td>

                        <td>
                            ⭐ ${restaurant['Aggregate rating']}
                        </td>

                        <td>
                            👍 ${restaurant['Votes']}
                        </td>

                    </tr>
                `;

                tableBody.innerHTML += row;
            }
        );

        // =========================================
        // DESTROY OLD CHARTS
        // =========================================

        if (cuisineChart) {
            cuisineChart.destroy();
        }

        if (ratingChart) {
            ratingChart.destroy();
        }

        if (topRatedChart) {
            topRatedChart.destroy();
        }

        if (cuisinePopularityChart) {
            cuisinePopularityChart.destroy();
        }

        // =========================================
        // TOP CUISINES CHART
        // =========================================

        cuisineChart = new Chart(

            document.getElementById(
                'cuisineChart'
            ),

            {

                type: 'bar',

                data: {

                    labels: Object.keys(
                        data.top_cuisines
                    ),

                    datasets: [{

                        label: 'Top Cuisines',

                        data: Object.values(
                            data.top_cuisines
                        ),

                        backgroundColor: '#22c55e'
                    }]
                },

                options: {

                    responsive: true,

                    plugins: {

                        legend: {
                            display: false
                        }
                    }
                }
            }
        );

        // =========================================
        // RATING DISTRIBUTION CHART
        // =========================================

        ratingChart = new Chart(

            document.getElementById(
                'ratingChart'
            ),

            {

                type: 'bar',

                data: {

                    labels: Object.keys(
                        data.rating_distribution
                    ),

                    datasets: [{

                        label: 'Ratings',

                        data: Object.values(
                            data.rating_distribution
                        ),

                        backgroundColor: '#3b82f6'
                    }]
                },

                options: {

                    responsive: true,

                    plugins: {

                        legend: {
                            display: false
                        }
                    }
                }
            }
        );

        // =========================================
        // TOP RESTAURANT RATINGS
        // =========================================

        topRatedChart = new Chart(

            document.getElementById(
                'topRatedChart'
            ),

            {

                type: 'bar',

                data: {

                    labels:

                        data.top_rated_restaurants.map(
                            item =>
                            item['Restaurant Name']
                        ),

                    datasets: [{

                        label: 'Restaurant Ratings',

                        data:

                            data.top_rated_restaurants.map(
                                item =>
                                item['Aggregate rating']
                            ),

                        backgroundColor: '#ec4899'
                    }]
                },

                options: {

                    responsive: true,

                    indexAxis: 'y',

                    plugins: {

                        legend: {
                            display: false
                        }
                    }
                }
            }
        );

        // =========================================
        // CUISINE POPULARITY CHART
        // =========================================

        cuisinePopularityChart = new Chart(

            document.getElementById(
                'cuisinePopularityChart'
            ),

            {

                type: 'doughnut',

                data: {

                    labels: Object.keys(
                        data.cuisine_popularity
                    ),

                    datasets: [{

                        data: Object.values(
                            data.cuisine_popularity
                        ),

                        backgroundColor: [

                            '#3b82f6',
                            '#22c55e',
                            '#ec4899',
                            '#f59e0b',
                            '#8b5cf6'
                        ]
                    }]
                },

                options: {

                    responsive: true
                }
            }
        );

    }

    catch (error) {

        console.log(
            'Dashboard Error:',
            error
        );
    }
}

// =====================================================
// INITIAL LOAD
// =====================================================

loadDashboard();

// =====================================================
// CITY DROPDOWN EVENT
// =====================================================

document.getElementById(
    'city-select'
).addEventListener(

    'change',

    () => {

        loadDashboard();
    }
);

// =====================================================
// AI CHAT
// =====================================================

async function sendMessage() {

    const userInput =

        document.getElementById(
            'user-question'
        ).value;

    if (!userInput) return;

    // =========================================
    // GET SELECTED CITY
    // =========================================

    const selectedCity =

        document.getElementById(
            'city-select'
        ).value;

    const chatBox =

        document.querySelector(
            '.chat-box'
        );

    // =========================================
    // USER MESSAGE
    // =========================================

    chatBox.innerHTML += `

        <div class="user-message">
            ${userInput}
        </div>
    `;

    // =========================================
    // CLEAR INPUT
    // =========================================

    document.getElementById(
        'user-question'
    ).value = '';

    // =========================================
    // LOADING MESSAGE
    // =========================================

    const loadingDiv = document.createElement(
        'div'
    );

    loadingDiv.className =
        'ai-message';

    loadingDiv.innerHTML =
        '🤖 Analyzing restaurant insights...';

    chatBox.appendChild(
        loadingDiv
    );

    chatBox.scrollTop =
        chatBox.scrollHeight;

    // =========================================
    // API REQUEST
    // =========================================

    const response = await fetch(

        '/chat',

        {

            method: 'POST',

            headers: {
                'Content-Type': 'application/json'
            },

            body: JSON.stringify({

                message: userInput,

                city: selectedCity
            })
        }
    );

    const data =
        await response.json();

    // =========================================
    // REMOVE LOADING
    // =========================================

    loadingDiv.remove();

    // =========================================
    // AI RESPONSE
    // =========================================

    chatBox.innerHTML += `

        <div class="ai-message">
            ${data.reply}
        </div>
    `;

    // =========================================
    // AUTO SCROLL
    // =========================================

    chatBox.scrollTop =
        chatBox.scrollHeight;
}

// =====================================================
// ENTER KEY SUPPORT
// =====================================================

document.getElementById(
    'user-question'
).addEventListener(

    'keypress',

    function(event) {

        if(event.key === 'Enter') {

            sendMessage();
        }
    }
);