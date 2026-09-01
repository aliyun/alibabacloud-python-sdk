# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_fcsandbox20260509 import models as main_models
from darabonba.model import DaraModel

class CreateTemplateInput(DaraModel):
    def __init__(
        self,
        build_config: main_models.CreateTemplateBuildConfig = None,
        name: str = None,
        runtime_config: main_models.CreateTemplateRuntimeConfig = None,
        team_id: str = None,
    ):
        # The template build configuration.
        self.build_config = build_config
        # The template name.
        self.name = name
        # The template runtime configuration.
        self.runtime_config = runtime_config
        # The unique identifier of the team.
        self.team_id = team_id

    def validate(self):
        if self.build_config:
            self.build_config.validate()
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

        if m.get('runtimeConfig') is not None:
            temp_model = main_models.CreateTemplateRuntimeConfig()
            self.runtime_config = temp_model.from_map(m.get('runtimeConfig'))

        if m.get('teamID') is not None:
            self.team_id = m.get('teamID')

        return self

