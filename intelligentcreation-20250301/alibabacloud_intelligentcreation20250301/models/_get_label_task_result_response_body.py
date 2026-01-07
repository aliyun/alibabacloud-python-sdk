# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetLabelTaskResultResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result_data_url: str = None,
        status: str = None,
        tokens: str = None,
    ):
        self.request_id = request_id
        self.result_data_url = result_data_url
        self.status = status
        self.tokens = tokens

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result_data_url is not None:
            result['ResultDataUrl'] = self.result_data_url

        if self.status is not None:
            result['Status'] = self.status

        if self.tokens is not None:
            result['Tokens'] = self.tokens

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResultDataUrl') is not None:
            self.result_data_url = m.get('ResultDataUrl')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Tokens') is not None:
            self.tokens = m.get('Tokens')

        return self

