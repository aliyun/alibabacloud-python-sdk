# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListSubSceneRequest(DaraModel):
    def __init__(
        self,
        page_num: int = None,
        page_size: int = None,
        scene_id: str = None,
        show_layout_data: bool = None,
        sort_field: str = None,
    ):
        # This parameter is required.
        self.page_num = page_num
        # This parameter is required.
        self.page_size = page_size
        # This parameter is required.
        self.scene_id = scene_id
        self.show_layout_data = show_layout_data
        self.sort_field = sort_field

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.scene_id is not None:
            result['SceneId'] = self.scene_id

        if self.show_layout_data is not None:
            result['ShowLayoutData'] = self.show_layout_data

        if self.sort_field is not None:
            result['SortField'] = self.sort_field

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')

        if m.get('ShowLayoutData') is not None:
            self.show_layout_data = m.get('ShowLayoutData')

        if m.get('SortField') is not None:
            self.sort_field = m.get('SortField')

        return self

