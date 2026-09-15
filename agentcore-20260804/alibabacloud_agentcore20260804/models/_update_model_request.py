# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_agentcore20260804 import models as main_models
from darabonba.model import DaraModel

class UpdateModelRequest(DaraModel):
    def __init__(
        self,
        body: main_models.UpdateModelRequestBody = None,
        client_token: str = None,
    ):
        # The model update request body. At least one non-null parameter must be provided among description, contextSize, maxTokens, and capabilities.
        self.body = body
        # The client token for idempotency. Not currently supported.
        self.client_token = client_token

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.body is not None:
            result['body'] = self.body.to_map()

        if self.client_token is not None:
            result['clientToken'] = self.client_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = main_models.UpdateModelRequestBody()
            self.body = temp_model.from_map(m.get('body'))

        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')

        return self

class UpdateModelRequestBody(DaraModel):
    def __init__(
        self,
        capabilities: main_models.UpdateModelRequestBodyCapabilities = None,
        context_size: int = None,
        description: str = None,
        max_tokens: int = None,
    ):
        # The model capability configuration. When an object is provided, it replaces the existing capability configuration as a whole. Capability fields not included in the object are treated as false. Providing an empty object {} sets all capabilities to false. If this parameter is not provided or set to null, the original configuration is retained.
        self.capabilities = capabilities
        # The context token limit of the model. The minimum value is 1000. The updated value must not be less than maxTokens. If maxTokens is not provided in this request, the existing value is used for validation. If this parameter is not provided or set to null, the original value is retained.
        self.context_size = context_size
        # The model description. The maximum length is 255 characters after leading and trailing whitespace is removed. Providing an empty string clears the description. If this parameter is not provided or set to null, the original value is retained. Modifying only the description does not refresh the model configuration of associated Agents.
        self.description = description
        # The maximum number of output tokens per generation. The value must be a positive integer. If contextSize is configured, the updated maxTokens must not exceed contextSize. If contextSize is not provided in this request, the existing value is used for validation. If this parameter is not provided or set to null, the original value is retained.
        self.max_tokens = max_tokens

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

        if self.context_size is not None:
            result['contextSize'] = self.context_size

        if self.description is not None:
            result['description'] = self.description

        if self.max_tokens is not None:
            result['maxTokens'] = self.max_tokens

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('capabilities') is not None:
            temp_model = main_models.UpdateModelRequestBodyCapabilities()
            self.capabilities = temp_model.from_map(m.get('capabilities'))

        if m.get('contextSize') is not None:
            self.context_size = m.get('contextSize')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('maxTokens') is not None:
            self.max_tokens = m.get('maxTokens')

        return self

class UpdateModelRequestBodyCapabilities(DaraModel):
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
        # Specifies whether the model supports audio input or output. A value of true indicates that it is supported. A value of false indicates that it is not supported.
        self.audio = audio
        # Specifies whether the model supports document input. A value of true indicates that it is supported. A value of false indicates that it is not supported.
        self.document = document
        # Specifies whether the model supports invoking multiple tools in a single response. A value of true indicates that it is supported. A value of false indicates that it is not supported.
        self.multi_tool_call = multi_tool_call
        # Specifies whether the model supports reasoning. A value of true indicates that it is supported. A value of false indicates that it is not supported. This field is a capability marker and is not used to set reasoning intensity or reasoning token budget.
        self.reasoning = reasoning
        # Specifies whether the model supports streaming tool invocation. A value of true indicates that it is supported. A value of false indicates that it is not supported.
        self.stream_tool_call = stream_tool_call
        # Specifies whether the model supports tool invocation. A value of true indicates that it is supported. A value of false indicates that it is not supported.
        self.tool_call = tool_call
        # Specifies whether the model supports video input. A value of true indicates that it is supported. A value of false indicates that it is not supported.
        self.video = video
        # Specifies whether the model supports image input. A value of true indicates that it is supported. A value of false indicates that it is not supported.
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

