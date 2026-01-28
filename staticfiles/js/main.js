// ========================================
// BIZKAIPOP - JAVASCRIPT GLOBAL (Dev 4)
// ========================================

document.addEventListener('DOMContentLoaded', function() {
    console.log('🚀 Bizkaipop cargado correctamente');
    
    // Inicializar funcionalidades globales
    initMessages();
    initSearchBar();
});

// ===== AUTO-CERRAR MENSAJES DEL SISTEMA =====
function initMessages() {
    const messages = document.querySelectorAll('.message');
    
    messages.forEach(message => {
        // Auto-cerrar después de 5 segundos
        setTimeout(() => {
            message.style.animation = 'slideOut 0.3s forwards';
            setTimeout(() => message.remove(), 300);
        }, 5000);
        
        // Cerrar al hacer clic
        message.addEventListener('click', () => {
            message.style.animation = 'slideOut 0.3s forwards';
            setTimeout(() => message.remove(), 300);
        });
    });
}

// ===== BUSCADOR BÁSICO =====
function initSearchBar() {
    const searchInput = document.querySelector('.search-input');
    const searchButton = document.querySelector('.search-bar .btn');
    
    if (searchButton && searchInput) {
        searchButton.addEventListener('click', (e) => {
            e.preventDefault();
            const query = searchInput.value.trim();
            
            if (query) {
                // Dev 3 implementará la búsqueda real
                console.log('Buscando:', query);
                // window.location.href = `/catalog/?search=${encodeURIComponent(query)}`;
                alert(`Función de búsqueda en desarrollo. Buscando: "${query}"`);
            } else {
                alert('Por favor, escribe algo para buscar');
            }
        });
        
        // Buscar al presionar Enter
        searchInput.addEventListener('keypress', (e) => {
            if (e.key === 'Enter') {
                searchButton.click();
            }
        });
    }
}

// ===== UTILIDADES GLOBALES =====

// Formatear precio con símbolo de euro
function formatPrice(price) {
    return `${parseFloat(price).toFixed(2)}€`;
}

// Validar email
function isValidEmail(email) {
    const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return regex.test(email);
}

// Mostrar mensaje temporal
function showMessage(text, type = 'info') {
    const container = document.querySelector('.messages-container') || createMessageContainer();
    
    const message = document.createElement('div');
    message.className = `message message-${type}`;
    message.textContent = text;
    
    container.appendChild(message);
    
    setTimeout(() => {
        message.style.animation = 'slideOut 0.3s forwards';
        setTimeout(() => message.remove(), 300);
    }, 5000);
}

function createMessageContainer() {
    const container = document.createElement('div');
    container.className = 'messages-container';
    document.body.appendChild(container);
    return container;
}

// Animación de slideOut para mensajes
const style = document.createElement('style');
style.textContent = `
    @keyframes slideOut {
        to {
            transform: translateX(400px);
            opacity: 0;
        }
    }
`;
document.head.appendChild(style);

// ===== EXPORTAR UTILIDADES PARA OTROS DEVS =====
window.BizkaipopUtils = {
    formatPrice,
    isValidEmail,
    showMessage
};