# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DataInterpretationRequest(DaraModel):
    def __init__(
        self,
        data: str = None,
        model_code: str = None,
        prompt_force_override: bool = None,
        user_prompt: str = None,
        user_question: str = None,
    ):
        # This parameter is required.
        self.data = data
        self.model_code = model_code
        self.prompt_force_override = prompt_force_override
        self.user_prompt = user_prompt
        self.user_question = user_question

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data

        if self.model_code is not None:
            result['ModelCode'] = self.model_code

        if self.prompt_force_override is not None:
            result['PromptForceOverride'] = self.prompt_force_override

        if self.user_prompt is not None:
            result['UserPrompt'] = self.user_prompt

        if self.user_question is not None:
            result['UserQuestion'] = self.user_question

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')

        if m.get('ModelCode') is not None:
            self.model_code = m.get('ModelCode')

        if m.get('PromptForceOverride') is not None:
            self.prompt_force_override = m.get('PromptForceOverride')

        if m.get('UserPrompt') is not None:
            self.user_prompt = m.get('UserPrompt')

        if m.get('UserQuestion') is not None:
            self.user_question = m.get('UserQuestion')

        return self

