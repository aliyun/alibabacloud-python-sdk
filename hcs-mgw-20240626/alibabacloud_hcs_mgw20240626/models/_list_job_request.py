# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListJobRequest(DaraModel):
    def __init__(
        self,
        all: bool = None,
        count: int = None,
        marker: str = None,
        parent_name: str = None,
    ):
        # Specifies whether to return subtasks.\\
        # Valid values: true and false.
        self.all = all
        # Specifies the number of migration tasks to be returned.\\
        # Valid values: 0 - 1000 (excluding 0).\\
        # Default value: 1000.
        self.count = count
        # The marker after which the migration tasks are listed.\\
        # By default, this parameter is left empty.
        self.marker = marker
        # The name of the parent task. If this parameter is specified, all subtasks of the parent task are returned.
        self.parent_name = parent_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.all is not None:
            result['all'] = self.all

        if self.count is not None:
            result['count'] = self.count

        if self.marker is not None:
            result['marker'] = self.marker

        if self.parent_name is not None:
            result['parentName'] = self.parent_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('all') is not None:
            self.all = m.get('all')

        if m.get('count') is not None:
            self.count = m.get('count')

        if m.get('marker') is not None:
            self.marker = m.get('marker')

        if m.get('parentName') is not None:
            self.parent_name = m.get('parentName')

        return self

