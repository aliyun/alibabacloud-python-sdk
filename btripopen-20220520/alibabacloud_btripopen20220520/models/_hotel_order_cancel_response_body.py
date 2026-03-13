# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_btripopen20220520 import models as main_models
from darabonba.model import DaraModel

class HotelOrderCancelResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        module: main_models.HotelOrderCancelResponseBodyModule = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.message = message
        # module。
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
            temp_model = main_models.HotelOrderCancelResponseBodyModule()
            self.module = temp_model.from_map(m.get('module'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')

        return self

class HotelOrderCancelResponseBodyModule(DaraModel):
    def __init__(
        self,
        cancel_success: bool = None,
        code: str = None,
        desc: str = None,
        forfeit_fee: int = None,
    ):
        self.cancel_success = cancel_success
        self.code = code
        self.desc = desc
        self.forfeit_fee = forfeit_fee

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cancel_success is not None:
            result['cancel_success'] = self.cancel_success

        if self.code is not None:
            result['code'] = self.code

        if self.desc is not None:
            result['desc'] = self.desc

        if self.forfeit_fee is not None:
            result['forfeit_fee'] = self.forfeit_fee

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cancel_success') is not None:
            self.cancel_success = m.get('cancel_success')

        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('desc') is not None:
            self.desc = m.get('desc')

        if m.get('forfeit_fee') is not None:
            self.forfeit_fee = m.get('forfeit_fee')

        return self

