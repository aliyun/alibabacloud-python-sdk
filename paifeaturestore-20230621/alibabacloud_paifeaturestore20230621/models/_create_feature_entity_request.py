# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateFeatureEntityRequest(DaraModel):
    def __init__(
        self,
        join_id: str = None,
        name: str = None,
        parent_feature_entity_id: str = None,
        project_id: str = None,
    ):
        # This parameter is required.
        self.join_id = join_id
        # This parameter is required.
        self.name = name
        self.parent_feature_entity_id = parent_feature_entity_id
        # This parameter is required.
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.join_id is not None:
            result['JoinId'] = self.join_id

        if self.name is not None:
            result['Name'] = self.name

        if self.parent_feature_entity_id is not None:
            result['ParentFeatureEntityId'] = self.parent_feature_entity_id

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JoinId') is not None:
            self.join_id = m.get('JoinId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ParentFeatureEntityId') is not None:
            self.parent_feature_entity_id = m.get('ParentFeatureEntityId')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        return self

