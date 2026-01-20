# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetProjectFeatureEntityResponseBody(DaraModel):
    def __init__(
        self,
        feature_entity_id: str = None,
        join_id: str = None,
        name: str = None,
        project_name: str = None,
        request_id: str = None,
        workspace_id: str = None,
    ):
        self.feature_entity_id = feature_entity_id
        self.join_id = join_id
        self.name = name
        self.project_name = project_name
        self.request_id = request_id
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.feature_entity_id is not None:
            result['FeatureEntityId'] = self.feature_entity_id

        if self.join_id is not None:
            result['JoinId'] = self.join_id

        if self.name is not None:
            result['Name'] = self.name

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FeatureEntityId') is not None:
            self.feature_entity_id = m.get('FeatureEntityId')

        if m.get('JoinId') is not None:
            self.join_id = m.get('JoinId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

