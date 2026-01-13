# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class DebugResourceRuleResponseBody(DaraModel):
    def __init__(
        self,
        current_values: Dict[str, Any] = None,
        output_values: Dict[str, Any] = None,
        request_id: str = None,
    ):
        self.current_values = current_values
        self.output_values = output_values
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_values is not None:
            result['CurrentValues'] = self.current_values

        if self.output_values is not None:
            result['OutputValues'] = self.output_values

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentValues') is not None:
            self.current_values = m.get('CurrentValues')

        if m.get('OutputValues') is not None:
            self.output_values = m.get('OutputValues')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

