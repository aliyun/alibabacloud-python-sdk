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
        self.app_statuses = app_statuses
        self.department = department
        self.device_belong = device_belong
        self.device_statuses = device_statuses
        self.device_tags = device_tags
        self.device_types = device_types
        self.dlp_statuses = dlp_statuses
        self.hostname = hostname
        self.ia_statuses = ia_statuses
        self.mac = mac
        self.nac_statuses = nac_statuses
        self.pa_statuses = pa_statuses
        self.sase_user_id = sase_user_id
        self.sharing_status = sharing_status
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

