# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_btripopen20220520 import models as main_models
from darabonba.model import DaraModel

class QueryCompenInfosForOpResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        module: List[main_models.QueryCompenInfosForOpResponseBodyModule] = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.message = message
        self.module = module
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

    def validate(self):
        if self.module:
            for v1 in self.module:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.message is not None:
            result['message'] = self.message

        result['module'] = []
        if self.module is not None:
            for k1 in self.module:
                result['module'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        if self.trace_id is not None:
            result['traceId'] = self.trace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('message') is not None:
            self.message = m.get('message')

        self.module = []
        if m.get('module') is not None:
            for k1 in m.get('module'):
                temp_model = main_models.QueryCompenInfosForOpResponseBodyModule()
                self.module.append(temp_model.from_map(k1))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')

        return self

class QueryCompenInfosForOpResponseBodyModule(DaraModel):
    def __init__(
        self,
        amount: int = None,
        category: int = None,
        compen_id: str = None,
        compensation_type: str = None,
        order_id: str = None,
        settle_time: str = None,
        settle_type: int = None,
        ticket_no: str = None,
    ):
        self.amount = amount
        self.category = category
        self.compen_id = compen_id
        self.compensation_type = compensation_type
        self.order_id = order_id
        self.settle_time = settle_time
        self.settle_type = settle_type
        self.ticket_no = ticket_no

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.amount is not None:
            result['amount'] = self.amount

        if self.category is not None:
            result['category'] = self.category

        if self.compen_id is not None:
            result['compen_id'] = self.compen_id

        if self.compensation_type is not None:
            result['compensation_type'] = self.compensation_type

        if self.order_id is not None:
            result['order_id'] = self.order_id

        if self.settle_time is not None:
            result['settle_time'] = self.settle_time

        if self.settle_type is not None:
            result['settle_type'] = self.settle_type

        if self.ticket_no is not None:
            result['ticket_no'] = self.ticket_no

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('amount') is not None:
            self.amount = m.get('amount')

        if m.get('category') is not None:
            self.category = m.get('category')

        if m.get('compen_id') is not None:
            self.compen_id = m.get('compen_id')

        if m.get('compensation_type') is not None:
            self.compensation_type = m.get('compensation_type')

        if m.get('order_id') is not None:
            self.order_id = m.get('order_id')

        if m.get('settle_time') is not None:
            self.settle_time = m.get('settle_time')

        if m.get('settle_type') is not None:
            self.settle_type = m.get('settle_type')

        if m.get('ticket_no') is not None:
            self.ticket_no = m.get('ticket_no')

        return self

