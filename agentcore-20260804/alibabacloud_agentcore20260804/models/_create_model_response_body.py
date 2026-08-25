# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_agentcore20260804 import models as main_models
from darabonba.model import DaraModel

class CreateModelResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.CreateModelResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The business status code. The value SUCCESS indicates success.
        self.code = code
        # The model information after creation.
        self.data = data
        # The HTTP status code. The value 200 indicates success.
        self.http_status_code = http_status_code
        # The request processing result message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('data') is not None:
            temp_model = main_models.CreateModelResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

class CreateModelResponseBodyData(DaraModel):
    def __init__(
        self,
        capabilities: main_models.CreateModelResponseBodyDataCapabilities = None,
        connection_id: str = None,
        context_size: int = None,
        created_at: str = None,
        description: str = None,
        max_tokens: int = None,
        model_id: str = None,
        model_name: str = None,
        updated_at: str = None,
        workspace_id: str = None,
    ):
        # The model capability configuration.
        self.capabilities = capabilities
        # The model connection ID.
        self.connection_id = connection_id
        # The model context window size, in tokens. The value must be a positive integer.
        self.context_size = context_size
        # The resource creation time in RFC 3339 UTC format.
        self.created_at = created_at
        # The model description. Maximum length: 255 characters.
        self.description = description
        # The maximum number of output tokens supported per model generation.
        self.max_tokens = max_tokens
        # The model ID.
        self.model_id = model_id
        # The upstream model name.
        self.model_name = model_name
        # The resource last update time in RFC 3339 UTC format.
        self.updated_at = updated_at
        # The workspace ID.
        self.workspace_id = workspace_id

    def validate(self):
        if self.capabilities:
            self.capabilities.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.capabilities is not None:
            result['capabilities'] = self.capabilities.to_map()

        if self.connection_id is not None:
            result['connectionId'] = self.connection_id

        if self.context_size is not None:
            result['contextSize'] = self.context_size

        if self.created_at is not None:
            result['createdAt'] = self.created_at

        if self.description is not None:
            result['description'] = self.description

        if self.max_tokens is not None:
            result['maxTokens'] = self.max_tokens

        if self.model_id is not None:
            result['modelId'] = self.model_id

        if self.model_name is not None:
            result['modelName'] = self.model_name

        if self.updated_at is not None:
            result['updatedAt'] = self.updated_at

        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('capabilities') is not None:
            temp_model = main_models.CreateModelResponseBodyDataCapabilities()
            self.capabilities = temp_model.from_map(m.get('capabilities'))

        if m.get('connectionId') is not None:
            self.connection_id = m.get('connectionId')

        if m.get('contextSize') is not None:
            self.context_size = m.get('contextSize')

        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('maxTokens') is not None:
            self.max_tokens = m.get('maxTokens')

        if m.get('modelId') is not None:
            self.model_id = m.get('modelId')

        if m.get('modelName') is not None:
            self.model_name = m.get('modelName')

        if m.get('updatedAt') is not None:
            self.updated_at = m.get('updatedAt')

        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')

        return self

class CreateModelResponseBodyDataCapabilities(DaraModel):
    def __init__(
        self,
        audio: bool = None,
        document: bool = None,
        multi_tool_call: bool = None,
        reasoning: bool = None,
        stream_tool_call: bool = None,
        tool_call: bool = None,
        video: bool = None,
        vision: bool = None,
    ):
        # Specifies whether the model supports audio input or output.
        self.audio = audio
        # Specifies whether the model supports document input.
        self.document = document
        # Specifies whether the model is able to invoke multiple tools in a single response.
        self.multi_tool_call = multi_tool_call
        # Specifies whether the model supports reasoning capabilities.
        self.reasoning = reasoning
        # Specifies whether the model supports streaming tool calling.
        self.stream_tool_call = stream_tool_call
        # Specifies whether the model supports tool calling.
        self.tool_call = tool_call
        # Specifies whether the model supports video input.
        self.video = video
        # Specifies whether the model supports image input.
        self.vision = vision

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.audio is not None:
            result['audio'] = self.audio

        if self.document is not None:
            result['document'] = self.document

        if self.multi_tool_call is not None:
            result['multiToolCall'] = self.multi_tool_call

        if self.reasoning is not None:
            result['reasoning'] = self.reasoning

        if self.stream_tool_call is not None:
            result['streamToolCall'] = self.stream_tool_call

        if self.tool_call is not None:
            result['toolCall'] = self.tool_call

        if self.video is not None:
            result['video'] = self.video

        if self.vision is not None:
            result['vision'] = self.vision

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('audio') is not None:
            self.audio = m.get('audio')

        if m.get('document') is not None:
            self.document = m.get('document')

        if m.get('multiToolCall') is not None:
            self.multi_tool_call = m.get('multiToolCall')

        if m.get('reasoning') is not None:
            self.reasoning = m.get('reasoning')

        if m.get('streamToolCall') is not None:
            self.stream_tool_call = m.get('streamToolCall')

        if m.get('toolCall') is not None:
            self.tool_call = m.get('toolCall')

        if m.get('video') is not None:
            self.video = m.get('video')

        if m.get('vision') is not None:
            self.vision = m.get('vision')

        return self

