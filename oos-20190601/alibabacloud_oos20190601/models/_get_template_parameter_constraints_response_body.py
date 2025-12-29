# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class GetTemplateParameterConstraintsResponseBody(DaraModel):
    def __init__(
        self,
        parameter_constraints: Dict[str, Any] = None,
        request_id: str = None,
    ):
        # The constraints of the parameters.
        self.parameter_constraints = parameter_constraints
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.parameter_constraints is not None:
            result['ParameterConstraints'] = self.parameter_constraints

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ParameterConstraints') is not None:
            self.parameter_constraints = m.get('ParameterConstraints')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

