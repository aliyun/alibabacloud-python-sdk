# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SubmitImageGenerationJobRequest(DaraModel):
    def __init__(
        self,
        aspect_ratio: str = None,
        client_token: str = None,
        input: str = None,
        job_parameters: str = None,
        job_type: str = None,
        model: str = None,
        n: str = None,
        resolution: str = None,
        scene: str = None,
        user_data: str = None,
    ):
        # The aspect ratio. Valid values: 16:9 (default), 9:16, 4:3, 3:4, and 1:1.
        self.aspect_ratio = aspect_ratio
        # The idempotency parameter.
        self.client_token = client_token
        # The task input. This is a JSON string that contains the following fields:
        # - Prompt: String. Required. The prompt.
        # - Medias: the media list. Required when the task type is `image_to_image`. A maximum of 9 items are supported.
        # > The Media struct contains: Type, the media type, String, valid value: image. URL, the media download URL, String.
        # >
        self.input = input
        # The task feature parameters. This is a JSON string. No configuration is required at this time.
        self.job_parameters = job_parameters
        # The type of the generation task. Valid values:
        # 
        # - text_to_image: text-to-image.
        # - image_to_image: image-to-image.
        self.job_type = job_type
        # The model name.
        self.model = model
        # The number of images. Valid values: 1 to 4. Default value: 1.
        self.n = n
        # The resolution. Valid values: 1K (default), 2K, and 4K.
        self.resolution = resolution
        # The scenario. This is an enumeration type. Currently, only `general` is supported.
        self.scene = scene
        # The user business data in JSON format.
        self.user_data = user_data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aspect_ratio is not None:
            result['AspectRatio'] = self.aspect_ratio

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.input is not None:
            result['Input'] = self.input

        if self.job_parameters is not None:
            result['JobParameters'] = self.job_parameters

        if self.job_type is not None:
            result['JobType'] = self.job_type

        if self.model is not None:
            result['Model'] = self.model

        if self.n is not None:
            result['N'] = self.n

        if self.resolution is not None:
            result['Resolution'] = self.resolution

        if self.scene is not None:
            result['Scene'] = self.scene

        if self.user_data is not None:
            result['UserData'] = self.user_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AspectRatio') is not None:
            self.aspect_ratio = m.get('AspectRatio')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Input') is not None:
            self.input = m.get('Input')

        if m.get('JobParameters') is not None:
            self.job_parameters = m.get('JobParameters')

        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')

        if m.get('Model') is not None:
            self.model = m.get('Model')

        if m.get('N') is not None:
            self.n = m.get('N')

        if m.get('Resolution') is not None:
            self.resolution = m.get('Resolution')

        if m.get('Scene') is not None:
            self.scene = m.get('Scene')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

