# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RenameHoloWarehouseRequest(DaraModel):
    def __init__(
        self,
        name: str = None,
        new_warehouse_name: str = None,
    ):
        # The original name of the virtual warehouse.
        # 
        # This parameter is required.
        self.name = name
        # The new name of the virtual warehouse.
        # 
        # This parameter is required.
        self.new_warehouse_name = new_warehouse_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['name'] = self.name

        if self.new_warehouse_name is not None:
            result['newWarehouseName'] = self.new_warehouse_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('newWarehouseName') is not None:
            self.new_warehouse_name = m.get('newWarehouseName')

        return self

