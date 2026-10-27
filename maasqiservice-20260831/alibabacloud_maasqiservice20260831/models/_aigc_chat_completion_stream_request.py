# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_maasqiservice20260831 import models as main_models
from darabonba.model import DaraModel

class AigcChatCompletionStreamRequest(DaraModel):
    def __init__(
        self,
        messages: List[main_models.AigcChatCompletionStreamRequestMessages] = None,
        metadata: main_models.AigcChatCompletionStreamRequestMetadata = None,
        model: str = None,
        stream: bool = None,
        stream_options: main_models.AigcChatCompletionStreamRequestStreamOptions = None,
    ):
        # The conversation message array. Creative Agent uses the last user message as the current objective and executes it in combination with the session history.
        # 
        # This parameter is required.
        self.messages = messages
        # The extended input for this image creation request. Use the parameters object to set generation parameters. Do not use this field to pass model addresses or keys.
        self.metadata = metadata
        # A compatibility placeholder field. Can be omitted or set to an empty string. You cannot use this field to switch the model used by the instance. The model field in the response is an empty string.
        self.model = model
        # Specifies whether to use SSE streaming responses. This parameter must be set to true for this operation.
        # 
        # This parameter is required.
        self.stream = stream
        # The HTTP JSON key is stream_options. Set include_usage to retrieve the token usage for this call.
        self.stream_options = stream_options

    def validate(self):
        if self.messages:
            for v1 in self.messages:
                 if v1:
                    v1.validate()
        if self.metadata:
            self.metadata.validate()
        if self.stream_options:
            self.stream_options.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['messages'] = []
        if self.messages is not None:
            for k1 in self.messages:
                result['messages'].append(k1.to_map() if k1 else None)

        if self.metadata is not None:
            result['metadata'] = self.metadata.to_map()

        if self.model is not None:
            result['model'] = self.model

        if self.stream is not None:
            result['stream'] = self.stream

        if self.stream_options is not None:
            result['streamOptions'] = self.stream_options.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.messages = []
        if m.get('messages') is not None:
            for k1 in m.get('messages'):
                temp_model = main_models.AigcChatCompletionStreamRequestMessages()
                self.messages.append(temp_model.from_map(k1))

        if m.get('metadata') is not None:
            temp_model = main_models.AigcChatCompletionStreamRequestMetadata()
            self.metadata = temp_model.from_map(m.get('metadata'))

        if m.get('model') is not None:
            self.model = m.get('model')

        if m.get('stream') is not None:
            self.stream = m.get('stream')

        if m.get('streamOptions') is not None:
            temp_model = main_models.AigcChatCompletionStreamRequestStreamOptions()
            self.stream_options = temp_model.from_map(m.get('streamOptions'))

        return self

class AigcChatCompletionStreamRequestStreamOptions(DaraModel):
    def __init__(
        self,
        include_usage: bool = None,
    ):
        # The HTTP JSON key is include_usage. When set to true, an independent usage chunk is returned before the end marker. The choices field in this chunk is an empty array. Token usage does not represent the number of images or the final bill.
        self.include_usage = include_usage

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.include_usage is not None:
            result['includeUsage'] = self.include_usage

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('includeUsage') is not None:
            self.include_usage = m.get('includeUsage')

        return self

class AigcChatCompletionStreamRequestMetadata(DaraModel):
    def __init__(
        self,
        parameters: main_models.AigcChatCompletionStreamRequestMetadataParameters = None,
    ):
        # The image parameters for this request. Only size, n, seed, negative_prompt, num_inference_steps, and guidance_scale are supported. Omitted fields use the default configurations. response_format is not supported.
        self.parameters = parameters

    def validate(self):
        if self.parameters:
            self.parameters.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.parameters is not None:
            result['parameters'] = self.parameters.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('parameters') is not None:
            temp_model = main_models.AigcChatCompletionStreamRequestMetadataParameters()
            self.parameters = temp_model.from_map(m.get('parameters'))

        return self

