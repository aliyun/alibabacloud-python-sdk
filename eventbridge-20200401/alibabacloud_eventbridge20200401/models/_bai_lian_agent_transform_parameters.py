# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_eventbridge20200401 import models as main_models
from darabonba.model import DaraModel

class BaiLianAgentTransformParameters(DaraModel):
    def __init__(
        self,
        api_key: str = None,
        application_id: str = None,
        prompt: main_models.BaiLianAgentTransformParametersPrompt = None,
        request_per_minute: int = None,
        token_per_minute: int = None,
    ):
        self.api_key = api_key
        self.application_id = application_id
        self.prompt = prompt
        self.request_per_minute = request_per_minute
        self.token_per_minute = token_per_minute

    def validate(self):
        if self.prompt:
            self.prompt.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_key is not None:
            result['ApiKey'] = self.api_key

        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        if self.prompt is not None:
            result['Prompt'] = self.prompt.to_map()

        if self.request_per_minute is not None:
            result['RequestPerMinute'] = self.request_per_minute

        if self.token_per_minute is not None:
            result['TokenPerMinute'] = self.token_per_minute

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiKey') is not None:
            self.api_key = m.get('ApiKey')

        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('Prompt') is not None:
            temp_model = main_models.BaiLianAgentTransformParametersPrompt()
            self.prompt = temp_model.from_map(m.get('Prompt'))

        if m.get('RequestPerMinute') is not None:
            self.request_per_minute = m.get('RequestPerMinute')

        if m.get('TokenPerMinute') is not None:
            self.token_per_minute = m.get('TokenPerMinute')

        return self



class BaiLianAgentTransformParametersPrompt(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.form is not None:
            result['Form'] = self.form

        if self.template is not None:
            result['Template'] = self.template

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

