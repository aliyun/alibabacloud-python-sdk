# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class HighCodeDeployResponseBody(DaraModel):
    def __init__(
        self,
        data: str = None,
        error_code: str = None,
        error_msg: str = None,
        success: bool = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_msg = error_msg
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['data'] = self.data

        if self.error_code is not None:
            result['errorCode'] = self.error_code

        if self.error_msg is not None:
            result['errorMsg'] = self.error_msg

        if self.success is not None:
            result['success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            self.data = m.get('data')

        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')

        if m.get('errorMsg') is not None:
            self.error_msg = m.get('errorMsg')

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

