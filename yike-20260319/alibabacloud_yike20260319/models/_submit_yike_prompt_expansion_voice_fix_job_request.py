# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SubmitYikePromptExpansionVoiceFixJobRequest(DaraModel):
    def __init__(
        self,
        job_params: str = None,
        user_data: str = None,
    ):
        # The task parameters, a JSON-formatted string. The following fields are included:
        # - model (String, required): The model name. Example: happyhorse-1.0-r2v.
        # - input (Object, required): The input data object.
        #   - prompt (String, required): The prompt content. Maximum length: 10,000 characters.
        #   - media (Array(Object), required): The list of media materials used to specify reference images and audio.
        #     - type (String, required): The type of the input media asset. Valid values: reference_image and reference_audio.
        #     - url (String, required): The URL of the input media asset.
        # - parameters (Object, required): The video generation parameter object.
        #   - duration (Integer, required): The video duration in seconds. The value must be a positive integer. Valid values: 5 to 15.
        #   - ratio (String, required): The aspect ratio of the video. Valid values: 16:9, 9:16, 4:3, 3:4, and 1:1.
        #   - resolution (String, required): The video resolution. Valid values: 720P and 1080P.
        #   - specialEdition (Bool, optional): The cost-effective edition parameter. This parameter can be set to true only when the resolution is 1080P.
        #   - skipPromptEnhancer (Bool, optional): Specifies whether to skip prompt enhancement. Default value: false.
        #   - skipVoiceResync (Bool, optional): Specifies whether to skip audio repair. Default value: false.
        # 
        # This parameter is required.
        self.job_params = job_params
        # The custom user parameter, a JSON string. This parameter is returned as-is in the callback result. Example: newsKey.
        # 
        # The system reserved field NotifyAddress specifies the callback URL. After the task is completed, a callback is sent. Example: {"NotifyAddress": "http://xxx.callback.url"}.
        self.user_data = user_data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.job_params is not None:
            result['JobParams'] = self.job_params

        if self.user_data is not None:
            result['UserData'] = self.user_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobParams') is not None:
            self.job_params = m.get('JobParams')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

