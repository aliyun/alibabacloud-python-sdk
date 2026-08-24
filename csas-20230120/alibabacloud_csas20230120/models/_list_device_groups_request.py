# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListDeviceGroupsRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        device_group_ids: List[str] = None,
        name: str = None,
        page_size: int = None,
    ):
        # The number of the page to return in a paged query. Valid values: 1 to 10000.
        # 
        # This parameter is required.
        self.current_page = current_page
        # The collection of device group IDs. Duplicate values are not allowed.
        self.device_group_ids = device_group_ids
        # The device label name. The name can be up to 128 characters in length and can contain Chinese characters, uppercase and lowercase letters, digits, periods (.), underscores (_), and hyphens (-).
        self.name = name
        # The number of entries to return on each page in a paged query. Valid values: 1 to 500.
        # 
        # This parameter is required.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.device_group_ids is not None:
            result['DeviceGroupIds'] = self.device_group_ids

        if self.name is not None:
            result['Name'] = self.name

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('DeviceGroupIds') is not None:
            self.device_group_ids = m.get('DeviceGroupIds')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self

