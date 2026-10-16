# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_codesec20260401 import models as main_models
from darabonba.model import DaraModel

class CreateProjectRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        engines: main_models.CreateProjectRequestEngines = None,
        instruction_prompt: str = None,
        name: str = None,
        source: main_models.CreateProjectRequestSource = None,
    ):
        # The description.
        self.description = description
        # The engine switches for the project or scan snapshot. Only SAST and SCA are supported.
        self.engines = engines
        # The natural language prompt that describes scanning or result processing preferences, such as ignoring low-risk vulnerabilities.
        self.instruction_prompt = instruction_prompt
        # The project name.
        # 
        # This parameter is required.
        self.name = name
        # The project source.
        self.source = source

    def validate(self):
        if self.engines:
            self.engines.validate()
        if self.source:
            self.source.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['description'] = self.description

        if self.engines is not None:
            result['engines'] = self.engines.to_map()

        if self.instruction_prompt is not None:
            result['instructionPrompt'] = self.instruction_prompt

        if self.name is not None:
            result['name'] = self.name

        if self.source is not None:
            result['source'] = self.source.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('engines') is not None:
            temp_model = main_models.CreateProjectRequestEngines()
            self.engines = temp_model.from_map(m.get('engines'))

        if m.get('instructionPrompt') is not None:
            self.instruction_prompt = m.get('instructionPrompt')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('source') is not None:
            temp_model = main_models.CreateProjectRequestSource()
            self.source = temp_model.from_map(m.get('source'))

        return self

class CreateProjectRequestSource(DaraModel):
    def __init__(
        self,
        type: str = None,
    ):
        # The project type.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class CreateProjectRequestEngines(DaraModel):
    def __init__(
        self,
        sast: bool = None,
        sast_config: main_models.CreateProjectRequestEnginesSastConfig = None,
        sca: bool = None,
        sca_config: main_models.CreateProjectRequestEnginesScaConfig = None,
    ):
        # Specifies whether SAST is supported.
        self.sast = sast
        # The engine-level configuration.
        self.sast_config = sast_config
        # Specifies whether SCA is supported.
        self.sca = sca
        # The engine-level configuration.
        self.sca_config = sca_config

    def validate(self):
        if self.sast_config:
            self.sast_config.validate()
        if self.sca_config:
            self.sca_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.sast is not None:
            result['sast'] = self.sast

        if self.sast_config is not None:
            result['sastConfig'] = self.sast_config.to_map()

        if self.sca is not None:
            result['sca'] = self.sca

        if self.sca_config is not None:
            result['scaConfig'] = self.sca_config.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('sast') is not None:
            self.sast = m.get('sast')

        if m.get('sastConfig') is not None:
            temp_model = main_models.CreateProjectRequestEnginesSastConfig()
            self.sast_config = temp_model.from_map(m.get('sastConfig'))

        if m.get('sca') is not None:
            self.sca = m.get('sca')

        if m.get('scaConfig') is not None:
            temp_model = main_models.CreateProjectRequestEnginesScaConfig()
            self.sca_config = temp_model.from_map(m.get('scaConfig'))

        return self

class CreateProjectRequestEnginesScaConfig(DaraModel):
    def __init__(
        self,
        remediation: bool = None,
    ):
        # Specifies whether to generate remediation suggestions.
        self.remediation = remediation

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.remediation is not None:
            result['remediation'] = self.remediation

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('remediation') is not None:
            self.remediation = m.get('remediation')

        return self

class CreateProjectRequestEnginesSastConfig(DaraModel):
    def __init__(
        self,
        remediation: bool = None,
    ):
        # Specifies whether to generate remediation suggestions.
        self.remediation = remediation

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.remediation is not None:
            result['remediation'] = self.remediation

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('remediation') is not None:
            self.remediation = m.get('remediation')

        return self

