# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eds_aic20230930 import models as main_models
from darabonba.model import DaraModel

class CheckResourceStockResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        resource_stock_models: List[main_models.CheckResourceStockResponseBodyResourceStockModels] = None,
    ):
        # Request ID.
        self.request_id = request_id
        # Details of resource inventory.
        self.resource_stock_models = resource_stock_models

    def validate(self):
        if self.resource_stock_models:
            for v1 in self.resource_stock_models:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['ResourceStockModels'] = []
        if self.resource_stock_models is not None:
            for k1 in self.resource_stock_models:
                result['ResourceStockModels'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.resource_stock_models = []
        if m.get('ResourceStockModels') is not None:
            for k1 in m.get('ResourceStockModels'):
                temp_model = main_models.CheckResourceStockResponseBodyResourceStockModels()
                self.resource_stock_models.append(temp_model.from_map(k1))

        return self

class CheckResourceStockResponseBodyResourceStockModels(DaraModel):
    def __init__(
        self,
        region_id: str = None,
        stock_status: str = None,
        zone_id: str = None,
    ):
        # Region ID.
        self.region_id = region_id
        # Inventory status of the instance group.
        self.stock_status = stock_status
        # Zone ID.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.stock_status is not None:
            result['StockStatus'] = self.stock_status

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('StockStatus') is not None:
            self.stock_status = m.get('StockStatus')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

