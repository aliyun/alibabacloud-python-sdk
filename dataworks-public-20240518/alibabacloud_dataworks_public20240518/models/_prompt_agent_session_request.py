# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class PromptAgentSessionRequest(DaraModel):
    def __init__(
        self,
        id: str = None,
        jsonrpc: str = None,
        params: main_models.PromptAgentSessionRequestParams = None,
    ):
        self.id = id
        self.jsonrpc = jsonrpc
        self.params = params

    def validate(self):
        if self.params:
            self.params.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.jsonrpc is not None:
            result['Jsonrpc'] = self.jsonrpc

        if self.params is not None:
            result['Params'] = self.params.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Jsonrpc') is not None:
            self.jsonrpc = m.get('Jsonrpc')

        if m.get('Params') is not None:
            temp_model = main_models.PromptAgentSessionRequestParams()
            self.params = temp_model.from_map(m.get('Params'))

        return self

class PromptAgentSessionRequestParams(DaraModel):
    def __init__(
        self,
        meta: main_models.PromptAgentSessionRequestParamsMeta = None,
        prompt: List[main_models.PromptAgentSessionRequestParamsPrompt] = None,
        session_id: str = None,
    ):
        self.meta = meta
        self.prompt = prompt
        self.session_id = session_id

    def validate(self):
        if self.meta:
            self.meta.validate()
        if self.prompt:
            for v1 in self.prompt:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.meta is not None:
            result['Meta'] = self.meta.to_map()

        result['Prompt'] = []
        if self.prompt is not None:
            for k1 in self.prompt:
                result['Prompt'].append(k1.to_map() if k1 else None)

        if self.session_id is not None:
            result['SessionId'] = self.session_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Meta') is not None:
            temp_model = main_models.PromptAgentSessionRequestParamsMeta()
            self.meta = temp_model.from_map(m.get('Meta'))

        self.prompt = []
        if m.get('Prompt') is not None:
            for k1 in m.get('Prompt'):
                temp_model = main_models.PromptAgentSessionRequestParamsPrompt()
                self.prompt.append(temp_model.from_map(k1))

        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        return self

class PromptAgentSessionRequestParamsPrompt(DaraModel):
    def __init__(
        self,
        description: str = None,
        meta: main_models.PromptAgentSessionRequestParamsPromptMeta = None,
        mime_type: str = None,
        name: str = None,
        size: int = None,
        text: str = None,
        title: str = None,
        type: str = None,
        uri: str = None,
    ):
        self.description = description
        self.meta = meta
        self.mime_type = mime_type
        self.name = name
        self.size = size
        self.text = text
        self.title = title
        self.type = type
        self.uri = uri

    def validate(self):
        if self.meta:
            self.meta.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.meta is not None:
            result['Meta'] = self.meta.to_map()

        if self.mime_type is not None:
            result['MimeType'] = self.mime_type

        if self.name is not None:
            result['Name'] = self.name

        if self.size is not None:
            result['Size'] = self.size

        if self.text is not None:
            result['Text'] = self.text

        if self.title is not None:
            result['Title'] = self.title

        if self.type is not None:
            result['Type'] = self.type

        if self.uri is not None:
            result['Uri'] = self.uri

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Meta') is not None:
            temp_model = main_models.PromptAgentSessionRequestParamsPromptMeta()
            self.meta = temp_model.from_map(m.get('Meta'))

        if m.get('MimeType') is not None:
            self.mime_type = m.get('MimeType')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('Text') is not None:
            self.text = m.get('Text')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Uri') is not None:
            self.uri = m.get('Uri')

        return self

class PromptAgentSessionRequestParamsPromptMeta(DaraModel):
    def __init__(
        self,
        hide: bool = None,
    ):
        self.hide = hide

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.hide is not None:
            result['Hide'] = self.hide

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Hide') is not None:
            self.hide = m.get('Hide')

        return self

class PromptAgentSessionRequestParamsMeta(DaraModel):
    def __init__(
        self,
        context: Any = None,
    ):
        self.context = context

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.context is not None:
            result['Context'] = self.context

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Context') is not None:
            self.context = m.get('Context')

        return self

