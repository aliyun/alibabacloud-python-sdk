# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ModelGroupDTO(DaraModel):
    def __init__(
        self,
        gmt_create: str = None,
        gmt_modified: str = None,
        group_id: str = None,
        model_count: int = None,
        model_list: List[int] = None,
        name: str = None,
        type: str = None,
    ):
        # The time when the group was created. Format: yyyy-MM-dd HH:mm:ss.
        self.gmt_create = gmt_create
        # The time when the group was updated. Format: yyyy-MM-dd HH:mm:ss.
        self.gmt_modified = gmt_modified
        # The unique identifier of the group. It starts with the mg_ prefix and remains unchanged after creation.
        self.group_id = group_id
        # The number of models currently included in the group.
        self.model_count = model_count
        # The array of all member model IDs.
        self.model_list = model_list
        # The name of the group. If a system group is unnamed, the default platform name is returned.
        self.name = name
        # The type of the group. Valid values:
        # - system: The group is automatically created by the system and cannot be edited or deleted.
        # - manual: The group is manually created.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified

        if self.group_id is not None:
            result['groupId'] = self.group_id

        if self.model_count is not None:
            result['modelCount'] = self.model_count

        if self.model_list is not None:
            result['modelList'] = self.model_list

        if self.name is not None:
            result['name'] = self.name

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')

        if m.get('groupId') is not None:
            self.group_id = m.get('groupId')

        if m.get('modelCount') is not None:
            self.model_count = m.get('modelCount')

        if m.get('modelList') is not None:
            self.model_list = m.get('modelList')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

