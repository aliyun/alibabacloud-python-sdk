# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sandbox20260820 import models as main_models
from darabonba.model import DaraModel

class CreateTemplateInput(DaraModel):
    def __init__(
        self,
        build_config: main_models.CreateTemplateBuildConfig = None,
        name: str = None,
        resource_tags: List[main_models.CreateTemplateInputResourceTags] = None,
        runtime_config: main_models.CreateTemplateRuntimeConfig = None,
        team_id: str = None,
    ):
        # The build configuration of the template. This configuration specifies the build process in action-based blocks. If this parameter is not specified, the service automatically derives the configuration based on the source image. Public runtime images are used directly without building. For other images, the copy and envdInject actions are automatically executed.
        self.build_config = build_config
        # The name of the template. The name must be unique within the same team.
        self.name = name
        # The resource tags.
        self.resource_tags = resource_tags
        # The runtime configuration of the template. This configuration determines the specifications and environment of the sandbox instances created from the template.
        self.runtime_config = runtime_config
        # The ID of the team to which the template belongs. The ID is in UUID format. If this parameter is not specified, the default team of the current account is used.
        self.team_id = team_id

    def validate(self):
        if self.build_config:
            self.build_config.validate()
        if self.resource_tags:
            for v1 in self.resource_tags:
                 if v1:
                    v1.validate()
        if self.runtime_config:
            self.runtime_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.build_config is not None:
            result['buildConfig'] = self.build_config.to_map()

        if self.name is not None:
            result['name'] = self.name

        if self.resource_tags is not None:
            result['resourceTags'] = []
            for k1 in self.resource_tags:
                result['resourceTags'].append(k1.to_map() if k1 else None)

        if self.runtime_config is not None:
            result['runtimeConfig'] = self.runtime_config.to_map()

        if self.team_id is not None:
            result['teamID'] = self.team_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('buildConfig') is not None:
            temp_model = main_models.CreateTemplateBuildConfig()
            self.build_config = temp_model.from_map(m.get('buildConfig'))

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('resourceTags') is not None:
            self.resource_tags = []
            for k1 in m.get('resourceTags'):
                temp_model = main_models.CreateTemplateInputResourceTags()
                self.resource_tags.append(temp_model.from_map(k1))

        if m.get('runtimeConfig') is not None:
            temp_model = main_models.CreateTemplateRuntimeConfig()
            self.runtime_config = temp_model.from_map(m.get('runtimeConfig'))

        if m.get('teamID') is not None:
            self.team_id = m.get('teamID')

        return self

class CreateTemplateInputResourceTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the tag.
        self.key = key
        # The value of the tag.
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

