# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListMachineGroupRequest(DaraModel):
    def __init__(
        self,
        group_name: str = None,
        offset: int = None,
        size: int = None,
    ):
        # The name of the machine group. This parameter is used to filter machine groups. Partial match is supported.
        self.group_name = group_name
        # The line from which the query starts. Default value: 0.
        self.offset = offset
        # The number of entries per page. Maximum value: 500.
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group_name is not None:
            result['groupName'] = self.group_name

        if self.offset is not None:
            result['offset'] = self.offset

        if self.size is not None:
            result['size'] = self.size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('groupName') is not None:
            self.group_name = m.get('groupName')

        if m.get('offset') is not None:
            self.offset = m.get('offset')

        if m.get('size') is not None:
            self.size = m.get('size')

        return self

