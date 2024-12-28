function togglePorts() {
    const portsSection = document.getElementById("ports-section");

    if (portsSection.style.maxHeight) {
        // Kapatma işlemi
        portsSection.style.maxHeight = null;
    } else {
        // Açma işlemi
        portsSection.style.maxHeight = portsSection.scrollHeight + "px";
    }
}