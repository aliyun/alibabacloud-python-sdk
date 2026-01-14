# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateAndPulishAgentShrinkRequest(DaraModel):
    def __init__(
        self,
        application_config_shrink: str = None,
        instructions: str = None,
        model_id: str = None,
        name: str = None,
        sample_library_shrink: str = None,
    ):
        self.application_config_shrink = application_config_shrink
        self.instructions = instructions
        self.model_id = model_id
        self.name = name
        self.sample_library_shrink = sample_library_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_config_shrink is not None:
            result['applicationConfig'] = self.application_config_shrink

        if self.instructions is not None:
            result['instructions'] = self.instructions

        if self.model_id is not None:
            result['modelId'] = self.model_id

        if self.name is not None:
            result['name'] = self.name

        if self.sample_library_shrink is not None:
            result['sampleLibrary'] = self.sample_library_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('applicationConfig') is not None:
            self.application_config_shrink = m.get('applicationConfig')

        if m.get('instructions') is not None:
            self.instructions = m.get('instructions')

        if m.get('modelId') is not None:
            self.model_id = m.get('modelId')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('sampleLibrary') is not None:
            self.sample_library_shrink = m.get('sampleLibrary')

        return self

