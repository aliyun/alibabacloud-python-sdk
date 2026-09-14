# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateCrossProjectPipelineRunShrinkRequest(DaraModel):
    def __init__(
        self,
        deployment_environment_id: int = None,
        description: str = None,
        object_ids_shrink: str = None,
        project_id: int = None,
        type: str = None,
    ):
        # The cross-workspace deployment environment ID.
        # 
        # This parameter is required.
        self.deployment_environment_id = deployment_environment_id
        # The deployment description.
        self.description = description
        # The list of top-level object IDs from the source project to deploy. The list must contain exactly one object. Child objects of composite objects such as workflows are automatically included by the system.
        # 
        # This parameter is required.
        self.object_ids_shrink = object_ids_shrink
        # The workspace ID.
        # 
        # This parameter is required.
        self.project_id = project_id
        # The deployment type. Valid values:
        # 
        # - Offline: Offline deployment.
        # - Online: Online deployment.
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.deployment_environment_id is not None:
            result['DeploymentEnvironmentId'] = self.deployment_environment_id

        if self.description is not None:
            result['Description'] = self.description

        if self.object_ids_shrink is not None:
            result['ObjectIds'] = self.object_ids_shrink

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeploymentEnvironmentId') is not None:
            self.deployment_environment_id = m.get('DeploymentEnvironmentId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ObjectIds') is not None:
            self.object_ids_shrink = m.get('ObjectIds')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

