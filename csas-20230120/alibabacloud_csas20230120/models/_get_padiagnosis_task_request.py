# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetPADiagnosisTaskRequest(DaraModel):
    def __init__(
        self,
        diagnose_id: str = None,
    ):
        # This parameter is required.
        self.diagnose_id = diagnose_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.diagnose_id is not None:
            result['DiagnoseId'] = self.diagnose_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DiagnoseId') is not None:
            self.diagnose_id = m.get('DiagnoseId')

        return self

