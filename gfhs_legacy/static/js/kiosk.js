let kioskIdleTimer;

function resetKioskTimer() {
    clearTimeout(kioskIdleTimer);

    kioskIdleTimer = setTimeout(function () {
        window.location.href = "/kiosk/";
    }, 120000);
}

document.addEventListener("mousemove", resetKioskTimer);
document.addEventListener("mousedown", resetKioskTimer);
document.addEventListener("touchstart", resetKioskTimer);
document.addEventListener("keypress", resetKioskTimer);

resetKioskTimer();