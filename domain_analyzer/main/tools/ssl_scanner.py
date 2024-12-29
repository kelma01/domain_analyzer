import datetime
from pathlib import Path
from typing import List
from sslyze import *
from datetime import timezone


def scan_ssl_cert(domain):
    scan_reqs = [ServerScanRequest(server_location=ServerNetworkLocation(hostname=domain))]

    scanner = Scanner()
    scanner.queue_scans(scan_reqs)

    all_server_scan_results = []
    for server_scan_result in scanner.get_results():
        all_server_scan_results.append(server_scan_result)
        if server_scan_result.scan_status == ServerScanStatusEnum.ERROR_NO_CONNECTIVITY:
            exit(0)

    not_valid_after = all_server_scan_results[0].scan_result.certificate_info.result.certificate_deployments[0].received_certificate_chain[0].not_valid_after_utc
    now = datetime.datetime.now()

    now = now.replace(tzinfo=timezone.utc) #converting naive datetime to aware datetime
    
    validity_status = 'True' if now < not_valid_after else 'False'
    
    return validity_status, not_valid_after