# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateApplicationPromptRequest(DaraModel):
    def __init__(
        self,
        application_id: str = None,
        prompt_name: str = None,
        prompt_type: str = None,
        prompt_value: str = None,
    ):
        # This parameter is required.
        self.application_id = application_id
        # This parameter is required.
        self.prompt_name = prompt_name
        # This parameter is required.
        self.prompt_type = prompt_type
        # This parameter is required.
        self.prompt_value = prompt_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        if self.prompt_name is not None:
            result['PromptName'] = self.prompt_name

        if self.prompt_type is not None:
            result['PromptType'] = self.prompt_type

        if self.prompt_value is not None:
            result['PromptValue'] = self.prompt_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('PromptName') is not None:
            self.prompt_name = m.get('PromptName')

        if m.get('PromptType') is not None:
            self.prompt_type = m.get('PromptType')

        if m.get('PromptValue') is not None:
            self.prompt_value = m.get('PromptValue')

        return self

