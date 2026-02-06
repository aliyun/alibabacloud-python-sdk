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
        # The preprocessing type. Set the value to **LivePreprocess**. LivePreprocess specifies that the video is preprocessed in the production studio.
        # 
        # This parameter is required.
        self.preprocess_type = preprocess_type
        # The ID of the video. You can use one of the following methods to obtain the ID:
        # 
        # *   After you upload a video in the ApsaraVideo VOD console, you can log on to the [ApsaraVideo VOD console](https://vod.console.aliyun.com) and choose **Media Files** > **Audio/Video** to view the ID of the video.
        # *   Obtain the VideoId from the response to the [CreateUploadVideo](https://help.aliyun.com/document_detail/55407.html) operation that you call to upload videos.
        # *   Obtain the VideoId from the response to the [SearchMedia](https://help.aliyun.com/document_detail/86044.html) operation that you call to query videos.
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

