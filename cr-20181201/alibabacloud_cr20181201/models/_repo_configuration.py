# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_cr20181201 import models as main_models
from darabonba.model import DaraModel

class RepoConfiguration(DaraModel):
    def __init__(
        self,
        artifact_build_rule_parameters: main_models.RepoConfigurationArtifactBuildRuleParameters = None,
        repo_type: str = None,
        tag_immutability: bool = None,
    ):
        self.artifact_build_rule_parameters = artifact_build_rule_parameters
        # This parameter is required.
        self.repo_type = repo_type
        # This parameter is required.
        self.tag_immutability = tag_immutability

    def validate(self):
        if self.artifact_build_rule_parameters:
            self.artifact_build_rule_parameters.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.artifact_build_rule_parameters is not None:
            result['ArtifactBuildRuleParameters'] = self.artifact_build_rule_parameters.to_map()

        if self.repo_type is not None:
            result['RepoType'] = self.repo_type

        if self.tag_immutability is not None:
            result['TagImmutability'] = self.tag_immutability

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArtifactBuildRuleParameters') is not None:
            temp_model = main_models.RepoConfigurationArtifactBuildRuleParameters()
            self.artifact_build_rule_parameters = temp_model.from_map(m.get('ArtifactBuildRuleParameters'))

        if m.get('RepoType') is not None:
            self.repo_type = m.get('RepoType')

        if m.get('TagImmutability') is not None:
            self.tag_immutability = m.get('TagImmutability')

        return self

class RepoConfigurationArtifactBuildRuleParameters(DaraModel):
    def __init__(
        self,
        image_index_only: bool = None,
    ):
        # This parameter is required.
        self.image_index_only = image_index_only

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.image_index_only is not None:
            result['ImageIndexOnly'] = self.image_index_only

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageIndexOnly') is not None:
            self.image_index_only = m.get('ImageIndexOnly')

        return self

