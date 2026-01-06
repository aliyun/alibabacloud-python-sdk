# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeTaskRequest(DaraModel):
    def __init__(
        self,
        resource_group_id: str = None,
        task_id: str = None,
        token: str = None,
    ):
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The ID of the job.
        self.task_id = task_id
        # The access token.
        self.token = token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.token is not None:
            result['Token'] = self.token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('Token') is not None:
            self.token = m.get('Token')

        return self

