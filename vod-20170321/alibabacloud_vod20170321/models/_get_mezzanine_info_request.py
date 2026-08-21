# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetMezzanineInfoRequest(DaraModel):
    def __init__(
        self,
        addition_type: str = None,
        auth_timeout: int = None,
        output_type: str = None,
        reference_id: str = None,
        video_id: str = None,
    ):
        # The type of additional information. Separate multiple values with commas (,). By default, only basic information is returned. Valid values:
        # 
        # - **video**: video stream information.
        # - **audio**: audio stream information.
        self.addition_type = addition_type
        # The validity period of the signature for FileURL (source file URL). Unit: seconds. Default value: **3600**. The minimum value is **1**.
        #  - If OutputType is set to **cdn**:
        #     - FileURL expires periodically only if URL signing is enabled. Otherwise, FileURL is permanently valid.
        #     - Minimum value: **1**.
        #     - Maximum value: unlimited.
        #     - Default value: **3600** if this parameter is not specified.
        # - If OutputType is set to **oss**:
        #     - FileURL expires periodically only if the storage permission is set to private. Otherwise, FileURL is permanently valid.
        #     - Minimum value: **1**.
        #     - Maximum value: To reduce security risks to the origin server, the maximum value is **2592000** (30 days) when the audio or video file is stored in a bucket managed by ApsaraVideo VOD, and **129600** (36 hours) when the file is stored in your own OSS bucket.
        #     - Default value: **3600** if this parameter is not specified.
        self.auth_timeout = auth_timeout
        # The type of the output URL. Valid values:
        # 
        # - **oss**: back-to-origin URL.
        # - **cdn** (default): CDN URL.
        # 
        # > If the bucket type of the source file is in, only the OSS URL is returned.
        self.output_type = output_type
        # The custom ID. Only lowercase letters, uppercase letters, digits, hyphens (-), and underscores (_) are supported. The value must be 6 to 64 characters in length and is unique at the user level.
        self.reference_id = reference_id
        # The audio or video ID. You can obtain the ID by using one of the following methods:
        # - For audio or video files uploaded through the console, log on to the [ApsaraVideo VOD console](https://vod.console.aliyun.com) and choose **Media Files** > **Audio/Video** to view the video ID.
        # - Obtain the video ID from the VideoId parameter returned by the [CreateUploadVideo](https://help.aliyun.com/document_detail/55407.html) operation when you request an upload URL and credential.
        # - After the video is uploaded, call the [SearchMedia](https://help.aliyun.com/document_detail/86044.html) operation to query the audio or video ID, which is the value of VideoId in the response.
        self.video_id = video_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.addition_type is not None:
            result['AdditionType'] = self.addition_type

        if self.auth_timeout is not None:
            result['AuthTimeout'] = self.auth_timeout

        if self.output_type is not None:
            result['OutputType'] = self.output_type

        if self.reference_id is not None:
            result['ReferenceId'] = self.reference_id

        if self.video_id is not None:
            result['VideoId'] = self.video_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdditionType') is not None:
            self.addition_type = m.get('AdditionType')

        if m.get('AuthTimeout') is not None:
            self.auth_timeout = m.get('AuthTimeout')

        if m.get('OutputType') is not None:
            self.output_type = m.get('OutputType')

        if m.get('ReferenceId') is not None:
            self.reference_id = m.get('ReferenceId')

        if m.get('VideoId') is not None:
            self.video_id = m.get('VideoId')

        return self

