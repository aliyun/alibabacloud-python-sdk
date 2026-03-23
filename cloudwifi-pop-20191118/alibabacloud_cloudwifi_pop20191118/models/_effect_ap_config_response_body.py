# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class EffectApConfigResponseBody(DaraModel):
    def __init__(
        self,
        data: str = None,
        error_code: int = None,
        error_message: str = None,
        is_success: bool = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_message = error_message
        self.is_success = is_success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.is_success is not None:
            result['IsSuccess'] = self.is_success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')

        return self

