# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aideepsign20260511 import models as main_models
from darabonba.model import DaraModel

class CreateVideoTaskRequest(DaraModel):
    def __init__(
        self,
        media: List[main_models.CreateVideoTaskRequestMedia] = None,
        audio: bool = None,
        client_token: str = None,
        duration: int = None,
        model: str = None,
        prompt: str = None,
        prompt_extend: bool = None,
        ratio: str = None,
        resolution: str = None,
        seed: int = None,
        watermark: bool = None,
    ):
        self.media = media
        # Specifies whether to include an audio track. Default value: true.
        self.audio = audio
        # The idempotency parameter.
        self.client_token = client_token
        # The video duration in seconds. Valid values: an integer from 2 to 30, -1 (intelligent duration), and 0 (server default of 5 seconds).
        self.duration = duration
        # The model name. Valid values: wan3.0-video (default) and wan3.0-video-prime (high-speed version).
        self.model = model
        # The video description prompt. You must specify either this parameter or Media. For text-to-video generation, only Prompt is required.
        self.prompt = prompt
        # Specifies whether to enable intelligent rewriting (prompt_extend). Default value: true.
        self.prompt_extend = prompt_extend
        # The aspect ratio. Valid values: adaptive (default), 16:9, 4:3, 1:1, 3:4, and 9:16.
        self.ratio = ratio
        # The resolution. Valid values: 1080P (default), 720P, and 480P.
        self.resolution = resolution
        # The random seed. Valid values: -1 (random), an integer from 0 to 2147483647, and 0 (server default of random).
        self.seed = seed
        # Specifies whether to add a Model Studio watermark. Default value: false.
        self.watermark = watermark

    def validate(self):
        if self.media:
            for v1 in self.media:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Media'] = []
        if self.media is not None:
            for k1 in self.media:
                result['Media'].append(k1.to_map() if k1 else None)

        if self.audio is not None:
            result['Audio'] = self.audio

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.model is not None:
            result['Model'] = self.model

        if self.prompt is not None:
            result['Prompt'] = self.prompt

        if self.prompt_extend is not None:
            result['PromptExtend'] = self.prompt_extend

        if self.ratio is not None:
            result['Ratio'] = self.ratio

        if self.resolution is not None:
            result['Resolution'] = self.resolution

        if self.seed is not None:
            result['Seed'] = self.seed

        if self.watermark is not None:
            result['Watermark'] = self.watermark

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.media = []
        if m.get('Media') is not None:
            for k1 in m.get('Media'):
                temp_model = main_models.CreateVideoTaskRequestMedia()
                self.media.append(temp_model.from_map(k1))

        if m.get('Audio') is not None:
            self.audio = m.get('Audio')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('Model') is not None:
            self.model = m.get('Model')

        if m.get('Prompt') is not None:
            self.prompt = m.get('Prompt')

        if m.get('PromptExtend') is not None:
            self.prompt_extend = m.get('PromptExtend')

        if m.get('Ratio') is not None:
            self.ratio = m.get('Ratio')

        if m.get('Resolution') is not None:
            self.resolution = m.get('Resolution')

        if m.get('Seed') is not None:
            self.seed = m.get('Seed')

        if m.get('Watermark') is not None:
            self.watermark = m.get('Watermark')

        return self



class CreateVideoTaskRequestMedia(DaraModel):
    def __init__(
        self,
        type: str = None,
        url: str = None,
    ):
        # The media type for the first item. Valid values: first_frame, last_frame, reference_image, reference_video, reference_audio, file, and link.
        self.type = type
        # The media URL for the first item. You can specify a public HTTP or HTTPS URL, a temporary oss:// URL, or inline data in the format of data:{mime};base64,....
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.type is not None:
            result['Type'] = self.type

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

