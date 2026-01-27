# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from alibabacloud_csas20230120 import models as main_models
from darabonba.model import DaraModel

class ListDynamicDisposalProcessesResponseBody(DaraModel):
    def __init__(
        self,
        disposal_processes: List[main_models.ListDynamicDisposalProcessesResponseBodyDisposalProcesses] = None,
        request_id: str = None,
        total_num: int = None,
    ):
        # List of disposal processes.
        self.disposal_processes = disposal_processes
        # Request ID.
        self.request_id = request_id
        # Total number of dynamic disposal processes.
        self.total_num = total_num

    def validate(self):
        if self.disposal_processes:
            for v1 in self.disposal_processes:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DisposalProcesses'] = []
        if self.disposal_processes is not None:
            for k1 in self.disposal_processes:
                result['DisposalProcesses'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_num is not None:
            result['TotalNum'] = self.total_num

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.disposal_processes = []
        if m.get('DisposalProcesses') is not None:
            for k1 in m.get('DisposalProcesses'):
                temp_model = main_models.ListDynamicDisposalProcessesResponseBodyDisposalProcesses()
                self.disposal_processes.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')

        return self

class ListDynamicDisposalProcessesResponseBodyDisposalProcesses(DaraModel):
    def __init__(
        self,
        department: str = None,
        dev_tag: str = None,
        device_basic_info: main_models.ListDynamicDisposalProcessesResponseBodyDisposalProcessesDeviceBasicInfo = None,
        device_status_info: main_models.ListDynamicDisposalProcessesResponseBodyDisposalProcessesDeviceStatusInfo = None,
        disposal_actions: List[str] = None,
        disposal_process_id: str = None,
        disposal_time: str = None,
        dynamic_policy_id: str = None,
        dynamic_policy_name: str = None,
        hostname: str = None,
        recovery_type: str = None,
        rule_content: Any = None,
        sase_user_id: str = None,
        status: str = None,
        user_name: str = None,
    ):
        # User\\"s department.
        self.department = department
        # Device ID.
        self.dev_tag = dev_tag
        # Basic device information.
        self.device_basic_info = device_basic_info
        # 设备状态信息。
        self.device_status_info = device_status_info
        # List of disposal actions.
        self.disposal_actions = disposal_actions
        # Disposal process ID.
        self.disposal_process_id = disposal_process_id
        # Disposal time, in seconds since the epoch.
        self.disposal_time = disposal_time
        # Dynamic policy ID.
        self.dynamic_policy_id = dynamic_policy_id
        # Dynamic policy name.
        self.dynamic_policy_name = dynamic_policy_name
        # Terminal device name. Length: 1~128 characters, supporting Chinese and uppercase/lowercase English letters, and can include numbers, half-width periods (.), commas (,), semicolons (;), hyphens (-), underscores (_), slashes (/), at (@) symbols, and spaces. Entering an underscore (_) alone will additionally query all terminal devices with 4-byte UTF-8 characters in their names.
        self.hostname = hostname
        # Recovery type.
        # - **auto**：Automatic recovery.
        # - **console**：Console recovery.
        # - **auth**：Certification and reporting recovery.
        self.recovery_type = recovery_type
        # Rule content.
        self.rule_content = rule_content
        # SASE用户ID。
        self.sase_user_id = sase_user_id
        # Disposal status. Values:
        # - **disposal**: In the disposal state.
        # - **finished**: Already automatically recovered.
        # - **recovery**: Recovered by authentication and reporting or console recovery.
        self.status = status
        # Username.
        self.user_name = user_name

    def validate(self):
        if self.device_basic_info:
            self.device_basic_info.validate()
        if self.device_status_info:
            self.device_status_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.department is not None:
            result['Department'] = self.department

        if self.dev_tag is not None:
            result['DevTag'] = self.dev_tag

        if self.device_basic_info is not None:
            result['DeviceBasicInfo'] = self.device_basic_info.to_map()

        if self.device_status_info is not None:
            result['DeviceStatusInfo'] = self.device_status_info.to_map()

        if self.disposal_actions is not None:
            result['DisposalActions'] = self.disposal_actions

        if self.disposal_process_id is not None:
            result['DisposalProcessId'] = self.disposal_process_id

        if self.disposal_time is not None:
            result['DisposalTime'] = self.disposal_time

        if self.dynamic_policy_id is not None:
            result['DynamicPolicyId'] = self.dynamic_policy_id

        if self.dynamic_policy_name is not None:
            result['DynamicPolicyName'] = self.dynamic_policy_name

        if self.hostname is not None:
            result['Hostname'] = self.hostname

        if self.recovery_type is not None:
            result['RecoveryType'] = self.recovery_type

        if self.rule_content is not None:
            result['RuleContent'] = self.rule_content

        if self.sase_user_id is not None:
            result['SaseUserId'] = self.sase_user_id

        if self.status is not None:
            result['Status'] = self.status

        if self.user_name is not None:
            result['UserName'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Department') is not None:
            self.department = m.get('Department')

        if m.get('DevTag') is not None:
            self.dev_tag = m.get('DevTag')

        if m.get('DeviceBasicInfo') is not None:
            temp_model = main_models.ListDynamicDisposalProcessesResponseBodyDisposalProcessesDeviceBasicInfo()
            self.device_basic_info = temp_model.from_map(m.get('DeviceBasicInfo'))

        if m.get('DeviceStatusInfo') is not None:
            temp_model = main_models.ListDynamicDisposalProcessesResponseBodyDisposalProcessesDeviceStatusInfo()
            self.device_status_info = temp_model.from_map(m.get('DeviceStatusInfo'))

        if m.get('DisposalActions') is not None:
            self.disposal_actions = m.get('DisposalActions')

        if m.get('DisposalProcessId') is not None:
            self.disposal_process_id = m.get('DisposalProcessId')

        if m.get('DisposalTime') is not None:
            self.disposal_time = m.get('DisposalTime')

        if m.get('DynamicPolicyId') is not None:
            self.dynamic_policy_id = m.get('DynamicPolicyId')

        if m.get('DynamicPolicyName') is not None:
            self.dynamic_policy_name = m.get('DynamicPolicyName')

        if m.get('Hostname') is not None:
            self.hostname = m.get('Hostname')

        if m.get('RecoveryType') is not None:
            self.recovery_type = m.get('RecoveryType')

        if m.get('RuleContent') is not None:
            self.rule_content = m.get('RuleContent')

        if m.get('SaseUserId') is not None:
            self.sase_user_id = m.get('SaseUserId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        return self

class ListDynamicDisposalProcessesResponseBodyDisposalProcessesDeviceStatusInfo(DaraModel):
    def __init__(
        self,
        app_version: str = None,
        department: str = None,
        dlp_status: str = None,
        internet_ip: str = None,
        la_status: str = None,
        login_status: str = None,
        nac_status: str = None,
        private_ip: str = None,
        sase_user_id: str = None,
        username: str = None,
        workshop: str = None,
        ztna_status: str = None,
    ):
        # Client version.
        self.app_version = app_version
        # Department to which the user belongs.
        self.department = department
        # Office data protection status. Values:
        # - **Enabled**: Enabled.
        # - **Disabled**: Disabled.
        # - **Unprovisioned**: Not configured.
        # - **Unauthorized**: Unauthorized.
        self.dlp_status = dlp_status
        # Public IP address.
        self.internet_ip = internet_ip
        # Internet behavior management enablement status.
        self.la_status = la_status
        # Login status.
        self.login_status = login_status
        # Network access control status. Values:
        # - **Enabled**: Enabled.
        # - **Disabled**: Disabled.
        # - **Unprovisioned**: Not configured.
        self.nac_status = nac_status
        # Private IP address.
        self.private_ip = private_ip
        # Unique ID of the SASE user.
        self.sase_user_id = sase_user_id
        # Username.
        self.username = username
        # Identified office area name.
        self.workshop = workshop
        # ZTNA enablement status.
        self.ztna_status = ztna_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_version is not None:
            result['AppVersion'] = self.app_version

        if self.department is not None:
            result['Department'] = self.department

        if self.dlp_status is not None:
            result['DlpStatus'] = self.dlp_status

        if self.internet_ip is not None:
            result['InternetIp'] = self.internet_ip

        if self.la_status is not None:
            result['LaStatus'] = self.la_status

        if self.login_status is not None:
            result['LoginStatus'] = self.login_status

        if self.nac_status is not None:
            result['NacStatus'] = self.nac_status

        if self.private_ip is not None:
            result['PrivateIp'] = self.private_ip

        if self.sase_user_id is not None:
            result['SaseUserId'] = self.sase_user_id

        if self.username is not None:
            result['Username'] = self.username

        if self.workshop is not None:
            result['Workshop'] = self.workshop

        if self.ztna_status is not None:
            result['ZtnaStatus'] = self.ztna_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppVersion') is not None:
            self.app_version = m.get('AppVersion')

        if m.get('Department') is not None:
            self.department = m.get('Department')

        if m.get('DlpStatus') is not None:
            self.dlp_status = m.get('DlpStatus')

        if m.get('InternetIp') is not None:
            self.internet_ip = m.get('InternetIp')

        if m.get('LaStatus') is not None:
            self.la_status = m.get('LaStatus')

        if m.get('LoginStatus') is not None:
            self.login_status = m.get('LoginStatus')

        if m.get('NacStatus') is not None:
            self.nac_status = m.get('NacStatus')

        if m.get('PrivateIp') is not None:
            self.private_ip = m.get('PrivateIp')

        if m.get('SaseUserId') is not None:
            self.sase_user_id = m.get('SaseUserId')

        if m.get('Username') is not None:
            self.username = m.get('Username')

        if m.get('Workshop') is not None:
            self.workshop = m.get('Workshop')

        if m.get('ZtnaStatus') is not None:
            self.ztna_status = m.get('ZtnaStatus')

        return self

class ListDynamicDisposalProcessesResponseBodyDisposalProcessesDeviceBasicInfo(DaraModel):
    def __init__(
        self,
        cpu: str = None,
        dev_tag: str = None,
        dev_type: str = None,
        disk: str = None,
        hostname: str = None,
        mac: str = None,
        memory: str = None,
        os_version: str = None,
    ):
        # CPU model.
        self.cpu = cpu
        # Device ID.
        self.dev_tag = dev_tag
        # Device operating system type. Values:
        # - **Windows**：Windows system.
        # - **macOS**：macOS system.
        # - **Linux**：Linux system.
        # - **Android**：Android system.
        # - **iOS**：iOS system.
        # - **Windows_Wuying**：Wuying cloud desktop system.
        self.dev_type = dev_type
        # Device disk model.
        self.disk = disk
        # Device name.
        self.hostname = hostname
        # Device MAC address.
        self.mac = mac
        # Device memory capacity. Unit: GB.
        self.memory = memory
        # Operating system version
        self.os_version = os_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cpu is not None:
            result['Cpu'] = self.cpu

        if self.dev_tag is not None:
            result['DevTag'] = self.dev_tag

        if self.dev_type is not None:
            result['DevType'] = self.dev_type

        if self.disk is not None:
            result['Disk'] = self.disk

        if self.hostname is not None:
            result['Hostname'] = self.hostname

        if self.mac is not None:
            result['Mac'] = self.mac

        if self.memory is not None:
            result['Memory'] = self.memory

        if self.os_version is not None:
            result['OsVersion'] = self.os_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')

        if m.get('DevTag') is not None:
            self.dev_tag = m.get('DevTag')

        if m.get('DevType') is not None:
            self.dev_type = m.get('DevType')

        if m.get('Disk') is not None:
            self.disk = m.get('Disk')

        if m.get('Hostname') is not None:
            self.hostname = m.get('Hostname')

        if m.get('Mac') is not None:
            self.mac = m.get('Mac')

        if m.get('Memory') is not None:
            self.memory = m.get('Memory')

        if m.get('OsVersion') is not None:
            self.os_version = m.get('OsVersion')

        return self