class AigcChatCompletionStreamRequestMetadataParameters(DaraModel):
    def __init__(
        self,
        guidance_scale: float = None,
        n: int = None,
        negative_prompt: str = None,
        num_inference_steps: int = None,
        seed: int = None,
        size: str = None,
    ):
        # The guidance scale. Must be a finite number between 0 and 20.
        self.guidance_scale = guidance_scale
        # The number of images to generate for this request. Must be an integer in the range of 1 to 6.
        self.n = n
        # The negative prompt that describes content you do not want to appear in the result.
        self.negative_prompt = negative_prompt
        # The number of model inference iterations. Must be an integer in the range of 1 to 200.
        self.num_inference_steps = num_inference_steps
        # The random seed. Must be an integer in the range of 0 to 2147483647.
        self.seed = seed
        # The output pixel dimensions, such as `1024*1024` or `1280*720`. The format `1024x1024` is also accepted. When specified, this value overrides the default canvas dimensions for this request. Use width and height values supported by the model.
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.guidance_scale is not None:
            result['guidanceScale'] = self.guidance_scale

        if self.n is not None:
            result['n'] = self.n

        if self.negative_prompt is not None:
            result['negativePrompt'] = self.negative_prompt

        if self.num_inference_steps is not None:
            result['numInferenceSteps'] = self.num_inference_steps

        if self.seed is not None:
            result['seed'] = self.seed

        if self.size is not None:
            result['size'] = self.size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('guidanceScale') is not None:
            self.guidance_scale = m.get('guidanceScale')

        if m.get('n') is not None:
            self.n = m.get('n')

        if m.get('negativePrompt') is not None:
            self.negative_prompt = m.get('negativePrompt')

        if m.get('numInferenceSteps') is not None:
            self.num_inference_steps = m.get('numInferenceSteps')

        if m.get('seed') is not None:
            self.seed = m.get('seed')

        if m.get('size') is not None:
            self.size = m.get('size')

        return self

class AigcChatCompletionStreamRequestMessages(DaraModel):
    def __init__(
        self,
        content: List[main_models.AigcChatCompletionStreamRequestMessagesContent] = None,
        role: str = None,
    ):
        # The message content. Can be text. A multimodal array can contain text, image_url, or video_url. The Creative Agent Lite edition performs image-to-image when a reference image is provided and text-to-image when no reference image is provided. It does not accept video.
        self.content = content
        # The message role. Place the current generation objective in a user message. History can include user, assistant, and tool.
        self.role = role

    def validate(self):
        if self.content:
            for v1 in self.content:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['content'] = []
        if self.content is not None:
            for k1 in self.content:
                result['content'].append(k1.to_map() if k1 else None)

        if self.role is not None:
            result['role'] = self.role

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.content = []
        if m.get('content') is not None:
            for k1 in m.get('content'):
                temp_model = main_models.AigcChatCompletionStreamRequestMessagesContent()
                self.content.append(temp_model.from_map(k1))

        if m.get('role') is not None:
            self.role = m.get('role')

        return self

class AigcChatCompletionStreamRequestMessagesContent(DaraModel):
    def __init__(
        self,
        image_url: main_models.AigcChatCompletionStreamRequestMessagesContentImageUrl = None,
        text: str = None,
        type: str = None,
        video_url: main_models.AigcChatCompletionStreamRequestMessagesContentVideoUrl = None,
    ):
        # The reference image when type is set to image_url. Supports HTTPS URLs or Base64 Data URLs.
        self.image_url = image_url
        # The generation or editing objective when type is set to text.
        self.text = text
        # The content part type: text, image_url, or video_url.
        self.type = type
        # The video input when type is set to video_url. Only accepted by the Creative Agent Dedicated edition Planner. The Creative Agent Lite edition rejects this type.
        self.video_url = video_url

    def validate(self):
        if self.image_url:
            self.image_url.validate()
        if self.video_url:
            self.video_url.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.image_url is not None:
            result['imageUrl'] = self.image_url.to_map()

        if self.text is not None:
            result['text'] = self.text

        if self.type is not None:
            result['type'] = self.type

        if self.video_url is not None:
            result['videoUrl'] = self.video_url.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('imageUrl') is not None:
            temp_model = main_models.AigcChatCompletionStreamRequestMessagesContentImageUrl()
            self.image_url = temp_model.from_map(m.get('imageUrl'))

        if m.get('text') is not None:
            self.text = m.get('text')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('videoUrl') is not None:
            temp_model = main_models.AigcChatCompletionStreamRequestMessagesContentVideoUrl()
            self.video_url = temp_model.from_map(m.get('videoUrl'))

        return self

class AigcChatCompletionStreamRequestMessagesContentVideoUrl(DaraModel):
    def __init__(
        self,
        url: str = None,
    ):
        # The video URL.
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.url is not None:
            result['url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('url') is not None:
            self.url = m.get('url')

        return self



class AigcChatCompletionStreamRequestMessagesContentImageUrl(DaraModel):
    def __init__(
        self,
        url: str = None,
    ):
        # The publicly accessible HTTPS URL of the reference image, or a complete Base64 image Data URL (such as data:image/png;base64,...). Signed URLs must remain valid during request execution. Re-upload or update the link for expired or unauthorized images.
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.url is not None:
            result['url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('url') is not None:
            self.url = m.get('url')

        return self

