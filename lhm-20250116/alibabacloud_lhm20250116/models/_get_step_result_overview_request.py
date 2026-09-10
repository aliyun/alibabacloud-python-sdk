# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetStepResultOverviewRequest(DaraModel):
    def __init__(
        self,
        result_id: str = None,
    ):
        # The unique ID of the validation result.
        # 
        # This parameter is required.
        self.result_id = result_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.result_id is not None:
            result['resultId'] = self.result_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('resultId') is not None:
            self.result_id = m.get('resultId')

        return self

