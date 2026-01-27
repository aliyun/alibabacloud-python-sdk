# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListDynamicRoutesRequest(DaraModel):
    def __init__(
        self,
        application_id: str = None,
        current_page: int = None,
        dynamic_route_ids: List[str] = None,
        name: str = None,
        next_hop: str = None,
        page_size: int = None,
        region_ids: List[str] = None,
        status: str = None,
        tag_id: str = None,
    ):
        self.application_id = application_id
        # This parameter is required.
        self.current_page = current_page
        self.dynamic_route_ids = dynamic_route_ids
        self.name = name
        self.next_hop = next_hop
        # This parameter is required.
        self.page_size = page_size
        self.region_ids = region_ids
        self.status = status
        self.tag_id = tag_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.dynamic_route_ids is not None:
            result['DynamicRouteIds'] = self.dynamic_route_ids

        if self.name is not None:
            result['Name'] = self.name

        if self.next_hop is not None:
            result['NextHop'] = self.next_hop

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_ids is not None:
            result['RegionIds'] = self.region_ids

        if self.status is not None:
            result['Status'] = self.status

        if self.tag_id is not None:
            result['TagId'] = self.tag_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('DynamicRouteIds') is not None:
            self.dynamic_route_ids = m.get('DynamicRouteIds')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NextHop') is not None:
            self.next_hop = m.get('NextHop')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionIds') is not None:
            self.region_ids = m.get('RegionIds')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TagId') is not None:
            self.tag_id = m.get('TagId')

        return self

