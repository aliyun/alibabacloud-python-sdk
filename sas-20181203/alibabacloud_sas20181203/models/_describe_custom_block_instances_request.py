# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeCustomBlockInstancesRequest(DaraModel):
    def __init__(
        self,
        block_ip: str = None,
        bound: str = None,
        current_page: int = None,
        page_size: int = None,
        resource_owner_id: int = None,
        status: int = None,
    ):
        # The IP address that you want to specify in the rule.
        # 
        # >  You can call the [DescribeCustomBlockRecords](~~DescribeCustomBlockRecords~~) operation to obtain the IP address.
        self.block_ip = block_ip
        # The traffic direction that you want to specify in the custom rule. Valid values:
        # 
        # *   **in**: inbound
        # *   **out**: outbound
        self.bound = bound
        # The page number. Default value: **1**.
        self.current_page = current_page
        # The number of entries per page. Default value: **20**.
        self.page_size = page_size
        self.resource_owner_id = resource_owner_id
        # Specifies whether the rule is enabled for the server.
        # 
        # *   **2**: enabling failed
        # *   **1**: enabled
        # *   **0**: disabled
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.block_ip is not None:
            result['BlockIp'] = self.block_ip

        if self.bound is not None:
            result['Bound'] = self.bound

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BlockIp') is not None:
            self.block_ip = m.get('BlockIp')

        if m.get('Bound') is not None:
            self.bound = m.get('Bound')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

