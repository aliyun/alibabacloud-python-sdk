# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeSecurityEventMarkMissListRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        event_name: str = None,
        page_size: int = None,
        remark: str = None,
        resource_owner_id: int = None,
        source_ip: str = None,
    ):
        # The page number of the page to return. Default value: **1**, which indicates that the first page is returned.
        # 
        # This parameter is required.
        self.current_page = current_page
        # The alert event name (child class).
        self.event_name = event_name
        # The number of whitelist rules to display on each page in a paged query. Default value: **20**, which indicates that 20 whitelist rules are displayed on each page.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The asset search keyword. You can enter the IP address, public IP address, private IP address, or asset name for fuzzy matching.
        self.remark = remark
        self.resource_owner_id = resource_owner_id
        # The IP address of the access source.
        self.source_ip = source_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.event_name is not None:
            result['EventName'] = self.event_name

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('EventName') is not None:
            self.event_name = m.get('EventName')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        return self

