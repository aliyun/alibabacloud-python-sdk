# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SubmitPreprocessJobsRequest(DaraModel):
    def __init__(
        self,
        preprocess_type: str = None,
        video_id: str = None,
    ):
        # The preprocessing type. Set the value to **LivePreprocess** (video preprocessing for the China Production Studio).
        # 
        # This parameter is required.
        self.preprocess_type = preprocess_type
        # The video ID. You can obtain the video ID by using one of the following methods:
        # - For videos uploaded through the console, log on to the [ApsaraVideo VOD console](https://vod.console.aliyun.com) and choose **Media Files** > **Audio/Video** to view the video ID.
        # - When you upload a video by calling the [CreateUploadVideo](https://help.aliyun.com/document_detail/55407.html) operation, the video ID is the value of the VideoId parameter in the response.
        # - After the video is uploaded, you can call the [SearchMedia](https://help.aliyun.com/document_detail/86044.html) operation to query the video ID, which is the value of the VideoId parameter in the response.
        # 
        # This parameter is required.
        self.video_id = video_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.preprocess_type is not None:
            result['PreprocessType'] = self.preprocess_type

        if self.video_id is not None:
            result['VideoId'] = self.video_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PreprocessType') is not None:
            self.preprocess_type = m.get('PreprocessType')

        if m.get('VideoId') is not None:
            self.video_id = m.get('VideoId')

        return self

