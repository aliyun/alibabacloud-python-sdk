# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetBaselineRequest(DaraModel):
    def __init__(
        self,
        baseline_id: int = None,
        project_id: int = None,
    ):
        # The baseline ID. You can call the [ListBaselines](https://help.aliyun.com/document_detail/2261507.html) operation to query the ID.
        # 
        # This parameter is required.
        self.baseline_id = baseline_id
        # The ID of the workspace to which the baseline belongs. You can call the [ListBaselines](https://help.aliyun.com/document_detail/2261507.html) operation to query the ID.
        # 
        # This parameter is required.
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.baseline_id is not None:
            result['BaselineId'] = self.baseline_id

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaselineId') is not None:
            self.baseline_id = m.get('BaselineId')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        return self

