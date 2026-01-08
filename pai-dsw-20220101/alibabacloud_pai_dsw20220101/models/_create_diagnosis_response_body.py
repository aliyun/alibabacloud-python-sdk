# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateDiagnosisResponseBody(DaraModel):
    def __init__(
        self,
        reason_code: str = None,
        reason_message: str = None,
        solution_message: str = None,
    ):
        self.reason_code = reason_code
        self.reason_message = reason_message
        self.solution_message = solution_message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.reason_code is not None:
            result['ReasonCode'] = self.reason_code

        if self.reason_message is not None:
            result['ReasonMessage'] = self.reason_message

        if self.solution_message is not None:
            result['SolutionMessage'] = self.solution_message

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ReasonCode') is not None:
            self.reason_code = m.get('ReasonCode')

        if m.get('ReasonMessage') is not None:
            self.reason_message = m.get('ReasonMessage')

        if m.get('SolutionMessage') is not None:
            self.solution_message = m.get('SolutionMessage')

        return self

