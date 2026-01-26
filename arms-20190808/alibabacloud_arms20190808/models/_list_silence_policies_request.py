# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListSilencePoliciesRequest(DaraModel):
    def __init__(
        self,
        is_detail: bool = None,
        name: str = None,
        page: int = None,
        region_id: str = None,
        size: int = None,
    ):
        # Specifies whether to query the details of a silence policy. Valid values:
        # 
        # *   `true`: Details of the silence policy are queried.
        # *   `false`: Details about notification policies are not queried.
        self.is_detail = is_detail
        # The name of the silence policy.
        self.name = name
        # The number of the page to return.
        # 
        # This parameter is required.
        self.page = page
        # The ID of the region.
        self.region_id = region_id
        # The number of entries to return on each page.
        # 
        # This parameter is required.
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.is_detail is not None:
            result['IsDetail'] = self.is_detail

        if self.name is not None:
            result['Name'] = self.name

        if self.page is not None:
            result['Page'] = self.page

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.size is not None:
            result['Size'] = self.size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsDetail') is not None:
            self.is_detail = m.get('IsDetail')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Page') is not None:
            self.page = m.get('Page')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        return self

