# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListUserDevicesRequest(DaraModel):
    def __init__(
        self,
        app_statuses: List[str] = None,
        app_versions: List[str] = None,
        auto_login_statuses: List[str] = None,
        current_page: int = None,
        department: str = None,
        device_belong: str = None,
        device_group_id: str = None,
        device_statuses: List[str] = None,
        device_tags: List[str] = None,
        device_types: List[str] = None,
        dlp_statuses: List[str] = None,
        hostname: str = None,
        ia_statuses: List[str] = None,
        inner_ip: str = None,
        mac: str = None,
        nac_statuses: List[str] = None,
        pa_statuses: List[str] = None,
        page_size: int = None,
        sase_user_id: str = None,
        sharing_status: bool = None,
        sn_bios: str = None,
        sn_system: str = None,
        sort_by: str = None,
        username: str = None,
        workshop: str = None,
    ):
        # The collection of client statuses.
        self.app_statuses = app_statuses
        # The collection of client versions.
        self.app_versions = app_versions
        self.auto_login_statuses = auto_login_statuses
        # The page number of the current page in a paging query. Valid values: 1 to 10000.
        # 
        # This parameter is required.
        self.current_page = current_page
        # The department to which the user belongs. The value is 1 to 128 characters in length and supports Chinese characters and uppercase and lowercase letters. It can contain digits, periods (.), commas (,), semicolons (;), hyphens (-), underscores (_), forward slashes (/), at signs (@), and spaces.
        self.department = department
        # The ownership of the endpoint device. Valid values:
        # - **Personal**: personal device.
        # - **Company**: company device.
        self.device_belong = device_belong
        # The device group ID.
        self.device_group_id = device_group_id
        # The collection of endpoint device statuses.
        self.device_statuses = device_statuses
        # The collection of endpoint device IDs.
        self.device_tags = device_tags
        # The collection of endpoint device operating system types.
        self.device_types = device_types
        # The collection of office data protection statuses.
        self.dlp_statuses = dlp_statuses
        # The name of the endpoint device. The value is 1 to 128 characters in length and supports Chinese characters and uppercase and lowercase letters. It can contain digits, periods (.), commas (,), semicolons (;), hyphens (-), underscores (_), forward slashes (/), at signs (@), and spaces. If you enter only an underscore (_), endpoint devices whose names contain 4-byte UTF-8 characters are also queried.
        self.hostname = hostname
        # The collection of Internet access statuses.
        self.ia_statuses = ia_statuses
        # The internal IP address of the endpoint device.
        self.inner_ip = inner_ip
        # The MAC address of the endpoint device.
        self.mac = mac
        # The collection of network access control statuses.
        self.nac_statuses = nac_statuses
        # The collection of private access statuses.
        self.pa_statuses = pa_statuses
        # The number of entries per page in a paging query. Settings: 1 to 500.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The user ID. You can obtain this value from the following operations:
        # - [GetUserDevice](~~GetUserDevice~~): Queries the details of a user endpoint device.
        # - [ListUserDevices](~~ListUserDevices~~): Lists user endpoint devices.
        self.sase_user_id = sase_user_id
        # Specifies whether sharing is enabled for the device. Valid values:
        # - **true**: Sharing is enabled.
        # - **false**: Sharing is disabled.
        self.sharing_status = sharing_status
        # The BIOS system serial number.
        self.sn_bios = sn_bios
        # The system serial number.
        self.sn_system = sn_system
        # The sort parameter. Valid values:
        # - **Username**: sorted by Username in ascending order.
        # - **AppVersion**: sorted by AppVersion in descending order.
        # - **UpdateTime**: sorted by UpdateTime in descending order.
        # - **CreateTime**: sorted by CreateTime in descending order.
        self.sort_by = sort_by
        # The username. The value is 1 to 128 characters in length and supports Chinese characters and uppercase and lowercase letters. It can contain digits, periods (.), underscores (_), hyphens (-), asterisks (*), at signs (@), and spaces.
        self.username = username
        # The name of the office area.
        self.workshop = workshop

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_statuses is not None:
            result['AppStatuses'] = self.app_statuses

        if self.app_versions is not None:
            result['AppVersions'] = self.app_versions

        if self.auto_login_statuses is not None:
            result['AutoLoginStatuses'] = self.auto_login_statuses

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.department is not None:
            result['Department'] = self.department

        if self.device_belong is not None:
            result['DeviceBelong'] = self.device_belong

        if self.device_group_id is not None:
            result['DeviceGroupId'] = self.device_group_id

        if self.device_statuses is not None:
            result['DeviceStatuses'] = self.device_statuses

        if self.device_tags is not None:
            result['DeviceTags'] = self.device_tags

        if self.device_types is not None:
            result['DeviceTypes'] = self.device_types

        if self.dlp_statuses is not None:
            result['DlpStatuses'] = self.dlp_statuses

        if self.hostname is not None:
            result['Hostname'] = self.hostname

        if self.ia_statuses is not None:
            result['IaStatuses'] = self.ia_statuses

        if self.inner_ip is not None:
            result['InnerIp'] = self.inner_ip

        if self.mac is not None:
            result['Mac'] = self.mac

        if self.nac_statuses is not None:
            result['NacStatuses'] = self.nac_statuses

        if self.pa_statuses is not None:
            result['PaStatuses'] = self.pa_statuses

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.sase_user_id is not None:
            result['SaseUserId'] = self.sase_user_id

        if self.sharing_status is not None:
            result['SharingStatus'] = self.sharing_status

        if self.sn_bios is not None:
            result['SnBios'] = self.sn_bios

        if self.sn_system is not None:
            result['SnSystem'] = self.sn_system

        if self.sort_by is not None:
            result['SortBy'] = self.sort_by

        if self.username is not None:
            result['Username'] = self.username

        if self.workshop is not None:
            result['Workshop'] = self.workshop

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppStatuses') is not None:
            self.app_statuses = m.get('AppStatuses')

        if m.get('AppVersions') is not None:
            self.app_versions = m.get('AppVersions')

        if m.get('AutoLoginStatuses') is not None:
            self.auto_login_statuses = m.get('AutoLoginStatuses')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('Department') is not None:
            self.department = m.get('Department')

        if m.get('DeviceBelong') is not None:
            self.device_belong = m.get('DeviceBelong')

        if m.get('DeviceGroupId') is not None:
            self.device_group_id = m.get('DeviceGroupId')

        if m.get('DeviceStatuses') is not None:
            self.device_statuses = m.get('DeviceStatuses')

        if m.get('DeviceTags') is not None:
            self.device_tags = m.get('DeviceTags')

        if m.get('DeviceTypes') is not None:
            self.device_types = m.get('DeviceTypes')

        if m.get('DlpStatuses') is not None:
            self.dlp_statuses = m.get('DlpStatuses')

        if m.get('Hostname') is not None:
            self.hostname = m.get('Hostname')

        if m.get('IaStatuses') is not None:
            self.ia_statuses = m.get('IaStatuses')

        if m.get('InnerIp') is not None:
            self.inner_ip = m.get('InnerIp')

        if m.get('Mac') is not None:
            self.mac = m.get('Mac')

        if m.get('NacStatuses') is not None:
            self.nac_statuses = m.get('NacStatuses')

        if m.get('PaStatuses') is not None:
            self.pa_statuses = m.get('PaStatuses')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SaseUserId') is not None:
            self.sase_user_id = m.get('SaseUserId')

        if m.get('SharingStatus') is not None:
            self.sharing_status = m.get('SharingStatus')

        if m.get('SnBios') is not None:
            self.sn_bios = m.get('SnBios')

        if m.get('SnSystem') is not None:
            self.sn_system = m.get('SnSystem')

        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')

        if m.get('Username') is not None:
            self.username = m.get('Username')

        if m.get('Workshop') is not None:
            self.workshop = m.get('Workshop')

        return self

