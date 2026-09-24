# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PetHealthAnalysisShrinkRequest(DaraModel):
    def __init__(
        self,
        image_url_shrink: str = None,
        system_prompt: str = None,
        user_prompt: str = None,
    ):
        # The list of HTTPS URLs of images to analyze. At least one accessible image must be provided.
        # 
        # This parameter is required.
        self.image_url_shrink = image_url_shrink
        # The system prompt used to specify the response role or requirements. The value must comply with JSON string escaping rules.
        self.system_prompt = system_prompt
        # The custom analysis requirement. If not specified or set to an empty string, excrement analysis is performed by default. The value must comply with JSON string escaping rules.
        self.user_prompt = user_prompt

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.image_url_shrink is not None:
            result['ImageUrl'] = self.image_url_shrink

        if self.system_prompt is not None:
            result['SystemPrompt'] = self.system_prompt

        if self.user_prompt is not None:
            result['UserPrompt'] = self.user_prompt

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageUrl') is not None:
            self.image_url_shrink = m.get('ImageUrl')

        if m.get('SystemPrompt') is not None:
            self.system_prompt = m.get('SystemPrompt')

        if m.get('UserPrompt') is not None:
            self.user_prompt = m.get('UserPrompt')

        return self

