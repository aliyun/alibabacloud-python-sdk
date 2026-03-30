# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cas20200407 import models as main_models
from darabonba.model import DaraModel

class ListWarehouseResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.ListWarehouseResponseBodyData] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.data = data
        self.max_results = max_results
        self.next_token = next_token
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListWarehouseResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListWarehouseResponseBodyData(DaraModel):
    def __init__(
        self,
        warehouse_instance_id: str = None,
        warehouse_name: str = None,
        warehouse_type: str = None,
    ):
        self.warehouse_instance_id = warehouse_instance_id
        self.warehouse_name = warehouse_name
        self.warehouse_type = warehouse_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.warehouse_instance_id is not None:
            result['WarehouseInstanceId'] = self.warehouse_instance_id

        if self.warehouse_name is not None:
            result['WarehouseName'] = self.warehouse_name

        if self.warehouse_type is not None:
            result['WarehouseType'] = self.warehouse_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('WarehouseInstanceId') is not None:
            self.warehouse_instance_id = m.get('WarehouseInstanceId')

        if m.get('WarehouseName') is not None:
            self.warehouse_name = m.get('WarehouseName')

        if m.get('WarehouseType') is not None:
            self.warehouse_type = m.get('WarehouseType')

        return self

