# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DashscopeAsyncTaskFinishEventResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        retry_able: bool = None,
        success: bool = None,
    ):
        self.code = code
        self.message = message
        self.retry_able = retry_able
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.message is not None:
            result['message'] = self.message

        if self.retry_able is not None:
            result['retryAble'] = self.retry_able

        if self.success is not None:
            result['success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('retryAble') is not None:
            self.retry_able = m.get('retryAble')

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

