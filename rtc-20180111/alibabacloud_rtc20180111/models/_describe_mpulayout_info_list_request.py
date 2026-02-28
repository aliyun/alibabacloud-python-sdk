# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeMPULayoutInfoListRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        layout_id: int = None,
        name: str = None,
        owner_id: int = None,
        page_num: int = None,
        page_size: int = None,
    ):
        # This parameter is required.
        self.app_id = app_id
        self.layout_id = layout_id
        self.name = name
        self.owner_id = owner_id
        self.page_num = page_num
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.layout_id is not None:
            result['LayoutId'] = self.layout_id

        if self.name is not None:
            result['Name'] = self.name

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('LayoutId') is not None:
            self.layout_id = m.get('LayoutId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self

