# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_btripopen20220520 import models as main_models
from darabonba.model import DaraModel

class FlightCancelOrderResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        module: main_models.FlightCancelOrderResponseBodyModule = None,
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
            self.module.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.message is not None:
            result['message'] = self.message

        if self.module is not None:
            result['module'] = self.module.to_map()

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

        if m.get('module') is not None:
            temp_model = main_models.FlightCancelOrderResponseBodyModule()
            self.module = temp_model.from_map(m.get('module'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')

        return self

class FlightCancelOrderResponseBodyModule(DaraModel):
    def __init__(
        self,
        cancel_time: str = None,
        fail_code: str = None,
        fail_reason: str = None,
        order_status: str = None,
    ):
        self.cancel_time = cancel_time
        self.fail_code = fail_code
        self.fail_reason = fail_reason
        self.order_status = order_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cancel_time is not None:
            result['cancel_time'] = self.cancel_time

        if self.fail_code is not None:
            result['fail_code'] = self.fail_code

        if self.fail_reason is not None:
            result['fail_reason'] = self.fail_reason

        if self.order_status is not None:
            result['order_status'] = self.order_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cancel_time') is not None:
            self.cancel_time = m.get('cancel_time')

        if m.get('fail_code') is not None:
            self.fail_code = m.get('fail_code')

        if m.get('fail_reason') is not None:
            self.fail_reason = m.get('fail_reason')

        if m.get('order_status') is not None:
            self.order_status = m.get('order_status')

        return self

