# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QuotasValue(DaraModel):
    def __init__(
        self,
        quota: str = None,
        operation_code: str = None,
        adjustable: bool = None,
        unit: str = None,
    ):
        # The value of the quota. If the quota limit is reached, submit an application in the [Quota Center console](https://quotas.console.aliyun.com/products/csk/quotas) to increase the quota.
        self.quota = quota
        # The quota code.
        self.operation_code = operation_code
        # Indicates whether the quota is adjustable.
        self.adjustable = adjustable
        # The unit.
        self.unit = unit

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.quota is not None:
            result['quota'] = self.quota

        if self.operation_code is not None:
            result['operation_code'] = self.operation_code

        if self.adjustable is not None:
            result['adjustable'] = self.adjustable

        if self.unit is not None:
            result['unit'] = self.unit

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('quota') is not None:
            self.quota = m.get('quota')

        if m.get('operation_code') is not None:
            self.operation_code = m.get('operation_code')

        if m.get('adjustable') is not None:
            self.adjustable = m.get('adjustable')

        if m.get('unit') is not None:
            self.unit = m.get('unit')

        return self

