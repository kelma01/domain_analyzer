function togglePorts() {
    const portsSection = document.getElementById("ports-section");

    if (portsSection.style.maxHeight)
        portsSection.style.maxHeight = null;
    else
        portsSection.style.maxHeight = portsSection.scrollHeight + "px";
}