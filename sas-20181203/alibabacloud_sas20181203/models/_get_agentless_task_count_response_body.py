# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetAgentlessTaskCountResponseBody(DaraModel):
    def __init__(
        self,
        baseline_check_count: int = None,
        cve_vul_count: int = None,
        last_task_time: int = None,
        malicious_file: int = None,
        request_id: str = None,
        risk_machine: int = None,
        sca_vul_count: int = None,
        scan_machine: int = None,
        sensitive_file_count: int = None,
        sys_vul_count: str = None,
        vulnerability: int = None,
    ):
        # The number of baseline checks.
        self.baseline_check_count = baseline_check_count
        # The number of system vulnerabilities.
        self.cve_vul_count = cve_vul_count
        # The timestamp generated when the last detection is performed.
        self.last_task_time = last_task_time
        # The number of malicious files.
        self.malicious_file = malicious_file
        # The request ID.
        self.request_id = request_id
        # The number of risky hosts.
        self.risk_machine = risk_machine
        # The number of application vulnerabilities.
        self.sca_vul_count = sca_vul_count
        # The number of hosts that are scanned.
        self.scan_machine = scan_machine
        # The total number of sensitive files.
        self.sensitive_file_count = sensitive_file_count
        # The total number of Windows system vulnerabilities.
        self.sys_vul_count = sys_vul_count
        # The number of vulnerabilities.
        self.vulnerability = vulnerability

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.baseline_check_count is not None:
            result['BaselineCheckCount'] = self.baseline_check_count

        if self.cve_vul_count is not None:
            result['CveVulCount'] = self.cve_vul_count

        if self.last_task_time is not None:
            result['LastTaskTime'] = self.last_task_time

        if self.malicious_file is not None:
            result['MaliciousFile'] = self.malicious_file

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.risk_machine is not None:
            result['RiskMachine'] = self.risk_machine

        if self.sca_vul_count is not None:
            result['ScaVulCount'] = self.sca_vul_count

        if self.scan_machine is not None:
            result['ScanMachine'] = self.scan_machine

        if self.sensitive_file_count is not None:
            result['SensitiveFileCount'] = self.sensitive_file_count

        if self.sys_vul_count is not None:
            result['SysVulCount'] = self.sys_vul_count

        if self.vulnerability is not None:
            result['Vulnerability'] = self.vulnerability

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaselineCheckCount') is not None:
            self.baseline_check_count = m.get('BaselineCheckCount')

        if m.get('CveVulCount') is not None:
            self.cve_vul_count = m.get('CveVulCount')

        if m.get('LastTaskTime') is not None:
            self.last_task_time = m.get('LastTaskTime')

        if m.get('MaliciousFile') is not None:
            self.malicious_file = m.get('MaliciousFile')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RiskMachine') is not None:
            self.risk_machine = m.get('RiskMachine')

        if m.get('ScaVulCount') is not None:
            self.sca_vul_count = m.get('ScaVulCount')

        if m.get('ScanMachine') is not None:
            self.scan_machine = m.get('ScanMachine')

        if m.get('SensitiveFileCount') is not None:
            self.sensitive_file_count = m.get('SensitiveFileCount')

        if m.get('SysVulCount') is not None:
            self.sys_vul_count = m.get('SysVulCount')

        if m.get('Vulnerability') is not None:
            self.vulnerability = m.get('Vulnerability')

        return self

