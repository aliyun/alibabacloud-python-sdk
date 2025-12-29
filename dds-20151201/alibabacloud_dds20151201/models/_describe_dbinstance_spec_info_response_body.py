# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDBInstanceSpecInfoResponseBody(DaraModel):
    def __init__(
        self,
        cpu: str = None,
        description: str = None,
        memory: str = None,
        request_id: str = None,
    ):
        self.cpu = cpu
        self.description = description
        self.memory = memory
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cpu is not None:
            result['CPU'] = self.cpu

        if self.description is not None:
            result['Description'] = self.description

        if self.memory is not None:
            result['Memory'] = self.memory

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CPU') is not None:
            self.cpu = m.get('CPU')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Memory') is not None:
            self.memory = m.get('Memory')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

