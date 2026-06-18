# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GenerateTraceDiagnoseResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        tip: str = None,
        url: str = None,
    ):
        # The request ID.
        self.request_id = request_id
        # A diagnostic message.
        self.tip = tip
        # The generated diagnostic link.
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.tip is not None:
            result['Tip'] = self.tip

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Tip') is not None:
            self.tip = m.get('Tip')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

