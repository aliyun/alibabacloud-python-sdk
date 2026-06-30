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
        # The node request content. JSON string. This parameter contains the following fields:
        # 
        # - SceneType: string. The common scenario type. Valid values: `creator-talk`: knowledge sharing, applicable to influencer sharing and explanation scenarios in industries such as finance and education.
        # - TextType: int. The text type. Valid values: 1: raw script (product or news information, which the system automatically converts to an oral broadcast script). 2: oral broadcast script.
        # - TextContent: string. The text content. Maximum length: 10000 characters.
        # - UserMaterials: Array\\<Object\\>. The list of user materials. Fields: MediaId: the media asset ID (image or video uploaded to Wanjing Yike).
        # - AvatarData: object. The digital human information. AvatarPortrait: required, string, the URL of the portrait image. AvatarVoice: optional, string, the audio URL (used as a reference for voice cloning) or a voice ID from the library (see the Wanjing Yike voice library. The system selects automatically).
        # - VoiceDuration: int. The expected oral broadcast duration. Settings for this field apply when TextType is 1. Unit: seconds. Default value: 60. The final video duration is slightly shorter than the expected duration.
        # - AspectRatio: string. The video dimensions. Valid values: 16:9, 9:16, 4:3, 3:4.
        # - Resolution: string. The video resolution. Valid values: 720P, 1080P.
        # - OutputLanguages: Array. The output video languages. Multiple values are supported. Currently, only Chinese is supported. Valid values: CN: Chinese (default). EN: English. YUE: Cantonese.
        # - WithSubtitles: bool. Specifies whether to include subtitles. Valid values: true: include subtitles (default). false: do not include subtitles.
        # 
        # -- The following parameters are for the vertical screen packaging template and are valid only for the creator-talk type. --
        # - TargetAspectRatio: string. The dimensions adapted for vertical screen. Valid values: `16:9`, `9:16`, `4:3`, `3:4`.
        # - Title: string. The main title displayed in the template.
        # - SubHeading: string. The subtitle displayed in the template.
        # - Date: string. The date displayed in the template.
        # - Watermark: object. The watermark displayed in the template. Fields: Text: the watermark text.
        # - EnabledAICover: bool. Specifies whether to use AI to generate a cover image.
        # - IPCharacter: Object. Specifies whether the AI-generated cover image includes an IP character. Fields: MediaId: the media asset ID. MediaUrl: a publicly accessible URL.
        # 
        # This parameter is required.
        self.job_params = job_params
        # The custom user parameter. JSON string. This parameter is returned as-is in the callback result (for example, newsKey).
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

