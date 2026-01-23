# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateArtifactBuildRuleShrinkRequest(DaraModel):
    def __init__(
        self,
        artifact_type: str = None,
        instance_id: str = None,
        parameters_shrink: str = None,
        scope_id: str = None,
        scope_type: str = None,
    ):
        # The type of the artifact.
        # 
        # *   `ACCELERATED_IMAGE`: accelerated images.
        # 
        # This parameter is required.
        self.artifact_type = artifact_type
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # Additional parameters.
        self.parameters_shrink = parameters_shrink
        # The ID of the effective range of the rule.
        # 
        # *   Set the value to the ID of the image repository.
        # 
        # This parameter is required.
        self.scope_id = scope_id
        # The effective range of the rule. Valid values:
        # 
        # *   `REPOSITORY`
        # 
        # This parameter is required.
        self.scope_type = scope_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.artifact_type is not None:
            result['ArtifactType'] = self.artifact_type

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.parameters_shrink is not None:
            result['Parameters'] = self.parameters_shrink

        if self.scope_id is not None:
            result['ScopeId'] = self.scope_id

        if self.scope_type is not None:
            result['ScopeType'] = self.scope_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArtifactType') is not None:
            self.artifact_type = m.get('ArtifactType')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Parameters') is not None:
            self.parameters_shrink = m.get('Parameters')

        if m.get('ScopeId') is not None:
            self.scope_id = m.get('ScopeId')

        if m.get('ScopeType') is not None:
            self.scope_type = m.get('ScopeType')

        return self

