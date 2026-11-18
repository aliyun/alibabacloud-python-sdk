# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetUploadDetailsRequest(DaraModel):
    def __init__(
        self,
        media_ids: str = None,
        media_type: str = None,
    ):
        # The media IDs, which are the audio or video IDs (VideoId). Separate multiple IDs with commas (,). You can specify up to 20 IDs. You can obtain the IDs by using one of the following methods:
        # - For audio or video files uploaded through the console, log on to the [ApsaraVideo VOD console](https://vod.console.aliyun.com) and choose **Media Library** > **Audio and Video** to view the audio or video IDs.
        # - When you call the [Create upload URLs and credentials for audio and video files](https://help.aliyun.com/document_detail/55407.html) operation to obtain the upload URL and credential, the value of the VideoId response parameter is the media ID.
        # - After an audio or video file is uploaded, you can call the [Search for media information](https://help.aliyun.com/document_detail/86044.html) operation to query the media ID. The value of the VideoId response parameter is the media ID.
        # 
        # This parameter is required.
        self.media_ids = media_ids
        # The media type. Set the value to **video**, which indicates audio and video files.
        self.media_type = media_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.media_ids is not None:
            result['MediaIds'] = self.media_ids

        if self.media_type is not None:
            result['MediaType'] = self.media_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MediaIds') is not None:
            self.media_ids = m.get('MediaIds')

        if m.get('MediaType') is not None:
            self.media_type = m.get('MediaType')

        return self

