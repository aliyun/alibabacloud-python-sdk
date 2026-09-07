# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SubmitVideoGenerationJobRequest(DaraModel):
    def __init__(
        self,
        aspect_ratio: str = None,
        client_token: str = None,
        duration: str = None,
        input: str = None,
        job_parameters: str = None,
        job_type: str = None,
        model: str = None,
        n: int = None,
        output: str = None,
        resolution: str = None,
        scene: str = None,
        user_data: str = None,
    ):
        # The aspect ratio. Valid values: 16:9 (default), 9:16, 4:3, 3:4, 1:1, and adaptive (valid only for wan3.0-video and wan3.0-video-prime).
        self.aspect_ratio = aspect_ratio
        # The idempotency token. A unique, case-sensitive string of up to 32 characters. This token ensures that the request is completed no more than once, preventing duplicate operations caused by multiple retries.
        self.client_token = client_token
        # The output duration. Valid values: 4 to 15 seconds. Default value: 5 seconds.
        # - For wan3.0-video and wan3.0-video-prime, the maximum value is 30 seconds.
        self.duration = duration
        # The task input. This parameter is required. The value is a JSON string that contains the following fields:
        # - Prompt: string. Required. The prompt.
        # - Medias: the list of media items.
        #   - If JobType is set to image_to_video, this field is required and only 1 media item is needed.
        #   - If JobType is set to first_last_frame, this field is required and exactly 2 media items are needed.
        #   - If JobType is set to reference_to_video, this field is required and up to 9 media items are allowed. For wan3.0-video and wan3.0-video-prime, up to 20 media items are allowed, including up to 10 images, 5 videos, and 5 audio files. The total duration of audio and video files cannot exceed 15 seconds.
        # > The Media structure contains the following fields: Type, the media type (string). Valid values: `image`, `video`, and `audio`. URL, the media download URL (string). MediaId, the media asset ID (string).
        # >
        self.input = input
        # The task parameters as a JSON string that contains the following fields:
        # - EnableAudio: boolean. Optional. Specifies whether to include audio in the output. Valid values: true and false.
        # - Watermark: boolean. Optional. Specifies whether to include a watermark. Valid values: true (an "AI-generated" watermark is added to the lower-right corner of the video) and false (no watermark is added).
        # - PromptExtend: boolean. Optional. Specifies whether to enable intelligent prompt rewriting. This parameter is valid only for wan3.0-video and wan3.0-video-prime. Valid values: true (enabled, default) and false (disabled).
        self.job_parameters = job_parameters
        # The task type. This parameter is required. Valid values:
        # - text_to_video: text-to-video.
        # - image_to_video: image-to-video.
        # - first_last_frame: first and last frame to video.
        # - reference_to_video: reference-to-video.
        self.job_type = job_type
        # The model name. This parameter is required. Valid values:
        # - wan3.0-video
        # - wan3.0-video-prime
        # - happyhorse-1.1
        # - happyhorse-1.0
        # - wan2.7
        self.model = model
        # The number of outputs. Valid values: 1 to 4. Default value: 1.
        self.n = n
        # The output configuration as a JSON string. OssUri is an optional OSS output directory. If not specified, a signed URL for the service-generated output is returned.
        self.output = output
        # The resolution. Valid values:
        # - 1080P
        # - 720P: default value.
        # - 480P: valid only for wan3.0-video and wan3.0-video-prime.
        self.resolution = resolution
        # The scene type. Currently, only `general` is supported.
        self.scene = scene
        # The custom user parameters as a JSON string. These parameters are returned as-is in the callback result. The system reserved field NotifyAddress specifies the callback URL. The system sends a callback to this URL when the task is complete.
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

        if self.duration is not None:
            result['Duration'] = self.duration

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

        if self.output is not None:
            result['Output'] = self.output

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

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

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

        if m.get('Output') is not None:
            self.output = m.get('Output')

        if m.get('Resolution') is not None:
            self.resolution = m.get('Resolution')

        if m.get('Scene') is not None:
            self.scene = m.get('Scene')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

