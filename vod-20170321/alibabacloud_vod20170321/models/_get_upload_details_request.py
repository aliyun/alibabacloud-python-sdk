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
        # The ID of the media file, namely, the audio or video ID. You can specify a maximum of 20 IDs. Separate multiple IDs with commas (,). You can use one of the following methods to obtain the audio or video ID:
        # *   Log on to the [ApsaraVideo VOD](https://vod.console.aliyun.com) console. In the left-side navigation pane, choose **Media Files** > **Audio/Video**. On the Video and Audio page, you can view the audio or video ID. Use this method if the audio or video file is uploaded by using the ApsaraVideo VOD console.
        # *   View the value of the VideoId parameter returned by the [CreateUploadVideo](https://help.aliyun.com/document_detail/55407.html) operation that you called to obtain an upload URL and credential.
        # *   View the value of the VideoId parameter returned by the [SearchMedia](https://help.aliyun.com/document_detail/86044.html) operation that you called to query media information after the audio or video file is uploaded.
        # 
        # This parameter is required.
        self.media_ids = media_ids
        # The type of the media file. Set the value to **video**, which indicates audio and video files.
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

