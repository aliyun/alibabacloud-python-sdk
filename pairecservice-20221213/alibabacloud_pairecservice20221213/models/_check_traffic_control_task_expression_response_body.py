# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CheckTrafficControlTaskExpressionResponseBody(DaraModel):
    def __init__(
        self,
        is_valie: bool = None,
        reason: str = None,
        request_id: str = None,
    ):
        self.is_valie = is_valie
        self.reason = reason
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.is_valie is not None:
            result['IsValie'] = self.is_valie

        if self.reason is not None:
            result['Reason'] = self.reason

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsValie') is not None:
            self.is_valie = m.get('IsValie')

        if m.get('Reason') is not None:
            self.reason = m.get('Reason')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

