# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ApplyApplicationPromptsShrinkRequest(DaraModel):
    def __init__(
        self,
        application_id: str = None,
        disabled_prompt_ids_shrink: str = None,
        enabled_prompt_ids_shrink: str = None,
    ):
        # This parameter is required.
        self.application_id = application_id
        self.disabled_prompt_ids_shrink = disabled_prompt_ids_shrink
        self.enabled_prompt_ids_shrink = enabled_prompt_ids_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        if self.disabled_prompt_ids_shrink is not None:
            result['DisabledPromptIds'] = self.disabled_prompt_ids_shrink

        if self.enabled_prompt_ids_shrink is not None:
            result['EnabledPromptIds'] = self.enabled_prompt_ids_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('DisabledPromptIds') is not None:
            self.disabled_prompt_ids_shrink = m.get('DisabledPromptIds')

        if m.get('EnabledPromptIds') is not None:
            self.enabled_prompt_ids_shrink = m.get('EnabledPromptIds')

        return self

