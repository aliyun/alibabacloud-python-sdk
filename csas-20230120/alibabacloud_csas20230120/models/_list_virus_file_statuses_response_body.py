# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_csas20230120 import models as main_models
from darabonba.model import DaraModel

class ListVirusFileStatusesResponseBody(DaraModel):
    def __init__(
        self,
        file_statuses: List[main_models.ListVirusFileStatusesResponseBodyFileStatuses] = None,
        request_id: str = None,
        total_num: str = None,
    ):
        # The list of virus files.
        self.file_statuses = file_statuses
        # The ID of the request.
        self.request_id = request_id
        # The total number of virus files that match the query conditions.
        self.total_num = total_num

    def validate(self):
        if self.file_statuses:
            for v1 in self.file_statuses:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['FileStatuses'] = []
        if self.file_statuses is not None:
            for k1 in self.file_statuses:
                result['FileStatuses'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_num is not None:
            result['TotalNum'] = self.total_num

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.file_statuses = []
        if m.get('FileStatuses') is not None:
            for k1 in m.get('FileStatuses'):
                temp_model = main_models.ListVirusFileStatusesResponseBodyFileStatuses()
                self.file_statuses.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')

        return self

class ListVirusFileStatusesResponseBodyFileStatuses(DaraModel):
    def __init__(
        self,
        console_operation_time: str = None,
        department: str = None,
        dev_tag: str = None,
        dev_type: str = None,
        discovery_time: str = None,
        file_md_5: str = None,
        file_path: str = None,
        file_process_status: str = None,
        file_size: int = None,
        hostname: str = None,
        operation: str = None,
        operation_time: str = None,
        risk_level: str = None,
        sase_user_id: str = None,
        scan_task_id: str = None,
        task_execution_info: str = None,
        username: str = None,
        virus_file_source: str = None,
        virus_type: str = None,
    ):
        # The time when the administrator initiated the disposition, in the format yyyy-MM-dd HH:mm:ss (UTC+8). An empty string is returned when the disposition was not initiated by an administrator.
        self.console_operation_time = console_operation_time
        # The name of the department to which the user belongs. Multiple departments are separated by commas (,). The nearest department name in the organizational structure is returned, not the full path.
        self.department = department
        # The unique identifier of the user\\"s endpoint device that detected this virus file.
        self.dev_tag = dev_tag
        # The operating system type of the user terminal device. Valid values:
        # - **windows**: Windows.
        # - **macOS**: macOS.
        self.dev_type = dev_type
        # The time when the virus file was discovered, in the format yyyy-MM-dd HH:mm:ss (UTC+8). A hyphen (-) is returned when no record exists.
        self.discovery_time = discovery_time
        # The MD5 hash of the virus file.
        self.file_md_5 = file_md_5
        # The absolute path of the virus file on the user\\"s endpoint device.
        self.file_path = file_path
        # The disposition status. Valid values:
        # - **Pending**: Pending disposition.
        # - **Processed**: Disposed.
        self.file_process_status = file_process_status
        # The size of the virus file, in bytes.
        self.file_size = file_size
        # The hostname of the user\\"s endpoint device.
        self.hostname = hostname
        # The disposition action that has been performed. An empty string is returned when no disposition has been performed. Valid values:
        # - **AdminQuarantine**: Quarantined by administrator.
        # - **AdminTrust**: Trusted by administrator.
        # - **UserQuarantine**: Quarantined by endpoint user.
        # - **UserTrust**: Trusted by endpoint user.
        # - **AutoQuarantine**: Automatically quarantined based on policy.
        # - **Fail**: Disposition failed.
        self.operation = operation
        # The effective period of the disposition, in the format yyyy-MM-dd HH:mm:ss (UTC+8). The later of the actual disposition time on the user\\"s endpoint device and the time when the administrator initiated the disposition is used. A hyphen (-) is returned when no disposition has been performed.
        self.operation_time = operation_time
        # The risk level. Valid values:
        # - **High**: High risk.
        # - **Mid**: Medium risk.
        # - **Low**: Low risk.
        self.risk_level = risk_level
        # The user ID.
        self.sase_user_id = sase_user_id
        # The ID of the virus scan task that detected this virus file. An empty string is returned when the file is detected by real-time protection.
        self.scan_task_id = scan_task_id
        # The execution result description of the disposition or scan, reported by the user\\"s endpoint device. If a disposition record exists, the execution result of the disposition task is returned. Otherwise, the execution result of the scan task is returned.
        self.task_execution_info = task_execution_info
        # The username.
        self.username = username
        # The detection source of the virus file. Valid values:
        # - **Task**: Detected by a virus scan task.
        # - **Download**: Detected by real-time protection during file download.
        # - **Process**: Detected by real-time protection during process execution.
        self.virus_file_source = virus_file_source
        # The virus type. Valid values:
        # - **Backdoor**: Backdoor program.
        # - **DDoS**: DDoS Trojan.
        # - **Downloader**: Downloader Trojan.
        # - **Engtest**: DPI engine test program.
        # - **Hacktool**: Hacking tool.
        # - **Trojan**: Self-mutating Trojan.
        # - **Malbaseware**: Contaminated base software.
        # - **MalScript**: Malicious script.
        # - **Malware**: Malicious program.
        # - **Miner**: Mining programs.
        # - **Proxytool**: Proxy tool.
        # - **RansomWare**: Ransomware.
        # - **RiskWare**: Risky software.
        # - **Rootkit**: Kernel-hidden program.
        # - **Stealer**: Credential-stealing tool.
        # - **Scanner**: Scanner.
        # - **Suspicious**: Suspicious program.
        # - **Virus**: File-infecting virus.
        # - **WebShell**: Web shell.
        # - **Worm**: Worms.
        # - **BlackList**: File that hit the blacklist.
        # - **Exp**: Vulnerability exploits program.
        # - **Patcher**: Cracking program.
        # - **Gametool**: Private server tool.
        # - **AdWare**: Adware.
        # - **Maldoc**: Malicious document.
        self.virus_type = virus_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.console_operation_time is not None:
            result['ConsoleOperationTime'] = self.console_operation_time

        if self.department is not None:
            result['Department'] = self.department

        if self.dev_tag is not None:
            result['DevTag'] = self.dev_tag

        if self.dev_type is not None:
            result['DevType'] = self.dev_type

        if self.discovery_time is not None:
            result['DiscoveryTime'] = self.discovery_time

        if self.file_md_5 is not None:
            result['FileMd5'] = self.file_md_5

        if self.file_path is not None:
            result['FilePath'] = self.file_path

        if self.file_process_status is not None:
            result['FileProcessStatus'] = self.file_process_status

        if self.file_size is not None:
            result['FileSize'] = self.file_size

        if self.hostname is not None:
            result['Hostname'] = self.hostname

        if self.operation is not None:
            result['Operation'] = self.operation

        if self.operation_time is not None:
            result['OperationTime'] = self.operation_time

        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level

        if self.sase_user_id is not None:
            result['SaseUserId'] = self.sase_user_id

        if self.scan_task_id is not None:
            result['ScanTaskId'] = self.scan_task_id

        if self.task_execution_info is not None:
            result['TaskExecutionInfo'] = self.task_execution_info

        if self.username is not None:
            result['Username'] = self.username

        if self.virus_file_source is not None:
            result['VirusFileSource'] = self.virus_file_source

        if self.virus_type is not None:
            result['VirusType'] = self.virus_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsoleOperationTime') is not None:
            self.console_operation_time = m.get('ConsoleOperationTime')

        if m.get('Department') is not None:
            self.department = m.get('Department')

        if m.get('DevTag') is not None:
            self.dev_tag = m.get('DevTag')

        if m.get('DevType') is not None:
            self.dev_type = m.get('DevType')

        if m.get('DiscoveryTime') is not None:
            self.discovery_time = m.get('DiscoveryTime')

        if m.get('FileMd5') is not None:
            self.file_md_5 = m.get('FileMd5')

        if m.get('FilePath') is not None:
            self.file_path = m.get('FilePath')

        if m.get('FileProcessStatus') is not None:
            self.file_process_status = m.get('FileProcessStatus')

        if m.get('FileSize') is not None:
            self.file_size = m.get('FileSize')

        if m.get('Hostname') is not None:
            self.hostname = m.get('Hostname')

        if m.get('Operation') is not None:
            self.operation = m.get('Operation')

        if m.get('OperationTime') is not None:
            self.operation_time = m.get('OperationTime')

        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')

        if m.get('SaseUserId') is not None:
            self.sase_user_id = m.get('SaseUserId')

        if m.get('ScanTaskId') is not None:
            self.scan_task_id = m.get('ScanTaskId')

        if m.get('TaskExecutionInfo') is not None:
            self.task_execution_info = m.get('TaskExecutionInfo')

        if m.get('Username') is not None:
            self.username = m.get('Username')

        if m.get('VirusFileSource') is not None:
            self.virus_file_source = m.get('VirusFileSource')

        if m.get('VirusType') is not None:
            self.virus_type = m.get('VirusType')

        return self

