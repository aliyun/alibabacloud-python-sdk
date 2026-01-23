# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetArtifactBuildRuleRequest(DaraModel):
    def __init__(
        self,
        artifact_type: str = None,
        build_rule_id: str = None,
        instance_id: str = None,
        scope_id: str = None,
        scope_type: str = None,
    ):
        # The type of the artifact.
        # 
        # *   `ACCELERATED_IMAGE`: accelerated images.
        self.artifact_type = artifact_type
        # The ID of the artifact building rule.
        self.build_rule_id = build_rule_id
        # The ID of the Container Registry instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The ID of the effective range of the artifact building rule.
        # 
        # *   Set the value to the ID of the image repository.
        self.scope_id = scope_id
        # The effective range of the artifact building rule. Valid values:
        # 
        # *   `REPOSITORY`: The artifact building rule is effective in the repository level.
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

        if self.build_rule_id is not None:
            result['BuildRuleId'] = self.build_rule_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.scope_id is not None:
            result['ScopeId'] = self.scope_id

        if self.scope_type is not None:
            result['ScopeType'] = self.scope_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArtifactType') is not None:
            self.artifact_type = m.get('ArtifactType')

        if m.get('BuildRuleId') is not None:
            self.build_rule_id = m.get('BuildRuleId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('ScopeId') is not None:
            self.scope_id = m.get('ScopeId')

        if m.get('ScopeType') is not None:
            self.scope_type = m.get('ScopeType')

        return self

