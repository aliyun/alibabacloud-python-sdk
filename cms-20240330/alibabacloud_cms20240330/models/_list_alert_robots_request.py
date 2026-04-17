# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListAlertRobotsRequest(DaraModel):
    def __init__(
        self,
        name: str = None,
        page_number: int = None,
        page_size: int = None,
        robot_ids: List[str] = None,
        types: List[str] = None,
        workspace: str = None,
    ):
        self.name = name
        self.page_number = page_number
        self.page_size = page_size
        self.robot_ids = robot_ids
        self.types = types
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['name'] = self.name

        if self.page_number is not None:
            result['pageNumber'] = self.page_number

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.robot_ids is not None:
            result['robotIds'] = self.robot_ids

        if self.types is not None:
            result['types'] = self.types

        if self.workspace is not None:
            result['workspace'] = self.workspace

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('robotIds') is not None:
            self.robot_ids = m.get('robotIds')

        if m.get('types') is not None:
            self.types = m.get('types')

        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')

        return self

