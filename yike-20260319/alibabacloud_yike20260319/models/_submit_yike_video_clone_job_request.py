# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SubmitYikeVideoCloneJobRequest(DaraModel):
    def __init__(
        self,
        job_params: str = None,
        user_data: str = None,
    ):
        # The job request content. JSON string that contains the following parameters:
        # - SceneType: string. The replication scene type. Valid values: `variant-clone`: full replication, applicable to same-category content rewriting scenarios where only partial elements (person/voice/image/text) are replaced.
        # - OriginalVideo: object type that contains the following field: MediaId - the media asset ID (video uploaded to the platform).
        # - SceneConfig: JSON string type. The scene extension parameters. For the variant-clone type, the value is `{"OldProductName":"xxx","ProductName":"xxx"}`.
        # - UserMaterials: Array<Object> type. The list of user materials that contains the following field: MediaId - the media asset ID (image or video uploaded to the platform).
        # - AvatarData: object type. The digital human information. AvatarPortrait: required, string, the portrait image URL. AvatarVoice: optional, string, the audio URL (used as a reference for audio replication).
        # - Resolution: string type. The video resolution. Valid values: `720P`, `1080P`.
        # - WithSubtitles: bool type. Specifies whether to include subtitles. Valid values: true: includes subtitles (default). false: does not include subtitles.
        # 
        # This parameter is required.
        self.job_params = job_params
        # The custom user parameter. JSON string. The callback result carries this value as-is (for example, newsKey).
        # 
        # System reserved field NotifyAddress: the callback URL. The system sends a callback to this URL after the task is completed. Example: {"NotifyAddress": "http://xxx.callback.url"}
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

