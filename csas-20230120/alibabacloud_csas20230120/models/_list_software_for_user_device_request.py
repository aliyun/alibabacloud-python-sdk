# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListSoftwareForUserDeviceRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        device_tag: str = None,
        page_size: int = None,
    ):
        # This parameter is required.
        self.current_page = current_page
        # This parameter is required.
        self.device_tag = device_tag
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

        if self.device_tag is not None:
            result['DeviceTag'] = self.device_tag

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('DeviceTag') is not None:
            self.device_tag = m.get('DeviceTag')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self

