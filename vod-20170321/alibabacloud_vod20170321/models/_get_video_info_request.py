# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetVideoInfoRequest(DaraModel):
    def __init__(
        self,
        reference_id: str = None,
        video_id: str = None,
    ):
        self.reference_id = reference_id
        # The ID of the audio or video file. You can specify only one ID in each call. You can use one of the following methods to obtain the ID:
        # 
        # *   Log on to the [ApsaraVideo VOD console](https://vod.console.aliyun.com). In the left-side navigation pane, choose **Media Files** > **Audio/Video**. On the Video and Audio page, view the ID of the audio or video file. This method is applicable to files that are uploaded by using the ApsaraVideo VOD console.
        # *   Obtain the value of VideoId from the response to the [CreateUploadVideo](https://help.aliyun.com/document_detail/55407.html) operation that you called to obtain the upload URL and credential.
        # *   Obtain the value of VideoId from the response to the [SearchMedia](https://help.aliyun.com/document_detail/86044.html) operation that you called to query the media ID after the media file is uploaded.
        self.video_id = video_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.reference_id is not None:
            result['ReferenceId'] = self.reference_id

        if self.video_id is not None:
            result['VideoId'] = self.video_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ReferenceId') is not None:
            self.reference_id = m.get('ReferenceId')

        if m.get('VideoId') is not None:
            self.video_id = m.get('VideoId')

        return self

