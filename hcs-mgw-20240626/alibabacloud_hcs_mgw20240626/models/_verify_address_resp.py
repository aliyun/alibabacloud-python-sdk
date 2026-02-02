# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class VerifyAddressResp(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        status: str = None,
        verify_time: str = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.status = status
        self.verify_time = verify_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.status is not None:
            result['Status'] = self.status

        if self.verify_time is not None:
            result['VerifyTime'] = self.verify_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('VerifyTime') is not None:
            self.verify_time = m.get('VerifyTime')

        return self

