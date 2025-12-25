# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DataStorageItem(DaraModel):
    def __init__(
        self,
        data_type: str = None,
        project: str = None,
        region_id: str = None,
        store_name: str = None,
        store_type: str = None,
    ):
        self.data_type = data_type
        self.project = project
        self.region_id = region_id
        self.store_name = store_name
        self.store_type = store_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_type is not None:
            result['dataType'] = self.data_type

        if self.project is not None:
            result['project'] = self.project

        if self.region_id is not None:
            result['regionId'] = self.region_id

        if self.store_name is not None:
            result['storeName'] = self.store_name

        if self.store_type is not None:
            result['storeType'] = self.store_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dataType') is not None:
            self.data_type = m.get('dataType')

        if m.get('project') is not None:
            self.project = m.get('project')

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        if m.get('storeName') is not None:
            self.store_name = m.get('storeName')

        if m.get('storeType') is not None:
            self.store_type = m.get('storeType')

        return self

