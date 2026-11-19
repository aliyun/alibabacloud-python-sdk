# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetKeywordImportResultRequest(DaraModel):
    def __init__(
        self,
        region_id: str = None,
        task_id: str = None,
    ):
        # The region ID.
        self.region_id = region_id
        # The task ID. Although this parameter is marked as required:false in the specification, it is actually required. If you do not provide this parameter, the service returns a 400 error. You can obtain the task ID from the TaskId field in the response of the AddKeywordsToLib operation when you import keywords in batches from a file.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

