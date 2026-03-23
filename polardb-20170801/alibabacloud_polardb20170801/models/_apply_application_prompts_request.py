# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ApplyApplicationPromptsRequest(DaraModel):
    def __init__(
        self,
        application_id: str = None,
        disabled_prompt_ids: List[str] = None,
        enabled_prompt_ids: List[str] = None,
    ):
        # This parameter is required.
        self.application_id = application_id
        self.disabled_prompt_ids = disabled_prompt_ids
        self.enabled_prompt_ids = enabled_prompt_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        if self.disabled_prompt_ids is not None:
            result['DisabledPromptIds'] = self.disabled_prompt_ids

        if self.enabled_prompt_ids is not None:
            result['EnabledPromptIds'] = self.enabled_prompt_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('DisabledPromptIds') is not None:
            self.disabled_prompt_ids = m.get('DisabledPromptIds')

        if m.get('EnabledPromptIds') is not None:
            self.enabled_prompt_ids = m.get('EnabledPromptIds')

        return self

