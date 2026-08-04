# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_csas20230120 import models as main_models
from darabonba.model import DaraModel

class GetUserDeviceResponseBody(DaraModel):
    def __init__(
        self,
        device: main_models.GetUserDeviceResponseBodyDevice = None,
        request_id: str = None,
    ):
        # The terminal device.
        self.device = device
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.device:
            self.device.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.device is not None:
            result['Device'] = self.device.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Device') is not None:
            temp_model = main_models.GetUserDeviceResponseBodyDevice()
            self.device = temp_model.from_map(m.get('Device'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetUserDeviceResponseBodyDevice(DaraModel):
    def __init__(
        self,
        app_status: str = None,
        app_version: str = None,
        auto_login_status: str = None,
        battery_health_percentage: int = None,
        battery_remaining_percentage: int = None,
        cpu: str = None,
        city: str = None,
        city_en: str = None,
        city_zh: str = None,
        continent: str = None,
        continent_en: str = None,
        continent_zh: str = None,
        country: str = None,
        country_en: str = None,
        country_zh: str = None,
        create_time: str = None,
        department: str = None,
        device_belong: str = None,
        device_model: str = None,
        device_status: str = None,
        device_tag: str = None,
        device_type: str = None,
        device_version: str = None,
        disk: str = None,
        disk_available: int = None,
        disk_used: int = None,
        dlp_status: str = None,
        edr_status: str = None,
        history_users: List[main_models.GetUserDeviceResponseBodyDeviceHistoryUsers] = None,
        hostname: str = None,
        ia_status: str = None,
        inner_ip: str = None,
        join_ad_domain: bool = None,
        mac: str = None,
        match_device_group_ids: List[str] = None,
        memory: str = None,
        nac_status: str = None,
        net_interface_info: List[main_models.GetUserDeviceResponseBodyDeviceNetInterfaceInfo] = None,
        pa_status: str = None,
        processes: List[main_models.GetUserDeviceResponseBodyDeviceProcesses] = None,
        province: str = None,
        province_en: str = None,
        province_zh: str = None,
        sase_user_id: str = None,
        sharing_status: bool = None,
        sn_base_board: str = None,
        sn_bios: str = None,
        sn_disk_drive: str = None,
        sn_processor: str = None,
        sn_system: str = None,
        src_ip: str = None,
        terminal_info_collect_time: int = None,
        update_time: str = None,
        username: str = None,
        workshop: str = None,
    ):
        # The client status. Valid values:
        self.app_status = app_status
        # The client version.
        self.app_version = app_version
        # The auto-logon status of the device. Valid values:
        self.auto_login_status = auto_login_status
        # The battery health percentage.
        self.battery_health_percentage = battery_health_percentage
        # The battery remaining charge percentage.
        self.battery_remaining_percentage = battery_remaining_percentage
        # The CPU model of the terminal device.
        self.cpu = cpu
        # The city to which the public IP address belongs.
        self.city = city
        # The city name in English.
        self.city_en = city_en
        # The city name in Chinese.
        self.city_zh = city_zh
        # The continent to which the public IP address belongs.
        self.continent = continent
        # The continent name in English.
        self.continent_en = continent_en
        # The continent name in Chinese.
        self.continent_zh = continent_zh
        # The country to which the public IP address belongs.
        self.country = country
        # The country name in English.
        self.country_en = country_en
        # The country name in Chinese.
        self.country_zh = country_zh
        # The registration time of the terminal device.
        self.create_time = create_time
        # The department to which the user belongs.
        self.department = department
        # The ownership of the terminal device. Valid values:
        self.device_belong = device_belong
        # The model of the terminal device.
        self.device_model = device_model
        # The status of the terminal device. Valid values:
        self.device_status = device_status
        # The ID of the terminal device.
        self.device_tag = device_tag
        # The operating system type of the terminal device. Valid values:
        self.device_type = device_type
        # The operating system version of the terminal device.
        self.device_version = device_version
        # The disk model of the terminal device.
        self.disk = disk
        # The available disk space, in GB.
        self.disk_available = disk_available
        # The used disk space, in GB.
        self.disk_used = disk_used
        # The office data protection status. Valid values:
        self.dlp_status = dlp_status
        # The anti-intrusion status. Valid values:
        self.edr_status = edr_status
        # The historical users of the terminal device.
        self.history_users = history_users
        # The name of the terminal device.
        self.hostname = hostname
        # The Internet access status. Valid values:
        self.ia_status = ia_status
        # The internal IP address of the terminal device.
        self.inner_ip = inner_ip
        # Indicates whether the terminal has joined an AD domain.
        self.join_ad_domain = join_ad_domain
        # The MAC address of the terminal device.
        self.mac = mac
        # The IDs of matched device groups.
        self.match_device_group_ids = match_device_group_ids
        # The memory capacity of the terminal device. Unit: GB.
        self.memory = memory
        # The network access control status. Valid values:
        self.nac_status = nac_status
        # The list of network interface controllers (NICs) of the terminal device.
        self.net_interface_info = net_interface_info
        # The private access status. Valid values:
        self.pa_status = pa_status
        # The list of processes running on the terminal.
        self.processes = processes
        # The province to which the public IP address belongs.
        self.province = province
        # The province name in English.
        self.province_en = province_en
        # The province name in Chinese.
        self.province_zh = province_zh
        # The user ID.
        self.sase_user_id = sase_user_id
        # Indicates whether sharing is enabled for the device. Valid values:
        self.sharing_status = sharing_status
        # The motherboard serial number.
        self.sn_base_board = sn_base_board
        # The serial number (SN) of the BIOS system.
        self.sn_bios = sn_bios
        # The hard disk serial number.
        self.sn_disk_drive = sn_disk_drive
        # The serial number (SN) of the processor.
        self.sn_processor = sn_processor
        # The system serial number.
        self.sn_system = sn_system
        # The logon IP address of the terminal device.
        self.src_ip = src_ip
        # The timestamp when the terminal process information was collected.
        self.terminal_info_collect_time = terminal_info_collect_time
        # The last online time of the terminal device.
        self.update_time = update_time
        # The username.
        self.username = username
        # The name of the office area.
        self.workshop = workshop

    def validate(self):
        if self.history_users:
            for v1 in self.history_users:
                 if v1:
                    v1.validate()
        if self.net_interface_info:
            for v1 in self.net_interface_info:
                 if v1:
                    v1.validate()
        if self.processes:
            for v1 in self.processes:
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

        if self.auto_login_status is not None:
            result['AutoLoginStatus'] = self.auto_login_status

        if self.battery_health_percentage is not None:
            result['BatteryHealthPercentage'] = self.battery_health_percentage

        if self.battery_remaining_percentage is not None:
            result['BatteryRemainingPercentage'] = self.battery_remaining_percentage

        if self.cpu is not None:
            result['CPU'] = self.cpu

        if self.city is not None:
            result['City'] = self.city

        if self.city_en is not None:
            result['CityEn'] = self.city_en

        if self.city_zh is not None:
            result['CityZh'] = self.city_zh

        if self.continent is not None:
            result['Continent'] = self.continent

        if self.continent_en is not None:
            result['ContinentEn'] = self.continent_en

        if self.continent_zh is not None:
            result['ContinentZh'] = self.continent_zh

        if self.country is not None:
            result['Country'] = self.country

        if self.country_en is not None:
            result['CountryEn'] = self.country_en

        if self.country_zh is not None:
            result['CountryZh'] = self.country_zh

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

        if self.disk_available is not None:
            result['DiskAvailable'] = self.disk_available

        if self.disk_used is not None:
            result['DiskUsed'] = self.disk_used

        if self.dlp_status is not None:
            result['DlpStatus'] = self.dlp_status

        if self.edr_status is not None:
            result['EdrStatus'] = self.edr_status

        result['HistoryUsers'] = []
        if self.history_users is not None:
            for k1 in self.history_users:
                result['HistoryUsers'].append(k1.to_map() if k1 else None)

        if self.hostname is not None:
            result['Hostname'] = self.hostname

        if self.ia_status is not None:
            result['IaStatus'] = self.ia_status

        if self.inner_ip is not None:
            result['InnerIP'] = self.inner_ip

        if self.join_ad_domain is not None:
            result['JoinAdDomain'] = self.join_ad_domain

        if self.mac is not None:
            result['Mac'] = self.mac

        if self.match_device_group_ids is not None:
            result['MatchDeviceGroupIds'] = self.match_device_group_ids

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

        result['Processes'] = []
        if self.processes is not None:
            for k1 in self.processes:
                result['Processes'].append(k1.to_map() if k1 else None)

        if self.province is not None:
            result['Province'] = self.province

        if self.province_en is not None:
            result['ProvinceEn'] = self.province_en

        if self.province_zh is not None:
            result['ProvinceZh'] = self.province_zh

        if self.sase_user_id is not None:
            result['SaseUserId'] = self.sase_user_id

        if self.sharing_status is not None:
            result['SharingStatus'] = self.sharing_status

        if self.sn_base_board is not None:
            result['SnBaseBoard'] = self.sn_base_board

        if self.sn_bios is not None:
            result['SnBios'] = self.sn_bios

        if self.sn_disk_drive is not None:
            result['SnDiskDrive'] = self.sn_disk_drive

        if self.sn_processor is not None:
            result['SnProcessor'] = self.sn_processor

        if self.sn_system is not None:
            result['SnSystem'] = self.sn_system

        if self.src_ip is not None:
            result['SrcIP'] = self.src_ip

        if self.terminal_info_collect_time is not None:
            result['TerminalInfoCollectTime'] = self.terminal_info_collect_time

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        if self.username is not None:
            result['Username'] = self.username

        if self.workshop is not None:
            result['Workshop'] = self.workshop

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppStatus') is not None:
            self.app_status = m.get('AppStatus')

        if m.get('AppVersion') is not None:
            self.app_version = m.get('AppVersion')

        if m.get('AutoLoginStatus') is not None:
            self.auto_login_status = m.get('AutoLoginStatus')

        if m.get('BatteryHealthPercentage') is not None:
            self.battery_health_percentage = m.get('BatteryHealthPercentage')

        if m.get('BatteryRemainingPercentage') is not None:
            self.battery_remaining_percentage = m.get('BatteryRemainingPercentage')

        if m.get('CPU') is not None:
            self.cpu = m.get('CPU')

        if m.get('City') is not None:
            self.city = m.get('City')

        if m.get('CityEn') is not None:
            self.city_en = m.get('CityEn')

        if m.get('CityZh') is not None:
            self.city_zh = m.get('CityZh')

        if m.get('Continent') is not None:
            self.continent = m.get('Continent')

        if m.get('ContinentEn') is not None:
            self.continent_en = m.get('ContinentEn')

        if m.get('ContinentZh') is not None:
            self.continent_zh = m.get('ContinentZh')

        if m.get('Country') is not None:
            self.country = m.get('Country')

        if m.get('CountryEn') is not None:
            self.country_en = m.get('CountryEn')

        if m.get('CountryZh') is not None:
            self.country_zh = m.get('CountryZh')

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

        if m.get('DiskAvailable') is not None:
            self.disk_available = m.get('DiskAvailable')

        if m.get('DiskUsed') is not None:
            self.disk_used = m.get('DiskUsed')

        if m.get('DlpStatus') is not None:
            self.dlp_status = m.get('DlpStatus')

        if m.get('EdrStatus') is not None:
            self.edr_status = m.get('EdrStatus')

        self.history_users = []
        if m.get('HistoryUsers') is not None:
            for k1 in m.get('HistoryUsers'):
                temp_model = main_models.GetUserDeviceResponseBodyDeviceHistoryUsers()
                self.history_users.append(temp_model.from_map(k1))

        if m.get('Hostname') is not None:
            self.hostname = m.get('Hostname')

        if m.get('IaStatus') is not None:
            self.ia_status = m.get('IaStatus')

        if m.get('InnerIP') is not None:
            self.inner_ip = m.get('InnerIP')

        if m.get('JoinAdDomain') is not None:
            self.join_ad_domain = m.get('JoinAdDomain')

        if m.get('Mac') is not None:
            self.mac = m.get('Mac')

        if m.get('MatchDeviceGroupIds') is not None:
            self.match_device_group_ids = m.get('MatchDeviceGroupIds')

        if m.get('Memory') is not None:
            self.memory = m.get('Memory')

        if m.get('NacStatus') is not None:
            self.nac_status = m.get('NacStatus')

        self.net_interface_info = []
        if m.get('NetInterfaceInfo') is not None:
            for k1 in m.get('NetInterfaceInfo'):
                temp_model = main_models.GetUserDeviceResponseBodyDeviceNetInterfaceInfo()
                self.net_interface_info.append(temp_model.from_map(k1))

        if m.get('PaStatus') is not None:
            self.pa_status = m.get('PaStatus')

        self.processes = []
        if m.get('Processes') is not None:
            for k1 in m.get('Processes'):
                temp_model = main_models.GetUserDeviceResponseBodyDeviceProcesses()
                self.processes.append(temp_model.from_map(k1))

        if m.get('Province') is not None:
            self.province = m.get('Province')

        if m.get('ProvinceEn') is not None:
            self.province_en = m.get('ProvinceEn')

        if m.get('ProvinceZh') is not None:
            self.province_zh = m.get('ProvinceZh')

        if m.get('SaseUserId') is not None:
            self.sase_user_id = m.get('SaseUserId')

        if m.get('SharingStatus') is not None:
            self.sharing_status = m.get('SharingStatus')

        if m.get('SnBaseBoard') is not None:
            self.sn_base_board = m.get('SnBaseBoard')

        if m.get('SnBios') is not None:
            self.sn_bios = m.get('SnBios')

        if m.get('SnDiskDrive') is not None:
            self.sn_disk_drive = m.get('SnDiskDrive')

        if m.get('SnProcessor') is not None:
            self.sn_processor = m.get('SnProcessor')

        if m.get('SnSystem') is not None:
            self.sn_system = m.get('SnSystem')

        if m.get('SrcIP') is not None:
            self.src_ip = m.get('SrcIP')

        if m.get('TerminalInfoCollectTime') is not None:
            self.terminal_info_collect_time = m.get('TerminalInfoCollectTime')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        if m.get('Username') is not None:
            self.username = m.get('Username')

        if m.get('Workshop') is not None:
            self.workshop = m.get('Workshop')

        return self

class GetUserDeviceResponseBodyDeviceProcesses(DaraModel):
    def __init__(
        self,
        cpu: float = None,
        description: str = None,
        memory: int = None,
        name: str = None,
    ):
        # The CPU usage percentage of the process.
        self.cpu = cpu
        # The process running description.
        self.description = description
        # The memory usage of the process, in MB.
        self.memory = memory
        # The process name.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cpu is not None:
            result['Cpu'] = self.cpu

        if self.description is not None:
            result['Description'] = self.description

        if self.memory is not None:
            result['Memory'] = self.memory

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Memory') is not None:
            self.memory = m.get('Memory')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class GetUserDeviceResponseBodyDeviceNetInterfaceInfo(DaraModel):
    def __init__(
        self,
        mac: str = None,
        name: str = None,
    ):
        # The MAC address of the NIC.
        self.mac = mac
        # The name of the NIC.
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

class GetUserDeviceResponseBodyDeviceHistoryUsers(DaraModel):
    def __init__(
        self,
        sase_user_id: str = None,
        username: str = None,
    ):
        # The user ID.
        self.sase_user_id = sase_user_id
        # The username.
        self.username = username

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.sase_user_id is not None:
            result['SaseUserId'] = self.sase_user_id

        if self.username is not None:
            result['Username'] = self.username

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SaseUserId') is not None:
            self.sase_user_id = m.get('SaseUserId')

        if m.get('Username') is not None:
            self.username = m.get('Username')

        return self

