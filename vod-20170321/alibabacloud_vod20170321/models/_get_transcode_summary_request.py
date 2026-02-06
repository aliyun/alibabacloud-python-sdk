# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetTranscodeSummaryRequest(DaraModel):
    def __init__(
        self,
        video_ids: str = None,
    ):
        # The ID of the audio or video file. You can specify up to 10 IDs. Separate the IDs with commas (,). You can use one of the following methods to obtain the ID:
        # 
        # *   After you upload a video in the [ApsaraVideo VOD console](https://vod.console.aliyun.com), you can log on to the ApsaraVideo VOD console and choose **Media Files** > **Audio/Video** to view the ID of the video.
        # *   Obtain the value of VideoId from the response to the [CreateUploadVideo](https://help.aliyun.com/document_detail/55407.html) operation that you call to obtain the upload URL and credential.
        # *   Obtain the value of VideoId by calling the [SearchMedia](https://help.aliyun.com/document_detail/86044.html) operation. This method is applicable to files that have been uploaded.
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

