function togglePorts() {
    const portsSection = document.getElementById("ports-section");

    if (portsSection.style.maxHeight)
        portsSection.style.maxHeight = null;
    else
        portsSection.style.maxHeight = portsSection.scrollHeight + "px";
}
function toggleWhois() {
    const whoisSection = document.getElementById("whois-section");

    if (whoisSection.style.maxHeight)
        whoisSection.style.maxHeight = null;
    else
    whoisSection.style.maxHeight = whoisSection.scrollHeight + "px";
}
function toggleSsl() {
    const sslSection = document.getElementById("ssl-section");

    if (sslSection.style.maxHeight)
        sslSection.style.maxHeight = null;
    else
    sslSection.style.maxHeight = sslSection.scrollHeight + "px";
}