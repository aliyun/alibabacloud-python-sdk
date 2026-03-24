# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeAntiBruteForceRulesRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        id: int = None,
        name: str = None,
        page_size: str = None,
        resource_owner_id: int = None,
        source_ip: str = None,
    ):
        # Set which page of the returned results to start displaying the query results. The default value is **1**, indicating that the display starts from the first page.
        self.current_page = current_page
        # The ID of the anti-brute force rule.
        # > You can obtain this parameter by calling the [DescribeAntiBruteForceRules](~~DescribeAntiBruteForceRules~~) interface.
        self.id = id
        # The name of the brute force rule.
        self.name = name
        # The maximum number of data entries displayed per page during a paginated query.
        self.page_size = page_size
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

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        return self

