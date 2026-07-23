# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListABMetricGroupsRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        order: str = None,
        page_number: int = None,
        page_size: int = None,
        realtime: bool = None,
        scene_id: str = None,
        sort_by: str = None,
    ):
        # The instance ID. You can call the [ListInstances](https://help.aliyun.com/document_detail/2411819.html) operation to obtain this ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The sort order. Valid values:
        # 
        # - ASC: ascending.
        # 
        # - DESC: descending.
        self.order = order
        # The page number.
        self.page_number = page_number
        # The number of entries to return on each page.
        self.page_size = page_size
        # Specifies whether to return only real-time A/B metric groups.
        self.realtime = realtime
        # The scene ID. You can call the [ListScenes](\\(~~2402581~~\\)) operation to obtain this ID.
        self.scene_id = scene_id
        # The field to sort the results by. Valid values:
        # 
        # - GmtCreateTime: creation time.
        # 
        # - GmtModifiedTime: modification time.
        self.sort_by = sort_by

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.order is not None:
            result['Order'] = self.order

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.realtime is not None:
            result['Realtime'] = self.realtime

        if self.scene_id is not None:
            result['SceneId'] = self.scene_id

        if self.sort_by is not None:
            result['SortBy'] = self.sort_by

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Order') is not None:
            self.order = m.get('Order')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Realtime') is not None:
            self.realtime = m.get('Realtime')

        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')

        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')

        return self

