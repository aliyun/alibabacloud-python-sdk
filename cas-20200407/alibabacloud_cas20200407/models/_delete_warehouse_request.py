# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteWarehouseRequest(DaraModel):
    def __init__(
        self,
        warehouse_instance_id: str = None,
    ):
        self.warehouse_instance_id = warehouse_instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.warehouse_instance_id is not None:
            result['WarehouseInstanceId'] = self.warehouse_instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('WarehouseInstanceId') is not None:
            self.warehouse_instance_id = m.get('WarehouseInstanceId')

        return self

