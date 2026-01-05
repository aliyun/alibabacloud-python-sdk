# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class RemoveTaskInstanceDependenciesRequest(DaraModel):
    def __init__(
        self,
        comment: str = None,
        id: int = None,
        upstream_task_instance_ids: List[int] = None,
    ):
        # The remarks.
        self.comment = comment
        # The instance ID.
        # 
        # This parameter is required.
        self.id = id
        # The IDs of ancestor instances of the instance
        self.upstream_task_instance_ids = upstream_task_instance_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.comment is not None:
            result['Comment'] = self.comment

        if self.id is not None:
            result['Id'] = self.id

        if self.upstream_task_instance_ids is not None:
            result['UpstreamTaskInstanceIds'] = self.upstream_task_instance_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('UpstreamTaskInstanceIds') is not None:
            self.upstream_task_instance_ids = m.get('UpstreamTaskInstanceIds')

        return self

