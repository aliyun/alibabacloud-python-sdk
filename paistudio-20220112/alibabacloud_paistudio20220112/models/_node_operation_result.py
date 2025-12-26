# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class NodeOperationResult(DaraModel):
    def __init__(
        self,
        message: str = None,
        node_name: str = None,
        status: str = None,
    ):
        self.message = message
        self.node_name = node_name
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.message is not None:
            result['Message'] = self.message

        if self.node_name is not None:
            result['NodeName'] = self.node_name

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

