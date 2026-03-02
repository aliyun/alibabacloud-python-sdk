# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetAccountMFAInfoResponseBody(DaraModel):
    def __init__(
        self,
        is_mfaenable: bool = None,
        request_id: str = None,
    ):
        self.is_mfaenable = is_mfaenable
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.is_mfaenable is not None:
            result['IsMFAEnable'] = self.is_mfaenable

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsMFAEnable') is not None:
            self.is_mfaenable = m.get('IsMFAEnable')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

