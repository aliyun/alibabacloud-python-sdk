# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ExportUserDevicesRequest(DaraModel):
    def __init__(
        self,
        app_statuses: List[str] = None,
        department: str = None,
        device_belong: str = None,
        device_statuses: List[str] = None,
        device_tags: List[str] = None,
        device_types: List[str] = None,
        dlp_statuses: List[str] = None,
        hostname: str = None,
        ia_statuses: List[str] = None,
        mac: str = None,
        nac_statuses: List[str] = None,
        pa_statuses: List[str] = None,
        sase_user_id: str = None,
        sharing_status: bool = None,
        username: str = None,
    ):
        # Collection of client statuses.
        self.app_statuses = app_statuses
        # Department name. Must be 1 to 128 characters long. Supports Chinese, uppercase and lowercase letters, digits, periods (.), commas (,), semicolons (;), hyphens (-), underscores (_), forward slashes (/), at signs (@), and spaces.
        self.department = department
        # Terminal device ownership. Valid values:
        # 
        # - **Personal**: Personal device.
        # 
        # - **Company**: Company device.
        self.device_belong = device_belong
        # Collection of terminal device statuses.
        self.device_statuses = device_statuses
        # Collection of terminal device IDs.
        self.device_tags = device_tags
        # Collection of terminal device operating system types.
        self.device_types = device_types
        # Collection of office data protection statuses.
        self.dlp_statuses = dlp_statuses
        # Terminal device name. Must be 1 to 128 characters long. Supports Chinese, uppercase and lowercase letters, digits, periods (.), commas (,), semicolons (;), hyphens (-), underscores (_), forward slashes (/), at signs (@), and spaces. If you enter only an underscore (_), the system returns all terminal devices whose names contain four-byte UTF-8 characters.
        self.hostname = hostname
        # Collection of Internet access statuses.
        self.ia_statuses = ia_statuses
        # MAC address of the terminal device.
        self.mac = mac
        # Collection of network admission statuses.
        self.nac_statuses = nac_statuses
        # Collection of private network access statuses.
        self.pa_statuses = pa_statuses
        # User ID.
        self.sase_user_id = sase_user_id
        # Whether device sharing is enabled. Valid values:
        # 
        # - **true**: Sharing is enabled.
        # 
        # - **false**: Sharing is disabled.
        self.sharing_status = sharing_status
        # Username. Must be 1 to 128 characters long. Supports Chinese, uppercase and lowercase letters, digits, periods (.), underscores (_), hyphens (-), asterisks (\\*), at signs (@), and spaces.
        self.username = username

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_statuses is not None:
            result['AppStatuses'] = self.app_statuses

        if self.department is not None:
            result['Department'] = self.department

        if self.device_belong is not None:
            result['DeviceBelong'] = self.device_belong

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

        if self.mac is not None:
            result['Mac'] = self.mac

        if self.nac_statuses is not None:
            result['NacStatuses'] = self.nac_statuses

        if self.pa_statuses is not None:
            result['PaStatuses'] = self.pa_statuses

        if self.sase_user_id is not None:
            result['SaseUserId'] = self.sase_user_id

        if self.sharing_status is not None:
            result['SharingStatus'] = self.sharing_status

        if self.username is not None:
            result['Username'] = self.username

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppStatuses') is not None:
            self.app_statuses = m.get('AppStatuses')

        if m.get('Department') is not None:
            self.department = m.get('Department')

        if m.get('DeviceBelong') is not None:
            self.device_belong = m.get('DeviceBelong')

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

        if m.get('Mac') is not None:
            self.mac = m.get('Mac')

        if m.get('NacStatuses') is not None:
            self.nac_statuses = m.get('NacStatuses')

        if m.get('PaStatuses') is not None:
            self.pa_statuses = m.get('PaStatuses')

        if m.get('SaseUserId') is not None:
            self.sase_user_id = m.get('SaseUserId')

        if m.get('SharingStatus') is not None:
            self.sharing_status = m.get('SharingStatus')

        if m.get('Username') is not None:
            self.username = m.get('Username')

        return self

