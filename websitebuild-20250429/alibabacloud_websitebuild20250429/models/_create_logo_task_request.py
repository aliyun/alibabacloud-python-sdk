# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateLogoTaskRequest(DaraModel):
    def __init__(
        self,
        logo_version: str = None,
        negative_prompt: str = None,
        parameters: str = None,
        prompt: str = None,
    ):
        self.logo_version = logo_version
        self.negative_prompt = negative_prompt
        self.parameters = parameters
        self.prompt = prompt

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.logo_version is not None:
            result['LogoVersion'] = self.logo_version

        if self.negative_prompt is not None:
            result['NegativePrompt'] = self.negative_prompt

        if self.parameters is not None:
            result['Parameters'] = self.parameters

        if self.prompt is not None:
            result['Prompt'] = self.prompt

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LogoVersion') is not None:
            self.logo_version = m.get('LogoVersion')

        if m.get('NegativePrompt') is not None:
            self.negative_prompt = m.get('NegativePrompt')

        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')

        if m.get('Prompt') is not None:
            self.prompt = m.get('Prompt')

        return self

