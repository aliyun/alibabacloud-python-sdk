# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryOrderPriceRequest(DaraModel):
    def __init__(
        self,
        code: str = None,
        instance_id: str = None,
        order_type: str = None,
        package: str = None,
        period: int = None,
        period_unit: str = None,
        total_size: int = None,
        user_count: int = None,
    ):
        # This parameter is required.
        self.code = code
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.order_type = order_type
        # This parameter is required.
        self.package = package
        # This parameter is required.
        self.period = period
        # This parameter is required.
        self.period_unit = period_unit
        # This parameter is required.
        self.total_size = total_size
        # This parameter is required.
        self.user_count = user_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.instance_id is not None:
            result['instance_id'] = self.instance_id

        if self.order_type is not None:
            result['order_type'] = self.order_type

        if self.package is not None:
            result['package'] = self.package

        if self.period is not None:
            result['period'] = self.period

        if self.period_unit is not None:
            result['period_unit'] = self.period_unit

        if self.total_size is not None:
            result['total_size'] = self.total_size

        if self.user_count is not None:
            result['user_count'] = self.user_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('instance_id') is not None:
            self.instance_id = m.get('instance_id')

        if m.get('order_type') is not None:
            self.order_type = m.get('order_type')

        if m.get('package') is not None:
            self.package = m.get('package')

        if m.get('period') is not None:
            self.period = m.get('period')

        if m.get('period_unit') is not None:
            self.period_unit = m.get('period_unit')

        if m.get('total_size') is not None:
            self.total_size = m.get('total_size')

        if m.get('user_count') is not None:
            self.user_count = m.get('user_count')

        return self

