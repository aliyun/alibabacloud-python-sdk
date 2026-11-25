# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetAIAppJobRequest(DaraModel):
    def __init__(
        self,
        job_id: str = None,
        only_outputs: bool = None,
    ):
        # The task ID.
        # 
        # This parameter is required.
        self.job_id = job_id
        # Specifies whether to return only the task results. If you set this parameter to true, the response does not include the results of each node.
        self.only_outputs = only_outputs

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.only_outputs is not None:
            result['OnlyOutputs'] = self.only_outputs

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('OnlyOutputs') is not None:
            self.only_outputs = m.get('OnlyOutputs')

        return self

