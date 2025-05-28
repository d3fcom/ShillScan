document.addEventListener('DOMContentLoaded', function() {
    const tokenSearch = document.getElementById('tokenSearch');
    const sidebar = document.getElementById('sidebar');
    const mainContent = document.getElementById('main-content');
    const sidebarToggle = document.getElementById('sidebarToggle');
    const sidebarOpen = document.getElementById('sidebarOpen');

    let previousPrices = {};

    function initializeSidebar() {
        console.log('Initializing sidebar');
        sidebar.classList.remove('w-64');
        sidebar.classList.add('w-16');
        mainContent.classList.remove('ml-64');
        mainContent.classList.add('ml-16');
        sidebarToggle.innerHTML = '<svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 5l7 7-7 7M5 5l7 7-7 7"></path></svg>';
        sidebarOpen.classList.remove('hidden');
        
        // Hide all sidebar content except for the toggle button and icons
        const sidebarContent = sidebar.querySelectorAll('.p-4 > *:not(#sidebarToggle):not(.sidebar-icon)');
        sidebarContent.forEach(element => element.classList.add('hidden'));
        
        // Show only icons
        const sidebarIcons = sidebar.querySelectorAll('.sidebar-icon');
        sidebarIcons.forEach(icon => icon.classList.remove('hidden'));
        console.log('Sidebar initialized');
    }

    initializeSidebar();

    function fetchTokens(searchQuery = '') {
        console.log('Fetching tokens with search query:', searchQuery);
        fetch(`/api/tokens/update?search=${searchQuery}`)
            .then(response => response.json())
            .then(tokens => {
                console.log('Received tokens:', tokens);
                updateTokenList(tokens);
            })
            .catch(error => console.error('Error fetching tokens:', error));
    }

    function updateTokenList(tokens) {
        console.log('Updating token list with', tokens.length, 'tokens');
        let tbody = document.querySelector('#tokenTable tbody');
        if (!tbody) {
            const table = document.getElementById('tokenTable');
            if (table) {
                tbody = document.createElement('tbody');
                tbody.id = 'tokenList';
                table.appendChild(tbody);
            } else {
                console.error('Token table not found');
                return;
            }
        }
        tbody.innerHTML = '';
        tokens.forEach(token => {
            const row = document.createElement('tr');
            row.className = 'token-row hover:bg-gray-100';
            row.innerHTML = `
                <td class="py-2 px-4"><a href="/token/${token.symbol}" class="text-blue-600 hover:underline">${token.symbol}</a></td>
                <td class="py-2 px-4">${token.name}</td>
                <td class="py-2 px-4 text-right">${updateTokenPrice(token)}</td>
                <td class="py-2 px-4 text-right ${token.change_5m >= 0 ? 'text-green-600' : 'text-red-600'}">${token.change_5m.toFixed(2)}%</td>
                <td class="py-2 px-4 text-right ${token.change_24h >= 0 ? 'text-green-600' : 'text-red-600'}">${token.change_24h.toFixed(2)}%</td>
                <td class="py-2 px-4 text-right">$${token.volume_24h.toLocaleString()}</td>
                <td class="py-2 px-4 text-right">$${token.market_cap.toLocaleString()}</td>
            `;
            tbody.appendChild(row);
        });
        console.log('Token list updated');
    }

    function updateTokenPrice(token) {
        if (!previousPrices[token.symbol]) {
            previousPrices[token.symbol] = token.price;
            return `$${token.price.toFixed(2)}`;
        }

        const previousPrice = previousPrices[token.symbol];
        const newPrice = token.price;
        const priceChange = (newPrice - previousPrice) / previousPrice;

        if (Math.abs(priceChange) > 0.05) {
            const interpolatedPrice = previousPrice * (1 + Math.sign(priceChange) * 0.05);
            previousPrices[token.symbol] = interpolatedPrice;
            return `$${interpolatedPrice.toFixed(2)}`;
        } else {
            previousPrices[token.symbol] = newPrice;
            return `$${newPrice.toFixed(2)}`;
        }
    }

    function toggleSidebar() {
        console.log('Toggling sidebar');
        sidebar.classList.toggle('w-64');
        sidebar.classList.toggle('w-16');
        mainContent.classList.toggle('ml-64');
        mainContent.classList.toggle('ml-16');

        const sidebarContent = sidebar.querySelectorAll('.p-4 > *:not(#sidebarToggle):not(.sidebar-icon)');
        const sidebarIcons = sidebar.querySelectorAll('.sidebar-icon');

        if (sidebar.classList.contains('w-16')) {
            sidebarToggle.innerHTML = '<svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 5l7 7-7 7M5 5l7 7-7 7"></path></svg>';
            sidebarOpen.classList.remove('hidden');
            sidebarContent.forEach(element => element.classList.add('hidden'));
            sidebarIcons.forEach(icon => icon.classList.remove('hidden'));
        } else {
            sidebarToggle.innerHTML = '<svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"></path></svg>';
            sidebarOpen.classList.add('hidden');
            sidebarContent.forEach(element => element.classList.remove('hidden'));
            sidebarIcons.forEach(icon => icon.classList.add('hidden'));
        }
        console.log('Sidebar toggled');
    }

    console.log('Initializing token list');
    fetchTokens();

    setInterval(fetchTokens, 5000);

    tokenSearch.addEventListener('input', function() {
        fetchTokens(this.value);
    });

    console.log('Adding event listeners to sidebar toggle buttons');
    sidebarToggle.addEventListener('click', toggleSidebar);
    sidebarOpen.addEventListener('click', toggleSidebar);

    const neonElements = document.querySelectorAll('.neon-effect');
    neonElements.forEach(element => {
        element.addEventListener('mouseenter', () => element.classList.add('neon-active'));
        element.addEventListener('mouseleave', () => element.classList.remove('neon-active'));
    });
});
