# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetQuotaOutput(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        instance_limit: int = None,
        instance_used: int = None,
    ):
        self.request_id = request_id
        self.instance_limit = instance_limit
        self.instance_used = instance_used

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.instance_limit is not None:
            result['instanceLimit'] = self.instance_limit

        if self.instance_used is not None:
            result['instanceUsed'] = self.instance_used

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('instanceLimit') is not None:
            self.instance_limit = m.get('instanceLimit')

        if m.get('instanceUsed') is not None:
            self.instance_used = m.get('instanceUsed')

        return self

