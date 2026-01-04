# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeSecurityGroupsRequest(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        security_group_id: str = None,
        security_group_name: str = None,
    ):
        # The page number.
        # 
        # *   Pages start from page 1.
        # *   Default value: 1
        self.page_number = page_number
        # The number of entries per page.
        # 
        # *   Maximum value: 50.
        # *   Default value: 10
        self.page_size = page_size
        # The ID of the security group.
        self.security_group_id = security_group_id
        # The name of the security group.
        self.security_group_name = security_group_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id

        if self.security_group_name is not None:
            result['SecurityGroupName'] = self.security_group_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')

        if m.get('SecurityGroupName') is not None:
            self.security_group_name = m.get('SecurityGroupName')

        return self

