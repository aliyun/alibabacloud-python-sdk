# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class BillOrderEntryDTO(DaraModel):
    def __init__(
        self,
        amount: float = None,
        balance_after: float = None,
        balance_before: float = None,
        balance_type: str = None,
        create_time: str = None,
        direction: str = None,
        model_code: str = None,
        operator_id: str = None,
        order_id: str = None,
        order_type: str = None,
        remark: str = None,
        source: str = None,
        total_after: float = None,
        total_before: float = None,
    ):
        self.amount = amount
        self.balance_after = balance_after
        self.balance_before = balance_before
        self.balance_type = balance_type
        self.create_time = create_time
        self.direction = direction
        self.model_code = model_code
        self.operator_id = operator_id
        self.order_id = order_id
        self.order_type = order_type
        self.remark = remark
        self.source = source
        self.total_after = total_after
        self.total_before = total_before

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.amount is not None:
            result['amount'] = self.amount

        if self.balance_after is not None:
            result['balanceAfter'] = self.balance_after

        if self.balance_before is not None:
            result['balanceBefore'] = self.balance_before

        if self.balance_type is not None:
            result['balanceType'] = self.balance_type

        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.direction is not None:
            result['direction'] = self.direction

        if self.model_code is not None:
            result['modelCode'] = self.model_code

        if self.operator_id is not None:
            result['operatorId'] = self.operator_id

        if self.order_id is not None:
            result['orderId'] = self.order_id

        if self.order_type is not None:
            result['orderType'] = self.order_type

        if self.remark is not None:
            result['remark'] = self.remark

        if self.source is not None:
            result['source'] = self.source

        if self.total_after is not None:
            result['totalAfter'] = self.total_after

        if self.total_before is not None:
            result['totalBefore'] = self.total_before

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('amount') is not None:
            self.amount = m.get('amount')

        if m.get('balanceAfter') is not None:
            self.balance_after = m.get('balanceAfter')

        if m.get('balanceBefore') is not None:
            self.balance_before = m.get('balanceBefore')

        if m.get('balanceType') is not None:
            self.balance_type = m.get('balanceType')

        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('direction') is not None:
            self.direction = m.get('direction')

        if m.get('modelCode') is not None:
            self.model_code = m.get('modelCode')

        if m.get('operatorId') is not None:
            self.operator_id = m.get('operatorId')

        if m.get('orderId') is not None:
            self.order_id = m.get('orderId')

        if m.get('orderType') is not None:
            self.order_type = m.get('orderType')

        if m.get('remark') is not None:
            self.remark = m.get('remark')

        if m.get('source') is not None:
            self.source = m.get('source')

        if m.get('totalAfter') is not None:
            self.total_after = m.get('totalAfter')

        if m.get('totalBefore') is not None:
            self.total_before = m.get('totalBefore')

        return self

