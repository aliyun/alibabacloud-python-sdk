# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CooperatorSyncPayStatusRequest(DaraModel):
    def __init__(
        self,
        cooperator_order_id: str = None,
        cooperator_pay_no: str = None,
        order_id: str = None,
        pay_status: str = None,
        pay_time: int = None,
    ):
        # This parameter is required.
        self.cooperator_order_id = cooperator_order_id
        # This parameter is required.
        self.cooperator_pay_no = cooperator_pay_no
        # This parameter is required.
        self.order_id = order_id
        # This parameter is required.
        self.pay_status = pay_status
        # This parameter is required.
        self.pay_time = pay_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cooperator_order_id is not None:
            result['cooperator_order_id'] = self.cooperator_order_id

        if self.cooperator_pay_no is not None:
            result['cooperator_pay_no'] = self.cooperator_pay_no

        if self.order_id is not None:
            result['order_id'] = self.order_id

        if self.pay_status is not None:
            result['pay_status'] = self.pay_status

        if self.pay_time is not None:
            result['pay_time'] = self.pay_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cooperator_order_id') is not None:
            self.cooperator_order_id = m.get('cooperator_order_id')

        if m.get('cooperator_pay_no') is not None:
            self.cooperator_pay_no = m.get('cooperator_pay_no')

        if m.get('order_id') is not None:
            self.order_id = m.get('order_id')

        if m.get('pay_status') is not None:
            self.pay_status = m.get('pay_status')

        if m.get('pay_time') is not None:
            self.pay_time = m.get('pay_time')

        return self

