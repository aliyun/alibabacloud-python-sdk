# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DataValue(DaraModel):
    def __init__(
        self,
        baseline_check_count: int = None,
        cve_vul_count: int = None,
        estimate_used_size: int = None,
        last_task_time: int = None,
        malicious_file: int = None,
        risk_machine: int = None,
        sca_vul_count: int = None,
        scan_machine: int = None,
        sensitive_file_count: int = None,
        sys_vul_count: int = None,
        vulnerability: int = None,
        cve_num: int = None,
        emg_num: int = None,
        sys_num: int = None,
        cms_num: int = None,
        app_num: int = None,
        sca_num: int = None,
        vul_asap_sum: int = None,
        vul_later_sum: int = None,
        vul_nntf_sum: int = None,
        sys_asap_num: int = None,
    ):
        # The total number of baseline check items.
        self.baseline_check_count = baseline_check_count
        # The total number of system vulnerability items.
        self.cve_vul_count = cve_vul_count
        # The estimated detection volume in GB. This field is not currently returned by the batch statistics operation.
        self.estimate_used_size = estimate_used_size
        # The timestamp of the last scan time, in milliseconds.
        self.last_task_time = last_task_time
        # The total number of malicious sample files.
        self.malicious_file = malicious_file
        # The number of vulnerable servers.
        self.risk_machine = risk_machine
        # The total number of application vulnerabilities.
        self.sca_vul_count = sca_vul_count
        # The number of scanned servers.
        self.scan_machine = scan_machine
        # The total number of sensitive files.
        self.sensitive_file_count = sensitive_file_count
        # The total number of Windows system vulnerability items.
        self.sys_vul_count = sys_vul_count
        # The number of vulnerability risks.
        self.vulnerability = vulnerability
        # The number of Linux software vulnerabilities.
        self.cve_num = cve_num
        # The number of emergency vulnerabilities. This field is 0 when ImageVul is set to true.
        self.emg_num = emg_num
        # The number of Windows system vulnerabilities. This field is 0 when ImageVul is set to true.
        self.sys_num = sys_num
        # The number of Web-CMS vulnerabilities. This field is 0 when ImageVul is set to true.
        self.cms_num = cms_num
        # The number of application vulnerabilities. This field is 0 when ImageVul is set to true.
        self.app_num = app_num
        # The number of software composition analysis (SCA) vulnerabilities.
        self.sca_num = sca_num
        # The number of high-priority vulnerabilities.
        self.vul_asap_sum = vul_asap_sum
        # The number of medium-priority vulnerabilities.
        self.vul_later_sum = vul_later_sum
        # The number of low-priority vulnerabilities.
        self.vul_nntf_sum = vul_nntf_sum
        # The number of high-priority system vulnerabilities among Linux software vulnerabilities and Windows system vulnerabilities.
        self.sys_asap_num = sys_asap_num

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

        if self.estimate_used_size is not None:
            result['EstimateUsedSize'] = self.estimate_used_size

        if self.last_task_time is not None:
            result['LastTaskTime'] = self.last_task_time

        if self.malicious_file is not None:
            result['MaliciousFile'] = self.malicious_file

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

        if self.cve_num is not None:
            result['CveNum'] = self.cve_num

        if self.emg_num is not None:
            result['EmgNum'] = self.emg_num

        if self.sys_num is not None:
            result['SysNum'] = self.sys_num

        if self.cms_num is not None:
            result['CmsNum'] = self.cms_num

        if self.app_num is not None:
            result['AppNum'] = self.app_num

        if self.sca_num is not None:
            result['ScaNum'] = self.sca_num

        if self.vul_asap_sum is not None:
            result['VulAsapSum'] = self.vul_asap_sum

        if self.vul_later_sum is not None:
            result['VulLaterSum'] = self.vul_later_sum

        if self.vul_nntf_sum is not None:
            result['VulNntfSum'] = self.vul_nntf_sum

        if self.sys_asap_num is not None:
            result['SysAsapNum'] = self.sys_asap_num

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaselineCheckCount') is not None:
            self.baseline_check_count = m.get('BaselineCheckCount')

        if m.get('CveVulCount') is not None:
            self.cve_vul_count = m.get('CveVulCount')

        if m.get('EstimateUsedSize') is not None:
            self.estimate_used_size = m.get('EstimateUsedSize')

        if m.get('LastTaskTime') is not None:
            self.last_task_time = m.get('LastTaskTime')

        if m.get('MaliciousFile') is not None:
            self.malicious_file = m.get('MaliciousFile')

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

        if m.get('CveNum') is not None:
            self.cve_num = m.get('CveNum')

        if m.get('EmgNum') is not None:
            self.emg_num = m.get('EmgNum')

        if m.get('SysNum') is not None:
            self.sys_num = m.get('SysNum')

        if m.get('CmsNum') is not None:
            self.cms_num = m.get('CmsNum')

        if m.get('AppNum') is not None:
            self.app_num = m.get('AppNum')

        if m.get('ScaNum') is not None:
            self.sca_num = m.get('ScaNum')

        if m.get('VulAsapSum') is not None:
            self.vul_asap_sum = m.get('VulAsapSum')

        if m.get('VulLaterSum') is not None:
            self.vul_later_sum = m.get('VulLaterSum')

        if m.get('VulNntfSum') is not None:
            self.vul_nntf_sum = m.get('VulNntfSum')

        if m.get('SysAsapNum') is not None:
            self.sys_asap_num = m.get('SysAsapNum')

        return self

