# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeInstanceAntiBruteForceRulesRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        resource_owner_id: int = None,
        source_ip: str = None,
        uuid_list: List[str] = None,
    ):
        # The number of the page to return. Default value: **1**.
        self.current_page = current_page
        # The number of entries to return on each page. Default value: **10000**.
        self.page_size = page_size
        self.resource_owner_id = resource_owner_id
        # The source IP address of the request.
        self.source_ip = source_ip
        # The UUIDs of the servers.
        # 
        # >  You can call the [DescribeCloudCenterInstances](~~DescribeCloudCenterInstances~~) operation to query the UUIDs of servers.
        self.uuid_list = uuid_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

        if self.uuid_list is not None:
            result['UuidList'] = self.uuid_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        if m.get('UuidList') is not None:
            self.uuid_list = m.get('UuidList')

        return self

