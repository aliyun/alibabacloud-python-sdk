# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_csas20230120 import models as main_models
from darabonba.model import DaraModel

class UpdateUserDevicesSharingStatusResponseBody(DaraModel):
    def __init__(
        self,
        devices: List[main_models.UpdateUserDevicesSharingStatusResponseBodyDevices] = None,
        request_id: str = None,
    ):
        # Device list.
        self.devices = devices
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.devices:
            for v1 in self.devices:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Devices'] = []
        if self.devices is not None:
            for k1 in self.devices:
                result['Devices'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.devices = []
        if m.get('Devices') is not None:
            for k1 in m.get('Devices'):
                temp_model = main_models.UpdateUserDevicesSharingStatusResponseBodyDevices()
                self.devices.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class UpdateUserDevicesSharingStatusResponseBodyDevices(DaraModel):
    def __init__(
        self,
        app_status: str = None,
        app_version: str = None,
        cpu: str = None,
        create_time: str = None,
        department: str = None,
        device_belong: str = None,
        device_model: str = None,
        device_status: str = None,
        device_tag: str = None,
        device_type: str = None,
        device_version: str = None,
        disk: str = None,
        dlp_status: str = None,
        hostname: str = None,
        ia_status: str = None,
        inner_ip: str = None,
        mac: str = None,
        memory: str = None,
        nac_status: str = None,
        net_interface_info: List[main_models.UpdateUserDevicesSharingStatusResponseBodyDevicesNetInterfaceInfo] = None,
        pa_status: str = None,
        sase_user_id: str = None,
        sharing_status: bool = None,
        src_ip: str = None,
        update_time: str = None,
        username: str = None,
    ):
        # The client status. Values:
        # 
        # - **Online**: Online.
        # 
        # - **Offline**: Offline.
        self.app_status = app_status
        # Client version.
        self.app_version = app_version
        # Device CPU model.
        self.cpu = cpu
        # Device registration time.
        self.create_time = create_time
        # User\\"s department.
        self.department = department
        # Device ownership. Values:
        # 
        # - **Personal**: Personal device.
        # 
        # - **Company**: Company device.
        self.device_belong = device_belong
        # Device model.
        self.device_model = device_model
        # The status of the device. Values:
        # 
        # - **Online**: Online.
        # 
        # - **Offline**: Offline.
        # 
        # - **LongTermOffline**: Long-term offline.
        # 
        # - **Locked**: Locked.
        # 
        # - **Lost**: Lost.
        # 
        # - **Unbound**: Unbound.
        self.device_status = device_status
        # Device ID.
        self.device_tag = device_tag
        # The operating system type of the device. Values:
        # 
        # - **Windows**: Windows system.
        # 
        # - **macOS**: macOS system.
        # 
        # - **Linux**: Linux system.
        # 
        # - **Android**: Android system.
        # 
        # - **iOS**: iOS system.
        # 
        # - **Windows_Wuying**: Wuying Cloud Desktop system.
        self.device_type = device_type
        # Device operating system version.
        self.device_version = device_version
        # Device disk model.
        self.disk = disk
        # Data protection status. Values:
        # 
        # - **Enabled**: Enabled.
        # 
        # - **Disabled**: Disabled.
        # 
        # - **Unprovisioned**: Unprovisioned.
        # 
        # - **Unauthorized**: Unauthorized.
        self.dlp_status = dlp_status
        # Device name.
        self.hostname = hostname
        # Internet access status. Values:
        # 
        # - **Enabled**: Enabled.
        # 
        # - **Disabled**: Disabled.
        # 
        # - **Unprovisioned**: Unprovisioned.
        self.ia_status = ia_status
        # Device private network IP address.
        self.inner_ip = inner_ip
        # Device MAC address.
        self.mac = mac
        # Device memory capacity. Unit: GB.
        self.memory = memory
        # Network access control status. Values:
        # 
        # - **Enabled**: Enabled.
        # 
        # - **Disabled**: Disabled.
        # 
        # - **Unprovisioned**: Unprovisioned.
        self.nac_status = nac_status
        # NIC list.
        self.net_interface_info = net_interface_info
        # Private network access status. Values:
        # 
        # - **Enabled**: Enabled.
        # 
        # - **Disabled**: Disabled.
        # 
        # - **Unprovisioned**: Unprovisioned.
        self.pa_status = pa_status
        # User ID.
        self.sase_user_id = sase_user_id
        # Indicates whether device sharing is enabled. Values:
        # 
        # - **true**: Enable sharing.
        # 
        # - **false**: Disable sharing.
        self.sharing_status = sharing_status
        # Device logon IP address.
        self.src_ip = src_ip
        # Device last online time.
        self.update_time = update_time
        # Username.
        self.username = username

    def validate(self):
        if self.net_interface_info:
            for v1 in self.net_interface_info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_status is not None:
            result['AppStatus'] = self.app_status

        if self.app_version is not None:
            result['AppVersion'] = self.app_version

        if self.cpu is not None:
            result['CPU'] = self.cpu

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.department is not None:
            result['Department'] = self.department

        if self.device_belong is not None:
            result['DeviceBelong'] = self.device_belong

        if self.device_model is not None:
            result['DeviceModel'] = self.device_model

        if self.device_status is not None:
            result['DeviceStatus'] = self.device_status

        if self.device_tag is not None:
            result['DeviceTag'] = self.device_tag

        if self.device_type is not None:
            result['DeviceType'] = self.device_type

        if self.device_version is not None:
            result['DeviceVersion'] = self.device_version

        if self.disk is not None:
            result['Disk'] = self.disk

        if self.dlp_status is not None:
            result['DlpStatus'] = self.dlp_status

        if self.hostname is not None:
            result['Hostname'] = self.hostname

        if self.ia_status is not None:
            result['IaStatus'] = self.ia_status

        if self.inner_ip is not None:
            result['InnerIP'] = self.inner_ip

        if self.mac is not None:
            result['Mac'] = self.mac

        if self.memory is not None:
            result['Memory'] = self.memory

        if self.nac_status is not None:
            result['NacStatus'] = self.nac_status

        result['NetInterfaceInfo'] = []
        if self.net_interface_info is not None:
            for k1 in self.net_interface_info:
                result['NetInterfaceInfo'].append(k1.to_map() if k1 else None)

        if self.pa_status is not None:
            result['PaStatus'] = self.pa_status

        if self.sase_user_id is not None:
            result['SaseUserId'] = self.sase_user_id

        if self.sharing_status is not None:
            result['SharingStatus'] = self.sharing_status

        if self.src_ip is not None:
            result['SrcIP'] = self.src_ip

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        if self.username is not None:
            result['Username'] = self.username

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppStatus') is not None:
            self.app_status = m.get('AppStatus')

        if m.get('AppVersion') is not None:
            self.app_version = m.get('AppVersion')

        if m.get('CPU') is not None:
            self.cpu = m.get('CPU')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Department') is not None:
            self.department = m.get('Department')

        if m.get('DeviceBelong') is not None:
            self.device_belong = m.get('DeviceBelong')

        if m.get('DeviceModel') is not None:
            self.device_model = m.get('DeviceModel')

        if m.get('DeviceStatus') is not None:
            self.device_status = m.get('DeviceStatus')

        if m.get('DeviceTag') is not None:
            self.device_tag = m.get('DeviceTag')

        if m.get('DeviceType') is not None:
            self.device_type = m.get('DeviceType')

        if m.get('DeviceVersion') is not None:
            self.device_version = m.get('DeviceVersion')

        if m.get('Disk') is not None:
            self.disk = m.get('Disk')

        if m.get('DlpStatus') is not None:
            self.dlp_status = m.get('DlpStatus')

        if m.get('Hostname') is not None:
            self.hostname = m.get('Hostname')

        if m.get('IaStatus') is not None:
            self.ia_status = m.get('IaStatus')

        if m.get('InnerIP') is not None:
            self.inner_ip = m.get('InnerIP')

        if m.get('Mac') is not None:
            self.mac = m.get('Mac')

        if m.get('Memory') is not None:
            self.memory = m.get('Memory')

        if m.get('NacStatus') is not None:
            self.nac_status = m.get('NacStatus')

        self.net_interface_info = []
        if m.get('NetInterfaceInfo') is not None:
            for k1 in m.get('NetInterfaceInfo'):
                temp_model = main_models.UpdateUserDevicesSharingStatusResponseBodyDevicesNetInterfaceInfo()
                self.net_interface_info.append(temp_model.from_map(k1))

        if m.get('PaStatus') is not None:
            self.pa_status = m.get('PaStatus')

        if m.get('SaseUserId') is not None:
            self.sase_user_id = m.get('SaseUserId')

        if m.get('SharingStatus') is not None:
            self.sharing_status = m.get('SharingStatus')

        if m.get('SrcIP') is not None:
            self.src_ip = m.get('SrcIP')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        if m.get('Username') is not None:
            self.username = m.get('Username')

        return self

class UpdateUserDevicesSharingStatusResponseBodyDevicesNetInterfaceInfo(DaraModel):
    def __init__(
        self,
        mac: str = None,
        name: str = None,
    ):
        # NIC MAC address.
        self.mac = mac
        # NIC name.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.mac is not None:
            result['Mac'] = self.mac

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Mac') is not None:
            self.mac = m.get('Mac')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

