# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PermissionAssistantApi(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        id: int = None,
        name: str = None,
        resource_type: str = None,
        update_time: str = None,
    ):
        self.create_time = create_time
        self.id = id
        self.name = name
        self.resource_type = resource_type
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.id is not None:
            result['id'] = self.id

        if self.name is not None:
            result['name'] = self.name

        if self.resource_type is not None:
            result['resourceType'] = self.resource_type

        if self.update_time is not None:
            result['updateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')

        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')

        return self

