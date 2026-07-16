# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class RunNodeOperationRequest(DaraModel):
    def __init__(
        self,
        operation_action: str = None,
        operation_args: List[str] = None,
    ):
        # This parameter is required.
        self.operation_action = operation_action
        self.operation_args = operation_args

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.operation_action is not None:
            result['operationAction'] = self.operation_action

        if self.operation_args is not None:
            result['operationArgs'] = self.operation_args

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('operationAction') is not None:
            self.operation_action = m.get('operationAction')

        if m.get('operationArgs') is not None:
            self.operation_args = m.get('operationArgs')

        return self

