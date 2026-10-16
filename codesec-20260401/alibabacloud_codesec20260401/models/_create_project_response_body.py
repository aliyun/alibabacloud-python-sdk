# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_codesec20260401 import models as main_models
from darabonba.model import DaraModel

class CreateProjectResponseBody(DaraModel):
    def __init__(
        self,
        config_revision: int = None,
        created_at: str = None,
        created_by: str = None,
        description: str = None,
        engines: main_models.CreateProjectResponseBodyEngines = None,
        id: int = None,
        instruction_prompt: str = None,
        name: str = None,
        request_id: str = None,
        source: main_models.CreateProjectResponseBodySource = None,
        updated_at: str = None,
    ):
        # The project configuration version number.
        self.config_revision = config_revision
        # The creation time.
        self.created_at = created_at
        # The user ID of the project creator.
        self.created_by = created_by
        # The description.
        self.description = description
        # The engine switches for the project or scan snapshot. Only SAST and SCA are supported.
        self.engines = engines
        # The project ID.
        self.id = id
        # The natural language prompt that describes scanning or result processing preferences, such as ignoring low-risk vulnerabilities.
        self.instruction_prompt = instruction_prompt
        # The project name.
        self.name = name
        # The request ID.
        self.request_id = request_id
        # The project source.
        self.source = source
        # The update time.
        self.updated_at = updated_at

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
        if self.config_revision is not None:
            result['configRevision'] = self.config_revision

        if self.created_at is not None:
            result['createdAt'] = self.created_at

        if self.created_by is not None:
            result['createdBy'] = self.created_by

        if self.description is not None:
            result['description'] = self.description

        if self.engines is not None:
            result['engines'] = self.engines.to_map()

        if self.id is not None:
            result['id'] = self.id

        if self.instruction_prompt is not None:
            result['instructionPrompt'] = self.instruction_prompt

        if self.name is not None:
            result['name'] = self.name

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.source is not None:
            result['source'] = self.source.to_map()

        if self.updated_at is not None:
            result['updatedAt'] = self.updated_at

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('configRevision') is not None:
            self.config_revision = m.get('configRevision')

        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')

        if m.get('createdBy') is not None:
            self.created_by = m.get('createdBy')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('engines') is not None:
            temp_model = main_models.CreateProjectResponseBodyEngines()
            self.engines = temp_model.from_map(m.get('engines'))

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('instructionPrompt') is not None:
            self.instruction_prompt = m.get('instructionPrompt')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('source') is not None:
            temp_model = main_models.CreateProjectResponseBodySource()
            self.source = temp_model.from_map(m.get('source'))

        if m.get('updatedAt') is not None:
            self.updated_at = m.get('updatedAt')

        return self

class CreateProjectResponseBodySource(DaraModel):
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

class CreateProjectResponseBodyEngines(DaraModel):
    def __init__(
        self,
        sast: bool = None,
        sca: bool = None,
    ):
        # Specifies whether SAST is supported.
        self.sast = sast
        # Specifies whether SCA is supported.
        self.sca = sca

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.sast is not None:
            result['sast'] = self.sast

        if self.sca is not None:
            result['sca'] = self.sca

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('sast') is not None:
            self.sast = m.get('sast')

        if m.get('sca') is not None:
            self.sca = m.get('sca')

        return self

