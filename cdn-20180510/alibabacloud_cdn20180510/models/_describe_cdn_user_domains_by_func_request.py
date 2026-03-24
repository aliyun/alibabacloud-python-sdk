# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeCdnUserDomainsByFuncRequest(DaraModel):
    def __init__(
        self,
        func_id: int = None,
        page_number: int = None,
        page_size: int = None,
        resource_group_id: str = None,
    ):
        # The ID of the feature.
        # 
        # For example, the ID of the origin host feature (set_req_host_header) is 18.
        # 
        # This parameter is required.
        self.func_id = func_id
        # The number of the page to return. Default value: **1**.
        # 
        # Valid values: **1** to **100000**.
        self.page_number = page_number
        # The number of domain names to return on each page. Default value: **20**.
        # 
        # Valid values: **1** to **50**.
        self.page_size = page_size
        # The ID of the resource group.
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.func_id is not None:
            result['FuncId'] = self.func_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FuncId') is not None:
            self.func_id = m.get('FuncId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        return self

