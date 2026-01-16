# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CheckDisposableResponseBody(DaraModel):
    def __init__(
        self,
        is_disposable: str = None,
        is_format_valid: str = None,
        is_mx_valid: str = None,
        is_ok_to_send: str = None,
        request_id: str = None,
    ):
        self.is_disposable = is_disposable
        self.is_format_valid = is_format_valid
        self.is_mx_valid = is_mx_valid
        self.is_ok_to_send = is_ok_to_send
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.is_disposable is not None:
            result['IsDisposable'] = self.is_disposable

        if self.is_format_valid is not None:
            result['IsFormatValid'] = self.is_format_valid

        if self.is_mx_valid is not None:
            result['IsMxValid'] = self.is_mx_valid

        if self.is_ok_to_send is not None:
            result['IsOkToSend'] = self.is_ok_to_send

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsDisposable') is not None:
            self.is_disposable = m.get('IsDisposable')

        if m.get('IsFormatValid') is not None:
            self.is_format_valid = m.get('IsFormatValid')

        if m.get('IsMxValid') is not None:
            self.is_mx_valid = m.get('IsMxValid')

        if m.get('IsOkToSend') is not None:
            self.is_ok_to_send = m.get('IsOkToSend')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

