# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDiagnosticResultRequest(DaraModel):
    def __init__(
        self,
        diagnostic_id: str = None,
    ):
        # The diagnostic task ID.
        self.diagnostic_id = diagnostic_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.diagnostic_id is not None:
            result['DiagnosticId'] = self.diagnostic_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DiagnosticId') is not None:
            self.diagnostic_id = m.get('DiagnosticId')

        return self

