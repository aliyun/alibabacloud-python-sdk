# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteWarehouseScheduleTaskRequest(DaraModel):
    def __init__(
        self,
        id: str = None,
        warehouse_id: str = None,
    ):
        # This parameter is required.
        self.id = id
        self.warehouse_id = warehouse_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['id'] = self.id

        if self.warehouse_id is not None:
            result['warehouseId'] = self.warehouse_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('warehouseId') is not None:
            self.warehouse_id = m.get('warehouseId')

        return self

