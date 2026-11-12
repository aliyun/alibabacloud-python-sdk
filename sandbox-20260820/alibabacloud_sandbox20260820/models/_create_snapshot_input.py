# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sandbox20260820 import models as main_models
from darabonba.model import DaraModel

class CreateSnapshotInput(DaraModel):
    def __init__(
        self,
        name: str = None,
        resource_tags: List[main_models.CreateSnapshotInputResourceTags] = None,
        sandbox_id: str = None,
        team_id: str = None,
    ):
        # The snapshot name.
        self.name = name
        # The resource tags.
        self.resource_tags = resource_tags
        # The source sandbox ID.
        # 
        # This parameter is required.
        self.sandbox_id = sandbox_id
        # The team ID.
        # 
        # This parameter is required.
        self.team_id = team_id

    def validate(self):
        if self.resource_tags:
            for v1 in self.resource_tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['name'] = self.name

        if self.resource_tags is not None:
            result['resourceTags'] = []
            for k1 in self.resource_tags:
                result['resourceTags'].append(k1.to_map() if k1 else None)

        if self.sandbox_id is not None:
            result['sandboxID'] = self.sandbox_id

        if self.team_id is not None:
            result['teamID'] = self.team_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('resourceTags') is not None:
            self.resource_tags = []
            for k1 in m.get('resourceTags'):
                temp_model = main_models.CreateSnapshotInputResourceTags()
                self.resource_tags.append(temp_model.from_map(k1))

        if m.get('sandboxID') is not None:
            self.sandbox_id = m.get('sandboxID')

        if m.get('teamID') is not None:
            self.team_id = m.get('teamID')

        return self

class CreateSnapshotInputResourceTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['key'] = self.key

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

