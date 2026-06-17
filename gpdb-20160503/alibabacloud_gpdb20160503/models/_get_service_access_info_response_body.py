# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetServiceAccessInfoResponseBody(DaraModel):
    def __init__(
        self,
        callback_url: str = None,
        request_id: str = None,
        verify_code: str = None,
    ):
        self.callback_url = callback_url
        self.request_id = request_id
        self.verify_code = verify_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.callback_url is not None:
            result['CallbackUrl'] = self.callback_url

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.verify_code is not None:
            result['VerifyCode'] = self.verify_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallbackUrl') is not None:
            self.callback_url = m.get('CallbackUrl')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('VerifyCode') is not None:
            self.verify_code = m.get('VerifyCode')

        return self

