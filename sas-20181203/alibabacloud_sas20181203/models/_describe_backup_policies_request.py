# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeBackupPoliciesRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        machine_remark: str = None,
        name: str = None,
        page_size: int = None,
        status: str = None,
    ):
        # The number of the page to return. Default value: 1.
        # 
        # This parameter is required.
        self.current_page = current_page
        # The information that you want to use to identify the servers protected by the anti-ransomware policy. You can enter the IP address or ID of a server.
        self.machine_remark = machine_remark
        # The name of the anti-ransomware policy that you want to query.
        self.name = name
        # The number of entries to return on each page. Default value: 10.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The status of the anti-ransomware policy. Valid values:
        # 
        # *   **enabled**: The anti-ransomware policy is manually enabled.
        # *   **disabled**: The anti-ransomware policy is manually disabled. After an anti-ransomware policy is disabled, the data backup task that is running based on the policy stops.
        # *   **closed**: The anti-ransomware policy automatically stops because the anti-ransomware capacity is insufficient.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.machine_remark is not None:
            result['MachineRemark'] = self.machine_remark

        if self.name is not None:
            result['Name'] = self.name

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('MachineRemark') is not None:
            self.machine_remark = m.get('MachineRemark')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

