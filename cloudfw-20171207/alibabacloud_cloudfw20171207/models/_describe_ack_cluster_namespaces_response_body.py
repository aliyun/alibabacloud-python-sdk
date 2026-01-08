# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeAckClusterNamespacesResponseBody(DaraModel):
    def __init__(
        self,
        ack_namespaces: List[str] = None,
        request_id: str = None,
    ):
        self.ack_namespaces = ack_namespaces
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ack_namespaces is not None:
            result['AckNamespaces'] = self.ack_namespaces

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AckNamespaces') is not None:
            self.ack_namespaces = m.get('AckNamespaces')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

