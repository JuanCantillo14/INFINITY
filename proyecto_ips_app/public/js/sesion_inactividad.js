document.addEventListener("DOMContentLoaded", function () {
    let tiempoInactividad = 10 * 60 * 1000; // 10 minutos
    let tiempoLogout = 12 * 60 * 1000;      // 12 minutos

    let alertaInactividad;
    let logoutTimer;

    function mostrarAdvertencia() {
        const continuar = confirm("Tu sesión está a punto de expirar por inactividad. ¿Deseas continuar?");
        if (continuar) {
            location.reload(); // Refresca para mantener la sesión activa
        }
    }

    function resetTimers() {
        clearTimeout(alertaInactividad);
        clearTimeout(logoutTimer);

        alertaInactividad = setTimeout(mostrarAdvertencia, tiempoInactividad);
        logoutTimer = setTimeout(() => {
            window.location.href = window.logoutUrl;
        }, tiempoLogout);
    }

    ['click', 'mousemove', 'keypress', 'scroll'].forEach(evt => {
        document.addEventListener(evt, resetTimers);
    });

    resetTimers();
});
