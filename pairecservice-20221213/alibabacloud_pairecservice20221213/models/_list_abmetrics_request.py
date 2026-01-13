# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListABMetricsRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        name: str = None,
        page_number: int = None,
        page_size: int = None,
        realtime: bool = None,
        scene_id: str = None,
        table_meta_id: str = None,
        type: str = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id
        self.name = name
        self.page_number = page_number
        self.page_size = page_size
        self.realtime = realtime
        self.scene_id = scene_id
        self.table_meta_id = table_meta_id
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.name is not None:
            result['Name'] = self.name

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.realtime is not None:
            result['Realtime'] = self.realtime

        if self.scene_id is not None:
            result['SceneId'] = self.scene_id

        if self.table_meta_id is not None:
            result['TableMetaId'] = self.table_meta_id

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Realtime') is not None:
            self.realtime = m.get('Realtime')

        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')

        if m.get('TableMetaId') is not None:
            self.table_meta_id = m.get('TableMetaId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

