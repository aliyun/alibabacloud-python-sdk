# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_aisearchengine20260417 import models as main_models
from darabonba.model import DaraModel

class QaChatResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.QaChatResponseBodyData = None,
        event: str = None,
        id: str = None,
    ):
        self.data = data
        self.event = event
        self.id = id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.event is not None:
            result['event'] = self.event

        if self.id is not None:
            result['id'] = self.id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = main_models.QaChatResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('event') is not None:
            self.event = m.get('event')

        if m.get('id') is not None:
            self.id = m.get('id')

        return self

class QaChatResponseBodyData(DaraModel):
    def __init__(
        self,
        data: str = None,
        delta: str = None,
        error_code: str = None,
        error_text: str = None,
        finish_reason: str = None,
        id: str = None,
        request_id: str = None,
        retryable: bool = None,
        type: str = None,
    ):
        self.data = data
        self.delta = delta
        self.error_code = error_code
        self.error_text = error_text
        self.finish_reason = finish_reason
        self.id = id
        self.request_id = request_id
        self.retryable = retryable
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['data'] = self.data

        if self.delta is not None:
            result['delta'] = self.delta

        if self.error_code is not None:
            result['errorCode'] = self.error_code

        if self.error_text is not None:
            result['errorText'] = self.error_text

        if self.finish_reason is not None:
            result['finishReason'] = self.finish_reason

        if self.id is not None:
            result['id'] = self.id

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.retryable is not None:
            result['retryable'] = self.retryable

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            self.data = m.get('data')

        if m.get('delta') is not None:
            self.delta = m.get('delta')

        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')

        if m.get('errorText') is not None:
            self.error_text = m.get('errorText')

        if m.get('finishReason') is not None:
            self.finish_reason = m.get('finishReason')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('retryable') is not None:
            self.retryable = m.get('retryable')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

