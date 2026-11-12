# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class VacancyDetectionRequest(DaraModel):
    def __init__(
        self,
        image_url: str = None,
        system_prompt: str = None,
        user_prompt: str = None,
    ):
        # The HTTPS URL of the single image to be detected. Arrays or other image encodings are not supported.
        # 
        # This parameter is required.
        self.image_url = image_url
        # The optional system prompt.
        self.system_prompt = system_prompt
        # The optional user prompt. If this parameter is empty, the complete vacancy detection prompt is used. Plain text and JSON containing only text in messages or content are supported.
        self.user_prompt = user_prompt

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url

        if self.system_prompt is not None:
            result['SystemPrompt'] = self.system_prompt

        if self.user_prompt is not None:
            result['UserPrompt'] = self.user_prompt

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')

        if m.get('SystemPrompt') is not None:
            self.system_prompt = m.get('SystemPrompt')

        if m.get('UserPrompt') is not None:
            self.user_prompt = m.get('UserPrompt')

        return self

