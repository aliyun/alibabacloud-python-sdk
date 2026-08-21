# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetVideoPlayAuthRequest(DaraModel):
    def __init__(
        self,
        api_version: str = None,
        auth_info_timeout: int = None,
        reference_id: str = None,
        video_id: str = None,
    ):
        # The API version number. Set the value to **1.0.0**.
        self.api_version = api_version
        # The expiration time of the playback credential. Unit: **seconds**. If the credential expires, the playback URL cannot be obtained. You must obtain a new credential.
        # 
        # - Default value: **100**.
        # - Valid values: `[100,3000]`.
        self.auth_info_timeout = auth_info_timeout
        # The custom ID. Only lowercase letters, uppercase letters, digits, hyphens, and underscores are supported. Length: 6 to 64 characters. The ID is unique per user.
        self.reference_id = reference_id
        # The audio or video ID. Only a single audio or video ID is supported. You can obtain the ID by using the following methods:
        # - For videos uploaded through the console, log on to the [ApsaraVideo VOD console](https://vod.console.aliyun.com) and choose **Media Files** > **Audio/Video** to view the audio or video ID.
        # - When uploading audio or video files by calling the [CreateUploadVideo](https://help.aliyun.com/document_detail/55407.html) operation, the audio or video ID is the value of the VideoId response parameter.
        # - After the audio or video file is uploaded, you can call the [SearchMedia](https://help.aliyun.com/document_detail/86044.html) operation to query the audio or video ID, which is the value of the VideoId response parameter.
        self.video_id = video_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_version is not None:
            result['ApiVersion'] = self.api_version

        if self.auth_info_timeout is not None:
            result['AuthInfoTimeout'] = self.auth_info_timeout

        if self.reference_id is not None:
            result['ReferenceId'] = self.reference_id

        if self.video_id is not None:
            result['VideoId'] = self.video_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiVersion') is not None:
            self.api_version = m.get('ApiVersion')

        if m.get('AuthInfoTimeout') is not None:
            self.auth_info_timeout = m.get('AuthInfoTimeout')

        if m.get('ReferenceId') is not None:
            self.reference_id = m.get('ReferenceId')

        if m.get('VideoId') is not None:
            self.video_id = m.get('VideoId')

        return self

