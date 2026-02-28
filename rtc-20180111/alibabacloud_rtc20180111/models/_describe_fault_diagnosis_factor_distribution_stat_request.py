# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeFaultDiagnosisFactorDistributionStatRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        end_ts: int = None,
        start_ts: int = None,
    ):
        # APP ID。
        # 
        # This parameter is required.
        self.app_id = app_id
        # This parameter is required.
        self.end_ts = end_ts
        # This parameter is required.
        self.start_ts = start_ts

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.end_ts is not None:
            result['EndTs'] = self.end_ts

        if self.start_ts is not None:
            result['StartTs'] = self.start_ts

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('EndTs') is not None:
            self.end_ts = m.get('EndTs')

        if m.get('StartTs') is not None:
            self.start_ts = m.get('StartTs')

        return self

