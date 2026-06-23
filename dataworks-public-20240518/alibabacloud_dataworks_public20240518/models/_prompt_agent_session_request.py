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
        # The ID passed in by the caller. The value is returned as-is in the response.
        self.id = id
        # The JSON-RPC version. Fixed value: 2.0.
        self.jsonrpc = jsonrpc
        # The business parameters.
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
        # The extended metadata.
        self.meta = meta
        # The array of user message content blocks. For more information, see https\\://agentclientprotocol.com/protocol/content
        self.prompt = prompt
        # The ID of the target session. If the session does not exist, an SSE error frame is returned.
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
        # The description of the file.
        self.description = description
        # The prompt metadata extended by DataWorks.
        self.meta = meta
        # The MIME type of the file.
        self.mime_type = mime_type
        # The file name.
        self.name = name
        # The size of the file. Unit: bytes.
        self.size = size
        # **The text content.**
        self.text = text
        # The title of the file.
        self.title = title
        # **The content block type.**
        self.type = type
        # The URI of the file.
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
        # Specifies whether to hide the prompt from the user. For example, if a user asks "Sales amount in the last 7 days" in a chat dialog, the calling system may use RAG to retrieve relevant business domain knowledge and append it to the agent context before calling the API. If you do not want to display this supplemental information to the user, set this parameter to true.
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
        # A Map-type value. In custom agent scenarios, you can use this parameter to replace placeholder parameters.
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

