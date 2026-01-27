# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListExcessiveDeviceRegistrationApplicationsRequest(DaraModel):
    def __init__(
        self,
        application_ids: List[str] = None,
        current_page: int = None,
        department: str = None,
        device_tag: str = None,
        hostname: str = None,
        mac: str = None,
        page_size: int = None,
        sase_user_id: str = None,
        statuses: List[str] = None,
        username: str = None,
    ):
        self.application_ids = application_ids
        # This parameter is required.
        self.current_page = current_page
        self.department = department
        self.device_tag = device_tag
        self.hostname = hostname
        self.mac = mac
        # This parameter is required.
        self.page_size = page_size
        self.sase_user_id = sase_user_id
        self.statuses = statuses
        self.username = username

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_ids is not None:
            result['ApplicationIds'] = self.application_ids

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.department is not None:
            result['Department'] = self.department

        if self.device_tag is not None:
            result['DeviceTag'] = self.device_tag

        if self.hostname is not None:
            result['Hostname'] = self.hostname

        if self.mac is not None:
            result['Mac'] = self.mac

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.sase_user_id is not None:
            result['SaseUserId'] = self.sase_user_id

        if self.statuses is not None:
            result['Statuses'] = self.statuses

        if self.username is not None:
            result['Username'] = self.username

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationIds') is not None:
            self.application_ids = m.get('ApplicationIds')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('Department') is not None:
            self.department = m.get('Department')

        if m.get('DeviceTag') is not None:
            self.device_tag = m.get('DeviceTag')

        if m.get('Hostname') is not None:
            self.hostname = m.get('Hostname')

        if m.get('Mac') is not None:
            self.mac = m.get('Mac')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SaseUserId') is not None:
            self.sase_user_id = m.get('SaseUserId')

        if m.get('Statuses') is not None:
            self.statuses = m.get('Statuses')

        if m.get('Username') is not None:
            self.username = m.get('Username')

        return self

