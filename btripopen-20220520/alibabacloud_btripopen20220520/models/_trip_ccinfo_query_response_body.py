# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_btripopen20220520 import models as main_models
from darabonba.model import DaraModel

class TripCCInfoQueryResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        module: List[main_models.TripCCInfoQueryResponseBodyModule] = None,
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
        # traceId
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
                temp_model = main_models.TripCCInfoQueryResponseBodyModule()
                self.module.append(temp_model.from_map(k1))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')

        return self

class TripCCInfoQueryResponseBodyModule(DaraModel):
    def __init__(
        self,
        notifier: str = None,
        notify_start_time: int = None,
    ):
        self.notifier = notifier
        self.notify_start_time = notify_start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.notifier is not None:
            result['notifier'] = self.notifier

        if self.notify_start_time is not None:
            result['notify_start_time'] = self.notify_start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('notifier') is not None:
            self.notifier = m.get('notifier')

        if m.get('notify_start_time') is not None:
            self.notify_start_time = m.get('notify_start_time')

        return self

