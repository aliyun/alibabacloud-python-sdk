# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SubmitYikeAvatarNarratorJobRequest(DaraModel):
    def __init__(
        self,
        job_params: str = None,
        user_data: str = None,
    ):
        # The task request content. The value is a JSON string that contains the following parameters:
        # 
        # - SceneType: string. The common scenario type. Valid values:
        #   - creator-talk: knowledge explanation. Applicable to scenarios such as news, popular science, and financial explanation.
        #   - avatar-broadcast: digital human broadcasting. A fixed single-shot scenario.
        # - TextType: int. The text type. Valid values:
        #   - 1: raw script. The system automatically converts product or news information into an oral broadcast script. This value is not supported for avatar-broadcast.
        #   - 2: oral broadcast script.
        # - TextContent: string. The text content. Maximum length: 10,000 characters.
        # - UserMaterials: Array\\<Object\\>. The list of user materials. This parameter is not supported for avatar-broadcast. Fields:
        #   - MediaId: the media asset ID. The ID of an image or video uploaded to Wanjing Yike.
        # - AvatarData: object. The digital human information.
        #   - AvatarPortrait: required. String. The URL of the portrait image.
        #   - AvatarVoice: optional. String. The URL of an audio file for voice cloning reference, or a voice ID from the built-in voice library. For more information, see the Wanjing Yike voice library. If this parameter is not specified, the system automatically selects a voice.
        # - VoiceDuration: int. The expected oral broadcast duration. Set this parameter when TextType is set to 1. Unit: seconds. Default value: 60. The final video duration is slightly shorter than the expected duration.
        # - AspectRatio: string. The video dimensions. Valid values: 16:9, 9:16, 4:3, and 3:4.
        # - Resolution: string. The video resolution. Valid values: 720P and 1080P.
        # - WithSubtitles: bool. Specifies whether to add subtitles. Valid values:
        #   - true (default): Add subtitles.
        #   - false: Do not add subtitles.
        # 
        # This parameter is required.
        self.job_params = job_params
        # The custom user parameter. The value is a JSON string that is returned as-is in the callback result, for example, newsKey.
        # 
        # The system reserved field NotifyAddress specifies the callback URL. The system sends a callback to this URL after the task is complete. Example: {"NotifyAddress": "http://xxx.callback.url"}.
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

