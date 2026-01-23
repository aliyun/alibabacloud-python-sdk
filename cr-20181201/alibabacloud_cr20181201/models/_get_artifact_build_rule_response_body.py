# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_cr20181201 import models as main_models
from darabonba.model import DaraModel

class GetArtifactBuildRuleResponseBody(DaraModel):
    def __init__(
        self,
        artifact_type: str = None,
        build_rule_id: str = None,
        code: str = None,
        is_success: bool = None,
        parameters: main_models.GetArtifactBuildRuleResponseBodyParameters = None,
        request_id: str = None,
        scope_id: str = None,
        scope_type: str = None,
    ):
        # The type of the artifact. Valid values:
        # 
        # *   `ACCELERATED_IMAGE`: accelerated images.
        self.artifact_type = artifact_type
        # The ID of the artifact building rule.
        self.build_rule_id = build_rule_id
        self.code = code
        # Indicates whether the API request is successful. Valid values:
        # 
        # *   `true`: The request is successful.
        # *   `false`: The request fails.
        self.is_success = is_success
        # Additional parameters.
        self.parameters = parameters
        # The request ID.
        self.request_id = request_id
        # The ID of the effective range of the artifact building rule.
        # 
        # *   The parameter value is the ID of the image repository.
        self.scope_id = scope_id
        # The effective range of the artifact building rule. Valid values:
        # 
        # *   `REPOSITORY`: The artifact building rule is effective in the repository level.
        self.scope_type = scope_type

    def validate(self):
        if self.parameters:
            self.parameters.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.artifact_type is not None:
            result['ArtifactType'] = self.artifact_type

        if self.build_rule_id is not None:
            result['BuildRuleId'] = self.build_rule_id

        if self.code is not None:
            result['Code'] = self.code

        if self.is_success is not None:
            result['IsSuccess'] = self.is_success

        if self.parameters is not None:
            result['Parameters'] = self.parameters.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

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

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')

        if m.get('Parameters') is not None:
            temp_model = main_models.GetArtifactBuildRuleResponseBodyParameters()
            self.parameters = temp_model.from_map(m.get('Parameters'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ScopeId') is not None:
            self.scope_id = m.get('ScopeId')

        if m.get('ScopeType') is not None:
            self.scope_type = m.get('ScopeType')

        return self

class GetArtifactBuildRuleResponseBodyParameters(DaraModel):
    def __init__(
        self,
        image_index_only: bool = None,
        priority_file: str = None,
    ):
        # Indicates whether the index-only mode is enabled.
        self.image_index_only = image_index_only
        # The list of files that you want to prefetch when you use the image acceleration feature. Each entry contains the Base64-encoded absolute path of a file.
        self.priority_file = priority_file

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.image_index_only is not None:
            result['ImageIndexOnly'] = self.image_index_only

        if self.priority_file is not None:
            result['PriorityFile'] = self.priority_file

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageIndexOnly') is not None:
            self.image_index_only = m.get('ImageIndexOnly')

        if m.get('PriorityFile') is not None:
            self.priority_file = m.get('PriorityFile')

        return self

