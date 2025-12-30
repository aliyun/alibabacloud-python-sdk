# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdatePipelineRequest(DaraModel):
    def __init__(
        self,
        name: str = None,
        pipeline_id: str = None,
        priority: int = None,
        status: str = None,
    ):
        # The name of the MPS queue.
        self.name = name
        # The ID of the MPS queue.
        # 
        # This parameter is required.
        self.pipeline_id = pipeline_id
        # The priority of the MPS queue. Valid values: 1 to 10.
        self.priority = priority
        # The state of the MPS queue.
        # 
        # Valid values:
        # 
        # *   Active
        # *   Paused
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.pipeline_id is not None:
            result['PipelineId'] = self.pipeline_id

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PipelineId') is not None:
            self.pipeline_id = m.get('PipelineId')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

