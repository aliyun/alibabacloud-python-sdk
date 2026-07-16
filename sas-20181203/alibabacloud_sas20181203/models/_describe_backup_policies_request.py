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
        # The page number from which to start displaying the returned results. Default value: 1, which indicates that the display starts from page 1.
        # 
        # This parameter is required.
        self.current_page = current_page
        # The identification information of the server protected by the anti-ransomware policy to query. You can enter the IP address or instance ID of the server.
        self.machine_remark = machine_remark
        # The name of the anti-ransomware protection policy to query.
        self.name = name
        # The number of backup policies on each page during paginated queries. Default value: 10, which indicates that each page contains 10 protection policies.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The status of the anti-ransomware protection policy.
        # 
        # - **enabled**: The policy is manually enabled.
        # 
        # - **disabled**: The policy is manually disabled. After the policy is disabled, running backup tasks will stop.
        # 
        # - **closed**: The anti-ransomware capacity is exceeded, and the system disables the policy.
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

