# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_aidge20260428 import realtime_speech_translation_models as main_models
from darabonba.model import DaraModel

class RealtimeError(DaraModel):
    def __init__(
        self,
        type: str = None,
        event_id: str = None,
        session_id: str = None,
        error: main_models.RealtimeErrorError = None,
    ):
        self.type = type
        self.event_id = event_id
        self.session_id = session_id
        self.error = error

    def validate(self):
        if self.error:
            self.error.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.type is not None:
            result['type'] = self.type

        if self.event_id is not None:
            result['event_id'] = self.event_id

        if self.session_id is not None:
            result['session_id'] = self.session_id

        if self.error is not None:
            result['error'] = self.error.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('event_id') is not None:
            self.event_id = m.get('event_id')

        if m.get('session_id') is not None:
            self.session_id = m.get('session_id')

        if m.get('error') is not None:
            temp_model = main_models.RealtimeErrorError()
            self.error = temp_model.from_map(m.get('error'))

        return self

class RealtimeErrorError(DaraModel):
    def __init__(
        self,
        type: str = None,
        code: str = None,
        message: str = None,
        param: str = None,
        fatal: bool = None,
        retryable: bool = None,
        caused_by: str = None,
    ):
        self.type = type
        self.code = code
        self.message = message
        self.param = param
        self.fatal = fatal
        self.retryable = retryable
        self.caused_by = caused_by

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.type is not None:
            result['type'] = self.type

        if self.code is not None:
            result['code'] = self.code

        if self.message is not None:
            result['message'] = self.message

        if self.param is not None:
            result['param'] = self.param

        if self.fatal is not None:
            result['fatal'] = self.fatal

        if self.retryable is not None:
            result['retryable'] = self.retryable

        if self.caused_by is not None:
            result['caused_by'] = self.caused_by

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('param') is not None:
            self.param = m.get('param')

        if m.get('fatal') is not None:
            self.fatal = m.get('fatal')

        if m.get('retryable') is not None:
            self.retryable = m.get('retryable')

        if m.get('caused_by') is not None:
            self.caused_by = m.get('caused_by')

        return self

