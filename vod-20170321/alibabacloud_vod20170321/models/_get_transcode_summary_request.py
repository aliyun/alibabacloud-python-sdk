# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetTranscodeSummaryRequest(DaraModel):
    def __init__(
        self,
        video_ids: str = None,
    ):
        # The audio or video IDs. You can specify a maximum of 10 IDs, separated by commas (,). You can obtain the audio or video ID by using the following methods:
        # - For audio or video files uploaded through the console, log on to the [ApsaraVideo VOD console](https://vod.console.aliyun.com) and choose **Media Files** > **Audio/Video** to view the audio or video ID.
        # - Obtain the video ID from the value of the VideoId parameter returned by the [CreateUploadVideo](https://help.aliyun.com/document_detail/55407.html) operation when you request an upload URL and credential.
        # - After the audio or video file is uploaded, call the [SearchMedia](https://help.aliyun.com/document_detail/86044.html) operation to query the audio or video ID, which is the value of the VideoId parameter in the response.
        # 
        # This parameter is required.
        self.video_ids = video_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.video_ids is not None:
            result['VideoIds'] = self.video_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VideoIds') is not None:
            self.video_ids = m.get('VideoIds')

        return self

