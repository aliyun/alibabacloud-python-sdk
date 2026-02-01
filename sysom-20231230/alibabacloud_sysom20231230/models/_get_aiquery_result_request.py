# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetAIQueryResultRequest(DaraModel):
    def __init__(
        self,
        analysis_id: str = None,
    ):
        self.analysis_id = analysis_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.analysis_id is not None:
            result['analysisId'] = self.analysis_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('analysisId') is not None:
            self.analysis_id = m.get('analysisId')

        return self

