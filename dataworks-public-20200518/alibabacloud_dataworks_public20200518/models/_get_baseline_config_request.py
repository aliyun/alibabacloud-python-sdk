# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetBaselineConfigRequest(DaraModel):
    def __init__(
        self,
        baseline_id: int = None,
    ):
        # The baseline ID. You can call the [GetNode](https://help.aliyun.com/document_detail/173977.html) operation to query the baseline ID.
        # 
        # This parameter is required.
        self.baseline_id = baseline_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.baseline_id is not None:
            result['BaselineId'] = self.baseline_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaselineId') is not None:
            self.baseline_id = m.get('BaselineId')

        return self

