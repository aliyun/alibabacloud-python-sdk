# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_paistudio20220112 import models as main_models
from darabonba.model import DaraModel

class SpotStockItem(DaraModel):
    def __init__(
        self,
        instance_type: str = None,
        internal_info: List[main_models.SpotStockInternalInfo] = None,
        stock_status: str = None,
    ):
        # The instance type.
        self.instance_type = instance_type
        # Internal information about the stock of the spot instance type.
        self.internal_info = internal_info
        # The stock status of the instance type. Valid values are `Available` and `SoldOut`.
        self.stock_status = stock_status

    def validate(self):
        if self.internal_info:
            for v1 in self.internal_info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_type is not None:
            result['instanceType'] = self.instance_type

        result['internalInfo'] = []
        if self.internal_info is not None:
            for k1 in self.internal_info:
                result['internalInfo'].append(k1.to_map() if k1 else None)

        if self.stock_status is not None:
            result['stockStatus'] = self.stock_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('instanceType') is not None:
            self.instance_type = m.get('instanceType')

        self.internal_info = []
        if m.get('internalInfo') is not None:
            for k1 in m.get('internalInfo'):
                temp_model = main_models.SpotStockInternalInfo()
                self.internal_info.append(temp_model.from_map(k1))

        if m.get('stockStatus') is not None:
            self.stock_status = m.get('stockStatus')

        return self

