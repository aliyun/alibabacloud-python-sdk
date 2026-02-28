# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeAppCallbackSecretKeyResponseBody(DaraModel):
    def __init__(
        self,
        callback_secret_key: str = None,
        request_id: str = None,
    ):
        self.callback_secret_key = callback_secret_key
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.callback_secret_key is not None:
            result['CallbackSecretKey'] = self.callback_secret_key

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallbackSecretKey') is not None:
            self.callback_secret_key = m.get('CallbackSecretKey')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

