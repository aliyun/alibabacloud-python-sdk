# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateSolutionResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        solution_id: int = None,
    ):
        self.request_id = request_id
        self.solution_id = solution_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.solution_id is not None:
            result['SolutionId'] = self.solution_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SolutionId') is not None:
            self.solution_id = m.get('SolutionId')

        return self

