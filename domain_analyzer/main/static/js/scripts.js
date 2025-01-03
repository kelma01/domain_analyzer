function toggleSsl() {
    const sslSection = document.getElementById("ssl-section");
    sslSection.style.display = sslSection.style.display === "none" ? "block" : "none";
}

function togglePorts() {
    const portsSection = document.getElementById("ports-section");
    portsSection.style.display = portsSection.style.display === "none" ? "block" : "none";
}

function toggleWhois() {
    const whoisSection = document.getElementById("whois-section");
    whoisSection.style.display = whoisSection.style.display === "none" ? "block" : "none";
}

function toggleDNSRecords() {
    const dnsRecordsSection = document.getElementById("dns-records-section");
    dnsRecordsSection.style.display = dnsRecordsSection.style.display === "none" ? "block" : "none";
}

function toggleSubdomains() {
    const subdomainSection = document.getElementById("subdomain-section");
    subdomainSection.style.display = subdomainSection.style.display === "none" ? "block" : "none";
}
