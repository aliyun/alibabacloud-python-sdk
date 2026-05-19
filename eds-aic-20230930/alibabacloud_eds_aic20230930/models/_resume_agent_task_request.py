# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ResumeAgentTaskRequest(DaraModel):
    def __init__(
        self,
        additional_prompt: str = None,
        task_ids: List[str] = None,
    ):
        self.additional_prompt = additional_prompt
        # This parameter is required.
        self.task_ids = task_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.additional_prompt is not None:
            result['AdditionalPrompt'] = self.additional_prompt

        if self.task_ids is not None:
            result['TaskIds'] = self.task_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdditionalPrompt') is not None:
            self.additional_prompt = m.get('AdditionalPrompt')

        if m.get('TaskIds') is not None:
            self.task_ids = m.get('TaskIds')

        return self

