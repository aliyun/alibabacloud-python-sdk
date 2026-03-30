# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListWarehouseRequest(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        warehouse_instance_ids: List[str] = None,
        warehouse_types: List[str] = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        self.warehouse_instance_ids = warehouse_instance_ids
        self.warehouse_types = warehouse_types

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.warehouse_instance_ids is not None:
            result['WarehouseInstanceIds'] = self.warehouse_instance_ids

        if self.warehouse_types is not None:
            result['WarehouseTypes'] = self.warehouse_types

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('WarehouseInstanceIds') is not None:
            self.warehouse_instance_ids = m.get('WarehouseInstanceIds')

        if m.get('WarehouseTypes') is not None:
            self.warehouse_types = m.get('WarehouseTypes')

        return self

