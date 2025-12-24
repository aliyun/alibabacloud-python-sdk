# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Any

from darabonba.model import DaraModel

class CreateFaultInjectionRequest(DaraModel):
    def __init__(
        self,
        fault_args: Any = None,
        fault_type: str = None,
    ):
        self.fault_args = fault_args
        self.fault_type = fault_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.fault_args is not None:
            result['FaultArgs'] = self.fault_args

        if self.fault_type is not None:
            result['FaultType'] = self.fault_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FaultArgs') is not None:
            self.fault_args = m.get('FaultArgs')

        if m.get('FaultType') is not None:
            self.fault_type = m.get('FaultType')

        return self

