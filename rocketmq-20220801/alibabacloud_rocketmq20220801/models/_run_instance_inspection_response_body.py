# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RunInstanceInspectionResponseBody(DaraModel):
    def __init__(
        self,
        run_id: str = None,
    ):
        self.run_id = run_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.run_id is not None:
            result['runId'] = self.run_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('runId') is not None:
            self.run_id = m.get('runId')

        return self

