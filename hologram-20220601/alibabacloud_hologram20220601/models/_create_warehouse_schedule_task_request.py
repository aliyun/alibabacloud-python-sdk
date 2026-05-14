# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateWarehouseScheduleTaskRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        elastic_cu: int = None,
        end_time: str = None,
        start_time: str = None,
        warehouse_id: int = None,
    ):
        self.description = description
        # This parameter is required.
        self.elastic_cu = elastic_cu
        # This parameter is required.
        self.end_time = end_time
        # This parameter is required.
        self.start_time = start_time
        # This parameter is required.
        self.warehouse_id = warehouse_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['description'] = self.description

        if self.elastic_cu is not None:
            result['elasticCu'] = self.elastic_cu

        if self.end_time is not None:
            result['endTime'] = self.end_time

        if self.start_time is not None:
            result['startTime'] = self.start_time

        if self.warehouse_id is not None:
            result['warehouseId'] = self.warehouse_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('elasticCu') is not None:
            self.elastic_cu = m.get('elasticCu')

        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')

        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')

        if m.get('warehouseId') is not None:
            self.warehouse_id = m.get('warehouseId')

        return self

