# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeVulCheckTaskStatusDetailRequest(DaraModel):
    def __init__(
        self,
        task_ids: List[str] = None,
        types: List[str] = None,
        uuid: str = None,
    ):
        # The task IDs.
        self.task_ids = task_ids
        # The types of the vulnerabilities that are detected by the tasks.
        self.types = types
        # The UUID of the server.
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.task_ids is not None:
            result['TaskIds'] = self.task_ids

        if self.types is not None:
            result['Types'] = self.types

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskIds') is not None:
            self.task_ids = m.get('TaskIds')

        if m.get('Types') is not None:
            self.types = m.get('Types')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self

